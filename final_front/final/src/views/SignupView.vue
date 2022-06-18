<template>
  <div class="d-flex justify-content-center">
    <!-- 이 안에 이미지는 새로고침 할 때 마다  배우사진이 바뀌는건 어떨까? -->
    <div class="card" style="width: 18rem;">
      <img src="@/assets/signup_image.jpg" class="card-img-top" alt="...">
      <!-- <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div> -->
    </div>
    <!--  -->
    <div class="card" style="width: 20rem;">
      <div class="card-header">
            <h1>회원가입</h1>
            <account-error-list></account-error-list>
      </div>
      <form @submit.prevent="signup(credentials)">
        <ul class="list-group list-group-flush">
          <li class="list-group-item">
            <label for="username" class="my-3 mx-2">아이디 : </label>
            <input type="text" id="username" v-model="credentials.username" required>
          </li>
          <li class="list-group-item">
            <label for="password1" class="my-3 mx-1">비밀번호 : </label>
            <input type="password" id="password1" v-model="credentials.password1" required>
          </li>
          <li class="list-group-item">
            <label for="password2" class="mx-1 ">비밀번호 확인 : </label>
            <input type="password" id="password2" v-model="credentials.password2" required>
            <br>
          </li>
        </ul>
        <div class="card-footer">
          <button class="btn btn-primary">signup</button>
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
        password1: '',
        password2: ''
      }
    }
  },
  methods: {
    ...mapActions(['signup'])
  },
  computed: {
    ...mapGetters(['authError'])
  }
}
</script>

<style>

</style>