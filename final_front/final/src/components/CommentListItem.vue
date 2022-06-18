<template>
  <div class="mb-2">
    <div class="card">
      <div class="card-header" :class="{'alert-danger':comment.versus_vote === 2, 'alert-primary':comment.versus_vote === 1}">
        <p class="mb-0"> 작성자 :
        <router-link :to="{name: 'profile', params: {username: comment.user.username}}" class="text-decoration-none">
          <img :src="photo" alt="유저 프로필 이미지" id="user-photo">
          {{ comment.user.username }} 
        </router-link>
        </p>
      </div>
      <div class="d-flex justify-content-arounds align-items-center">
        <div class="card-body p-1">
          <h5 class="card-title my-1">
            <div v-if="!isEditing">
              {{ comment.versus_content }}
            </div>
            <div v-if="isEditing" class="d-flex flex-column ">
              <div class="mb-2">
              <label class="radio-input me-2"><input type="radio" name="vote" value="1" v-model="payload.versus_vote"><span class="radio-span">{{ article.movie1_title }}</span></label>
              <label class="radio-input me-2"><input type="radio" name="vote" value="2" v-model="payload.versus_vote"><span class="radio-span">{{ article.movie2_title }}</span></label>
              <input type="text" v-model="payload.versus_content" class="me-2" id="content-input">
              </div>
              <div>
              <button @click="update" class="btn btn-warning btn-sm me-2">수정</button>
              <button @click="switchIsEditing" class="btn btn-danger btn-sm">취소</button>
              </div>
            </div>
          </h5>
        </div>
        <div v-if="currentUser.pk === comment.user.id && !isEditing">
          <button @click="switchIsEditing" class="btn btn-warning btn-sm mx-1">수정</button>
          <button @click="onDelete" class="btn btn-danger btn-sm mx-1">삭제</button>
        </div>
      </div>
    </div>
    <!-- <router-link :to="{name: 'profile', params: {username: comment.user.username}}">
      {{ comment.user.username }} 
    </router-link>
    <div v-if="!isEditing">
      {{ comment.versus_content }}
    </div> -->

    <!-- <div v-if="currentUser.pk === comment.user.id && !isEditing">
      <button @click="switchIsEditing" class="btn btn-warning btn-sm">수정</button>
      <button @click="onDelete" class="btn btn-danger btn-sm">삭제</button>
    </div> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
  data() {
    return{
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.id,
        versus_vote: this.comment.versus_vote,
        versus_content: this.comment.versus_content,
      }
    }
  },
  methods: {
    ...mapActions(['deleteComment', 'updateComment', 'fetchArticle']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    update() {
      this.updateComment(this.payload)
      this.isEditing = false
    },
    onDelete() {
      this.deleteComment(this.payload)
      this.isEditing = false
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'article']),
    photo() {
      return this.comment.user.user_photo ? 'http://127.0.0.1:8000' + this.comment.user.user_photo : 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
    },
  },
}
</script>

<style scoped>
#content-input {
    border-top: none;
    border-left: none;
    border-right: none;
    border-bottom: 2px solid black;
    width: 200px;
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