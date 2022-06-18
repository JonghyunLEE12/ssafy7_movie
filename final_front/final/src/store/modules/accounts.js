import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    token: '',
    currentUser: {},
    profile: {},
    authError: null,
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({Authorization: `Token ${state.token}`}),
    tokenString: state => state.token,
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.token = token
    },
    SET_CURRENT_USER(state, user) {
      state.currentUser = user
    },
    SET_PROFILE(state, profile) {
      state.profile = profile
    },
    SET_AUTH_ERROR(state, error) {
      state.authError = error
    },

  },
  actions: {
    saveToken({commit}, token) {
      commit('SET_TOKEN', token)
    },
    removeToken({commit}) {
      commit('SET_TOKEN', '')
    },
    login({commit, dispatch}, credentials) {
     axios({
       method: 'post',
       url: drf.accounts.login(),
       data: credentials,
     })
     .then(res => {
      const token = res.data.key
      dispatch('saveToken', token)
      dispatch('fetchCurrentUser')
      router.push({ name : 'home' })
     })
     .catch(err => {
      console.log(err);
      commit('SET_AUTH_ERROR', err.response.data)
     })
    },
    logout({commit, getters, dispatch}) {
      axios({
        method: 'post',
        url: drf.accounts.logout(),
        headers: getters.authHeader
      })
      .then(() => {
        dispatch('removeToken')
        commit('SET_AUTH_ERROR', null)
        router.push({name : 'login'})
      })
      .catch(err => {
        console.log(err);
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    signup({commit, dispatch}, credentials) {
      axios({
        method: 'post',
        url: drf.accounts.signup(),
        data: credentials
      })
      .then(res => {
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        router.push({ name : 'home' })
      })
      .catch(err => {
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    fetchCurrentUser({commit, getters, dispatch}) {
      if (getters.isLoggedIn) {
        axios({
          method: 'get',
          url: drf.accounts.currentUserInfo(),
          headers: getters.authHeader
        })
        .then(res => {
          console.log(res.data);
          commit('SET_CURRENT_USER', res.data)
        })
        .catch(err => {
          console.log('실패');
          if (err.response.status === 401) {
            dispatch('removeToken')
            router.push({ name : 'login'})
          }
        })
      }
    },
    fetchProfile({getters, commit}, {username}) {
      axios({
        method: 'get',
        url: drf.accounts.profile(username),
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_PROFILE', res.data)
      })
      .catch(err => {
        console.log(err);
      })
    },
    updateProfile({getters, commit}, {username, userData}) {
      axios({
        method: 'put',
        url: drf.accounts.profile(username),
        headers: {Authorization: `Token ${getters.tokenString}` ,'Content-Type': 'multipart/form-data' },
        data: userData
      })
      .then(res => {
        commit('SET_PROFILE', res.data)
      })
      .catch(err => {
        console.log(err);
      })
    },
  },
}