from django import forms
from .models import Task, Blog, Student

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'cols': 80}),
        }
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),            
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),                       
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
        }
    

         
       
# Compare this snippet from myapp/urls.py: