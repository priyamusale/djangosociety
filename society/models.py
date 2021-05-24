from django.db import models

# Create your models here.
class Group(models.Model):
	name = models.CharField(max_length=100)
	members = models.TextField()
	description = models.TextField()
	category = models.TextField()
	website_url = models.URLField()

class Event(models.Model):
	description = models.TextField()
	creator_name = models.CharField(max_length=100)
	start_time = models.DateField()
	end_time = models.DateField()
	location = models.TextField()
	event_title = models.TextField()

class People(models.Model):
	about_me = models.TextField()
	birth_date = models.DateField()
	fav_movies = models.TextField()
	first_name = models.TextField()
	last_name = models.TextField()
	username = models.CharField(max_length=100)
	photo_url = models.URLField()