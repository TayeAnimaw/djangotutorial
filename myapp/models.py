from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.title}       -{self.content}               -{self.created}'


class Student(models.Model):
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)      
    email = models.EmailField()
    phone = models.CharField(max_length=10)        
    grade = models.CharField(max_length=2)
    

    def __str__(self):
        return self.name
# Compare this snippet from myapp/views.py: