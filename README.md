# 제목
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

## 실행예제
```

```

```
코드를 실행하면 나오는 내용에 대한 코드
```

## 동작 내용
본 패키지 함수 호출시 
- Transform 처리가 완료된 파일을 import한 다음
- ~/data/DE32_megabox/load 디렉토리 안에 데이터를 일자별로 export합니다.
- 모든 데이터는 parquet 파일로 저장되며 일자별로 디렉토리가 자동생성되어집니다.
- https://github.com/DE32megabox/ 일련과정의 데이터는 2021년의 데이터를 기준으로 작업됩니다.

