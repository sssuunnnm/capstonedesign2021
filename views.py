from django.shortcuts import render, redirect
# from .models import user_info,file
from Test.polls.models import user_info
from . import main
import random
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import user_info

array1 = np.zeros((20, 20))


def home(request):
    return render(request, 'home.html')


def info1(request):
    return render(request, 'info1.html')


@csrf_exempt
def info2(request):
    # data=user_info()
    # data.age=request.POST['age']
    # data.job=request.POST['job']
    # data.gender=request.POST['gender']
    return render(request, 'info2.html')


def info3(request):
    # user_info.room_name=request.GET.get('Rname')
    # shape=request.GET.get('chk_shape')

    # print("shape",shape)
    return render(request, 'info3.html')


def info4(request):
    chk_fur1 = request.POST.getlist('chk_fur1[]')
    kname = []
    if 'kitchen' in chk_fur1:
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
    array1 = main.fixgenerate(chk_fur1, kname)
    print("fix")
    print(array1)
    return render(request, 'info4.html', {'array1': array1})


def recommend(request):
    chk_fur1 = request.POST.getlist('chk_fur1[]')
    print(chk_fur1)
    kname = []
    if 'kitchen' in chk_fur1:
        kname1 = request.POST.getlist('Kname1[]')
        if (len(kname1) == 1):
            kname11 = list(map(int, kname1[0].split(',')))
            kname.append(kname11)
    if 'front' in chk_fur1:
        kname2 = request.POST.getlist('Kname2[]')
        if (len(kname2) == 1):
            kname22 = list(map(int, kname2[0].split(',')))
            kname.append(kname22)
    if 'refri' in chk_fur1:
        kname3 = request.POST.getlist('Kname3[]')
        if (len(kname3) == 1):
            kname33 = list(map(int, kname3[0].split(',')))
            kname.append(kname33)
    if 'restroom' in chk_fur1:
        kname4 = request.POST.getlist('Kname4[]')
        if (len(kname4) == 1):
            kname44 = list(map(int, kname4[0].split(',')))
            kname.append(kname44)
    if 'bed' in chk_fur1:
        kname5 = request.POST.getlist('Kname5[]')
        if (len(kname5) == 1):
            kname55 = list(map(int, kname5[0].split(',')))
            kname.append(kname55)
    if 'closet' in chk_fur1:
        kname6 = request.POST.getlist('Kname6[]')
        if (len(kname6) == 1):
            kname66 = list(map(int, kname6[0].split(',')))
            kname.append(kname66)
    if 'washer' in chk_fur1:
        kname7 = request.POST.getlist('Kname7[]')
        if (len(kname7) == 1):
            kname77 = list(map(int, kname7[0].split(',')))
            kname.append(kname77)
    array1 = main.fixgenerate(chk_fur1, kname)
    msize = request.POST.get('size')
    '''chk_fur2 = request.POST.getlist('chk_fur2[]')
    array1 = main.addgenerate(chk_fur2)
    print("add")
    print(array1)'''
    back = Image.new('RGB', (400, 400), '#AAAAAA')
    back.save("002.png")
    main.show_image1(array1, "back1.png")
    image = Image.open("back1.png")
    image.save('??????.png')
    image.show()
    return render(request, 'recommend.html', {'array1': array1})


def image(request):
    return render


# ?????? ??????
def signup(request):
    # signup ?????? POST ????????? ?????? ???, ????????? ????????? ????????? ????????? ?????????.
    if request.method == 'POST':
        # password??? confirm??? ????????? ?????? ?????????
        if request.POST['password'] == request.POST['confirm']:
            if request.POST['first_name'] is not None and request.POST['last_name'] is not None and request.POST['job']\
                    is not None and request.POST['day'] is not None and request.POST['month'] is not None and request.POST['year'] is not None and request.POST['gender']:
            # user ????????? ?????? ??????
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                                first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                auth.login(request, user)
                userInfo = user_info()
                userInfo.gender = request.POST['gender']
                userInfo.user = request.user
                userInfo.job = request.POST['job']
                userInfo.year = request.POST['year']
                userInfo.month = request.POST['month']
                userInfo.day = request.POST['day']
                #userID = auth.authenticate(request, username='username', password='password')
                #userinfo = user_info.objects.all
                #userinfo = user_info(user_id=User.id, gender=request.POST['gender'], job=request.POST['job'])
                userInfo.save()
                # ????????? ??????
                auth.login(request, user)
                return redirect('/')

    # signup?????? GET ????????? ?????? ???, ???????????? ????????? ????????????.
    return render(request, 'signup.html')


# ?????????
def login(request):
    # login?????? POST ????????? ???????????? ???, ????????? ????????? ?????????.
    if request.method == 'POST':
        # login.html?????? ????????? username??? password??? ??? ????????? ????????????.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # ?????? username??? password??? ???????????? user ????????? ????????????.
        user = auth.authenticate(request, username=username, password=password)

        # ?????? user ????????? ???????????????
        if user is not None:
            # ????????? ??????
            auth.login(request, user)
            return redirect('/')
        # ???????????? ????????????
        else:
            # ??????????????? ?????????????????? ???????????? ?????? login.html ???????????? ????????????.
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    # login?????? GET ????????? ???????????????, ????????? ????????? ????????????
    else:
        return render(request, 'login.html')


# ?????? ??????
def logout(request):
    auth.logout(request)
    return redirect('/')
    # logout?????? POST ????????? ???????????? ???, ???????????? ????????? ?????????.
    #if request.method == 'POST':
    # logout?????? GET ????????? ???????????? ???, ????????? ????????? ????????????.
    #else:
        #return render(request, 'login.html')

# Create your views here.
