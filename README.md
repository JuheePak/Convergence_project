### Convergence_Project

### `공장 화재 예방을 위한 영상 데이터 기반 스마트 화재 감지 서비스(불死조)`

1. 팀명: 119조
2. 팀원: 박주희, 김규영, 이영현, 김가현, 박진수, 김유진
3. 프로젝트 수행방향

- Bigdata

  - IoT에서 받은 영상 데이터 수집/전처리(전처리는 AI반과 같이 진행)
  - IoT에서 받은 열, 가스 센서 데이터 전처리
  - 화재 관련 변수(날씨, 온도, 습도 데이터 등)의 상관관계 분석
  - 화재 발생 데이터 분석을 통해 화재 감시 시스템 입지 선정 및 지도 시각화
  - 화재 감지 카메라/센서 설치 시 가장 효율적으로 작동할 수 있는 위치 선정

- AI

  - IoT에서 받은 CCTV 영상 데이터를 이미지로 변환(전처리는 Bigdata반과 같이 진행)
  - 화재로 이어지는 불씨가 생기는지 실시간으로 학습/예측하여 화재 초기 감지
  - 화재 발생 시 IoT반에 결과를 바로 전송

- IoT

  - CCTV 영상 데이터 수집
  - 아두이노 센서 제어(가스, 열 감지 등)
  - 디바이스 구현(형태/작동 방식)
  - 안드로이드 어플리케이션 구현
  - 아두이노, 라즈베리파이 통신

- Cloud

  - 데이터베이스 서버(RDS) 구축(화재 관련 데이터)
  - S3 생성 및 관리(이미지, 영상 데이터)
  - IoT MQTT 서버 구축(기기간 통신)
- 각 기능간 이벤트 처리(SNS, CloudWatch)
  - 웹 페이지 제작 및 배포(영상 실시가 스트리밍 등)
  
  

4. 프로젝트 수행 도구

- Bigdata
  - Python(Selenium, Seaborn, Matplotlib, Folium, etc.)
  - Pyspark
  - MongoDB
  - R

- AI

  - AWS
  - 서버용 컴퓨터
  - Python

- IoT

  - 통합개발도구: VSC, 안드로이드
  - 디바이스: 라즈베리파이, 아두이노
  - UI: CSS, Javascript

- Cloud

  - Django

  - Docker

  - AWS

    

5. 일정관리

![New Sheet](https://user-images.githubusercontent.com/69948723/100039665-0a959e80-2e49-11eb-9b3a-f2bf1afc37a1.png)

- 과제 진행 사항은 slack으로 파악