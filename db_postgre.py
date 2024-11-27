'''Настраиваем Российскую СУБД postgre в django'''

# удалить родную  базу данных db.sqlite3

'''Установка базы данных'''

# Если мы хотим установить на локальную машину PostgreSQL, 
# то переходим на официальный сайт и скачиваем Postgres.

# в терминале нам необходимо установить драйвер для работы с СУБД: 
# pip install psycopg2
# pip install psycopg2-binary


# В меню пуск введите в поиске pgAdmin, подключитесь по созданному паролю при установке.

# Теперь нам необходимо создать базу данных для нашего сайта (нажать левой кнопкой мыши на Базы Данных и создать базу данных):

'''Сохранение данных для переноса БД из SQLITE в PostgreSQL в Django'''

# Если вы не хотите терять данные, которые вы написали за время уроков, это статьи, зарегистированные пользователи, категории, то до следующего пункта настроек мы можем воспользоваться 
# созданием копии базы данных для последующего переноса в PostgreSQL. 
# Чтобы создать дамп базы данных, нам необходимо в терминале прописать следующую команду: 
# python -Xutf8 manage.py dumpdata --exclude contenttypes --output db.json
# Данной командой мы создадим дамп базы данных в json формате.
# также мы можем исключать ненужные таблицы добавляя исключения в команду: 
# --exclude auth.permission --exclude admin.logentry
# таким образом мы исключим ещё логи и права доступа.
# Исключим contenttypes, из дампа, чтоб не возникло лишних ошибок при импорте базы данных при использовании PostgreSQL.
# После успешной настройки БД PostgreSQL, вы можете восстановить дамп следующей командой: 
# python manage.py loaddata db.json
# если возникла проблема при восстановлении с кодировкой, то восстановите дамп через следующую команду: 
# python -Xutf8 manage.py loaddata db.json

'''Настройка Django для работы с PostgreSQL'''

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'имя вашей базы данных',
        'USER': 'postgres',
        'PASSWORD': 'ваш пароль',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}'''

'''Далее после установки проводим миграции и создаем суперпользователя:'''

# python manage.py makemigrations
# python manage.py migrate 
# python manage.py createsuperuser
#
# python manage.py check
#

'''войти в консоль базы данных, если ничего не помогает'''

# psql -U postgres -h localhost -p 5432

# sudo service postgresql status


# CREATE DATABASE db_horses; создание

# \c db_horses подключение

# \q выход

# python manage.py makemigrations 
# python manage.py migrate app  
# python manage.py migrate


'''Запросы в базу данных через терминал'''

# python manage.py shell
# from app.models import Buyer
# from app.models import Horse

# Buyer.objects.all()

# Buyer.objects.get(id=1)

# Buyer.objects.get(name='Екатерина')

# Buyer.objects.filter(name='Екатерина')

# Buyer(name='Святослав', age='30').save()

# Buyer(id=4).delete()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#