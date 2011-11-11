from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from classes.models import Class, Assignment, Rating
from time import strptime, strftime

def home(request):
	if request.method == 'POST':
		if 'class' in request.POST:
			try:
				classzy_key = request.POST['class'].lower().replace(' ','')
				classzy = Class.objects.get(key=classzy_key)	
				classzy.views += 1
				classzy.save()
				assignments = classzy.assignments.all()
				assignments = sorted(assignments, key=lambda assignment: assignment.due_date)
				return render_to_response('index.html', {'classzy' : classzy, 'assignments' : assignments, 'total_ratings' : [1, 2, 3, 4, 5]}, context_instance=RequestContext(request))
			except:
				return render_to_response('index.html', {'warning' : "Sorry, class code not found", 'error_class' : request.POST['class'] }, context_instance=RequestContext(request))
				
		elif 'class_code' in request.POST:
			try:
				classzy_key = request.POST['class_code'].lower().replace(' ','')
				classzy = Class.objects.get(key=classzy_key)
				return render_to_response('index.html', {'adding_warning' : "That class is already in Classzy!" }, context_instance=RequestContext(request))
			except:
				classzy_key = request.POST['class_code'].lower().replace(' ','')
				classzy = Class(key=classzy_key, code=request.POST['class_code'])
				classzy.views += 1
				classzy.save()
				assignments = classzy.assignments.all()
				assignments = sorted(assignments, key=lambda assignment: assignment.due_date)
				return render_to_response('index.html', {'classzy' : classzy, 'assignments' : assignments, 'total_ratings' : [1, 2, 3, 4, 5]}, context_instance=RequestContext(request))
				
		elif 'edit_class_code' in request.POST:
			classzy = Class.objects.get(code=request.POST['edit_class_code'])
			classzy.name = request.POST['edit_class_name']
			classzy.professor = request.POST['edit_class_professor']
			classzy.save()
			assignments = classzy.assignments.all()
			assignments = sorted(assignments, key=lambda assignment: assignment.due_date)
			return render_to_response('index.html', {'classzy' : classzy, 'assignments' : assignments, 'total_ratings' : [1, 2, 3, 4, 5], 'updated': True}, context_instance=RequestContext(request))
			
		elif 'add_assignment_classzy' in request.POST:
			classzy = Class.objects.get(key=request.POST['add_assignment_classzy'])
			assignments = classzy.assignments.all()
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
				return render_to_response('index.html', {'classzy' : classzy, 'assignments' : sorted(assignments, key=lambda assignment: assignment.due_date), 'warning': "Incorrect info submitted"}, context_instance=RequestContext(request))
			prev_assignments = list(assignments)
			prev_assignments.append(assignment)
			classzy.assignments = prev_assignments
			classzy.save()
			return render_to_response('index.html', {'classzy' : classzy, 'assignments' : sorted(classzy.assignments.all(), key=lambda assignment: assignment.due_date), 'added': True}, context_instance=RequestContext(request))
			
	return render_to_response('index.html', context_instance=RequestContext(request))
