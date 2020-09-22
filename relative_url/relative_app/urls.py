from django.urls import path
from relative_app import views

app_name = 'relative_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('relative', views.relative, name='relative'),
    path('other_page', views.other_page, name='other_page')
]
