from django.db import models
import uuid
# Create your models here.
class Project(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title =  models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    votetotal = models.IntegerField(default=0, null=True, blank=True)
    voteratio = models.IntegerField(default=0, null=True, blank=True)
    tags= models.ManyToManyField('Tag', blank=True)
    demo_link = models.CharField(max_length=1000, blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return self.title

class Review(models.Model):
    
    VOTE_TYPE = (
        ('up', 'up vote'),
        ('down', 'down vote')
    )
    #owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE) 
    created = models.DateTimeField(auto_now_add=True)
    id =  models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    
    def __str__(self):
        return self.value
    
class Tag(models.Model):
    
    id=  models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name =  models.CharField(max_length= 100)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name