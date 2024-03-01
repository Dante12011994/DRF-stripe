# Тестовый проект по интеграции платежной системы stripe 
# Выполнил: Гордеев А.В.

Запуск Docker контейнера

Установите Docker
Соберите образ Docker - sudo docker build -t your-python-app
Запустите Docker - sudo docker run -p 8000:8000 your-python-app, python manage.py runserver 0.0.0.0:8000
Создайте суперпользователя чтобы войти в административную панель

### Модели
Item:
  name - название товара
  description - описание товара
  price - стоимость товара

### Методы

GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item.
GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy.
