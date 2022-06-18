import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import RandomRecommendView from '../views/RandomRecommendView.vue'
import VersusArticleListView from '../views/VersusArticleListView.vue'
import VersusArticleDetail from '../views/VersusArticleDetail.vue'
import VersusArticleNewView from '../views/VersusArticleNewView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import SignupView from '../views/SignupView.vue'
import ProfileView from '../views/ProfileView.vue'
import NotFound404 from '../views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movies/:movieId',
    name: 'movieDetail',
    component: MovieDetailView
  },
  {
    path: '/random',
    name: 'random',
    component: RandomRecommendView
  },
  {
    path: '/versus/articles',
    name: 'versusArticleList',
    component: VersusArticleListView
  },
  {
    path: '/versus/articles/:articlePk',
    name: 'versusArticleDetail',
    component: VersusArticleDetail
  },
  {
    path: '/versus/articles/new',
    name: 'versusArticleNew',
    component: VersusArticleNewView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404' 
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
