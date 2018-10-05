from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length = 255) 
	pub_date = models.DateTimeField() # publication date 
	body = models.TextField() # text of post 
	image = models.ImageField(upload_to = 'images\\') 
	 
