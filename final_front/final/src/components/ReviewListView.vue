<template>
  <div class="mt-3">
    <br>
    <h4>리뷰 목록</h4>
    <div class="container">
      <review-list-form v-show="!reviews.find(el => {return el.user.id === currentUser.pk})"></review-list-form>
      <div class="container">
        <review-list-item v-for="(review, idx) in reviews" :key="`review-${idx}`" :review="review"></review-list-item>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewListForm from '@/components/ReviewListForm.vue'
import ReviewListItem from '@/components/ReviewListItem.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'ReviewListView',
  components: {
    ReviewListForm,
    ReviewListItem,
  },
  props: {
    reviews: Array,
  },
  computed: {
    ...mapGetters(['currentUser', 'isMovie'])
  }
}
</script>

<style>

</style>