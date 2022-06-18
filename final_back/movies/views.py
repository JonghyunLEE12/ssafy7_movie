from os import set_inheritable
from signal import raise_signal
from django.shortcuts import render,get_object_or_404,get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# from rest_framework.status import status
from .serializers import(
    TodayWeatherSerializer,
    WeatherListSerializer,
    RecommendListSerializer,
    ReviewSerializer,
    MovieDetailSerializer,
)
from .models import (
    Weather,
    Movie,
    Actor,
    Genre,
    Review,
    Youtube,
)
import datetime 
import requests
import random



def get_weather():
    # 날씨 검색
    now = datetime.datetime.now()
    url = 'http://data.ex.co.kr/openapi/restinfo/restWeatherList?'
    params = {
        'key' : '2958097790',
        'type' : 'json',
        'sdate' : f'{int(now.strftime("%Y%m%d"))-1}',
        'stdHour' : '10',
    }
    response = requests.get(url,params=params).json()
    target = response['list'][0]

    ## 현재 날씨 정보
    target_weather = target['weatherContents']
    return target_weather


genre_dict = {
    28: '액션',
    12: '어드밴쳐',
    16: '애니매이션',
    35: '코미디',
    80: '범죄',
    99: '다큐멘터리',
    18: '드라마',
    10751: '가족',
    14: '판타지',
    36: '역사',
    27: '공포',
    10402: '음악',
    9648: '미스터리',
    10749: '로맨스',
    878: 'SF',
    10770: 'TV 영화',
    53: '스릴러',
    10752: '전쟁',
    37: '서부'
}

weather_genre = {
    '맑음' : [10751,10402,10749,35,16,10770,28],
    '구름' : [9648,80,28,36,878],
    '비' : [27,80,99,18,53,10752,16],
    '눈' : [10751,35,10749,36,878,10770],
    '흐림' : [9648,14,53,10752,12]
}

# 지우면 안돼
###################################################################################################

def today_weather():
    target_weather = get_weather()
    # 날씨 -> 간편화 value 로 key 찾아야해
    weather_short = {
        '맑음' : ['맑음','하늘상태 변화없음','비끝남','눈끝남','안개끝','구름없음',],
        '구름' : ['구름조금','연기','이슬비끝','구름 생성/발달','구름많음','공중먼지','연무'],
        '비' : ['강한비단속(매시15mm이상)','격심한소나기','보통이슬비 단속(시정0.5~1km)','약한비단속(매시3mm이하)','소나기끝','약/보통뇌우','약한소나기','보통비계속(매시3~15mm)'],
        '눈' : ['소낙눈/소낙진눈개비끝','보통/강한얼비 우빙발생','약한소낙눈','약한 진눈개비','보통/강한소낙눈'],
        '흐림' : ['흐림','안개','안개,하늘보임(강해짐)','안개,하늘안보임(약해짐)']
    }
    for k,v in weather_short.items():
        if target_weather in v:
            target = k
    
    data ={
        'weather_status': target,
    }
    return target



def get_movie2():
    total_genre_num = len(Genre.objects.all())
    if not total_genre_num:
        for k,v in genre_dict.items():
            genre = Genre()
            genre.genre = v
            genre.save()

    random_num = random.randint(1,50)
    BASE = 'https://api.themoviedb.org/3'
    path = f'/movie/popular'
    params = {
        'api_key' : '599d9943faf8858722e82a75833aa6b0',
        'region' : 'KR',
        'language' : 'ko',
        'page' : f'{random_num}',
    }
    response2 = requests.get(BASE+path,params=params).json()
    go_to_db = response2['results']
    # db 저장
    data = []
    for i in go_to_db:
        ######################################################################
        movie_data = {}
        movie_data['title'] = i['title']
        movie_data['description'] = i['overview']
        movie_data['poster_url'] = i['poster_path']
        movie_data['rating'] = i['vote_average']
        movie_data['release_date'] = i['release_date']
        movie_data['genre_ids'] = i['genre_ids']
        movie_data['movie_id'] = i['id']
        # 배우 목록, 크루 목록 요청

        # movie = Movie()
        # movie.movie_id = i['id']
        # movie.rating = i['vote_average']
        # movie.release_date = i['release_date']
        # movie.save()
        data.append(movie_data)
    return data


@api_view(['GET'])
def today_movie(request):
    data = get_movie2()
    return Response(data)


