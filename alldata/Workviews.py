from django.shortcuts import render,HttpResponse, redirect
from .storework import Worksubmit
# Create your views here.
def work(request):
    if request.method=='POST' and 'submit2' in request.POST:
        id=request.POST.get('unique')
        fromhour=request.POST.get('from')
        description=request.POST.get('description')
        tohour=request.POST.get('to')
        if id != "":
            user=Worksubmit()
            user.uniqueID=id
            user.work_from=fromhour
            user.Work_Description=description
            user.work_to=tohour
            user.save()
        else:
            print('Field is null')
    return render(request,'Work.html')
