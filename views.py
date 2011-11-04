from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from classes.models import Class

def home(request):
<<<<<<< HEAD
	return render_to_response('index.html', context_instance=RequestContext(request))
	
def profile(request):
	return render_to_response('profile.html', context_instance=RequestContext(request))
=======
	if request.method == 'POST':
		try:
			classzy = Class.objects.get(code=request.POST['class'])	
			return render_to_response('index.html', {'classzy' : classzy}, context_instance=RequestContext(request))
		except:
			return render_to_response('index.html', {'warning' : "Sorry, class code not found" }, context_instance=RequestContext(request))
	return render_to_response('index.html', context_instance=RequestContext(request))
>>>>>>> baa5604c5bf9e10c9f4e1b6d018efd228a83ae23