@api_view(['GET'])
def recommend_today_movie(request):
    total_movie = Movie.objects.all()
    today = today_weather()
    new_genre_dict = dict()
    for k,v in weather_genre.items():
        genre_list = []
        for i in v:
            value = genre_dict[i]
            genre_list.append(value)
        new_genre_dict[k]=genre_list

    for key,value in new_genre_dict.items():
        if key == today:
            recommend_genre = value
    
    
    recommend_genre_id = []

    for key,value in genre_dict.items():
        if value in recommend_genre:
            recommend_genre_id.append(key)
    data = get_movie2()
    
    recommend_data = []
    for movie in data:
        for reco in movie['genre_ids']:
            if reco in recommend_genre_id:
                recommend_data.append(movie)
    
    for movie in recommend_data:
        genre_word = []
        for genre in movie['genre_ids']:
            genre_word.append(genre_dict[genre])
        movie['genre_word'] = genre_word
    
    data = []
    for reco in recommend_data:
        if total_movie.filter(movie_id=reco['movie_id']).exists() == 0:
            movie = Movie()
            movie.title = reco['title']
            movie.description =  reco['description']
            movie.poster_url = reco['poster_url']
            movie.rating = reco['rating']
            movie.release_date = reco['release_date']
            movie.movie_id = reco['movie_id']
            movie.save()
            for genre_name in reco['genre_word']:
                movie_genre = Genre.objects.get(genre=genre_name)
                movie.genre.add(movie_genre)
        if reco not in data:
            data.append(reco)
    
    return Response(data[:5])



@api_view(['GET'])
def recoomend_random_movie(request):
    today = today_weather()
    new_genre_dict = dict()
    for k,v in weather_genre.items():
        genre_list = []
        for i in v:
            value = genre_dict[i]
            genre_list.append(value)
        new_genre_dict[k]=genre_list

    for key,value in new_genre_dict.items():
        if key == today:
            recommend_genre = value
    

    recommend_genre_id = []

    for key,value in genre_dict.items():
        if value in recommend_genre:
            recommend_genre_id.append(key)
    data = get_movie2()
    
    recommend_data = []
    for movie in data:
        for reco in movie['genre_ids']:
            if reco in recommend_genre_id:
                recommend_data.append(movie)


    for movie in recommend_data:
        genre_word = []
        for genre in movie['genre_ids']:
            genre_word.append(genre_dict[genre])
        movie['genre_word'] = genre_word

    random_movie = random.choice(recommend_data)
    total_movie = Movie.objects.all()
    if total_movie.filter(movie_id=random_movie['movie_id']).exists() == 0:
        movie = Movie()
        movie.title = random_movie['title']
        movie.description = random_movie['description']
        movie.poster_url = random_movie['poster_url']
        movie.rating = random_movie['rating']
        movie.release_date = random_movie['release_date']
        movie.movie_id = random_movie['movie_id']
        movie.save()
    
    return Response(random_movie)


@api_view(['GET'])
def movie_detail(request,movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)

    BASE = 'https://api.themoviedb.org/3'
    params = {
        'api_key' : '599d9943faf8858722e82a75833aa6b0',
        'region' : 'KR',
        'language' : 'ko',
    }

    # 배우 3명 추리기
    actors = []
    cast_data = requests.get(BASE+f'/movie/{movie.movie_id}/credits', params=params).json()['cast']
    cast_data.sort(key=lambda x: -x['popularity'])
    for name in cast_data:
        actors_name = name['name']
        actors_profile = name['profile_path']
        actors_dict = {
            'name' : actors_name,
            'profile_path' : actors_profile,
        }
        actors.append(actors_dict)

    actors = actors[:3]
    for a in actors:
        actor = Actor()
        actor.name  = a['name']
        actor.poster_url = a['profile_path']
        actor.save()
        actor.movies.add(movie)
    # 권수린 유튜브 키'AIzaSyBOMakqw2Jx55mxTm34ALe3O2rOPh8rvIA'
    YBASE = 'https://www.googleapis.com/youtube/v3/search'
    yparams = {
        'key' : 'AIzaSyBOMakqw2Jx55mxTm34ALe3O2rOPh8rvIA',
        'q': f'{movie.title}',
        'type': 'video',
        'part': 'snippet'
    }

    total_movie_youtube = Youtube.objects.filter(movie_id=movie.id)
    youtube_data = requests.get(YBASE, params=yparams).json()['items'][:5]
    for i in range(5):
        youtube = Youtube()
        if total_movie_youtube.filter(youtube_link='https://www.youtube.com/embed/'+f'{youtube_data[i]["id"]["videoId"]}').exists() == False:
            youtube.youtube_link = 'https://www.youtube.com/embed/'+f'{youtube_data[i]["id"]["videoId"]}'
            youtube.youtube_thumbnail = youtube_data[i]['snippet']['thumbnails']['default']['url']
            youtube.movie = movie
            youtube.save()

    youtube = []
    for you in youtube_data:
        data = {}
        # print(you['id']['videoId'])
        data['link'] = 'https://www.youtube.com/embed/'+ you['id']['videoId']
        data['thumbnails'] = you['snippet']['thumbnails']['default']['url']
        youtube.append(data)
        
    # 감독
    crew_data = requests.get(BASE+f'/movie/{movie.movie_id}/credits', params=params).json()['crew']

    for crew in crew_data:
        if crew['job'] == 'Director':
            director = {'name': crew['name'], 'profile':crew['profile_path']}

    serializer = MovieDetailSerializer(movie)

    detail_data = {}
    detail_data['movie_detail'] = serializer.data
    detail_data['actors'] = actors
    detail_data['director'] = director
    detail_data['youtube'] = youtube
    return Response(detail_data)

