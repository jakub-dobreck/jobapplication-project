from django.shortcuts import render

def jobapp_form(request):
    return render(request, 'jobapp_form.html')

def candidate_info(request):
    return render(request, 'candidate_info.html')
