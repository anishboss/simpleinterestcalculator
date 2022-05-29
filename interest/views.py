from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.method == "POST":
        principal = float(request.POST['principal'])
        time = float(request.POST['time'])
        rate = float(request.POST['rate'])
        si_yr =  int((principal* time * rate)/100)
        si_month = int(si_yr/12)
        print(si_yr)
        print(si_month)
        context = {'si_yr':si_yr,'si_month':si_month}
        return render(request,'interest/index.html',context)
    else:

        return render(request,'interest/index.html')