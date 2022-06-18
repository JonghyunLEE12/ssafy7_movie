<template>
  <div>
    <p class="fs-4">투표</p>
    <div class="mt-3">
      <div class="d-flex justify-content-center">
        <div class="row" id="form">
          <form @submit.prevent="onSubmit">
            <div class="d-flex">
              <label class="me-1"><input type="radio" name="vote" value="1" v-model="versus_vote">{{ article.movie1_title }}</label>
              <label class="me-1"><input type="radio" name="vote" value="2" v-model="versus_vote">{{ article.movie2_title }}</label>
              <div class="mx-1">
                <input type="text" width="100" v-model="versus_content" required id="content-input" placeholder="댓글을 입력해주세요">
              </div>
              <button type="submit" class="btn btn-warning btn-sm ml-3">작성</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'CommentListForm',
  data() {
    return {
      versus_vote: 0,
      versus_content: '',
    }
  },
  methods: {
    ...mapActions(['createComment', 'fetchArticle']),
    onSubmit() {
      this.createComment({articlePk : this.article.id, versus_vote: Number(this.versus_vote), versus_content: this.versus_content})
      this.fetchArticle(this.article.id)
    },
  },
  computed: {
    ...mapGetters(['article'])
  }
}
</script>

<style scoped>
  #content-input {
    border-top: none;
    border-left: none;
    border-right: none;
    border-bottom: 2px solid black;
    width: 230px;
  }

  #form {
    width: 650px;
    height: 50px;
  }
</style>