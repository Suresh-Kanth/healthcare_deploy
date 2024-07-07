from django.urls import path, re_path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.user_login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout/', views.Logout, name='logout'),
    path('addblog/', views.Add_Blog, name='addblog'),
    path('blogs/', views.blogs, name='blogs'),
    path('myblogs/', views.myblogs, name='myblogs'),
    path('mydrafts/', views.mydrafts, name='mydrafts'),
    re_path(r'^blog/(?P<blog_no>[0-9a-f-]+)/$', views.blog, name='blog'),
    re_path(r'^draft/(?P<blog_no>[0-9a-f-]+)/$', views.draft, name='draft'),
]
