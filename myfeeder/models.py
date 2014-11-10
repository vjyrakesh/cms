from django.db import models

# Create your models here.

class FeedCategory(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(blank=True)

	class Meta:
		ordering = ['title']
		verbose_name_plural = "Categories"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/categories/%s/" %self.title

class FeedSource(models.Model):
	title = models.CharField(max_length=250)
	link = models.URLField()
	description = models.TextField(blank=True)
	updated_on = models.DateTimeField()
	category = models.ForeignKey(FeedCategory)

	class Meta:
		ordering=['title']

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/source/%s" %self.title

class FeedItem(models.Model):
	title = models.CharField(max_length=500)
	link = models.URLField()
	description = models.TextField()
	published = models.DateTimeField()
	feed_source = models.ForeignKey(FeedSource)

	class Meta:
		ordering=['title']

	def __unicode__(self):
		return self.title
