from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def addProfiles(request):
    print("sjhdfhghfsh")
    # return HttpResponse('jhdhfdfh')
    return render(request,'gallery/ profile.html')

def profiles(request):
    return render(request,'home.html')
