from django.shortcuts import render
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import matplotlib.pyplot as plt
from django.http import JsonResponse
# Create your views here.

# from django.views.decorators.csrf import csrf_protect

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
def Matplot(request):
    if request.method =='POST':
        data = json.loads(request.body)
        x = data['y']
        y = data['nomi']
        plt.pie(x, labels=y)
        d = plt.show()
        return JsonResponse(d, safe=True)
    else:
        return JsonResponse('xato')

@method_decorator(csrf_exempt, name='dispatch')
def Matplot1(request):
    if request.method =='POST':
        data = json.loads(request.body)
        x = data['nomi']
        y = data['y']
        plt.bar(x, y, color="#4CAF50")
        d = plt.show()
        return JsonResponse(d, safe=True)
    else:
        return JsonResponse('xato')
@method_decorator(csrf_exempt, name='dispatch')
def Matplot2(request):
    if request.method =='POST':
        data = json.loads(request.body)
        x = data['y']
        plt.plot(x, marker = 'o', ms=10, mec = 'r', color = 'k', linestyle = 'dashed')
        d = plt.show()
        return JsonResponse(d, safe=True)
    else:
        return JsonResponse('xato')