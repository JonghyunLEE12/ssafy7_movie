import requests

# 영화 데이터 db 저장 

def get_movie():
    # genre_list = [
    #     'Action','Animation','Comedy','Crime','Documentary',
    #     'Drama','Family','Fantasy','History','Horror',
    #     'Music','Mystery','Romance','Science','Fiction','Thriller',
    #     'TV Movie','War','Western'
    # ]

    BASE = 'https://api.themoviedb.org/3'
    path = '/genre/movie/list'
    params = {
        'api_key' : '599d9943faf8858722e82a75833aa6b0',
    }
    response1 = requests.get(BASE+path,params=params).json()
    genre_target = response1['genres']
    # print(genre_target[1]['id'])
    
    for i in range(len(genre_target)-1):
        BASE = 'https://api.themoviedb.org/3'
        path = f'/movie/{genre_target[i]["id"]}/similar'
        params = {
            'api_key' : '599d9943faf8858722e82a75833aa6b0',
            'region' : 'KR',
            'language' : 'ko',
        }

        response2 = requests.get(BASE+path,params=params).json()
        print(response2)








    # Json 형식으로 data에 저장


get_movie()