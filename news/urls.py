from django.urls import path

from . import views_V1, views_V2, views_V3

app_name = 'news'
urlpatterns = [
    path('', views_V3.ListView.as_view(), name='index'),
    path('<int:post_id>/', views_V3.DetailView.as_view(), name='detail'),
    path('create/', views_V3.CreateView.as_view(), name='create'),
    path('update/<int:post_id>/', views_V3.UpdateView.as_view(), name='update'),
    path('delete/<int:post_id>/', views_V3.DeleteView.as_view(), name='delete'),
]