<template>
  <div class="container">
    <h2>게시글 작성</h2>
    <form @submit.prevent="onSubmit" class="mb-2">
      <div class="mb-3 input-element">
        <label for="title" class="form-label">제목</label>
        <input type="text" v-model="article.title" class="form-control" id="title" placeholder="게시글 제목을 입력해주세요">
      </div>
      <div class="mb-3 input-element">
        <label for="movie1-title" class="form-label">영화1 제목</label>
        <input type="text" v-model="article.movie1_title" class="form-control" id="movie1-title" placeholder="">
      </div>
      <div class="mb-3 input-element">
        <label for="movie1-image" class="form-label">영화1 이미지</label>
        <input class="form-control" type="file" id="movie1-image" accept="image/*">
      </div>
      <div class="mb-3 input-element">
        <label for="movie2-title" class="form-label">영화2 제목</label>
        <input type="text" v-model="article.movie2_title" class="form-control" id="movie2-title" placeholder="">
      </div>
      <div class="mb-3 input-element">
        <label for="movie2-image" class="form-label">영화2 이미지</label>
        <input class="form-control" type="file" id="movie2-image" accept="image/*">
      </div>
      <button type="submit" class="btn btn-success btn-sm me-3">제출</button>
      <button type="button" @click="back" class="btn btn-danger btn-sm">뒤로 가기</button>
    </form>
    <br>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'ArticleForm',
  data() {
    return {
      article: {
        title: '',
        movie1_title: '',
        movie2_title: '',
      }
    }
  },
  methods: {
    ...mapActions(['createArticle']),
    onSubmit(event) {
      const articleData = new FormData()
      articleData.append('title', this.article.title)
      articleData.append('movie1_title', this.article.movie1_title)
      articleData.append('movie1_image', event.target[2].files[0])
      articleData.append('movie2_title', this.article.movie2_title)
      articleData.append('movie2_image', event.target[4].files[0])
      this.createArticle(articleData)
    },
    back() {
      this.$router.push({name: 'versusArticleList'})
    },
  },
}

</script>

<style>
.input-element {
  display: flex;
  flex-direction: column;
}

label {
  text-align: start;
}
</style>