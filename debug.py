'''Работа с debug в Django'''

# pip install django-debug-toolbar
# 

# настройка settings
''' INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",             
    "django.contrib.staticfiles",
    "rest_framework",  
    "debug_toolbar",            # вот здесь            
    "app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware"    # вот здесь  
]

DEBUG = True
#локалхост
INTERNAL_IPS = ['127.0.0.1']     # вот здесь 

'''


# URLS добавить сам дебаг

# from django.urls import include

# path('__debug__/', include('debug_toolbar.urls'))