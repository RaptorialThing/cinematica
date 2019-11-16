from django.urls import path
from . import views

urlpatterns = [
	path('',views.movies_index,name='movies_index'),
	path('<int:pk>/',views.movies_detail,name='movies_detail'),
]



