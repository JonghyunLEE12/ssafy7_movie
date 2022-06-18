<template>
  <nav class="navbar navbar-expand-lg navbar-white bg-white sticky-top">
    <div class="container-fluid">
      <router-link :to="{ name : 'home'}" class="navbar-brand">
        <div class="mx-5">
          <img src='@/assets/logo.jpg' alt="" width='70px' height='70px'>
        </div>
        </router-link>
      <button class="navbar-toggler bg-light border-dark" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
        <p class="text-dark ts-6 mb-0"><i class="fa-solid fa-bars"></i></p>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarTogglerDemo02" style="width: 250px">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link :to="{ name : 'home'}" class="nav-link" aria-current="page">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name : 'random'}" class="nav-link">RandomMovie</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name : 'versusArticleList'}" class="nav-link">Movie vs Movie</router-link>
          </li>
          <li class="nav-item" v-if="!isLoggedIn">
          <router-link :to="{ name : 'login' }" class="nav-link">login</router-link>
          </li>
          <li class="nav-item" v-if="!isLoggedIn">
            <router-link :to="{ name : 'signup'}" class="nav-link">signup</router-link>
          </li>
          <li class="nav-item" v-if="isLoggedIn">
          <router-link :to="{ name : 'logout'}" class="nav-link">logout</router-link>
          </li>
          <li class="nav-item" v-if="isLoggedIn">
            <router-link :to="{ name : 'profile', params: {username}}" class="nav-link">profile</router-link>
          </li>
      </ul>
      </div>
    </div>
  </nav>
</template>


<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
    username() {
      return this.currentUser.username ? this.currentUser.username: 'guest'
    }
  }

}
</script>

<style scope>
.fa-bars {
  color: black;
}
</style>