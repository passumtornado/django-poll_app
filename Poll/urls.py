
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('create/',views.create,name='create_page'),
    path('vote/<int:id>', views.vote,name='vote_page'),
    path('result/<int:id>',views.result,name='result_page')
]