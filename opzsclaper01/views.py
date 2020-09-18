from django.shortcuts import render
from .models import News
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup

from django.http import HttpResponse
import csv
import io

from opzsclaper01.modules import twitterscr

class Create(CreateView):
   template_name = 'home.html'
   model = News
   fields = ('url',)
   success_url = reverse_lazy('list')

def listfunc(request):
   context = {'list': twitterscr.data_get(),}
   return render(request, 'list.html', context)


def csvdownload(request):
   response = HttpResponse(content_type='text/csv; charset=UTF-8')
   filename = urllib.parse.quote(('omedetou.csv'))
   response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
   writer = csv.writer(response)
   writer.writerow(['text', 'id', 'user', 'created_at'])
   writer.writerows(twitterscr.data_get())
   return response