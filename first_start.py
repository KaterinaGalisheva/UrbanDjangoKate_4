'''создание нового проекта '''

# заходим в новую папку нового проекта 
# в терминал вводим команду: python -m venv venv 
 
# далее активируем екзешник командой в терминале 
# venv\Scripts\activate

# в комвндной строке терминала в самом начале должна появится надпись (venv)

# скомпоновать библиотека в файл 
# pip freeze > requirements.txt

# распаковка файла с библиотеками
# pip install -r requirements.txt

# установить Django с помощью pip: 
# pip install django

# Создание первого проекта в конце - это имя проекта
# django-admin startproject project

# Создание приложения внутри проекта, в конце - имя приложения на сервере
# cd project
# python manage.py startapp app
# подключить его в настройках

# создать таблицы в базе данных для всех приложений из списка INSTALLED_APPS в папке progect
# cd project
# python manage.py migrate

# фиксация изменений таблиц в базе данных из модуля models, 
# если есть необходимость создания своих таблиц
# python manage.py makemigrations

# заново создать таблицы в базе данных для всех приложений из списка INSTALLED_APPS в папке mysite
# cd progect
# python manage.py migrate

# Создание приложения внутри проекта, в конце - имя приложения на сервере
# python manage.py startapp app
# подключить его в settings.py

# создать папки (в папке с manage.py) templates для шаблонов html и 
# static для визуализации 
# подключить в settings.py
# 'DIRS': [BASE_DIR / 'templates'],
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Запуск сервера для разработки
# python manage.py runserver

# на папку выше
# cd ..


'''QuerySet запросы в БД (трансформация питона в sql)'''

# Открыть необходимый терминал
# python manage.py shell

# импорт таблицы
# from app.models import (имя таблицы)

# Все объекты в таблице
# Tablename.objects.all()

# Создание объекта
# Tablename.objects.create(name=newname, age=newage)

# Фильтрация, найти какой-то параметр
# Tablename.objects.filter(name='')

# Обновить
# Tablename.objects.filter(name='').update(name='secondname')

# Количество объектов в базе данных
# Tablename.objects.count()

# Обращение к объекту через переменную по заданному параметру
# а = Tablename.objects.get(id=12)
# a.delete() или другие методы

# а = Tablename.objects.all() переменная со всеми объектами
# a.delete() или другие методы

# Присвоить значение из другой таблицы
# Tablename.objects.get(id=1).othertablefield.set(username)
# Game.objects.get(id=2).buyer.set((1, )) 
# Game.objects.get(id=6).buyer.set((8, 7)) 
# Game.objects.get(id=1).buyer.set((first_buyer, second_buyer)) - 
# здесь игра c id=1 приобретается покупателями first_buyer и second_buyer.



'''Работа с панелью администратора'''
# Регистрация администратора (после миграций)
# python manage.py createsuperuser
# записать имя пользователя и пароль



'''Работа с пагинатором'''
# установить в проекте пагинатор в файле settings.py
# INSTALLED_APPS = [
    # ...
    # 'django.core.paginator',




'''Отправка проекта в репозиторий'''

# создать папку с именем '.git'

# инициализация гит
# git init

# добавление файлов в гит папку
# git add .
# git add filename.py.

# Сделайте первый коммит (фиксация изменений)
# git commit -m "Initial commit"

# Настройте удаленный репозиторий
# git remote add origin <URL-удаленного-репозитория>

# Отправьте изменения в удаленный репозиторий
# git push -u origin master

# Проверьте статус репозитория
# git status


