from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext

def home(request):
	if request.POST:
		return render_to_response('profile.html', context_instance=RequestContext(request))
	return render_to_response('index.html', context_instance=RequestContext(request))

def create(request):
	if request.POST:
		return render_to_response('profile.html', context_instance=RequestContext(request))
	return render_to_response('create.html', context_instance=RequestContext(request))
	
def profile(request):
	return render_to_response('profile.html', context_instance=RequestContext(request))
	
def view_class(request):
	return render_to_response('class.html', context_instance=RequestContext(request))
	
def add(request):
	return render_to_response('add.html', context_instance=RequestContext(request))