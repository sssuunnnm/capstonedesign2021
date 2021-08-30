from django.shortcuts import render, redirect
from .models import user_info,file
from . import main
import random
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from PIL import Image,ImageDraw, ImageFont
from django.utils.datastructures import MultiValueDictKeyError

array1=np.zeros((20,20))
def home(request):
    return render(request, 'home.html')

def info1(request):
    return render(request, 'info1.html')

@csrf_exempt
def info2(request):
    #data=user_info()
    #data.age=request.POST['age']
    #data.job=request.POST['job']
    #data.gender=request.POST['gender']
    return render(request, 'info2.html')

def info3(request):
    #user_info.room_name=request.GET.get('Rname')
    #shape=request.GET.get('chk_shape')

    #print("shape",shape)
    return render(request, 'info3.html')

def info4(request):
    chk_fur1 = request.POST.getlist('chk_fur1[]')
    kname = []
    kname1 = request.POST.getlist('Kname1[]')
    if (len(kname1) == 1):
        kname11 = list(map(int, kname1[0].split(',')))
        kname.append(kname11)

    kname2 = request.POST.getlist('Kname2[]')
    if (len(kname2) == 1):
        kname22 = list(map(int, kname2[0].split(',')))
        kname.append(kname22)
    kname3 = request.POST.getlist('Kname3[]')
    if (len(kname3) == 1):
        kname33 = list(map(int, kname3[0].split(',')))
        kname.append(kname33)

    kname4 = request.POST.getlist('Kname4[]')
    if (len(kname4) == 1):
        kname44 = list(map(int, kname4[0].split(',')))
        kname.append(kname44)

    kname5 = request.POST.getlist('Kname5[]')
    if (len(kname5) == 1):
        kname55 = list(map(int, kname5[0].split(',')))
        kname.append(kname55)

    kname6 = request.POST.getlist('Kname6[]')
    if (len(kname6) == 1):
        kname66 = list(map(int, kname6[0].split(',')))
        kname.append(kname66)

    kname7 = request.POST.getlist('Kname7[]')
    if (len(kname7) == 1):
        kname77 = list(map(int, kname7[0].split(',')))
        kname.append(kname77)
        print(kname77[0])
        print(type(kname77[0]))
    array1=main.fixgenerate(chk_fur1,kname)
    print("fix")
    print(array1)
    return render(request, 'info4.html',{'array1':array1})

def recommend(request):
    msize=request.POST.get('size')
    chk_fur2 = request.POST.getlist('chk_fur2[]')
    array1=main.addgenerate(chk_fur2)
    print("add")
    print(array1)
    back = Image.new('RGB', (400, 400), '#AAAAAA')
    back.save("002.png")
    for i in range(1,10):
        main.show_image1(array1,i,"002.png")
    image = Image.open("002.png")
    image.save('추천.png')
    image.show()
    return render(request, 'recommend.html',{'array1':array1})
def image(request):

    return render
def signup(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')
