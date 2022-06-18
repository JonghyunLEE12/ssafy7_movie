<template>
  <div class="home my-5">
    <div>
      <h2>{{ currentUser.username }}님! 오늘 같은 날엔 이 영화들 어떠세요?</h2>
      <div class="container">
        <v-carousel :cycle="true" :interval="5000" :show-arrows="false" hide-delimiters>
          <today-movie-list-item v-for="(todayMovie, idx) in todayMovies" :key="idx" :todayMovie="todayMovie"></today-movie-list-item>
        </v-carousel>
      </div>

      <!-- <div class="d-flex">
        <div id="carouselExampleSlidesOnly" class="carousel slide d-flex" data-bs-ride="carousel">
          <today-movie-list-item v-for="(todayMovie, idx) in todayMovies" :key="idx" :todayMovie="todayMovie"></today-movie-list-item>
        </diV>
      </div> -->
    </div>
    <br>

    <div class="d-flex justify-content-evenly">
      <button @click="recommend('맑음')"><i id="sun" class="fa-solid fa-sun fa-2xl"></i></button>
      <button @click="recommend('구름')"><i id="cloud" class="fa-solid fa-cloud fa-2xl"></i></button>
      <button @click="recommend('비')"><i id="rain" class="fa-solid fa-umbrella fa-2xl"></i></button>
      <button @click="recommend('눈')"><i id="snow" class="fa-solid fa-snowflake fa-2xl"></i></button>
      <button @click="recommend('흐림')"><i id="fog" class="fa-solid fa-smog fa-2xl"></i></button>
    </div>
    <br>
    <div>
      <recommend-movie-list v-if="isRecommended" :weatherKeyword="keyword">
      </recommend-movie-list>
    </div>
  </div>
</template>

<script>
import TodayMovieListItem from '@/components/TodayMovieListItem.vue'
import RecommendMovieList from '@/components/RecommendMovieList.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'HomeView',
  components: {
    TodayMovieListItem,
    RecommendMovieList,
  },
  data() {
    return {
      isRecommended: false,
      keyword: ''
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'todayMovies', 'isTodayMovies', 'isLoggedIn'])
  },
  methods: {
    ...mapActions(['fetchTodayMovies', 'fetchRecommendMovies']),
    recommend(keyword) {
      if (this.keyword) {
        if (this.keyword === keyword) {
          this.isRecommended = false
          this.keyword = ''
        } else {
          this.fetchRecommendMovies({keyword})
          this.keyword = keyword
        }
      } else {
        this.keyword = keyword
        this.fetchRecommendMovies({keyword})
        this.isRecommended = true
      }
    },
  },
  created() {
    if (!this.isLoggedIn) {
      alert('로그인 후 이용해주세요')
      this.$router.push({ name : 'login'})  
    }
    
    if (!this.isTodayMovies) {
      this.fetchTodayMovies()
    } 
  }
}
</script>

<style scoped>
#sun {
 color: rgb(255, 157, 10);
}

#cloud {
 color: rgb(173, 218, 255);
}

#rain {
 color: rgb(19, 141, 255);
}

#snow {
 color: rgb(223, 223, 223);
}

#fog {
 color: rgb(165, 165, 165);
}

</style>