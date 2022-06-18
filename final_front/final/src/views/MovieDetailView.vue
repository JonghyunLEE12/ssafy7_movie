<template>
  <div>
    <div class="d-flex justify-content-center">
      <div class="card" style="width: 18rem;">
        <img id="movie-poster" :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+movie.movie_detail.poster_url" alt="">
      </div>
      <div class="card" style="width: 18rem;">
        <div class="card-header">
          <div class= "text-center">
            <h4 class="mb-0">{{movie.movie_detail.title}}</h4>
          </div>
        </div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">
            <details>
            <summary>줄거리</summary>
            <p>{{movie.movie_detail.description}}</p>
            </details>
          </li>
          <li class="list-group-item">개봉일: {{movie.movie_detail.release_date.slice(0, 10)}}</li>
          <li class="list-group-item"><p class="mb-0">TMDB 평점: {{movie.movie_detail.rating}}</p></li>
          <li class="list-group-item"><p class="mb-0">오늘같은날엔 평점: {{(totalRate / totalReviewNum) ?totalRate / totalReviewNum : '아직 데이터가 없습니다.'}}</p></li>
          <li class="list-group-item"><span> 장르 : </span>
            <span v-for="(genre, idx) in movie.movie_detail.genre.slice(0, 6)" :key="`genre-${idx}`">
              {{ genre.genre }}
            </span>
          </li>
          <li class="list-group-item">
            <div>
              <div class="d-flex">
                <p>감독 : {{movie.director.name}}</p>
              </div>
              <div class="d-flex">
                <div class="d-flex">
                  <img :src="directorPhoto" id="director-photo" >
                </div>
              </div>
              <br>
              <p class="d-flex">배우 :</p>
              <div class="d-flex">
                <div v-for="(actor, idx) in movie.actors" :key="`actor_${idx}`" class="mx-2">
                  <img :src="'https://www.themoviedb.org/t/p/w138_and_h175_face/'+actor.profile_path" width="70px">
                  <p id="actor-name">{{actor.name}}</p>
                </div>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>


    <!-- <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+movie.movie_detail.poster_url" alt="">
    <h3>제목: {{movie.movie_detail.title}}</h3>
    <p>줄거리: {{movie.movie_detail.description}}</p>
    <p>개봉일: {{movie.movie_detail.release_date}}</p>
    <p>TMDB 평점: {{movie.movie_detail.rating}}</p>
    <p>유저 평점: {{(totalRate / totalReviewNum) ?totalRate / totalReviewNum : '아직 데이터가 없습니다.'}}</p> -->
    
    <!-- <div>
      <h3>영화 세부 정보</h3>
    </div>
    <h4>감독</h4>
    <img :src="directorPhoto" alt="" id="director-photo">
    <p>이름: {{movie.director.name}}</p>

    <h4>배우들</h4>
    <div v-for="(actor, idx) in movie.actors" :key="`actor_${idx}`">
      <img :src="'https://www.themoviedb.org/t/p/w138_and_h175_face/'+actor.profile_path" alt="">
      <p>이름: {{actor.name}}</p>
    </div> -->
    <br>
    <div>
      <div>
        <h4> <i class="fa-brands fa-youtube" style="color:red;"></i> 추천 영상 </h4>
      </div>
      <div class="d-flex justify-content-center">
        <div v-for="(video, idx) in movie.youtube" :key="`video_${idx}`">
          <div class="mx-1">
            <a :href="video.link" target="_blank">
              <img :src="video.thumbnails" alt="">
            </a>
          </div>
        </div>
      </div>
      <div>
        <review-list-view :reviews="movie.movie_detail.review_set"></review-list-view>
      </div>
    </div>

    <!-- <h4>관련 영상</h4>
    <div v-for="(video, idx) in movie.youtube" :key="`video_${idx}`">
      <a :href="video.link" target="_blank">
        <img :src="video.thumbnails" alt="">
      </a>
    </div> -->

    <!-- <review-list-view :reviews="movie.movie_detail.review_set"></review-list-view> -->

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import ReviewListView from '@/components/ReviewListView.vue'

export default {
  name: 'MovieDetailView',
  data() {
    return {
      totalRate: 0,
      totalReviewNum: 0,
    }
  },
  components: {
    ReviewListView,
  },
  methods: {
    ...mapActions(['fetchMovie'])
  },
  computed: {
    ...mapGetters(['movie', 'isMovie', 'isLoggedIn']),
    directorPhoto() {
      return this.movie.director.profile_path ? 'https://www.themoviedb.org/t/p/w138_and_h175_face/'+ this.movie.director.profile_path : 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
    }
  },
  created() {
    if (!this.isLoggedIn) {
      alert('로그인 후 이용해주세요')
      this.$router.push({ name : 'login'})  
    } else {
      this.fetchMovie(this.$route.params.movieId)
      this.movie.movie_detail.review_set.forEach(el => {
        this.totalRate += el.user_rate
        this.totalReviewNum += 1
      });
    }
  }
}
</script>

<style scoped>
#director-photo {
  width: 138px;
  height: 175px;
}

#actor-name{
  font-size: 10px;
}

#director-photo{
  width : 70px;
  height : 70px;
}

#movie-poster{
  width: inherit;
  height: inherit;
  margin-top: auto;
  margin-bottom: auto;
}
</style> 