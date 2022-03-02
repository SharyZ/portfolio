from django.db import models
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=150, help_text="Name of the project")
    featured_image = models.ImageField(upload_to='uploads/')
    content = RichTextUploadingField(config_name='portfolio_ckeditor')
    tags = TaggableManager()

    def __str__(self):
        return self.name
