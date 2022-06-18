<template>
  <div class="d-flex justify-content-center">
    <div class="card" style="width: 18rem;">
      <img src="@/assets/login_image.jpg" class="card-img-top" >
      <!-- <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div> -->
    </div>
    <div class="card" style="width: 18rem;">
      <div class="card-header">
            <h1>로그인</h1>
            <account-error-list v-if="authError"></account-error-list>
      </div>
      <form @submit.prevent="login(credentials)">
        <ul class="list-group list-group-flush">
        <li class="list-group-item">
          <label for="username">아이디: </label>
          <input type="text" id="username" class= "mx-1" v-model="credentials.username" required>
        </li>
        <li class="list-group-item">
          <label for="password">비밀번호: </label>
          <input type="password" id="password" class="mx-1" v-model="credentials.password" required>
        </li>
        </ul>
        <div class="card-footer">
          <button class="btn btn-primary">login</button>
        </div>
      </form>
      </div>
  </div>
</template>

<script>
import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'LoginView',
  components: {
    AccountErrorList,
  },
  data(){
    return{
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    ...mapActions(['login'])
  },
  computed: {
    ...mapGetters(['authError'])
  }

}
</script>

<style>

</style>