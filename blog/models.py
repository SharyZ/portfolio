from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='uploads/blog/')
    content = RichTextUploadingField(config_name='portfolio_ckeditor')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
