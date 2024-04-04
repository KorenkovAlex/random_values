# **Отправки случайных значений в СУБД PostgreSQL через брокер сообщений RabbitMQ**

## ****Описание****
Запуск в docker-compose контейнеров позволяет отправлять случайные значения в PostgreSQL через RabbitMQ.
Создается по одному контейнеру для RabbitMQ и producer(отправитель), а для consumer(получатель) - 2 контейнера. Это позволяет использовать параллельное использование из одной очереди.
Для подключения к RabbitMQ используется библиотека Pika на Python.
Для подключения к PostgreSQL используется Psycord2.

## ****Использованные технологии****
- [Python](https://www.python.org/) - язык программирования;
- [RabbitMQ](https://www.rabbitmq.com/)- программный брокер сообщений на основе стандарта AMQP, тиражируемое связующее программное обеспечение, ориентированное на обработку сообщений;
- [PostgreSQL](https://www.postgresql.org/) - объектно-реляционная система управления базами данных (СУБД);
- [Docker)](https://www.docker.com/) - платформа контейнеризации с открытым исходным кодом;
- [Pika](https://pika.readthedocs.io/en/stable/) - данная библиотека обеспечивает отличный баланс между простотой и функциональностью для большинства сценариев работы с rabbitmq;
- [Psycord2](https://pypi.org/project/psycopg2/) - модуль для подключения к PostgreSQL, выполнения SQL-запросов и других операций с базой данных;

## ****Установка проекта****
#### Подключение проекта и запуск:
 - [ ] Клонируйте проект с GitHub:
```
git clone git@github.com:ваш_аккаунт/foodgram-project-react.git
```
 - [ ] Запуск программы(поднять сеть контейнеров:
```
docker compose up
```
 - [ ] Просмотр запущенных контейнеров:
```
docker ps
```
 - [ ] Удалить контейнеры, сеть, тома, образы
```
docker-compose down -v --rmi all --remove-orphans
```
## **Автор**
- Алексей Коренков
