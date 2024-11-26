from django.shortcuts import render

# Create your views here.
def eventView(request):
  return render(request,'eventView.html')