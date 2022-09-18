from django.shortcuts import render,HttpResponse,redirect
from .models import foodExercise
def home(request):
    return render(request,"index.html")
def add_data(request):
    Ffname = request.POST.get("fname")
    Flname = request.POST.get("lname")
    Femail = request.POST.get("email")
    Fphone_no = request.POST.get("phone_no")
    Fno_people = request.POST.get("no_people")
    Fenquiry = request.POST.get("enquiry")

    obj = foodExercise.objects.create(Cname=Ffname,Clname=Flname,Cemail=Femail,Cphone=Fphone_no,Cno_people=Fno_people,Cenquiry=Fenquiry)
    obj.save()
    return redirect("/")

