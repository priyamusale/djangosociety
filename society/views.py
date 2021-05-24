from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from .models import Group, Event, People

def index(request):
	return render(request, 'society/index.html', {})

def all_events(request):
	event_list = Event.objects.all()
	count = Event.objects.all().count()
	template = loader.get_template('society/all_events.html')
	context = {
		'event_list': event_list,
		'count': count,
	}
	return HttpResponse(template.render(context, request))

def all_groups(request):
	group_list = Group.objects.order_by('name')
	count = Group.objects.all().count()
	template = loader.get_template('society/all_groups.html')
	context = {
		'group_list': group_list,
		'count': count,
	}
	return HttpResponse(template.render(context, request))

def all_people(request):
	people_list = People.objects.all()
	count = People.objects.all().count()
	template = loader.get_template('society/people.html')
	context = {
		'people_list': people_list,
		'count': count,
	}
	return HttpResponse(template.render(context, request))

def event_detail(request, event_id):
	template = loader.get_template('society/event.html')
	context = {
		'event_obj': Event.objects.get(id = event_id),
	}
	return HttpResponse(template.render(context, request))

def group_detail(request, group_id):
	template = loader.get_template('society/group.html')
	context = {
		'group_obj': Group.objects.get(id = group_id),
	}
	return HttpResponse(template.render(context, request))

def person_detail(request, person_id):
	template = loader.get_template('society/person.html')
	context = {
		'person_obj': People.objects.get(id = person_id),
	}
	return HttpResponse(template.render(context, request))

