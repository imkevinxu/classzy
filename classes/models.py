from django.db import models

class Class(models.Model):
	key = models.CharField(max_length=20, primary_key=True)
	code = models.CharField(max_length=20)
	name = models.CharField(max_length=100, blank=True, null=True)
	professor = models.CharField(max_length=100, blank=True, null=True)
	views = models.IntegerField(default=0)
	assignments = models.ManyToManyField("Assignment", blank=True, null=True, related_name='Class_Assignments')
	
	def __unicode__(self):
		return u'%s - %s' % (self.code, self.name)
		
class Assignment(models.Model):
	classzy = models.ForeignKey(Class, blank=True, null=True)
	name = models.CharField(max_length=100, default="Assignment")
	homework = models.BooleanField()
	test = models.BooleanField()
	due_date = models.DateField(blank=True, null=True)
	ratings = models.ManyToManyField("Rating", blank=True, null=True, related_name='Assignments_Ratings')
	avg_rating = models.IntegerField(default=0)
	num_ratings = models.IntegerField(default=0)
	
	def __unicode__(self):
		return u'%s - %s' % (self.classzy.code, self.name)
		
class Rating(models.Model):
	assignment = models.ForeignKey(Assignment, blank=True, null=True)
	rating = models.IntegerField(default=0)
	
	def __unicode__(self):
		return u'%s : %s - %d' % (self.assignment.classzy.code, self.assignment.name, self.rating)
