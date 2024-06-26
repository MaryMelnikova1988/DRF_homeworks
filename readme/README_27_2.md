# DRF_homeworks
### 27.2 Docker Compose

Критерии выполнения заданий
1. Оформили Dockerfile.
2.  Оформили файл docker-compose.yaml.
3.  Инструкции по запуску находятся в файле Readme.
4.  Результат выполнения всего задания залили в GitHub и сдали в виде ссылки на репозиторий.
5. Для выполнения заданий используйте проект для онлайн-обучения, над которым вы работали в рамках домашних заданий на курсе DRF.

Задачи
1. Опишите Dockerfile для запуска контейнера с проектом.
2.  Оберните в Docker Compose Django-проект с БД PostgreSQL.
3.  Допишите в docker-compose.yaml работу с Redis.
4.  Допишите в docker-compose.yaml работу с Celery.


## Запуск проекта с помощью Docker Compose

Для запуска проекта с помощью Docker Compose выполните следующие шаги:

1. Установите Docker и Docker Compose, если они еще не установлены на вашем компьютере.
2. Соберите и запустите контейнеры Docker.
3. Откройте браузер и перейдите по адресу http://localhost:8000 для доступа к проекту.

* Сборка образов: docker-compose build
* Запуск контейнеров: docker-compose up
* Запуск контейнеров в фоне: docker-compose up -d
* Сборка образа и запуск в фоне после успешной сборки: docker-compose up -d —build
* Выполнение команды внутри контейнера app: docker-compose exec app <здесь ваша команда>
* Остановка контейнеров: docker-compose stop
* Удаление контейнеров: docker-compose down

* Проверка в shelle всех запущенных и остановленных контейнеров: docker ps -a 

