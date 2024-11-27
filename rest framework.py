''' Установка rest framework '''

# Расширение устанавливается отдельно при необходимости
# pip install djangorestframework

# настройка settings
''' INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",             
    "django.contrib.staticfiles",
    "rest_framework",              # вот здесь
    "app",
]'''


''' APIдоступ в views'''

# Парсинг модели

# создаем в папке с приложением пайтон файл для serializers

# from rest_framework import serializers
# from .models import *

# сериализация по модели из папки models

'''class BuyerSerializer(serializers.ModelSerializer): 
    class Meta:
    model = Buyer
    fields = ('', '', '')'''

# создаем класс, который будет отвечать за апи представление этой модели
'''
from rest_framework import generics
from .serializers import BuyerSerializer

class BuyerAPIView(generics.ListAPIView):
    # запрос в базу данных
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer'''


'''В urls прописать путь'''

# path('api/buyerlist', views.BuyerAPIView.as_view)






''' сериализация с нуля (редко используется) '''

# создаем в папке с приложением пайтон файл для serializers

# from rest_framework import serializers
# from .models import *

'''class UserModel:
    def __init__(self, name, age, ): # здесь указываются поля
    self.name = name
    self.age = age


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_leght=20)
    age = serializers.CharField(max_leght=20)'''


# from rest_framework.renderers import JsonRender

# функция зашифровки
'''def encode():
    model = UserModel('Misha', '65')
    model_sr = UserSerializer(model)
    print(model_sr, type(model_sr))
    json = JSONRenderer().render(model_sr.data) #использовать это
    print(json)'''

# from rest_framework.parsers import JsonParser
# функция расшифровки
'''def decode():
    sr =io.BytesIO(b'{"name":"Misha", "age":"65"}')
    data = JSONParser.parse(sr)
    serializer = UserSerializer(data=data)
    serializer.is_valid()
    a = serializer.validated_data #использовать это
    
'''