from django.contrib import admin
from django.urls import path
from account import views
admin.site.site_header = "CDC ADMIN"
admin.site.site_title = "CDC ADMIN"
admin.site.index_title = "CDC ADMIN"

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('cdc/', views.cdc, name='cdc'),
    path('activity/', views.activity, name='activity'),
    path('academic/', views.academic, name='academic'),
    path('allstudent/', views.allstudent, name='allstudent'),
    path('addacademic/<int:pk>', views.addacademic, name='addacademic'),
    path('viewacademic', views.viewacademic, name='viewacademic'),

  ]
