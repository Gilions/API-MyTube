# API для MyTube


API для социальной сети MyTube. Предоставляет возмодность используя API создавать/удалять/обновлять посты, группы и комментарии.
Подписываться/отписываться на авторов.

Данный проект разрабатывался в рамках обучающей программы курсов Yandex Практикум.
Цель данного проекта, изучить возможность REST API

##  Установка
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
