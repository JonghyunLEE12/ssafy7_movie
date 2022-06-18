<template>
  <div>
    <article-form></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'VersusArticleNewView',
  components: {
    ArticleForm
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  created() {
    if (!this.isLoggedIn) {
      alert('로그인 후 이용해주세요')
      this.$router.push({ name : 'login'})  
    }
  }
}
</script>

<style>

</style>