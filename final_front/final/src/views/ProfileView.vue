<template>
  <div class="container my-3">
    <noscript>
      Copyright (c) 2022 by George W. Park (https://codepen.io/GeorgePark/pen/VXrwOP)
      Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
      The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
      THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    </noscript>
    <div class="profile" v-if="!isEditing">
      <div class="d-flex justify-content-start ms-5">
        <div class="profile-image">
          <img :src="photo" alt="">
        </div>
        <div class="profile-user-settings d-flex justify-content-evenly align-items-center ms-3">
          <h1 class="profile-user-name">{{profile.username}}</h1>
          <button class="edit-btn profile-edit-btn" @click="switchIsEditing" v-if="profile.id === currentUser.pk">Edit</button>
        </div>
      </div>
				<p>{{profile.about}}</p>
			<div class="profile-stats mt-3">
				<ul>
					<li><span class="profile-stat-count">{{profile.review_set.length}}</span> reviews</li>
					<li><span class="profile-stat-count">{{profile.article_set.length}}</span> articles</li>
					<li><span class="profile-stat-count">{{profile.comment_set.length}}</span> comments</li>
				</ul>
			</div>


		</div>

    <div v-if="isEditing" class="mb-3">
      <div class="row d-felx  justify-content-around">
        <img :src="photo" alt="" class="m-0 p-2">
        <div>
          <form @submit.prevent="update">
            <div class="mb-3 form-input">
              <label for="user-photo" class="form-label">사진 선택</label>
              <input class="form-control" type="file" id="user-photo" accept="image/*">
            </div>
            <div class="mb-3 form-input">
              <label for="about" class="form-label">About</label>
              <textarea class="form-control" id="about" rows="3" v-model="about"></textarea>
            </div>
            <button type="submit" class="btn btn-sm btn-warning me-3">수정</button>
            <button type="button" @click="switchIsEditing" class="btn btn-sm btn-danger">취소</button>
          </form>
        </div>
      </div>
    </div>

    <div class="d-flex flex-column justify-content-center align-items-start">
      <h2>{{user}} 평가한 영화</h2>
      <div v-for="(review, idx) in profile.review_set" :key="`review_${idx}`" class="d-flex justify-content-between">
        <router-link :to="{name: 'movieDetail', params: {movieId: review.movie.movie_id}}" class="me-2 text-decoration-none">
          {{review.movie.title}}
        </router-link>
        <p v-if="review.user_rate === 0.5"><i class="fa-regular fa-star"></i></p>
        <p v-else-if="review.user_rate === 1"><i class="fa-solid fa-star"></i></p>
        <p v-else-if="review.user_rate === 2"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></p>
        <p v-else-if="review.user_rate === 3"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></p>
        <p v-else-if="review.user_rate === 4"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></p>
        <p v-else><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></p>
      </div>
      <hr>
      <h2>{{user}} 작성한 글</h2>
      <div v-for="(article, idx) in profile.article_set" :key="`article_${idx}`">
        <router-link :to="{name: 'versusArticleDetail', params: {articlePk: article.id}}" class="text-decoration-none">
        {{article.title}}
        </router-link>
      </div>
      <hr>
      <h2>{{user}} 작성한 댓글</h2>
      <div v-for="(comment, idx) in profile.comment_set" :key="`ocmment_${idx}`">
        <router-link :to="{name: 'versusArticleDetail', params: {articlePk : comment.article}}" class="text-decoration-none">
          {{comment.article}}번 게시글: {{comment.versus_content}}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'ProfileView',
  data() {
    return {
      isEditing: false,
      reviews: [],
      articles: [],
      comments: [],
      about: ''
    }
  },
  computed: {
    ...mapGetters(['profile', 'currentUser', 'isLoggedIn']),
    photo() {
      return this.profile.user_photo ? 'http://127.0.0.1:8000' + this.profile.user_photo : 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
    },
    user() {
      return this.profile.id === this.currentUser.pk ? '내가' : this.profile.username + '님이'
    }
  },
  methods: {
    ...mapActions(['fetchProfile', 'updateProfile',]),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    update(event) {
      const userData = new FormData()
      userData.append('username', this.profile.username)
      if (event.target[0].files[0]) {
        userData.append('user_photo', event.target[0].files[0])
      }
      userData.append('about', this.about)
      const payload = {
        username: this.profile.username,
        userData: userData
      }
      this.updateProfile(payload)
      this.fetchProfile({username : this.$route.params.username})
      this.isEditing = false
    },
  },
  created() {
    if (!this.isLoggedIn) {
      alert('로그인 후 이용해주세요')
      this.$router.push({ name : 'login'})  
    } else {
      const payload = {username : this.$route.params.username}
      this.fetchProfile(payload)
      this.reviews = this.profile.review_set
      this.articles = this.profile.article_set
      this.comments = this.profile.comment_set
    }
  }
}
</script>

<style scoped>
img {
    display: block;
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

.edit-btn {
    display: inline-block;
    font: inherit;
    background: none;
    border: none;
    color: inherit;
    padding: 0;
    cursor: pointer;
}

.profile {
    padding: 5rem 0;
}

.profile-edit-btn {
    line-height: 1.8;
    border: 0.1rem solid #dbdbdb;
    border-radius: 0.3rem;
    padding: 0 1rem;
    margin-left: 1rem;
    height: 30px;
}

.profile-stats li {
    display: inline-block;
    line-height: 1.5;
    margin-right: 4rem;
}

.fa-star {
  color: #ffe96e;
}

</style>