from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "society"

urlpatterns = [

	path('', views.index, name='index'),
	path('events/', views.all_events, name='events'),
	path('groups/', views.all_groups, name='groups'),
	path('people/', views.all_people, name='people'),
	path('events/<int:event_id>/', views.event_detail, name='event'),
	path('groups/<int:group_id>/', views.group_detail, name='group'),
	path('people/<int:person_id>/', views.person_detail, name='person'),

]

urlpatterns += staticfiles_urlpatterns()