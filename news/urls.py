from django.urls import path

from . import views_V1, views_V2, views_V3

app_name = 'news'
urlpatterns = [
    path('v1/', views_V1.list_posts_v1, name='list_v1'),
    path('v1/<int:pk>/', views_V1.detail_post_v1, name='detail_v1'),
    path('v1/create/', views_V1.create_post_v1, name='create_v1'),
    path('v1/update/<int:pk>/', views_V1.update_post_v1, name='update_v1'),
    path('v1/delete/<int:pk>/', views_V1.delete_post_v1, name='delete_v1'),

    path('', views_V3.ListView.as_view(), name='index'),
    path('<int:pk>/', views_V3.DetailView.as_view(), name='detail'),
    path('create/', views_V3.CreateView.as_view(), name='create'),
    path('update/<int:pk>/', views_V3.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views_V3.DeleteView.as_view(), name='delete'),
]