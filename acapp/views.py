from django.shortcuts import render
from .forms import AcForm
from math import *

# Create your views here.
def home(request):
	if request.method == "POST":
		num = float(request.POST.get("num"))
		area = pi * pow(num,2)
		circ = 2 * pi * num
		msg = " The Number " + str(num)  + " has area " +str(area)  + " and circumference " + str(circ)
		ac = AcForm()
		return render(request,"home.html",{"ac":ac , "msg":msg})
	else:
		ac = AcForm()
		return render(request,"home.html",{"ac":ac})
