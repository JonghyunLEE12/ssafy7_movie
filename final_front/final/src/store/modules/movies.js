import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'

export default {
  state: {
    todayMovies: [],
    recommendMovies: [],
    movie: {},
    randomMovie: {},
  },
  getters: {
    todayMovies(state) {
      return state.todayMovies
    },
    recommendMovies(state) {
      return state.recommendMovies
    },
    movie(state) {
      return state.movie
    },
    randomMovie(state) {
      return state.randomMovie
    },
    isMovie(state) {
      return !_.isEmpty(state.movie)
    },
    isTodayMovies(state) {
      return !_.isEmpty(state.todayMovies)
    },
  },
  mutations: {
    SET_TODAY_MOVIES(state, todayMovies) {
      state.todayMovies = todayMovies
    },
    SET_RECOMMEND_MOVIES(state, recommendMovies) {
      state.recommendMovies = recommendMovies
    },
    SET_MOVIE(state, movie){
      state.movie = movie
    },
    SET_RANDOM_MOVIE(state,randomMovie){
      state.randomMovie = randomMovie
    },
    SET_MOVIE_REVIEW(state, reviews){
      state.movie.reviews = reviews
    },
  },
  actions: {
    fetchTodayMovies({commit, getters}){
      axios({
        method: 'get',
        url: drf.movies.todayMovies(),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_TODAY_MOVIES', res.data)
      })
      .catch(err => {
        console.log(err);
      })
    },
    fetchRecommendMovies({commit, getters}, {keyword}){
      axios({
        method: 'get',
        url: drf.movies.recommendMovies(keyword),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_RECOMMEND_MOVIES', res.data)
      })
      .catch(err => {
        console.log(err);
      })
    },
    fetchRandomMovie({commit, getters}){
      axios({
        method: 'get',
        url: drf.movies.randomMovie(),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_RANDOM_MOVIE', res.data)
      })
      .catch(err => {
        console.log(err);
      })
    },
    fetchMovie({commit, getters}, moviePk){
      axios({
        method: 'get',
        url: drf.movies.movie(moviePk),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_MOVIE', res.data)
      })
      .catch(err => {
        console.log(err);
        if (err.response.status === 404) {
          router.push({name: 'NotFound404'})
        }
      })
    },
    createReview({commit, getters}, {moviePk, title, content, user_rate}){
      axios({
        method: 'post',
        url: drf.movies.movieReviewCreate(moviePk),
        headers: getters.authHeader,
        data: {title, content, user_rate},
      })
      .then(res => {
        commit('SET_MOVIE_REVIEW', res.data)
      })
      .catch(err => {
        console.log(err);
      })
    },
    updateReview({commit, getters}, {reviewPk, title, content, user_rate}){
      axios({
        method: 'put',
        url: drf.movies.movieReview(reviewPk),
        headers: getters.authHeader,
        data: {title, content, user_rate}
      })
      .then(res => {
        commit('SET_MOVIE_REVIEW', res.data)
      })
      .catch(err => {
        console.log(err);
      })
    },
    deleteReview({commit, getters}, {reviewPk}){
      if (confirm('리뷰를 삭제하시겠습니까?')){
        axios({
          method: 'delete',
          url: drf.movies.movieReview(reviewPk),
          headers: getters.authHeader
        })
        .then(res => {
          commit('SET_MOVIE_REVIEW', res.data)
        })
        .catch(err => {
          console.log(err);
        })
      }
    }
  },
}