from django.shortcuts import render,redirect
from.models import Movie
from django.http import HttpResponse

# Create your views here.
def home(req):
    movies=Movie.objects.all()
    return render(req,'index.html',{'movies':movies})
def register(req):
    if req.method=='POST':
        name=req.POST.get('name','')
        rating=req.POST.get('rating','')
        type=req.POST.get('type','')
        language=req.POST.get('language','')
        certificate=req.POST.get('certificate','')
        category=req.POST.get('category','')
        duration=req.POST.get('duration','')
        date=req.POST.get('date','')
        poster=req.FILES['poster']
        banner=req.FILES['banner']
        movie=Movie(name=name,rating=rating,type=type,language=language,certificate=certificate,category=category,duration=duration,date=date,poster=poster,banner=banner)    
        movie.save()
    return render(req,'register.html')
def details(req,id):
    movies=Movie.objects.get(id=id)
    return render(req,'details.html',{'movies':movies})

def update(req,id):
    movies=Movie.objects.get(id=id)
    if req.method=='POST':
        name=req.POST.get('name','')
        rating=req.POST.get('rating','')
        type=req.POST.get('type','')
        language=req.POST.get('language','')
        certificate=req.POST.get('certificate','')
        category=req.POST.get('category','')
        duration=req.POST.get('duration','')
        date=req.POST.get('date','')
        poster=req.FILES['poster']
        banner=req.FILES['banner']
        Movie.objects.filter(id=id).update(name=name,rating=rating,type=type,language=language,certificate=certificate,category=category,duration=duration,date=date,poster=poster,banner=banner)
        return redirect("details")
    return render(req,'update.html',{"movies":movies})


def delete(req,id):
    tasks=Movie.objects.get(id=id)
    if req.method=="POST":
                                              
        
        Movie.objects.filter(id=id).delete()
        return redirect("home")
    return render(req,'delete.html',{"task":tasks})
