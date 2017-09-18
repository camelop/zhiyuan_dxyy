from django.http import HttpResponse
import time

def hello(request):
#  return HttpResponse("Abracadabra!")
  return HttpResponse("Hello <br>"+str(request.get_raw_uri()))

def save(request):
  file = open('record.txt', 'a')
  getString = request.get_raw_uri().split('/')[-1]
  file.write(getString)
  file.write('\n')
  file.close()
  return HttpResponse("Save: <br>"+getString)

def home(request):
  p = 5
# return HttpResponse('Welcome, <a target="_blank" href="/logout/">logout'+str(p)+'</a>')  
  return HttpResponse('Nothing u can do.')

def alive(request):
  return HttpResponse('I\'m alive!<br>'+str(time.ctime()))

import win32api

def ex(request):
  win32api.ShellExecute(0, 'open', 'C:\\UTJS_Server\\utjs_backend.exe', '', '', 1)
  return HttpResponse('Done')