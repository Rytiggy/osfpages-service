from django.db import models

# Create your models here.

class Home(models.Model):
	guid = models.CharField(max_length=5, primary_key=True)
	page_data = models.TextField()
	unpublished_page_data = models.TextField(null=True, blank=True)
	meta_data = models.TextField(null=True, blank=True)
