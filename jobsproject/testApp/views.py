from django.shortcuts import render
from testApp.models import Hydjobs,Begjobs,Punejobs,Channaijobs

# Create your views here.
def index(request):
    return render(request,'testApp/index.html')

def hydview(request):
    hyd_list = Hydjobs.objects.order_by('date')
    my_dict = {'hyd_list':hyd_list}
    return render(request,'testApp/hyd.html',context=my_dict)

def begview(request):
    return render(request,'testApp/beg.html')

def puneview(request):
    return render(request,'testApp/pune.html')

def channaiview(request):
    return render(request,'testApp/channai.html')