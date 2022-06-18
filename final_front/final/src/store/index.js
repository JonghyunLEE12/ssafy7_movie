import Vue from 'vue'
import Vuex from 'vuex'
import accounts from './modules/accounts'
import movies from './modules/movies'
import versusArticles from './modules/versusArticles'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    accounts, movies, versusArticles
  }
})
