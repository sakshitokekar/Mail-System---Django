from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from random import randrange

def ulogin(request):
	if request.method == "POST":
		em = request.POST.get("em")
		pw = request.POST.get("pw") 
		usr = authenticate(username = em, password = pw)
		if usr is not None:
			login(request, usr)
			return redirect("home")
		else:
			return render(request,"ulogin.html",{"msg":"Invalid Login Details"})
	else:
		return render(request,"ulogin.html")

def usignup(request):
	if request.method == "POST":
		em = request.POST.get("em")
		try:
			usr = User.objects.get(username = em)
			return render(request, "usignup.html", {"msg": "Email Already Registered"})
		except User.DoesNotExist:
			pw = ""
			text = "123456789abcdefghijklmnopqrstuvwxyz"
			for i in range(4):
				pw = pw + text[randrange(len(text))]
			subject="Welcome to Email-Ops"
			msg="Your Password is: "  + str(pw)
			host = "medinsure72@gmail.com"
			recepient = [em]
			send_mail(subject,msg,host,recepient)
			usr = User.objects.create_user(username=em, password=pw)
			usr.save()
			return redirect("ulogin")

	return render(request,"usignup.html")

def uchangepw(request):
	return render(request,"uchangepw.html")

def ulogout(request):
	logout(request)
	return redirect("ulogin")