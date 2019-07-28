from django.urls import path
from . import views
# from .views import MainpageView
urlpatterns = [
    # path('', MainpageView.as_view(), name='mainpage'),
    path('', views.home, name='home'),
    path('blogapp/<int:blog_id>/', views.detail, name='detail' ),
    # path('blogapp/new.html', views.new, name="new"),
    path('blogapp/create', views.create, name="create"),
    path('blogapp/new.html', views.blogform, name="blogform"),
] 