from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserProfile

# Create your views here.
@login_required
def index(request):
	return render(request,'index.html')

@login_required
def get_profile(request):
	if request.method=='POST':
		form = UserProfile(request.POST)
	else:
		form = UserProfile()
	return render(request, 'userprofile.html', {'form': form})

