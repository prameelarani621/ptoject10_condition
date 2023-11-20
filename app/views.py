from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':1000,'b':1388,'c':633867}
    return render(request,'condition.html',d)