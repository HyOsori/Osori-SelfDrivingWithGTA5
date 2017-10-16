# Osori-SelfDrivingWithGTA5
**GTA5**를 이용해 자율주행 자동차를 학습 시키는 프로젝트 <br>
[소개 ppt](https://github.com/HyOsori/Osori-SelfDrivingWithGTA5/blob/master/ppt/Self-Driving_Car_In_GTA5.ppt)

## 팀원(ABC 순)

1. [jhyang12345](https://github.com/jhyang12345)
2. [JiHyeonSEO](https://github.com/JiHyeonSEO)
3. [JunsuLime](https://github.com/JunsuLime)
4. [Sikurity](https://github.com/Sikurity)

## 팀장

### [Sentdex](https://github.com/Sentdex) (Harrison)<br>
[<img src="https://avatars1.githubusercontent.com/u/5905296?v=4&s=460" width="150px" />](https://github.com/Sentdex)

### 자료
https://github.com/Sentdex/pygta5 <br>
https://pythonprogramming.net/ <br>

## 목표
1. 파이썬(**Python3**)을 이용해 차량(캐릭터)를 조작

2. **OpenCV**를 이용해 **차선**, **사람**, **차량**, **신호등** 및 **표지판**을 인식

3. **목적지를 설정**해주면, **인간의 조작 없이 자율주행**으로만 도착하는 것을 목표<br>
    a. 차선, 사람, 차량, 신호등 및 표지판 정보를 이용해 **유한상태기계(Finite-state machine, FSM)로** 자율주행 구현<br>
      b. 차선, 사람, 차량, 신호등 및 표지판 정보를 이용해 **DQN(Deep Q Network – 딥러닝을 이용한 강화학습)으로** 학습하기<br>
     (**충돌 횟수**, **역주행 여부**, **네비게이션 경로에서 떨어진 거리** 등을 이용)

## 강좌

(필수) https://pythonprogramming.net/game-frames-open-cv-python-plays-gta-v/ <br>
(옵션) https://hunkim.github.io/ml/ <br>
(옵션) https://psyber.io <br>
(옵션) http://download.visinf.tu-darmstadt.de/data/from_games/index.html <br>

## 계획

### (~11월 말)
1. 강좌를 듣고, 자신의 Github에 상세한 한글 주석을 달아 업로드

### (~12월 초)
2. Python을 활용한 GTA 5 조작법과 기계학습 지식을 활용해 자율주행 구현 방식을 논의

### (~겨울방학)
3.  윤리의식을 함양한 자율주행 에이전트 개발 시작

### (발표 전)
4. 목적 달성여부를 확인하고, 오픈 소스로 배포…<br>
  a. 경로이탈 없이<br>
  b. 교통법규 준수<br>
  c. 인명피해 없이<br>
  d. 차량파손 없이<br>
  e. 목적지에 도착<br>

※ 오소리 회원분들 및 모든 개발자 분들의 관심(**Issue**, **Comment**, **Pull Request** 등)을 환영합니다.<br>
※ 시험 기간(**중간고사**/**기말고사**)에는 2주 가량 쉽니다<br>



자율주행 프로젝트를 위한 GTA5 운전중 단축키 모음: Cheat 입력창

1. `Q`,  `, `, `.`: Radio On/Off
2. `E`: Klaxon(경적) 울리기
3. `H`: Head Light On/Off
4. `R`, `V`: Camera 시점 변경
5. `P`: 상호 작용 메뉴
6. `C`: 뒤돌아보기
7. `M`: 빠른 GPS 설정
8. `Space Bar`: 사이드 브레이크
9. `Caps Lock`: 집중하기
10. `F12`: 스크린샷 저장

![GTA5_Cheat_Sheet](https://github.com/Sikurity/Osori-SelfDrivingWithGTA5/blob/master/resources/imgs/GTA5_Cheat_Sheet.png?raw=true)
