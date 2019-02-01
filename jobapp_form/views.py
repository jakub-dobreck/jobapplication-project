from django.shortcuts import render
from datetime import datetime
from .models import Candidate

def jobapp_form(request):
	if request.method == 'POST':
		candidate = Candidate()
		candidate.first_name = request.POST['first_name']
		candidate.last_name = request.POST['last_name']
		candidate.picture_url = request.POST['picture']
		candidate.cv_url = request.POST['cv']
		candidate.save()
		return render(request, 'candidate_info.html', { "candidate": candidate })
	else:
		return render(request, 'jobapp_form.html')
