<template>
  <div>
    <h1>logout</h1>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'LogoutView',
  methods: {
    ...mapActions(['logout'])
  },
  computed: {
    ...mapGetters(['isLoggedIn']),
  },
  created() {
    if (this.isLoggedIn) {
      this.logout()
    } else {
      alert('로그인 먼저 해주세요')
      this.$router.back()
    }
  }

}
</script>

<style>

</style>