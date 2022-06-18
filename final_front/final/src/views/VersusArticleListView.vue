<template>
  <div class="container d-flex justify-content-center">
    <div>
      <h1>영화 vs 영화</h1>
      <div>
        <img src="@/assets/vote_image.png" width="60%" height="60%">
      </div>
      <article>
        주제를 정하고 투표해보세요!
      </article>
      <br>
      <button @click="goToCreateArticle" class="btn btn-primary">글 쓰기</button>
      <br>
      <br>
      <div class="" >
        <div class="">
          <table class="table table-hover">
            <thead class="table-light">
              <th>제목</th>
              <th>작성자</th>
              <th>글번호</th>
            </thead>
            <tbody>
              <tr v-for="(article, idx) in pageData" :key="idx">
                <th>
                  <router-link :to="{name: 'versusArticleDetail', params: {articlePk: article.id}}" class="text-decoration-none">
                        {{article.title}}
                  </router-link>
                </th>
                <td>
                  {{article.user.username}}
                </td>
                <td>
                  {{article.id}}
                </td>
              </tr>
            </tbody>
          </table>     
          <div class="d-flex justify-content-center">
            <!-- <nav aria-label="Page navigation example">
              <ul class="pagination justify-content-end">
                <li class="page-item disabled">
                  <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                </li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item">
                  <a class="page-link" href="#">Next</a>
                </li>
              </ul>
            </nav> -->
            <v-pagination
              v-model="page"
              :length="parseInt(this.articleList.length/5)+1"
              circle
            ></v-pagination>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'VersusArticleListView',
  data(){
    return {
      page: 1,
      itemsPerPage: 5,
      search: '',
      loading: false,
      headers: [
        { text: '제목', align: 'center', sortable: false, value: 'corpName' },
        { text: '작성자', align: 'center', sortable: false, value: 'corpCode' },
        { text: '글번호', align: 'center', sortable: false, value: 'stockCode' },
      ],
      items: [],
    };
  },
  methods: {
    ...mapActions(['fetchArticleList']),
    goToCreateArticle() {
      this.$router.push({name:'versusArticleNew'})
    },
  },
  computed: {
    ...mapGetters(['articleList', 'isLoggedIn']),
    startIdx() {
      return ((this.page - 1) * this.itemsPerPage)
    },
    endIdx() {
      return (this.startIdx + this.itemsPerPage)
    },
    pageData() {
      if (this.articleList !== []) {
        return [...this.articleList].reverse().slice(this.startIdx, this.endIdx)
      } else {
        return this.articleList
      }
    }
  },
  created() {
    if (!this.isLoggedIn) {
      alert('로그인 후 이용해주세요')
      this.$router.push({ name : 'login'})  
    } else {
      this.fetchArticleList()
    }
  },
}
</script>

<style>

</style>