from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField(max_length=1100)
  slug = models.SlugField(max_length=100, unique=True)

  def slug(self):
    return slugify(self.title)
