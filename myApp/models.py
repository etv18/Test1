from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete = models.CASCADE) 
    '''EL metodo ForeingKey() se utiliza para especificar que
    esta tabla tendra una relacion con otra, y dicah tabla se le pasa por parametro al metodo
    
    El 'on_delete = models.CASCADE' es para que en dado caso se elemine un proyecto las tareas 
    relacionadas a el se eliminen tambien.
    '''


