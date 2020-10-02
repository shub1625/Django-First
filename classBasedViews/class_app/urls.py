from django.urls import path, include
from class_app import views

app_name = 'class_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail')
]
