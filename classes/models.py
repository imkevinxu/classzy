from django.db import models

class Class(models.Model):
	code = models.CharField(max_length=20)
	name = models.CharField(max_length=100)
	professor = models.CharField(max_length=100, blank=True, null=True)
	
	def __unicode__(self):
		return u'%s - %s' % (self.code, self.name)