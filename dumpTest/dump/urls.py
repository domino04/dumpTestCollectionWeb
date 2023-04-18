from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<test_id>/', views.test, name='test'),
    path('<test_id>/<question_id>/', views.test_question, name='test_question'),
    path('<test_id>/result/', views.result, name='result')
]