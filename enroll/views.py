from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def showdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Your Account create successfully')
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render (request,'enroll/sturegistration.html',{'form':fm})    