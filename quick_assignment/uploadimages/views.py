from django.http import HttpResponse
from django.shortcuts import render
from .models import UserDetails

# Create your views here.
def home(request):
    if(request.method == 'POST' and request.FILES['user_image']):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        user_image = request.FILES['user_image']
        userdetails = UserDetails.objects.create(first_name=first_name,last_name=last_name,user_name=username,email=email,user_image=user_image)
        userdetails.save()
        print(user_image)
        userdata = UserDetails.objects.last()
        # userdata = {'first_name':first_name,'last_name':last_name,'user_name':username,'email':email,'user_image':user_image}
        # return HttpResponse('<img src="{{user_image}}" alt="image">')
        return render(request,'show_data.html',{"userdata" : userdata})
    return render(request,'register.html')