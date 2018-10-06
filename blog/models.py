from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length = 255) 
	pub_date = models.DateTimeField() # publication date 
	body = models.TextField() # text of post 
	image = models.ImageField(upload_to = 'images\\') 
	 
	def summary(self):
		# Returns only the first 100 characters of the blog post. 
		return self.body[:100]

	def pub_date_pretty(self):
		# CLeans up the pub date for rendering.
		# strftime lets you alter a datetime in the way you want. 
		# Takes a datetime and converts it to a string. 
		# dattimeFIeld above is based off of the datetime module 
		return self.pub_date.strftime('%b %e %Y') # month abbr, day, Year

	def __str__(self):
		# This is the name that's used whenever the django admin is showing
		return self.title
