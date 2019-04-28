from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField() #url address of the file
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #author
    #thumbnail

    # making changes to database
    # python manage.py makemigrations
    # python manage.py migrate
    def __str__(self):
        return self.title
