# AWS LIGHTSAIL 내부에서 DOCKER를 사용하여 FastAPI 배포시 주의사항
## 1. /services/backend/src/env.py 개인 lightsail database 정보로 변경
## 2. 개인정보 보호를 위해 env.py 파일을 .gitignore에 추가

---

# Developing a Single Page App with FastAPI and Vue.js

### Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs).

## Want to use this project?

Build the images and spin up the containers:

```sh
$ yarn install
$ docker-compose up -d --build
```

Apply the migrations:

```sh
$ docker-compose exec backend aerich upgrade
```

Ensure [http://localhost:5000](http://localhost:5000), [http://localhost:5000/docs](http://localhost:5000/docs), and [http://localhost:8080](http://localhost:8080) work as expected.
