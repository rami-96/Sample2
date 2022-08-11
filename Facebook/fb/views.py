from django.shortcuts import render, redirect
from .models import Register

# Create your views here.



def Sample(request):
    if request.method == 'POST':
        member = Register(FirstName=request.POST['firstname'],SurtName=request.POST['surname'],Email=request.POST['email'],
                        Password=request.POST['password'],DOB=request.POST['dob'],)

        member.save()
        return redirect('index/')
    else:
        return render(request, 'index.html')

def login_request(request):
    if request.method == 'POST':
        if Register.objects.filter(Email=request.POST['email'], Password=request.POST['Password']).exists():
            member = Register.objects.get(Email=request.POST['email'], Password=request.POST['Password'])
            return render(request, 'index.html')
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'index.html', context)
    return render(request=request, template_name="index.html")
