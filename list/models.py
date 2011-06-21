from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	user = models.ForeignKey(User)
	creator_id = models.IntegerField()
	creation_date = models.DateTimeField()

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['creation_date']

