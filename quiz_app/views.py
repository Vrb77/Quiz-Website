from django.shortcuts import render
from django.shortcuts import redirect
from quiz_app.form import *
from quiz_app.models import *
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import *
from quiz_app.form import CreateUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	context={}
	form=contactForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('home')
	context["form"]=form
	return render(request,'home.html',context)
	
	return render(request,"home.html")

def profile(request):
	username = request.POST.get('username')
	print(username)
	context={}	
	if request.method=='POST':
		pr=User.objects.filter(username=username)
		print(pr)
		context={
			'username':username,
			'pr':pr,	
		}
		return render(request,'profile.html',context)
	else:
		return render(request, 'accounts/login.html', context)
	

	
def Quiz_history(request):
	return render(request,'Quiz_history.html')
	
def phy(request):
	return render(request,'phy.html')
def chem(request):
	return render(request,"chem.html")
def math(request):
	return render(request,'math.html')
def bio(request):
	return render(request,'bio.html')

def c1(request):
	c1=c1Model.objects.all()
	if request.method == 'POST':
		print(request.POST)
		questions=c1Model.objects.all()
		score=0
		wrong=0
		correct=0
		total=0
		percent=0.0
		for q in questions:
			total+=1
			print(request.POST.get(q.que))
			print(q.ans)
			print()
			if q.ans ==  request.POST.get(q.que):
				score+=10
				correct+=1
			else:
				wrong+=1
		percent = round((score/(total*10) *100),2)
		context = {
				'score':score,
				'correct':correct,
				'wrong':wrong,
				'percent':percent,
				'total':total,
					}
		return render(request,'result.html',context)
	return render(request,"c1.html",{'c1':c1})

def c2(request):
	c2=c2Model.objects.all()
	if request.method == 'POST':
		print(request.POST)
		questions=c2Model.objects.all()
		score=0
		wrong=0
		correct=0
		total=0
		percent=0.0
		for q in questions:
			total+=1
			print(request.POST.get(q.que))
			print(q.ans)
			print()
			if q.ans ==  request.POST.get(q.que):
				score+=10
				correct+=1
			else:
				wrong+=1
		percent = round((score/(total*10) *100),2)
		context = {
				'score':score,
				'correct':correct,
				'wrong':wrong,
				'percent':percent,
				'total':total,
					}
		return render(request,'result.html',context)
	return render(request,"c2.html",{'c2':c2})

def addc1(request):
	context={}
	form=c1Form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/c1')
	context["form"]=form
	return render(request,'addc1.html',context)
def addc2(request):
	context={}
	form=c2Form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/c2')
	context["form"]=form
	return render(request,'addc2.html',context)

#Physics
def p1(request):	
	p1=p1Model.objects.all()
	if request.method == 'POST':
		print(request.POST)
		questions=p1Model.objects.all()
		score=0
		wrong=0
		correct=0
		total=0
		percent=0.0	
		for q in questions:
			total+=1
			print(request.POST.get(q.que))
			print(q.ans)
			print()
			if q.ans ==  request.POST.get(q.que):
				score+=10
				correct+=1
			else:
				wrong+=1
		percent = round((score/(total*10) *100),2)
		context = {
				'score':score,
				'correct':correct,
				'wrong':wrong,
				'percent':percent,
				'total':total,
					}
		return render(request,'result.html',context)
	return render(request,"p1.html",{'p1':p1})

def p2(request):
	p2=p2Model.objects.all()
	if request.method == 'POST':
		print(request.POST)
		questions=p2Model.objects.all()
		score=0
		wrong=0
		correct=0
		total=0
		percent=0.0
		username = request.POST.get('username')
		for q in questions:
			total+=1
			print(request.POST.get(q.que))
			print(q.ans)
			print()
			if q.ans ==  request.POST.get(q.que):
				score+=10
				correct+=1
			else:
				wrong+=1
		percent = round((score/(total*10) *100),2)
		context = {
				'score':score,
				'correct':correct,
				'wrong':wrong,
				'percent':percent,
				'total':total,
				'username':username,
					}
		return render(request,'result.html',context)
	return render(request,"p2.html",{'p2':p2})

