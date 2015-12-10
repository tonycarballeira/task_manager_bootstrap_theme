from django.shortcuts import render

# Create your views here.

#basic view function below:
def home(request):

	return render(request, "home.html", {})