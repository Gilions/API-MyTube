# API для MyTube
API для социальной сети MyTube.

На сайте можно создать темотические группы по интересам.

Реализована возможность публиковать посты в группах либо без группы.

Существует возможность комментировать опубликованные посты, подписываться на авторов.

# Работа с API
## Получение JWT-токена:

POST запрос URL api/v1/token/

Обязательные поля:

- username
- password

## Работа с постами.

Публикация поста:

POST запрос URL api/v1/posts/

Обязательное поле "text"

В поле group указывается id  ранее созданной группы.

Получить список всех опубликованных постов можно отправив GET запрос на URL api/v1/posts/

Для получения данных конкретного поста необходимо отправить GET запрос на URL api/v1/posts/id_post

"id_post" - номер нужного поста.

По данному URL можно оформить PUT и PATCH запросы для изменения данных нужного поста.

Удаление поста:

DELETE запрос на URL api/v1/posts/id_post

"id_post" - номер нужного поста.

Удалить пост может только автор, либо администратор сайта.
## Работа с группами

Создание группы:

POST запрос на URL api/v1/group/

Обязательное поле "title"

Получить список созданных групп:

GET запрос на URL api/v1/group/
## Комметарии

Добавить комментарий к посту:

POST запрос на URL api/v1/posts/id_post/comments/

Обязательное поле "text"

Просмотреть все комментарии к посту:

GET запрос на URL api/v1/posts/id_post/comments/

Посмотреть конкретный комментарий:

POST запрос на URL api/v1/posts/id_post/comments/comment_id/

Сайт поддерживает возможность изменять существующие комментарии:

PUT/PATCH - запрос на URL api/v1/posts/id_post/comments/

DELETE запрос на URL api/v1/posts/id_post/comments/comment_id/ - удалит комментарий

Удаление либо изменение комментариев доступно только автору либо администратору сайта.

## Подписка/отписка

Получиит список всех подпищиков:

GET запрос на URL /api/v1/follow/

[
  {
    "user": "string",
    "following": "string"
  }
]

Техническая документация доступна по URL redoc/

# Системные требования

- Python 3
- Django
- REST API Framework
- NGINX + Gunicorn

#  Установка
______


Потребуется Pytho3, проверьте версию Вашего Python командой:

`python3 --version`

Для установки Python на операционные системы Linux/Mac используйте команду:

`sudo apt update`

Для установки Python на Windows пройдите по ссылке

https://www.microsoft.com/ru-ru/p/python-37/9nj46sx7x90p?rtc=1&activetab=pivot:overviewtab

`sudo apt install python3-pip python3-venv git -y`

Будет установлен: Python3, venv(виртуальное окружение), GitHub


Клонируйте репозитарий командой:

`git clone https://github.com/Gilions/api_final_yatube.git`

В репозитарии проекта создайте вертуальное окружение:

`python3 -m venv venv & source venv/bin/activate`

Потребуется установка нужных пакетов, используйте:

`python -m pip install -r requirements.txt`

Запустите проект используя команду:

`python3 manage.py runserver`

Данный проект поддерживает только API
