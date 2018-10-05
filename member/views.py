from django.shortcuts import render


# Create your views here.
def google_test(request):
    return render(request, 'OAuthTest.html')
