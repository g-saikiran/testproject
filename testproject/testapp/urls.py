from django.contrib import admin
from django.urls import path
from testapp import views


urlpatterns = [
    path('test/',views.test, name='test'),

]