def addp1(request):
	context={}
	form=p1Form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/p1')
	context["form"]=form
	return render(request,'addp1.html',context)
def addp2(request):
	context={}
	form=p2Form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/p2')
	context["form"]=form
	return render(request,'addp2.html',context)

#Mathematics
def m1(request):
	m1=m1Model.objects.all()
	if request.method == 'POST':
		print(request.POST)
		questions=m1Model.objects.all()
		score=0
		wrong=0
		correct=0
		total=0
		percent=0.0
		for q in questions:
			total+=1
			print(request.POST.get(q.que))
			print(q.ans)
			print()
			if q.ans ==  request.POST.get(q.que):
				score+=10
				correct+=1
			else:
				wrong+=1
		percent = round((score/(total*10) *100),2)
		context = {
				'score':score,
				'correct':correct,
				'wrong':wrong,
				'percent':percent,
				'total':total,
					}
		return render(request,'result.html',context)
	return render(request,"m1.html",{'m1':m1})
def m2(request):
	m2=m2Model.objects.all()
	if request.method == 'POST':
		print(request.POST)
		questions=m2Model.objects.all()
		score=0
		wrong=0
		correct=0
		total=0
		percent=0.0
		for q in questions:
			total+=1
			print(request.POST.get(q.que))
			print(q.ans)
			print()
			if q.ans ==  request.POST.get(q.que):
				score+=10
				correct+=1
			else:
				wrong+=1
		percent = round((score/(total*10) *100),2)
		context = {
				'score':score,
				'correct':correct,
				'wrong':wrong,
				'percent':percent,
				'total':total,
					}
		return render(request,'result.html',context)
	return render(request,"m2.html",{'m2':m2})

def addm1(request):
	context={}
	form=m1Form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/m1')
	context["form"]=form
	return render(request,'addm1.html',context)
def addm2(request):
	context={}
	form=m2Form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/m2')
	context["form"]=form
	return render(request,'addm2.html',context)


#biology
def b1(request):
	b1=b1Model.objects.all()
	
	if request.method == 'POST':
		print(request.POST)
		questions=b1Model.objects.all()
		score=0
		wrong=0
		correct=0
		total=0
		percent=0.0
		for q in questions:
			total+=1
			print(request.POST.get(q.que))
			print(q.ans)
			print()
			if q.ans ==  request.POST.get(q.que):
				score+=10
				correct+=1
			else:
				wrong+=1
		percent = round((score/(total*10) *100),2)
		context = {
				
				'score':score,
				'correct':correct,
				'wrong':wrong,
				'percent':percent,
				'total':total,
					}
		return render(request,'result.html',context)
	
	return render(request,"b1.html",{'b1':b1})

def b2(request):
	b2=b2Model.objects.all()
	if request.method == 'POST':
		print(request.POST)
		questions=b2Model.objects.all()
		score=0
		wrong=0
		correct=0
		total=0
		percent=0.0
		for q in questions:
			total+=1
			print(request.POST.get(q.que))
			print(q.ans)
			print()
			if q.ans ==  request.POST.get(q.que):
				score+=10
				correct+=1
			else:
				wrong+=1
		percent = round((score/(total*10) *100),2)
		context = {
				'score':score,
				'correct':correct,
				'wrong':wrong,
				'percent':percent,
				'total':total,
					}
		return render(request,'result.html',context)
	return render(request,"b2.html",{'b2':b2})

def addb1(request):
	context={}
	form=b1Form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/b1')
	context["form"]=form
	return render(request,'addb1.html',context)
def addb2(request):
	context={}
	form=b2Form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/b2')
	context["form"]=form
	return render(request,'addb2.html',context)

def result(request):
	
	
		return render(request,'result.html',context)
	
	


def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def login(request):
	username = request.POST.get('username')
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				messages.success(request,   username)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')
		context={}
		return render(request, 'accounts/login.html', context)

def logout(request):
	return redirect('/')

def index(request):
	return render(request,'index.html')



