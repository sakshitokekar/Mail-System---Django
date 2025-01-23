from django.shortcuts import render, redirect

def calc(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			if request.POST.get("add"):
				n1 = float(request.POST.get("num1"))
				n2 = float(request.POST.get("num2"))
				ans = str(n1) + " + " + str(n2) + " = " + str(round(n1+n2,2))
				return render(request,"calc.html",{"msg":str(ans)})
			if request.POST.get("sub"):
				n1 = float(request.POST.get("num1"))
				n2 = float(request.POST.get("num2"))
				ans = str(n1) + " - " + str(n2) + " = " + str(round(n1-n2,2))
				return render(request,"calc.html",{"msg":str(ans)})
			if request.POST.get("mul"):
				n1 = float(request.POST.get("num1"))
				n2 = float(request.POST.get("num2"))
				ans = str(n1) + " x " + str(n2) + " = " + str(round(n1*n2,2))
				return render(request,"calc.html",{"msg":str(ans)})
			if request.POST.get("div"):
				n1 = float(request.POST.get("num1"))
				n2 = float(request.POST.get("num2"))
				if n2 == 0:
					ans = " Number 2 cannot be 0 "
				else:
					ans = str(n1) + " / " + str(n2) + " = " + str(round(n1/n2,2))
				return render(request,"calc.html",{"msg":str(ans)})
			if request.POST.get("mod"):
				n1 = float(request.POST.get("num1"))
				n2 = float(request.POST.get("num2"))
				if n2 == 0:
					ans = " Number 2 cannot be 0 "
				else:
					ans = str(n1) + " % " + str(n2) + " = " + str(round(n1%n2,2))
				return render(request,"calc.html",{"msg":str(ans)})
		else:
			return render(request,"calc.html")
	else:
		return redirect("ulogin")


