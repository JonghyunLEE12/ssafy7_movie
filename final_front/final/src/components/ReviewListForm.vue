<template>
  <div>
      <form @submit.prevent="onSubmit" class="d-flex flex-column align-items-center">
        <div class="d-flex mb-2">
          <p>
            <i id="star-1" @click="rating(1)" class="fa-regular fa-star fa-2xl rating-star"></i>
            <i id="star-2" @click="rating(2)" class="fa-regular fa-star fa-2xl rating-star"></i>
            <i id="star-3" @click="rating(3)" class="fa-regular fa-star fa-2xl rating-star"></i>
            <i id="star-4" @click="rating(4)" class="fa-regular fa-star fa-2xl rating-star"></i>
            <i id="star-5" @click="rating(5)" class="fa-regular fa-star fa-2xl rating-star"></i>
          </p>
        </div>
        <div class="d-flex mb-2" id="title-form">
          <label for="review-title" class="form-label">제목 : </label>
          <input class="form-control" type="text" name="review-title" id="review-title" v-model="title">
        </div>
        <div class="d-flex mb-2" id="content-form">
          <label for="review-content" class="form-label">리뷰 : </label>
          <input class="form-control" type="text" name="review-content" id="review-content" v-model="content">
        </div>
          <button class="btn btn-primary btn-sm" id="submit-btn">작성</button>
      </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'ReviewListForm',
  data() {
    return {
      title: '',
      content: '',
      user_rate: 0.5,
    }
  },
  methods: {
    ...mapActions(['createReview', 'fetchMovie']),
    rating(rate) {
      let rate_v = rate
      const star1 = document.querySelector('#star-1')
      const star2 = document.querySelector('#star-2')
      const star3 = document.querySelector('#star-3')
      const star4 = document.querySelector('#star-4')
      const star5 = document.querySelector('#star-5')
      if (this.user_rate === rate) {
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
      this.user_rate = rate_v
    },
    onSubmit() {
      this.createReview({moviePk: this.movie.movie_detail.movie_id, title: this.title, content: this.content, user_rate: Number(this.user_rate)})
      this.fetchMovie(this.movie.movie_detail.movie_id)
    }
  },
  computed: {
    ...mapGetters(['movie'])
  }
}
</script>

<style scoped>
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