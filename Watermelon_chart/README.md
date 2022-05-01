# Watermelon-Chart 🍉

#### GUI 를 사용하여 멜론차트의 일간/주간/월간 차트를 검색할 수 있도록 하여 , 기존의 음원사이트에 접속해야하는 부분 을 간소화 시킴 
#### 차트(순위, 가수, 곡정보 등)는 SQL을 이용하여 DB에 저장하고, 원하는 앨범 재킷은 Mongo DB를 통하여 저장 가능하도록 하였다. 

‣ crawling.py : 멜론차트의 일간/주간/월간 차트를 가져옴  
‣ database.py : 가져온 차트를 SQL에 저장  
‣ gui.py : 서비스 화면을 구성  
‣ main.py : 서비스 실행  (해당파일을 키면 연동)
‣ mongoDB.py : 앨범 재킷을 MongoDB에 저장

#### 권장 OS : window 
