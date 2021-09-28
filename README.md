# chandori 소개
해당 저장소는 가계부 사이트를 구현한 프로젝트입니다.

## 사용법 (Windows 기준)
해당 프로젝트의 경로에서 쉘을 열어 아래의 명령어를 순서대로 입력합니다.

파이썬 가상환경 설정   
python -m venv myvenv   
source myvenv/Scripts/activate   

필요한 파이썬 라이브러리 다운로드   
pip install -r requirements.txt

경로 이동   
cd chandori

데이터베이스 설정   
python manage.py makemigrations   
python manage.py migrate

서버 실행   
python manage.py runserver


## 웹브라우저에서 아래의 주소 입력 후 접속
http://127.0.0.1:8000/
