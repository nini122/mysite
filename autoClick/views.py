import os
import subprocess
import sys

import numpy as np
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from .models import Coordinate


# class autoClick(ListView):
#     model = Coordinate


def button(request):
    return render(request,'index.html')


def coordinate(request):
    subprocess.run([sys.executable, 'C:/Users/mhyon/PycharmProjects/myweb/venv/mysite/autoClick/coordinate.py'],
                   shell=False, stdout=subprocess.PIPE)
    out = 'saved the coordinate'
    return render(request, 'index.html', {'data2': out})


def inputClicks(request):
    c = request.POST.get('int')
    i = request.POST.get('interval')

    npPath = "C:/Users/mhyon/PycharmProjects/myweb/venv/mysite/autoClick"
    npName = os.path.join(npPath, "ci.npy")
    np.save(npName, arr=c)

    # np.save('c', arr=i)
    # out = ci
    return render(request, 'index.html', {'data3': c})


def click(request):
    out = subprocess.run([sys.executable, 'C:/Users/mhyon/PycharmProjects/myweb/venv/mysite/autoClick/click.py'],
                         shell=False, stdout=subprocess.PIPE)
    return render(request, 'index.html', {'data1': out.stdout})


class autoClick1(CreateView):
    model = Coordinate
    fields = ['clicks', 'url']
    # fields = ['interval', 'url']

    template_name = "index"
