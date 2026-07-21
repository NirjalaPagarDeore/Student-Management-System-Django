from django.urls import path
from . import views

urlpatterns = [
     path("", views.user_login, name="home"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.user_login, name="login"),
    path('add/', views.add_student, name='add_student'),

    #Course Add
    path('course/', views.add_course, name='add_course'),
    path('list/', views.student_list, name='student_list'),

    # Course list 

    path('course_list/', views.course_list, name='course_list'),


    path('edit/<int:id>/', views.edit_student, name='edit_student'),

    #Edit Course Path
     path('edit_course/<int:id>/', views.edit_course, name='edit_course'),

    # VIEW SINGLE STUDENT
    path('view/<int:id>/', views.view_student, name= 'view_student'),

    # ==========================
     # DELETE URL
     # ==========================
    path('delete/<int:id>/', views.delete_student, name='delete_student'),

    # Delete Course url below
     path('delete_course/<int:id>/', views.delete_course, name='delete_course'),

    path("logout/", views.user_logout, name="logout"),
]
