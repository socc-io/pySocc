# SOCC API Server (Python Flask)
##Run
```sh
python run.py
```
or
```sh
uwsgi wsgi.ini
```
##Requirements
* flask
* flask_login
* flask_admin
* flask_sqlalchemy
* pytest
* pymysql
* SQLAlchemy
* sqlalchemy_utils

위의 모듈들을 설치해야한다.

```sh
sudo python -m pip install -r requirements.txt
```

### Database 연동

 /app/configure.py
 MYSQL Configuration set

## testment

```sh
pytest
```

## TODO

TODO는 기본적으로 Model을 중심으로 나열되어 있습니다. 각 항목은 항목명을 이름으로하는 Model을 다루는 Service, Controller전반에 대한 Task를 의미합니다.

각 항목의 완성도에 따른 체크 여부는 그 항목을 개발한 분의 주관으로 판단하셔도 됩니다. 각 모델에 대하여 기본적인 CRUD만 제대로 동작한다면 체크하셔도 될 것 같습니다.

TODO리스트는 Model중심으로 나열되어있습니다. 자식항목들이 있는 것은, 부모항목과 자식항목이 OneToMany Relation를 가지고 있음을 의미합니다.

OneToOne, ManyToMany를 TODO에서 표현하지 않았습니다. 세부 마크다운에서 확인해주세요.

- [x] [Study](md/TODO_Study.md) 
      - [x] [StudyIssue](md/TODO_StudyIssue.md)
- [x] Event
      - [x] EventComment
      - [x] EventAttendance
- [x] User

- [ ] Change controller style to `Method Views for APIs` in http://flask.pocoo.org/docs/0.12/views/
## 기타

* None
