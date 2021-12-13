from django.shortcuts import render,redirect
from .models import Analytics
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == "GET": 
        return render(request, 'home.html')
    else:
        nam = request.POST.get('username')
        comp = request.POST.get('Competency')
        tea = request.POST.get('TeachingSkills')
        pun = request.POST.get('Punctuality')
        pra = request.POST.get('PracticalKnowledge')
        appr = request.POST.get('Approachability')
        control = request.POST.get('ClassControl')
        obj = Analytics( name= nam, competen = comp,teach = tea,punc = pun,prac=pra,approach = appr,classcontrol = control)
        obj.save()
        # print(nam,comp,tea,pun,pra,appr,control)
        messages.success(request, 'Feedback submission successful')
        return render(request, 'home.html')     


