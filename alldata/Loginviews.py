from django.shortcuts import render,HttpResponse, redirect
from .storemodels import Employee
from .storework import Worksubmit
# Create your views here.
def login(request):
    if request.method == 'POST' and 'submit1' in request.POST:
        U_ID=request.POST.get('U')
        passwords=request.POST.get('Passw')
        print('Logined')
        try:
            password=Employee.objects.get(Unique_ID=U_ID)
            id=password.Unique_ID
            pswd=password.Password
            username=password.Employee_Name
            print('Try in button 1')
            if id == U_ID and pswd == passwords:
                print('Match')
                print(username)
                context={
                    'data': id,
                    'displayname': username,
                    }
                return render(request,'Work.html',context)
            else:
                return render(request,'erroruser.html')
                print('else')
        except:
            print('None')
            return render(request,'erroruser.html')
    if request.method == 'POST' and 'submit2' in request.POST:
        try:
            print('Try in button 2')
            id=request.POST.get('unique')
            fromhour=request.POST.get('from')
            description=request.POST.get('description')
            tohour=request.POST.get('to')
            print('html work id:',id)
            print('html from hour:' ,fromhour)
            print('html dscription:' ,description)
            print('html tohour:' ,tohour)
            print('submitted')
            if id != "":
                user=Worksubmit()
                user.uniqueID=id
                user.work_from=fromhour
                user.Work_Description=description
                user.work_to=tohour
                user.save()
            else:
                print('Field is null')
        except:
            print('Button 2 Error')
            return render(request,'erroruser.html')

    return render(request,'Login.html')
