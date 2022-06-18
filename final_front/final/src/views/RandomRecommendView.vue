<template>
  <div class="mb-5">
    <h1> 어떤 영화를 볼까 ?</h1>
    <button @click="randomPick" class="btn btn-primary"><i class="fa-solid fa-shuffle fa-xl"></i></button>
    
    <div>
      <br>
      <div v-if="isRancomMovie">
        <h4>좋았어 오늘은 이 영화닷!</h4>
        <div class="d-flex justify-content-center">
          <div class="card d-flex justify-content-center" style="width: 18rem;">
            <div>
              <div>
                <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+randomMovie.poster_url" width="250">
              </div>
            </div>
          </div>
          <div class="card" style="width: 18rem;">
            <div class="card-header">
              <div class= "text-center">
                <h4>{{randomMovie.title}}</h4>
              </div>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <details>
                <summary>줄거리</summary>
                <p>{{randomMovie.description}}</p>
                </details>
              </li>
              <li class="list-group-item">개봉일: {{randomMovie.release_date}}</li>
              <li class="list-group-item"><span>TMDB 평점: {{randomMovie.rating}}</span></li>
              <li class="list-group-item"><p class="mb-0">오늘같은날에는 평점: {{(totalRate / totalReviewNum) ?totalRate / totalReviewNum : '아직 데이터가 없습니다.'}}</p></li>
              <li class="list-group-item">
                <span> 장르 : </span>
                <div v-for="(genre, idx) in randomMovie.genre_word.slice(0, 6)" :key="`genre-${idx}`">
                  {{ genre }}
                </div>
              </li>
              <li class="list-group-item" id="detail-page-btn">
                <router-link :to="{name:'movieDetail', params: {movieId: randomMovie.movie_id}}" class="btn btn-primary">
                  영화 상세 페이지
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <!-- <div v-show="isRancomMovie">
      <h4>좋았어 오늘은 이 영화닷!</h4>
      <img :src="'https://www.themoviedb.org/t/p/w138_and_h175_face/'+randomMovie.poster_url" alt="">
      <h3>제목: {{randomMovie.title}}</h3>
      <p>TMDB 평점: {{randomMovie.rating}}</p>
      <p>개봉일: {{randomMovie.release_date}}</p>
      <p>줄거리: {{randomMovie.description}}</p>
      장르: 
      <div v-for="(genre, idx) in randomMovie.genre_word" :key="`genre-${idx}`">
        {{ genre }}
      </div>
      <router-link :to="{name:'movieDetail', params: {movieId: randomMovie.movie_id}}">
      <button>영화 상세 페이지</button>
      </router-link>
    </div> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'RandomRecommendView',
  data() {
    return {
      isRancomMovie: false
    }
  },
  methods: {
    ...mapActions(['fetchRandomMovie']),
    randomPick() {
      this.fetchRandomMovie()
      this.isRancomMovie = true
    }
  },
  computed: {
    ...mapGetters(['randomMovie', 'isLoggedIn'])
  },
  created() {
    if (!this.isLoggedIn) {
      alert('로그인 후 이용해주세요')
      this.$router.push({ name : 'login'})  
    }
  }
}
</script>

<style scoped>
#detail-page-btn {
  margin-top: auto;
}
</style>