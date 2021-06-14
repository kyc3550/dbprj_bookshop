># 데이터베이스 수업시간 기말 프로젝트로 작성한 <br> 인터넷 서점
>>## 요구사항 정리
>>>### 수업시간 교수님의 요구사항
>>>![image](https://user-images.githubusercontent.com/66798060/121952659-83355b80-cd97-11eb-99bc-2432370759aa.png)
>>>![image](https://user-images.githubusercontent.com/66798060/121952754-9f38fd00-cd97-11eb-800b-0752f1eb5303.png)
>>>### 사용자의 권한 및 업무 내용
>>>![image](https://user-images.githubusercontent.com/66798060/121952829-b841ae00-cd97-11eb-82e6-58fdafa119f8.png)
>>>### 추가사항
>>>![image](https://user-images.githubusercontent.com/66798060/121952885-c98aba80-cd97-11eb-8c86-51172911bcee.png)
>>>### er다이어그램
>>>![image](https://user-images.githubusercontent.com/66798060/121952928-da3b3080-cd97-11eb-8e7d-174dcf8f6b86.png)
>>>### 테이블명세서
>>>![image](https://user-images.githubusercontent.com/66798060/121953203-3b630400-cd98-11eb-99e7-abd31c93ddf2.png)
>>>![image](https://user-images.githubusercontent.com/66798060/121953231-4453d580-cd98-11eb-9005-063e2655bc77.png)
>>>![image](https://user-images.githubusercontent.com/66798060/121953283-52a1f180-cd98-11eb-9e37-26edbd794e4c.png)
>>>![image](https://user-images.githubusercontent.com/66798060/121953314-5cc3f000-cd98-11eb-98dc-6cc0f4263b98.png)


>## 구현 사진
>>### 구현 테이블 (Model)
>>#### Model 은 aws의 mysql을 장고와 연동하여 사용하였고, <br> MYSQL Workbench를 사용하여 장고ORM으로 구현된 테이블을 확인 하였다
>>>### auth_user
>>>![image](https://user-images.githubusercontent.com/66798060/121955055-70705600-cd9a-11eb-8650-f13537fc9d59.png)
>>>### accounts_address
>>>![image](https://user-images.githubusercontent.com/66798060/121955061-723a1980-cd9a-11eb-978f-7fdd949ba83b.png)
>>>### accounts_card
>>>![image](https://user-images.githubusercontent.com/66798060/121955073-7403dd00-cd9a-11eb-92ee-7a4354d71c6f.png)
>>>order_order
>>>![image](https://user-images.githubusercontent.com/66798060/121955080-75cda080-cd9a-11eb-9363-ba8b439b2fb0.png)
>>>Cart
>>>![image](https://user-images.githubusercontent.com/66798060/121955088-782ffa80-cd9a-11eb-8ab2-3539b7c475c5.png)
>>>CartItem
>>>![image](https://user-images.githubusercontent.com/66798060/121955098-7a925480-cd9a-11eb-92b6-c16c79e81c46.png)
>>##구현 화면
>>>### 메인페이지
>>>![image](https://user-images.githubusercontent.com/66798060/121955515-05734f00-cd9b-11eb-80e3-a87e316d71c0.png)
>>>### 회원가입 페이지
>>>![image](https://user-images.githubusercontent.com/66798060/121955520-073d1280-cd9b-11eb-8e1b-4b186341ceec.png)
>>>### 프로필 페이지
>>>![image](https://user-images.githubusercontent.com/66798060/121955543-0d32f380-cd9b-11eb-90a9-bd153e7e4921.png)
>>>### 디테일 페이지
>>>![image](https://user-images.githubusercontent.com/66798060/121955551-115f1100-cd9b-11eb-80cc-729b4437c9a1.png)
>>>### 장바구니 페이지
>>>![image](https://user-images.githubusercontent.com/66798060/121955563-1328d480-cd9b-11eb-9e18-437a7760571f.png)
>>>### 주문 페이지
>>>![image](https://user-images.githubusercontent.com/66798060/121955570-158b2e80-cd9b-11eb-89a7-797f49c879f7.png) 
>>> 
>># 후기
>>>##### 과제의 내용은 데이터베이스를 활용한 응용프로그램(어떠한 것도 상관없음 ex)웹, 앱, 프로그램...)을 실제 구현하는 것이였다. 과제의 내용을 봤을때 공부하고있던 장고라는 프레임워크로 과제를 해결하는것이 가장 효율적이고 구현이빠르며 개발자 서버 (py manage.py runserver)를 활용하여 발표또한 쉽게 할 수 있을것이라고 생각했다.
>>>##### 과제의 시작은 교수님이 주신 사용자의 요구명세서를 바탕으로 프로그램을 구현할 때 필요한 데이터들을 스스로 찾아 er다이어그램 작성을 요구하셨고 모든 학생들에게 제출을 받으셨다. 그 결과 내가 작성한 er다이어그램이 교수님이 원하던 er다이어그램과 가장 흡사하여 플러스 점수을 받았고 내가그린 er다이어그램이 수업자료로 활용되었다. 명세서에 적힌 내용을 개발자로써 이해하고 내가 직접 코딩으로 사용자에게 필요한 기능을 제공해주는것이 너무 재미있었고 교수님에게 인정까지 받으니 테이블 구현(Model) 뿐 아니라 요구사항에 적힌 기능들(View) 또한 열심히 하여 모든 조건을 충족하고싶은 욕심이 생겼다.
>>>#### 그 결과 교수님이 주신 명세서의 모든 조건을 충족시키는 웹 사이트를 만들었고 발표또한 성공적으로 하여 좋은 점수를 받았다.
>>>#### 한가지 아쉬운점은 html, css, js 같은 프론트 부분의 언어의 숙지가 되어있지않아 인터넷에있는 부트스르랩, 블로그 등의 기본 템플릿을 가지고 구현하였다. 웹개발에 필요한 기본적인 기능들(CRUD)을 완벽히 할 수 있게되면 사용자에게 보여지는 부분을 구현하는 언어도 공부해보고싶다.
