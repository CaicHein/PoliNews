from django.urls import path

from . import views_V1, views_V2, views_V3

app_name = 'news'
urlpatterns = [
    path('v1/', views_V1.list_posts_v1, name='list_v1'),
    path('v1/<int:pk>/', views_V1.detail_post_v1, name='detail_v1'),
    path('v1/create/', views_V1.create_post_v1, name='create_v1'),
    path('v1/update/<int:pk>/', views_V1.update_post_v1, name='update_v1'),
    path('v1/delete/<int:pk>/', views_V1.delete_post_v1, name='delete_v1'),
    path('<int:post_id>/comments/v1/create/', views_V1.create_comment_v1, name='create_comment_v1'),

    path('v2/', views_V2.list_posts_v2, name='list_v2'),
    path('v2/<int:pk>/', views_V2.detail_post_v2, name='detail_v2'),
    path('v2/create/', views_V2.create_post_v2, name='create_v2'),
    path('v2/update/<int:pk>/', views_V2.update_post_v2, name='update_v2'),
    path('v2/delete/<int:pk>/', views_V2.delete_post_v2, name='delete_v2'),
    path('<int:post_id>/comments/v2/create/', views_V2.create_comment_v2, name='create_comment_v2'),

    path('', views_V3.ListView.as_view(), name='index'),
    path('<int:pk>/', views_V3.DetailView.as_view(), name='detail'),
    path('create/', views_V3.CreateView.as_view(), name='create'),
    path('update/<int:pk>/', views_V3.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views_V3.DeleteView.as_view(), name='delete'),
    path('<int:id>/create_comment/', views_V3.CreateCommentView.as_view(), name='create_comment'),
]