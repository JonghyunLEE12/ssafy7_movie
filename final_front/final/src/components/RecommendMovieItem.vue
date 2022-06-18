<template>
  <div>
    <div class="card">
      <router-link :to="{name: 'movieDetail', params: {movieId: recommendMovie.movie_id}}">
        <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+recommendMovie.poster_url" width="210">
      </router-link>
      <div class="card-body">
        <p class="card-text">{{recommendMovie.title}}</p>
      </div>
    </div>
    <!-- <router-link :to="{name: 'movieDetail', params: {movieId: recommendMovie.movie_id}}">
    <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+recommendMovie.poster_url" alt="">
    </router-link> -->
  </div>
</template>

<script>
export default {
  name: 'RecommendMovieItem',
  props: {
    recommendMovie: Object,
  }
}
</script>

<style>

</style>