from django.db import models

class Class(models.Model):
	key = models.CharField(max_length=20, primary_key=True)
	code = models.CharField(max_length=20)
	name = models.CharField(max_length=100, blank=True, null=True)
	professor = models.CharField(max_length=100, blank=True, null=True)
	views = models.IntegerField(default=0)
	assignments = models.ManyToManyField("Assignment", blank=True, null=True, related_name='Class_Assignments')
	delete = models.BooleanField()
	delete_queue = models.OneToOneField("Delete_Queue", blank=True, null=True, related_name='Class_Delete')
	
	def __unicode__(self):
		return u'%s - %s' % (self.code, self.name)
		
class Assignment(models.Model):
	classzy = models.ForeignKey(Class, blank=True, null=True)
	name = models.CharField(max_length=100, default="Assignment")
	homework = models.BooleanField()
	test = models.BooleanField()
	due_date = models.DateField(blank=True, null=True)
	ratings = models.ManyToManyField("Rating", blank=True, null=True, related_name='Assignments_Ratings')
	ratings_chart_url = models.CharField(max_length=500, blank=True, null=True)
	avg_rating = models.IntegerField(default=0)
	num_ratings = models.IntegerField(default=0)
	comments = models.ManyToManyField("Comment", blank=True, null=True, related_name='Assignments_Comments')
	latest_comment_name = models.CharField(max_length=500, blank=True, null=True)
	latest_comment_text = models.CharField(max_length=500, blank=True, null=True)
	times = models.ManyToManyField("Time", blank=True, null=True, related_name='Assignments_Times')
	num_times = models.IntegerField(default=0)
	chart_url = models.CharField(max_length=500, blank=True, null=True)
	delete = models.BooleanField()
	delete_queue = models.OneToOneField("Delete_Queue", blank=True, null=True, related_name='Assignment_Delete')
	
	def __unicode__(self):
		return u'%s - %s' % (self.classzy.code, self.name)
		
class Rating(models.Model):
	assignment = models.ForeignKey(Assignment, blank=True, null=True)
	rating = models.IntegerField(default=0)
	
	def __unicode__(self):
		return u'%s : %s - %d' % (self.assignment.classzy.code, self.assignment.name, self.rating)

class Comment(models.Model):
	assignment = models.ForeignKey(Assignment, blank=True, null=True)
	comment = models.CharField(max_length=500, blank=True, null=True)
	name = models.CharField(max_length=500, blank=True, null=True)
	date_created = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return u'%s : %s - %s : %s' % (self.assignment.classzy.code, self.assignment.name, self.name, self.comment)

class Time(models.Model):
	assignment = models.ForeignKey(Assignment, blank=True, null=True)
	time = models.IntegerField(default=0)
	
	def __unicode__(self):
		return u'%s : %s - %d hours' % (self.assignment.classzy.code, self.assignment.name, self.time)
		
class Delete_Queue(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return u'%s' % (self.title)