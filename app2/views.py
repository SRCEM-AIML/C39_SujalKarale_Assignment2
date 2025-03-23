from django.shortcuts import render

# Create your views here.


def sample_page(request):
    return render(request, 'app2/sample.html')
