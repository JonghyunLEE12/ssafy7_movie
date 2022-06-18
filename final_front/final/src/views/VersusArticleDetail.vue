<template>
  <div>
    <div class="container">
      <h1>{{article.title}}</h1>
      <div class="d-flex justify-content-between gap-2">
        <p class="mb-0 fs-5">작성자: 
          <router-link :to="{name: 'profile', params: {username: article.user.username}}" class="text-decoration-none">
            <img id="user-photo" :src="photo" alt="">
            {{article.user.username}}
          </router-link>
        </p>
        <form @submit.prevent="onDelete" v-if="isAuthor">
          <input type="submit" class="btn btn-danger btn-sm" value="삭제">
        </form>
      </div>
      <hr>
      <div class="d-flex justify-content-center">
        <div style="width: 700px;">
          <div class="container">
            <div class="d-flex justify-content-evenly mt-3">
              <div class="d-flex">
                <p class="text-primary mb-0">
                  {{ article.movie1_title }}
                  <br>
                  <img :src="image1" alt="영화1 이미지">
                  <br>
                  {{(movie1_vote_count/(movie1_vote_count+movie2_vote_count)) * 100 ? (movie1_vote_count/(movie1_vote_count+movie2_vote_count)) * 100 : 0}}%
                </p>
              </div>
              <div>
                <img src="@/assets/versus_image.png">
              </div>
              <div class="d-flex">
                <p class="text-danger mb-0">
                {{ article.movie2_title }}
                <br>
                <img :src="image2" alt="영화2 이미지">
                <br>
                  {{(movie2_vote_count/(movie1_vote_count+movie2_vote_count)) * 100 ? (movie2_vote_count/(movie1_vote_count+movie2_vote_count)) * 100 : 0}}%
                </p>
              </div>        
            </div>
          </div>
          <div class="container">
            <div class="progress" v-if="isArticle">
              <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" :style="{width: (movie1_vote_count/(movie1_vote_count+movie2_vote_count)) * 100 + '%'}"></div>
              <div class="progress-bar progress-bar-striped progress-bar-animated bg-danger" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" :style="{width: (movie2_vote_count/(movie1_vote_count+movie2_vote_count)) * 100 + '%'}"></div>
            </div>
          </div>
          </div>
        </div>
        <div>
      </div>
      <hr>
      <div class="container d-flex justify-content-center">
        <div style = "width:500px; height:300px;">
          <comment-list-view :comments="article.comment_set" v-if="isArticle"></comment-list-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import CommentListView from '@/components/CommentListView.vue'

export default {
  name: 'VersusArticleDetail',
  components: {
    CommentListView
  },
  data() {
    return {
      articlePk: this.$route.params.articlePk,
      image1: '',
      image2: '',
      movie1_vote_count: 0,
      movie2_vote_count: 0,
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'article', 'isArticle', 'isLoggedIn']),
    photo() {
      return this.article.user.user_photo ? 'http://127.0.0.1:8000' + this.article.user.user_photo : 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
    },
  },
  methods: {
    ...mapActions(['deleteArticle', 'fetchArticle']),
    onDelete() {
      this.deleteArticle(this.articlePk)
    }
  },
  created() {
    if (!this.isLoggedIn) {
      alert('로그인 후 이용해주세요')
      this.$router.push({ name : 'login'})  
    } else {
      this.fetchArticle(this.articlePk)
      this.image1 = 'http://127.0.0.1:8000' + this.article.movie1_image
      this.image2 = 'http://127.0.0.1:8000' + this.article.movie2_image
      this.article.comment_set.forEach(element => {
        if (element.versus_vote === 1) {
          this.movie1_vote_count += 1
        } else {
          this.movie2_vote_count += 1
        }
        this.total_vote += 1
      });
    }
  },
}
</script>

<style scoped>
img {
  width: 180px;
  height: 250px;
}

#user-photo {
  width: 20px;
  height: 20px;
  display: inline;
  border-radius: 50%;
  margin-right: 1px;
  margin-left: 1px;
}

</style>