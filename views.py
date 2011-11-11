from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from classes.models import Class, Assignment, Rating, Comment, Time
from time import strptime, strftime
from GChartWrapper import *

def home(request):
	if request.method == 'POST':
		if 'class' in request.POST:
			try:
				classzy_key = request.POST['class'].lower().replace(' ','')
				classzy = Class.objects.get(key=classzy_key)	
				classzy.views += 1
				classzy.save()
				assignments = classzy.assignments.all()
				assignments = sorted(assignments, key=lambda assignment: assignment.due_date, reverse=True)
				chart = Pie([5,10]).title('Hello Pie').color('red','lime').label('hello', 'world')
				return render_to_response('index.html', {'classzy' : classzy, 'assignments' : assignments, 'total_ratings' : [1, 2, 3, 4, 5], 'chart':chart}, context_instance=RequestContext(request))
			except:
				return render_to_response('index.html', {'warning' : "Sorry, class code not found", 'error_class' : request.POST['class'] }, context_instance=RequestContext(request))
				
		elif 'class_code' in request.POST:
			try:
				classzy_key = request.POST['class_code'].lower().replace(' ','')
				classzy = Class.objects.get(key=classzy_key)
				return render_to_response('index.html', {'adding_warning' : "That class is already in Classzy!" }, context_instance=RequestContext(request))
			except:
				classzy_key = request.POST['class_code'].lower().replace(' ','')
				classzy = Class(key=classzy_key, code=request.POST['class_code'].upper())
				classzy.views += 1
				classzy.save()
				assignments = classzy.assignments.all()
				assignments = sorted(assignments, key=lambda assignment: assignment.due_date, reverse=True)
				return render_to_response('index.html', {'classzy' : classzy, 'assignments' : assignments, 'total_ratings' : [1, 2, 3, 4, 5]}, context_instance=RequestContext(request))
				
		elif 'edit_class_code' in request.POST:
			classzy = Class.objects.get(code=request.POST['edit_class_code'])
			classzy.name = request.POST['edit_class_name']
			classzy.professor = request.POST['edit_class_professor']
			classzy.save()
			assignments = classzy.assignments.all()
			assignments = sorted(assignments, key=lambda assignment: assignment.due_date, reverse=True)
			return render_to_response('index.html', {'classzy' : classzy, 'assignments' : assignments, 'total_ratings' : [1, 2, 3, 4, 5], 'updated': True}, context_instance=RequestContext(request))
			
		elif 'add_assignment_classzy' in request.POST:
			classzy = Class.objects.get(key=request.POST['add_assignment_classzy'])
			assignments = classzy.assignments.all()
			if 'add_assignment_name' in request.POST and request.POST['add_assignment_name'] != "":
				try:
					assignment = Assignment(name=request.POST['add_assignment_name'])
					assignment.classzy = classzy
					if request.POST['add_assignment_type'] == "homework":
						assignment.homework = True		
					if request.POST['add_assignment_type'] == "test":
						assignment.test = True
					assignment.due_date = request.POST['add_assignment_due_date']
					assignment.save()
					rating = Rating(rating=int(request.POST['add_assignment_rating']))
					rating.assignment = assignment
					rating.save()
					ratings = assignment.ratings.all()
					prev_ratings = list(ratings)
					prev_ratings.append(rating)
					assignment.ratings = prev_ratings
					assignment.avg_rating = rating.rating
					assignment.num_ratings = 1
					assignment.save()
				except:
					return render_to_response('index.html', {'classzy' : classzy, 'assignments' : sorted(assignments, key=lambda assignment: assignment.due_date, reverse=True), 'total_ratings' : [1, 2, 3, 4, 5], 'warning': "Incorrect info submitted"}, context_instance=RequestContext(request))
			else:
				return render_to_response('index.html', {'classzy' : classzy, 'assignments' : sorted(assignments, key=lambda assignment: assignment.due_date, reverse=True), 'total_ratings' : [1, 2, 3, 4, 5], 'warning': "Assignment needs a name"}, context_instance=RequestContext(request))
			prev_assignments = list(assignments)
			prev_assignments.append(assignment)
			classzy.assignments = prev_assignments
			classzy.save()
			return render_to_response('index.html', {'classzy' : classzy, 'assignments' : sorted(classzy.assignments.all(), key=lambda assignment: assignment.due_date, reverse=True), 'total_ratings' : [1, 2, 3, 4, 5], 'added': True}, context_instance=RequestContext(request))
			
		elif 'add_assignment_difficulty_name' in request.POST:
			classzy = Class.objects.get(key=request.POST['hidden_classzy'])
			assignment = Assignment.objects.get(name=request.POST['add_assignment_difficulty_name'])
			rating = Rating(rating=int(request.POST['add_assignment_rating']))
			rating.assignment = assignment
			rating.save()
			ratings = assignment.ratings.all()
			prev_ratings = list(ratings)
			prev_ratings.append(rating)
			assignment.ratings = prev_ratings
			ratings_sum = 0
			for rate in prev_ratings:
				ratings_sum += rate.rating
			assignment.avg_rating = ratings_sum / len(prev_ratings)
			assignment.num_ratings += 1
			assignment.save()
			return render_to_response('index.html', {'classzy' : classzy, 'assignments' : sorted(classzy.assignments.all(), key=lambda assignment: assignment.due_date, reverse=True), 'total_ratings' : [1, 2, 3, 4, 5], 'warning': "New rating added"}, context_instance=RequestContext(request))
			
		elif 'add_assignment_time_name' in request.POST:
			classzy = Class.objects.get(key=request.POST['hidden_classzy'])
			assignment = Assignment.objects.get(name=request.POST['add_assignment_time_name'])
			time = Time(time=int(request.POST['add_assignment_time']))
			time.assignment = assignment
			time.save()
			times = assignment.times.all()
			prev_times = list(times)
			prev_times.append(time)
			assignment.times = prev_times
			assignment.num_times += 1
			
			chart_data = [0, 0, 0, 0]
			for time in prev_times:
				if (time.time < 10):
					chart_data[0] += 1
				elif (time.time < 20):
					chart_data[1] += 1
				elif (time.time < 30):
					chart_data[2] += 1
				else:
					chart_data[3] += 1
			G = VerticalBarStack(chart_data)
			G.color('3D71A3')
			G.label('0-9','10-19','20-29','30 plus')
			G.size(250,125)
			G.bar(50,15)
			G.marker('N*','black',0,-1,11)
			chart_url = str(G) + '&chds=0,'+str(max(chart_data) + 4)+'&chf=bg,s,E6E6E6'
			assignment.chart_url = chart_url
			assignment.save()
			return render_to_response('index.html', {'classzy' : classzy, 'assignments' : sorted(classzy.assignments.all(), key=lambda assignment: assignment.due_date, reverse=True), 'total_ratings' : [1, 2, 3, 4, 5], 'warning': "New time added"}, context_instance=RequestContext(request))
			
		elif 'add_assignment_comment_name' in request.POST:
			classzy = Class.objects.get(key=request.POST['hidden_classzy'])
			assignment = Assignment.objects.get(name=request.POST['add_assignment_comment_name'])
			if 'comment_text' in request.POST and request.POST['comment_text'] != "" and 'comment_name' in request.POST and request.POST['comment_name'] != "":
				comment = Comment(name=request.POST['comment_name'],comment=request.POST['comment_text'])
				comment.assignment = assignment
				comment.save()
				comments = assignment.comments.all()
				prev_comments = list(comments)
				prev_comments.append(comment)
				assignment.comments = prev_comments
				assignment.latest_comment_name = request.POST['comment_name']
				assignment.latest_comment_text = request.POST['comment_text']
				assignment.save()
			else:
				return render_to_response('index.html', {'classzy' : classzy, 'assignments' : sorted(classzy.assignments.all(), key=lambda assignment: assignment.due_date, reverse=True), 'total_ratings' : [1, 2, 3, 4, 5], 'warning': "Cannot leave empty comment"}, context_instance=RequestContext(request))
			return render_to_response('index.html', {'classzy' : classzy, 'assignments' : sorted(classzy.assignments.all(), key=lambda assignment: assignment.due_date, reverse=True), 'total_ratings' : [1, 2, 3, 4, 5], 'warning': "New comment added"}, context_instance=RequestContext(request))
			
	return render_to_response('index.html', context_instance=RequestContext(request))
