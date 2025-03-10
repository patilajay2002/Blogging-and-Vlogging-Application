from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
import datetime


# Create your models here.
class CustomManager(models.Manager):
      def get_queryset(self):
            return super().get_queryset().filter(status='published')
class Post(models.Model):
 STATUS_CHOICES=(('draft','Draft'),('published','Published'))
 title=models.CharField(max_length=256)
 slug=models.SlugField(max_length=264,unique_for_date='publish')
 author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
 body=models.TextField()
 publish=models.DateTimeField(default=timezone.now)
 created=models.DateTimeField(auto_now_add=True)
 updated=models.DateTimeField(auto_now=True)
 status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
 objects=CustomManager()
 tags=TaggableManager()
 
 class Meta:
  ordering=("-publish",)
 def get_absolute_url(self):
  return reverse('post_detail',
       args=[self.publish.year,
       self.publish.strftime('%m'),
       self.publish.strftime('%d'),
       self.slug]) 
 
 
       
 def __str__(self):
  return self.title

# class Commentm(models.Model):
#       post=models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
#       name=models.CharField(max_length=32)
#       email=models.EmailField()
#       body=models.TextField()
#       created=models.DateTimeField(auto_now_add=True)
#       updated=models.DateTimeField(auto_now=True)
#       active=models.BooleanField(default=True)
#       class Meta:
#           ordering=("created",)
#       def __str__(self):
#        return 'commented By {} on {} '.format(self.name,self.post)

class Commentm(models.Model): 
 post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE) 
 name=models.CharField(max_length=32) 
 email=models.EmailField() 
 body=models.TextField() 
 created=models.DateTimeField(auto_now_add=True) 
 updated=models.DateTimeField(auto_now=True) 
 active=models.BooleanField(default=True) 
 class Meta: 
  ordering=('created',) 
 def __str__(self): 
  return 'Commented By {} on {}'.format(self.name,self.post) 