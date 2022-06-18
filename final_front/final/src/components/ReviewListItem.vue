<template>
  <div>
    <hr>
    <div v-if="!isEditing" class="mb-2">
      <div class="container">
        <div class="row">
          <div class="d-flex flex-column align-items-start justify-content-center">
            <div class="mb-1">
              <router-link :to="{name: 'profile', params: {username: review.user.username}}" class="text-decoration-none fs-4">
                <img :src="photo" alt="유저 프로필 이미지" id="user-photo">
                {{ review.user.username }} 
              </router-link>
              <p class="d-inline">{{review.created_at.slice(0, 10)}}</p>
            </div>
            <p v-if="review.user_rate === 0.5"><i class="fa-regular fa-star fa-lg"></i></p>
            <p v-else-if="review.user_rate === 1"><i class="fa-solid fa-star fa-lg"></i></p>
            <p v-else-if="review.user_rate === 2"><i class="fa-solid fa-star fa-lg"></i><i class="fa-solid fa-star fa-lg"></i></p>
            <p v-else-if="review.user_rate === 3"><i class="fa-solid fa-star fa-lg"></i><i class="fa-solid fa-star fa-lg"></i><i class="fa-solid fa-star fa-lg"></i></p>
            <p v-else-if="review.user_rate === 4"><i class="fa-solid fa-star fa-lg"></i><i class="fa-solid fa-star fa-lg"></i><i class="fa-solid fa-star fa-lg"></i><i class="fa-solid fa-star fa-lg"></i></p>
            <p v-else><i class="fa-solid fa-star fa-lg"></i><i class="fa-solid fa-star fa-lg"></i><i class="fa-solid fa-star fa-lg"></i><i class="fa-solid fa-star fa-lg"></i><i class="fa-solid fa-star fa-lg"></i></p>
            <h4 class="mb-1">{{review.title}}</h4>
            <p class="m-0">{{review.content}}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-if="isEditing">
        <form @submit.prevent="update" class="d-flex flex-column align-items-center">
          <div class="d-flex mb-2">
            <p>
              <i id="star1" @click="reRating(1)" class="fa-star fa-2xl rating-star" :class="{ 'fa-solid' : review.user_rate >= 1, 'fa-regular' : review.user_rate < 1}"></i>
              <i id="star2" @click="reRating(2)" class="fa-star fa-2xl rating-star" :class="{ 'fa-solid' : review.user_rate > 1, 'fa-regular' : review.user_rate < 2}"></i>
              <i id="star3" @click="reRating(3)" class="fa-star fa-2xl rating-star" :class="{ 'fa-solid' : review.user_rate > 2, 'fa-regular' : review.user_rate < 3}"></i>
              <i id="star4" @click="reRating(4)" class="fa-star fa-2xl rating-star" :class="{ 'fa-solid' : review.user_rate > 3, 'fa-regular' : review.user_rate < 4}"></i>
              <i id="star5" @click="reRating(5)" class="fa-star fa-2xl rating-star" :class="{ 'fa-solid' : review.user_rate > 4, 'fa-regular' : review.user_rate < 5}"></i>
            </p>
          </div>
          <div class="d-flex mb-2" id="title-form">
            <label for="review-title" class="form-label">제목 : </label>
            <input class="form-control" type="text" name="review-title" id="review-title" v-model="payload.title">
          </div>
          <div class="d-flex mb-2" id="content-form">
            <label for="review-content" class="form-label">리뷰 : </label>
            <input class="form-control" type="text" name="review-content" id="review-content" v-model="payload.content">
          </div>
          <div class="d-flex">
            <button type="submit" class="btn btn-sm btn-warning me-2 ms-0" id="submit-btn">수정 확인</button>
            <button @click="switchIsEditing" type="button" class="btn btn-sm btn-danger">취소</button>
          </div>
        </form>
    </div>

    <div v-if="currentUser.pk === review.user.id && !isEditing" class="d-flex justify-content-end">
      <button @click="switchIsEditing" class="btn btn-warning btn-sm me-2">수정</button>
      <button @click="onDelete" class="btn btn-danger btn-sm">삭제</button>
    </div>
    <hr>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.review.id,
        title: this.review.title,
        content: this.review.content,
        user_rate: Number(this.review.user_rate),
      }
    }
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview','fetchMovie']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    update() {
      this.updateReview(this.payload)
      this.fetchMovie(this.movie.movie_detail.movie_id)
      this.isEditing = false
    },
    onDelete() {
      this.deleteReview(this.payload)
      this.payload.title = ''
      this.payload.content = ''
      this.payload.user_rate = 0.5
      this.fetchMovie(this.movie.movie_detail.movie_id)
    },
    reRating(rate) {
      let rate_v = rate
      const star1 = document.querySelector('#star1')
      const star2 = document.querySelector('#star2')
      const star3 = document.querySelector('#star3')
      const star4 = document.querySelector('#star4')
      const star5 = document.querySelector('#star5')
      if (this.payload.user_rate === rate) {
        rate_v = 0.5
        star1.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
        star2.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
        star3.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
        star4.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
        star5.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
      } else if (rate === 1) {
        star1.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star2.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
        star3.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
        star4.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
        star5.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
      } else if (rate === 2) {
        star1.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star2.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star3.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
        star4.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
        star5.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
      } else if (rate === 3) {
        star1.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star2.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star3.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star4.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
        star5.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
      } else if (rate === 4) {
        star1.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star2.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star3.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star4.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star5.setAttribute('class', 'fa-regular fa-star fa-2xl rating-star')
      } else {
        star1.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star2.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star3.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star4.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
        star5.setAttribute('class', 'fa-solid fa-star fa-2xl rating-star')
      }
      this.payload.user_rate = rate_v
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'movie']),
    photo() {
      return this.review.user.user_photo ? 'http://127.0.0.1:8000' + this.review.user.user_photo : 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
    },
  }
}
</script>

<style scoped>
  select {
    border: 1px solid rgb(214, 214, 214);
    appearance: none;
  }
  #user-photo {
  width: 30px;
  height: 30px;
  display: inline;
  border-radius: 50%;
  margin-right: 1px;
  margin-left: 1px;
}

#submit-btn {
  margin-left: auto;
}

.fa-star {
  color: #ffe96e;
}

.rating-star{
  cursor: pointer;
}

.form-label {
  padding: 5px;
  width: 55px;
}

.form-control {
  width: 500px;
}

#title-form {
  height: 30px;
}

#content-form {
  height: 30px;
}
</style>