# 지우면 안돼
# now
######################################################################
def get_now_weather():
    # 날씨 검색
    now = datetime.datetime.now()
    url = 'http://data.ex.co.kr/openapi/restinfo/restWeatherList?'
    params = {
        'key' : '2958097790',
        'type' : 'json',
        'sdate' : f'{int(now.strftime("%Y%m%d"))}',
        'stdHour' : f'{now.strftime("%H")}',
    }
    response = requests.get(url,params=params).json()
    target = response['list'][0]

    ## 현재 날씨 정보
    target_weather = target['weatherContents']
    return target_weather

def now_weather():
    target_weather = get_weather()
    # 날씨 -> 간편화 value 로 key 찾아야해
    weather_short = {
        '맑음' : ['맑음','하늘상태 변화없음','비끝남','눈끝남','안개끝','구름없음',],
        '구름' : ['구름조금','연기','이슬비끝','구름 생성/발달','구름많음','공중먼지','연무'],
        '비' : ['강한비단속(매시15mm이상)','격심한소나기','보통이슬비 단속(시정0.5~1km)','약한비단속(매시3mm이하)','소나기끝','약/보통뇌우','약한소나기','보통비계속(매시3~15mm)'],
        '눈' : ['소낙눈/소낙진눈개비끝','보통/강한얼비 우빙발생','약한소낙눈','약한 진눈개비','보통/강한소낙눈'],
        '흐림' : ['흐림','안개','안개,하늘보임(강해짐)','안개,하늘안보임(약해짐)','박무']
    }
    for k,v in weather_short.items():
        if target_weather in v:
            target = k
    
    data ={
        'weather_status': target,
    }
    return target




@api_view(['GET'])
def recommend_now_movie(request):
    today = now_weather()
    new_genre_dict = dict()
    for k,v in weather_genre.items():
        genre_list = []
        for i in v:
            value = genre_dict[i]
            genre_list.append(value)
        new_genre_dict[k]=genre_list
    
    for key,value in new_genre_dict.items():
        if key == today:
            recommend_genre = value
    
    recommend_genre_id = []

    for key,value in genre_dict.items():
        if value in recommend_genre:
            recommend_genre_id.append(key)
    data = get_movie2()
    
    recommend_data = []
    for movie in data:
        for reco in movie['genre_ids']:
            if reco in recommend_genre_id:
                recommend_data.append(movie)



    for movie in recommend_data:
        genre_word = []
        for genre in movie['genre_ids']:
            genre_word.append(genre_dict[genre])
        movie['genre_word'] = genre_word

    data = []
    for reco in recommend_data:
        if reco not in data:
            data.append(reco)
    
    return Response(data[:5])


# keyword_recommend
######################################################################
@api_view(['GET'])
def keyword_recommend(request,keyword):
    weather_genre = {
        '맑음' : [10751,10402,10749,35,16,10770,28],
        '구름' : [9648,80,28,36,878],
        '비' : [27,80,99,18,53,10752,16],
        '눈' : [10751,35,10749,36,878,10770],
        '흐림' : [9648,14,53,10752,12]
    }
    data = get_movie2()
    
    recommend_data = []
    for movie in data:
        for reco in movie['genre_ids']:
            if reco in weather_genre[keyword]:
                recommend_data.append(movie)

    genre_dict = {
        28: '액션',
        12: '어드밴쳐',
        16: '애니매이션',
        35: '코미디',
        80: '범죄',
        99: '다큐멘터리',
        18: '드라마',
        10751: '가족',
        14: '판타지',
        36: '역사',
        27: '공포',
        10402: '음악',
        9648: '미스터리',
        10749: '로맨스',
        878: 'SF',
        10770: 'TV 영화',
        53: '스릴러',
        10752: '전쟁',
        37: '서부'
    }

    for movie in recommend_data:
        genre_word = []
        for genre in movie['genre_ids']:
            genre_word.append(genre_dict[genre])
        movie['genre_word'] = genre_word
    
    print(recommend_data)
    data = []
    total_movie = Movie.objects.all()
    for reco in recommend_data:
        if total_movie.filter(movie_id=reco['movie_id']).exists() == 0:
            movie = Movie()
            movie.title = reco['title']
            movie.description =  reco['description']
            movie.poster_url = reco['poster_url']
            movie.rating = reco['rating']
            movie.release_date = reco['release_date']
            movie.movie_id = reco['movie_id']
            movie.save()
            for genre_name in reco['genre_word']:
                movie_genre = Genre.objects.get(genre=genre_name)
                movie.genre.add(movie_genre)
        if reco not in data:
            data.append(reco)
    
    return Response(data[:5])



# reviews
######################################################################

@api_view(['POST'])
def create_review(request,movie_id):
    movie= get_object_or_404(Movie, movie_id = movie_id)
    if movie.review_set.filter(user=request.user).exists() == False:
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'DELETE', 'PUT'])
def review(request, review_id):
    review = get_object_or_404(Review, id = review_id)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if review.user == request.user:
            review.delete()
            data = {
                'data' : f'{review_id}번 댓글이 삭제되었습니다.'
            }
            return Response(data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
