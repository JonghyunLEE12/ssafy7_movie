<template>
  <div class="container">
    <div class="d-flex justify-content-center">
      <div class="mx-2" style="color : blue;">
        <h3 v-if="weatherKeyword === '맑음'">맑은 날엔</h3>
        <h3 v-else-if="weatherKeyword === '구름'">구름 낀 날엔</h3>
        <h3 v-else-if="weatherKeyword === '비'">비가 오는 날엔</h3>
        <h3 v-else-if="weatherKeyword === '눈'">눈이 오는 날엔</h3>
        <h3 v-else>흐린 날엔</h3>
      </div>
      <h3> 이런 영화는 어때요? </h3>
    </div>
    <div class="row d-flex justify-content-evenly flex-wrap">
      <recommend-movie-item v-for="(recommendMovie, idx) in recommendMovies"
      :key="`recommendMovie-${idx}`"
      :recommendMovie="recommendMovie"
      class="col"></recommend-movie-item>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import RecommendMovieItem from '@/components/RecommendMovieItem.vue'
export default {
  name: 'RecommendMovieList',
  components: {
    RecommendMovieItem
  },
  props : {
    weatherKeyword : String
  },
  computed: {
    ...mapGetters(['recommendMovies'])
  }
}
</script>

<style>

</style>