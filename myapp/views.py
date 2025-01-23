from django.shortcuts import render , redirect
from django.http import HttpResponse
from myapp.models import Blog, Task , Student
from myapp.forms import TaskForm, BlogForm, StudentForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
# def  index( request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# def about(request):
#     return HttpResponse("Hello, world. You're at the about index.")
# Create your views here.
def index(request): 
    if request.method == 'POST':
        form = BlogForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = BlogForm()      
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        'form': form
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'name': 'Taye',
        'course': 'Welcome to the about page'
    }
    return render(request, 'about.html', context)
def about(request):
    context = {
        'name':'Taye',
        'course':'welcome to the about page'
    }
    return render(request, 'about.html', context)
def home(request):
    context = {
        'name':'Taye',
        'course':'welcome to the home page'
    }
    return render(request, 'home.html', context)
def contact(request):
    context = {
        'name':'Taye',  
        'course':'welcome to the contact page'
    }
    return render(request, 'contact.html', context)
def todo(request):
    context = { 
        'name':'Taye',
        'course':'welcome to the todo page'
    }
    return render(request, 'todo.html', context)


def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the student data to the database
            messages.success(request, 'Student data saved successfully')
            # return render(request, 'student.html')  # Redirect to the student list page after saving
    else:
        form = StudentForm()
    students = Student.objects.all()
    paginator = Paginator(students, 5)  # Show 5 students per page
    page_number = request.GET.get('page', 1)
    students = paginator.get_page(page_number) 

    context = {'form': form, 'students': students }  # Fetch all students to display in the table
    return render(request, 'student.html', context )
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student')
def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student data updated successfully')
            return redirect('student')
    else:
        form = StudentForm(instance=student)
    context = {'form': form}
    return render(request, 'edit_student.html', context)
