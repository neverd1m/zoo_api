### Мой первый опыт с DRF и django-filters

## Requirements.txt
asgiref==3.3.1
Django==3.1.3
django-filter==2.4.0
djangorestframework==3.12.2
pytz==2020.4
sqlparse==0.4.1

## Установка из терминала
`pip install requirements.txt`

## Запуск сервера
`cd zoo/`
`./manage.py runserver`

## Использование
Так как проверял я только в http представлении в браузере, то и пишу согласно тому, что успел потыкать.
Параметры CRUD полностью взяты из возможностей DefaultRouter, потому их описание укажу [тут](https://www.django-rest-framework.org/api-guide/routers/#defaultrouter).

Сортировка работает с помощью параметра **ordering** и поддерживает все поля моделей, обратная сортировка с помощью символа **-**.

Сортировка:
`http://127.0.0.1:8000/animal_types/?ordering=name`
`http://127.0.0.1:8000/shelters/?ordering=-created_at`

Стандартные фильтры:
`http://127.0.0.1:8000/animals/?created_at=2020-11-15`
`http://127.0.0.1:8000/animals/?animal_type=Млекопитающие`
`http://127.0.0.1:8000/animals/?staff=Дима`
`http://127.0.0.1:8000/animals/?shelter=Вольер`


Сложные фильтры:
`http://127.0.0.1:8000/animals/?staff=Дима&linked_duration=2019-11-14`
`http://127.0.0.1:8000/animals/?shelter_created=2020-11-10&shelter_updated=2020-11-16`

## Чего точно не хватает этому коду или мне O.o
* Тестов
* Миксинов
* Описание JSON представлений связанных моделей в serializers.py
* Исключений, т.к. некоторые комбинировнные фильтры возвращают базовый queryset
* Явно упустил какие-то возможности библиотек, т.к. не работал раньше с ними.


