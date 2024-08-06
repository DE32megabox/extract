# movie_extract/movie_e.py
해당 년월의 영화 데이터 추출 모듈

## 설치방법
- repository 설치 방법

```
git clone https://github.com/DE32megabox/extract.git
```
- repository 설치 이후 환경설정 
```
pdm init
pdm install
source .venv/bin/activate
```
- 개발환경에 브랜치 설정
```
git branch release/d1.0.0
git checkout release/d1.0.0

git branch dev/d1.0.0
git checkout dev/d1.0.0
```

## 사용법
- url 생성하고, api 활용을 위한 key값 받아오기
```
def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def gen_url(dt="20210101", url_param={}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    for key, value in url_param.items():
        url = url + f"&{key}={value}"

    print(f"url: {url}")
    return url
```

- 데이터 요청
```
def req(load_dt="20210101", url_param={}):
    url = gen_url(load_dt, url_param)
    r = requests.get(url)

    code = r.status_code
    data = r.json()
    return code, data
```

- 데이터 받아와 데이터프레임 형식으로 저장
```
def req2df(load_dt='20210101', url_param={}):
    code, data = req(load_dt, url_param)
    movie = data['boxOfficeResult']['dailyBoxOfficeList']
    df = pd.DataFrame(movie)
    print(df)
    return df
```

