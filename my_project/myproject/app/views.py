from django.shortcuts import render
import time
import datetime

# Create your views here.
def test(request):
    current = datetime.datetime.now()
    time.sleep(1)
    return render(request,'testPage.html',{"ct":current})