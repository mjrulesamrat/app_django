from django.db import models

# Create your models here.
class Demo1(models.Model):
	demo_name = models.CharField(max_length = 10)
	pub_date = models.DateTimeField('Pub Date')
	likes = models.IntegerField()

	def __unicode__(self):
		return self.title

