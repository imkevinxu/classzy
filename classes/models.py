from django.db import models

class Class(models.Model):
	code = models.CharField(max_length=20, primary_key=True)
	name = models.CharField(max_length=100, blank=True, null=True)
	views = models.IntegerField(default=0)
	assignments = models.ManyToManyField("Assignment", blank=True, null=True, related_name='Class_Assignments')
	
	def __unicode__(self):
		return u'%s - %s' % (self.code, self.name)
		
class Assignment(models.Model):
	classzy = models.ForeignKey(Class)
	name = models.CharField(max_length=100, default="Assignment")
	homework = models.BooleanField()
	test = models.BooleanField()
	due_date = models.DateField()

	def __unicode__(self):
		return u'%s - %s' % (self.classzy.code, self.name)