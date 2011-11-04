from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from classes.models import Class

def home(request):
	if request.method == 'POST':
		try:
			classzy = Class.objects.get(code=request.POST['class'])	
			return render_to_response('index.html', {'class' : classzy}, context_instance=RequestContext(request))
		except:
			return render_to_response('index.html', {'warning' : "Sorry, class code not found" }, context_instance=RequestContext(request))
	return render_to_response('index.html', context_instance=RequestContext(request))