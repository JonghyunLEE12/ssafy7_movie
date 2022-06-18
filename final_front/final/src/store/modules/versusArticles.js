import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'

export default {
  state: {
    articleList: {},
    article: {}
  },
  getters: {
    articleList(state) {
      return state.articleList
    },
    article(state) {
      return state.article
    },
    isAuthor(state, getters) {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle(state) {
      return !_.isEmpty(state.article)
    }
  },
  mutations: {
    SET_ARTICLE_LIST(state, articleList) {
      state.articleList = articleList
    },
    SET_ARTICLE(state, article) {
      state.article = article
    },
    SET_ATICLE_COMMENT(state, comments){
      state.article.comments = comments
    },
  },
  actions: {
    fetchArticleList({commit, getters}){
      axios({
        method: 'get',
        url: drf.versus.versusArticles(),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_ARTICLE_LIST', res.data)
      })
      .catch(err => {
        console.log(err);
        if (err.response.status === 404) {
          commit('SET_ARTICLE_LIST', [])
        }
      })
    },
    fetchArticle({commit, getters}, articlePk){
      axios({
        method: 'get',
        url: drf.versus.versusArticle(articlePk),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
        console.log(getters.article.movie1_image);
      })
      .catch(err => {
        console.log(err);
        if (err.response.status === 404) {
          router.push({name: 'NotFound404'})
        }
      })
    },
    createArticle({commit, getters}, article){
      axios({
        method: 'post',
        url: drf.versus.versusArticles(),
        headers: {Authorization: `Token ${getters.tokenString}` ,'Content-Type': 'multipart/form-data' },
        data: article
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
        router.push({ name : 'versusArticleDetail', params: {articlePk: res.data.id}})
      })
      .catch(err => {
        console.log(err.response.data);
      })
    },
    deleteArticle({commit, getters, dispatch}, articlePk){
      if (confirm('게시글을 삭제하시겠습니까?')) {
        axios({
          method: 'delete',
          url: drf.versus.versusArticle(articlePk),
          headers: getters.authHeader
        })
        .then(() => {
          commit('SET_ARTICLE', {})
          dispatch('fetchArticleList')
          router.push({name:'versusArticleList'})
        })
        .catch(err => {
          console.log(err);
        })
      }
    },
    createComment({commit, getters, dispatch}, {articlePk, versus_vote, versus_content}){
      axios({
        method: 'post',
        url: drf.versus.versusCommentCreate(articlePk),
        headers: getters.authHeader,
        data: {versus_vote, versus_content},
      })
      .then(res => {
        commit('SET_ATICLE_COMMENT', res.data)
        commit('SET_ARTICLE', {})
        dispatch('fetchArticle', articlePk)
      })
      .catch(err => {
        console.log(err);
      })
    },
    updateComment({commit, getters, dispatch}, {articlePk, commentPk, versus_vote, versus_content}){
      axios({
        method: 'put',
        url: drf.versus.versusComment(articlePk, commentPk),
        headers: getters.authHeader,
        data: {versus_vote, versus_content}
      })
      .then(res => {
        commit('SET_ATICLE_COMMENT', res.data)
        commit('SET_ARTICLE', {})
        dispatch('fetchArticle', articlePk)
      })
      .catch(err => {
        console.log(err);
      })
    },
    deleteComment({commit, getters, dispatch}, {articlePk, commentPk}){
      if (confirm('댓글을 삭제하시겠습니까?')){
        axios({
          method: 'delete',
          url: drf.versus.versusComment(articlePk, commentPk),
          headers: getters.authHeader
        })
        .then(res => {
          commit('SET_ATICLE_COMMENT', res.data)
          commit('SET_ARTICLE', {})
          dispatch('fetchArticle', articlePk)
        })
        .catch(err => {
          console.log(err);
        })
      }
    }
  },
}