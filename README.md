# celery-rabbitmqTest

1. 샐러리 실행(rabbitMQ 서버 실행 여부 체크 필요)<br>
celery -A mysite worker --loglevel=info

2. 서버 실행<br>
python manage.py runserver 

3. postman으로 api 테스트<br>
<img src="https://user-images.githubusercontent.com/59545680/141643132-24d9ed1e-619c-4c5e-b5e1-6ea06cbcc28b.png" width="70%"><br>

4. 샐러리 로그에서 결과 확인<br>
<img src="https://user-images.githubusercontent.com/59545680/141643380-6c9f517f-1b8f-4e0f-bb71-83e005a7291b.png" width="100%"><br>

4. 폴더 내에 DB 파일 확인<br>
<img src="https://user-images.githubusercontent.com/59545680/141643188-8c955107-70dd-40aa-94f4-733cb7834d9b.png" width="70%"><br>

5. auth_user, django_celery_results_taskresult 테이블 확인<br>
<img src="https://user-images.githubusercontent.com/59545680/141643456-d70b4962-3d75-4f75-8b6b-bc65d63e5cfb.png" width="100%"><br>
<img src="https://user-images.githubusercontent.com/59545680/141643458-5c2da3a1-3416-4d61-9cb7-45fb2a81725a.png" width="100%"><br>
