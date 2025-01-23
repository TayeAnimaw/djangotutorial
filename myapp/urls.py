
from django.urls import path 
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('todo/', views.todo, name='todo'),
    path('student/', views.student, name='student'),
    path('delte/<student_id>', views.delete_student, name='delete_student'),
    path('edit/<student_id>', views.edit_student, name='edit_student'),
    # path('',views.about, name='about'),
    
   
]
