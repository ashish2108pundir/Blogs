from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
import string
from MyBlog.utils import unique_slug_generator
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Homestay(models.Model):
    
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    slug=models.SlugField(max_length=500, unique=True, blank=True)
    
    def __str__(self):
        return self.name

    def imageurl(self):
        self.image
        try:
            url=self.image.url
        except:
            url='static/images/dummy.png'    
        return url


def slug_generator(sender,instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)
              
    
pre_save.connect(slug_generator,sender=Homestay)



class Author(models.Model):
    author=models.CharField(max_length=255)
    def __str__(self):
        return self.author


class Category(models.Model):

    category = models.CharField(max_length=255,blank=True, null=True)
    def __str__(self):
        return self.category


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True,upload_to="static/img/")
    title=models.CharField(max_length=100)
    content=RichTextUploadingField(null=True,blank=True)
    #category =models.ForeignKey(Category, on_delete=models.CASCADE,to_field="category")
    #content=models.TextField()
    slug=models.CharField(max_length=100,)
    views=models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-timestamp']


    def __str__(self):
        return self.title


