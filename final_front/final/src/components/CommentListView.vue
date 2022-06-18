<template>
  <div>
    <br>
    <comment-list-form v-show="!comments.find(el => {return el.user.id === currentUser.pk})" class="mb-2"></comment-list-form>
    <h4 class="mb-3">투표 목록</h4>
    <comment-list-item v-for="(comment, idx) in comments" :key="`comment-${idx}`" :comment="comment"></comment-list-item>
  </div>
</template>

<script>
import CommentListForm from '@/components/CommentListForm.vue'
import CommentListItem from '@/components/CommentListItem.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'commentListView',
  components: {
    CommentListForm,
    CommentListItem
  },
  props: {
    comments: Array
  },
  computed: {
    ...mapGetters(['currentUser'])
  }
}
</script>

<style>

</style>