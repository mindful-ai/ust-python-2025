from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # root URL -> 127.0.0.1:8000/ -> run a function called home in views
    path('info', views.info, name='info'), # 127.0.0.1:8000/info -> run a function called info in views
    path('index', views.index, name='index'), # 127.0.0.1:8000/index
    path('check', views.age_check, name='check'), # 127.0.0.1:8000/check
    path('fruits', views.fruit_list, name='fruits'), # 127.0.0.1:8000/fruits
    path('input', views.input_form, name='input'), # 127.0.0.1:8000/input
    path('result', views.result, name='result'), # 127.0.0.1:8000/result
    path('calculator', views.calculator, name='calculator'), # 127.0.0.1:8000/calculator
    path('calc', views.calc, name='calc'), # 127.0.0.1:8000/calc
]   