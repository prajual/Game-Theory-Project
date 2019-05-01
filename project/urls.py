from django.urls import path

from . import views
from .views import Gamer
from .views import namana
from .views import sourabha
from .views import aarzoo1
from .views import jay
from .views import gurasheesh
from .views import Muskan
from .views import Aditya
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	path('aditya/',views.ad1,name='ad1'),
	path('arzoo/',views.ar1,name='ar1'),
	path('gurasheesh/',views.gu1,name='gu1'),
	path('jay/',views.ja1,name='ja1'),
	path('maisam/',views.ma1,name='ma1'),
	path('muskan/',views.mu1,name='mu1'),
	path('naman/',views.nam1,name='nam1'),
	path('ritika/',views.ri1,name='ri1'),
	path('saurabh/',views.sa1,name='sa1'),
	path('uday/',views.uda1,name='uda1'),
	path('udayhome/',Gamer.as_view(),name = 'Gamer'),
	path('namanhome/',namana.as_view(),name = 'namana'),
	path('sourabhhome/',sourabha.as_view(),name = 'sourabha'),
	path('aarzoohome/',aarzoo1.as_view(),name = 'aarzoo'),
	path('jayhome/',jay.as_view(),name = 'Jay'),
	path('gurasheeshhome/',gurasheesh.as_view(),name = 'gurasheesh'),
	path('muskanhome/',Muskan.as_view(),name = 'muskan'),
	path('Aditya_maisam/',Aditya.as_view(),name = 'aditya'),
]

urlpatterns += staticfiles_urlpatterns()
