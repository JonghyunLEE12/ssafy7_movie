const HOST = 'http://127.0.0.1:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const VERSUS = 'versus/'
const ARTICLES = 'articles/'
const MOVIES = 'movies/'
const COMMENTS = 'comments/'
const REVIEWS = 'reviews/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username + '/',
  },
  versus: {
    versusArticles: () => HOST + VERSUS + ARTICLES,
    versusArticle: articlePk => HOST + VERSUS + ARTICLES + `${articlePk}/`,
    versusCommentCreate: articlePk => HOST + VERSUS + ARTICLES + `${articlePk}/` + COMMENTS,
    versusComment: (articlePk, commentPk) => HOST + VERSUS + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`
  },
  movies: {
    todayMovies: () => HOST + MOVIES + 'today/recommend/',
    recommendMovies: (keyword) => HOST + MOVIES + `recommend/${keyword}/`,
    randomMovie: () => HOST + MOVIES + 'recommend/random/',
    movie: (moviePk) => HOST + MOVIES + `${moviePk}/detail/`,
    movieReviewCreate: (moviePk) =>  HOST + MOVIES + `${moviePk}/` + REVIEWS,
    movieReview: (reviewPk) =>  HOST + MOVIES + REVIEWS + `${reviewPk}/` 
  },
}