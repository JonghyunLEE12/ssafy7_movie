<template>
  <div>
    <!-- <div class="carousel-inner">
      <div class="carousel-item active">
        <router-link :to="{name: 'movieDetail', params: {movieId: todayMovie.movie_id}}">
          <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+this.todayMovie.poster_url">
        </router-link>
      </div>
    </div>
    <hr> -->

    <!-- <div class="card" style="width: 10rem;">
      <router-link :to="{name: 'movieDetail', params: {movieId: todayMovie.movie_id}}">
        <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+this.todayMovie.poster_url" width="200">
      </router-link>
      <div class="card-body">
        <p class="card-text">{{todayMovie.title}}</p>
      </div>
    </div> -->
    <v-carousel-item>
      <h1>{{todayMovie.title}}</h1>
      <router-link :to="{name: 'movieDetail', params: {movieId: todayMovie.movie_id}}">
      <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+this.todayMovie.poster_url" alt="">
      </router-link>
    </v-carousel-item>
  </div>
</template>

<script>

export default {
  name: 'TdayMovies',
  props: {
    todayMovie: Object,
  },
}
</script>

<style>

</style>