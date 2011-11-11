from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from classes.models import Class, Assignment
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
				return render_to_response('index.html', {'classzy' : classzy, 'assignments' : assignments}, context_instance=RequestContext(request))
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
				return render_to_response('index.html', {'classzy' : classzy, 'assignments' : assignments}, context_instance=RequestContext(request))
				
		elif 'edit_class_code' in request.POST:
			classzy = Class.objects.get(code=request.POST['edit_class_code'])
			classzy.name = request.POST['edit_class_name']
			classzy.professor = request.POST['edit_class_professor']
			classzy.save()
			assignments = classzy.assignments.all()
			return render_to_response('index.html', {'classzy' : classzy, 'assignments' : assignments, 'updated': True}, context_instance=RequestContext(request))
			
		elif 'add_assignment_classzy' in request.POST:
			classzy = Class.objects.get(key=request.POST['add_assignment_classzy'])
			assignments = classzy.assignments.all()
			assignment = Assignment(name=request.POST['add_assignment_name'])
			assignment.classzy = classzy
			if request.POST['add_assignment_type'] == "homework":
				assignment.homework = True		
			if request.POST['add_assignment_type'] == "test":
				assignment.test = True
			datestring = request.POST['add_assignment_due_date']
			due_date = strftime("%Y-%m-%d", strptime(datestring,"%m/%d/%Y"))
			assignment.due_date = due_date
			assignment.save()
			prev_assignments = list(assignments)
			prev_assignments.append(assignment)
			classzy.assignments = prev_assignments
			classzy.save()
			return render_to_response('index.html', {'classzy' : classzy, 'assignments' : classzy.assignments.all(), 'added': True}, context_instance=RequestContext(request))
			
	return render_to_response('index.html', context_instance=RequestContext(request))
