### Convergence_Project

### `산업시설 화재 예방을 위한 영상 데이터 기반 스마트 화재 감지 서비스(불死조)`

1. ##### 팀명: 119조

2. ##### 팀원: 박주희, 김규영, 이영현, 김가현, 박진수, 김유진

3. ##### 프로젝트 목적:

  소방청에 따르면 2019년 한 해에 화재 발생 건수는 40,000건 이상으로, 약 8조5천억원 이상의 재산 피해와 2,515명의 인명 피해를 입었다고 한다. 그 중 공장시설, 창고, 작업장 등을 포함한 산업시설에서 발생한 재산 피해 금액이 약 3억 4천만원으로 가장 큰 부분을 차지했다. 

  119조는 이번 프로젝트를 통해 산업시설에 스마트 화재 감지 서비스를 도입하여 화재를 예방하고 피해를 줄이고자 한다. 

   기존 화재 경보 및 화재 식별 시스템은 컴퓨터 비전에 의한 탐지와 연기, 가스 등의 센서 기술을 배경으로 하며, 사람이 센서를 확인해야 한다.

  이를 개선하고자 CCTV 영상 데이터를 활용하여 딥러닝으로 이미지 데이터를 학습/예측하여 화재를 초기에 감지하고, 화재 탐지 정확도를 높이고자 한다. 또 화재 경보 시스템의 센서 데이터를 수집/분석하여 산업 시설 내에 센서와 CCTV 위치를 선정하는 작업을 통해 시스템의 효율성을 높이고, 사람의 개입을 줄여 사람으로 인해 발생될 수 있는 오류를 방지할 수 있다.

  후에 연구 결과가 민간에 도입되었을 때 화염과 연기로 인해 소방관들의 잘못된 출동 건수를 감소하여 불필요한 비용을 절감하고 인력 낭비를 줄일 수 있을 것으로 예상한다

4. ##### 프로젝트 수행방향

- `Bigdata`

  - IoT에서 받은 영상 데이터 수집/전처리(전처리는 AI반과 같이 진행)

  - IoT에서 받은 열, 가스 센서 데이터 전처리

  - 해당 시스템 도입 입지 선정 및 지도 시각화

    (소방청 연간화재통계 데이터, 기상청 기상관측 데이터)

  - 화재 감지 카메라/센서 설치 시 가장 효율적으로 작동할 수 있는 위치 선정

- `AI`

  - IoT에서 받은 CCTV 영상 데이터를 이미지로 변환(전처리는 Bigdata반과 같이 진행)
  - 화재로 이어지는 불씨가 생기는지 실시간으로 학습/예측하여 화재 초기 감지
  - 화재 발생 시 IoT반에 결과를 바로 전송

- `IoT`

  - CCTV 영상 데이터 수집
  - 아두이노 센서 제어(가스, 열 감지 등)
  - 디바이스 구현(형태/작동 방식)
  - 안드로이드 어플리케이션 구현
  - 아두이노, 라즈베리파이 통신

- `Cloud`

  - 데이터베이스 서버(RDS) 구축(화재 관련 데이터)
  - S3 생성 및 관리(이미지, 영상 데이터)
  - IoT MQTT 서버 구축(기기간 통신)
  - 각 기능간 이벤트 처리(SNS, CloudWatch)
  
  - 웹 페이지 제작 및 배포(영상 실시가 스트리밍 등)
  
  

5. ##### 프로젝트 수행 도구

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

    

6. ##### 일정관리

![New Sheet (1)](https://user-images.githubusercontent.com/69948723/100064282-a806c780-2e75-11eb-894a-a260b75b374d.png)

- 과제 진행 사항은 slack으로 파악