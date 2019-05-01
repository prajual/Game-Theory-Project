from django.shortcuts import render
from django.template import loader
import webbrowser
from django.views.generic import TemplateView
from django.http import HttpResponse
from .aditya import aditya1
from .arzoo import arzoo1
from .gurasheesh import gurasheesh1
from .Jay import jay1
from .ritika import ritika1 
from .maisam import maisam1
from .muskan import muskan1
from .naman import naman1
from .saurabh import saurabh1
from .uday1 import game

class Gamer(TemplateView):
	template_name='My-game.html'

class namana(TemplateView):
	template_name='naman.html'
	
class sourabha(TemplateView):
	template_name ='HTML/Game.html'

class aarzoo1(TemplateView):
	template_name = 'aarzoo.html'
class jay(TemplateView):
	template_name = 'Jay.html'
class gurasheesh(TemplateView):
	template_name = 'gurasheesh'
class Muskan(TemplateView):
	template_name = 'webpage.html'
class Aditya(TemplateView):
	template_name = 'page1.html'

def uda1(request):
	if request.method=='POST':
		a=request.POST['a']
		b=request.POST['b']
		res = game(a,b)
		return HttpResponse(res)
	else:
		return HttpResponse("Please click the Button otherwise you will not get nothing")

def nam1(request):
	if request.method=='POST':
		a=request.POST['a']
		b=request.POST['b']
		c = request.POST['c']
		d=request.POST['d']
		e=request.POST['e']
		f = request.POST['f']		
		res = naman1(a,b,c,d,e,f)
		return HttpResponse(res)
	else:
		return HttpResponse("Please click the Button otherwise you will not get nothing")

def sa1(request):
	if request.method=='POST':
		a=request.POST['a']
		b=request.POST['b']
		res = saurabh1(a,b)
		return HttpResponse(res)
	else:
		return HttpResponse("Please click the Button otherwise you will not get nothing")


def ad1(request):
	if request.method=='POST':
		a=request.POST['friendliness_1']
		b=request.POST['imitation_1']
		c=request.POST['vindictiveness_1']
		d=request.POST['friendliness_2']
		e=request.POST['imitation_2']
		f=request.POST['vindictiveness_2']
		res = aditya1(a,b,c,d,e,f)
		return HttpResponse(res)
	else:
		return HttpResponse("Please click the Button otherwise you will not get nothing")

def ar1(request):
	if request.method=='POST':
		behaviour1 = request.POST['firstname']
		behaviour2 = request.POST['secondname']
		p1=request.POST['a2']
		p2=request.POST['a3']
		p3=request.POST['a3']
		p4=request.POST['a4']
		p11=request.POST['p2']
		p22=request.POST['p3']
		p33=request.POST['p3']
		p44=request.POST['p4']
		res = arzoo1(behaviour1,behaviour2,p1,p2,p3,p4,p11,p22,p33,p44)
		return HttpResponse(res)
	else:
		return HttpResponse("Please click the Button otherwise you will not get nothing")
def gu1(request):
	if request.method=='POST':
		a=request.POST['Cooperation']
		b=request.POST['Vindictiveness']
		c=request.POST['Cooperation2']
		d=request.POST['Vindictiveness2']
		res = gurasheesh1(a,b,c,d)
		return HttpResponse(res)
	else:
		return HttpResponse("Please click the Button otherwise you will not get nothing")
def ja1(request):
	if request.method=='POST':
		aa=request.POST['a']
		y1=request.POST['y1']
		z1=request.POST['z1']
		b=request.POST['b']
		y2=request.POST['y2']
		z2=request.POST['z2']
		res = jay1(aa,y1,z1,b,y2,z2)
		return HttpResponse(res)
	else:
		return HttpResponse("Please click the Button otherwise you will not get nothing")
def ri1(request):
	if request.method=='POST':
		a=request.POST['a']
		b=request.POST['b']
		res = ritika1(a,b)
		return HttpResponse(res)
	else:
		return HttpResponse("Please click the Button otherwise you will not get nothing")
def ma1(request):
	if request.method=='POST':
		a=request.POST['a']
		b=request.POST['b']
		res = maisam1(a,b)
		return HttpResponse(res)
	else:
		return HttpResponse("Please click the Button otherwise you will not get nothing")
def mu1(request):
	if request.method=='POST':
		a=request.POST['a']
		b=request.POST['b']
		res = muskan1(a,b)
		return HttpResponse(res)
	else:
		return HttpResponse("Please click the Button otherwise you will not get nothing")

