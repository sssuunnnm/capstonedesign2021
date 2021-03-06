from django.shortcuts import render, redirect
# from .models import user_info,file
from . import main
import random
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import user_info, File, Rating, layout, Grouptable, Usertable, Testrate

array1 = np.zeros((20, 20))
username = ''
age = '20s'
gender = '여'
job = 'univ_students'
room_name = ''
user = User.objects
# test1 = Test()
# rating1 = Rating()
furniture_list = ['kitchen', 'front', 'refri', 'restroom', 'bed', 'closet', 'washer']
tagvalue=0
groupvalue=0
infolist=[]
personal = 0
lay= layout()
#group = Grouptable.objects.all()
#usertable = Usertable.objects.all()
#testrate = Testrate.objects.all()
pic1 =0
pic2 =0
pic3 =0
def home(request):
    return render(request, 'home.html')

def info1(request):
    return render(request, 'info1.html')

@csrf_exempt
def info2(request):
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    job = request.POST.get('job')
    {'age': age}, {'job' : job}, {'gender': gender}
    infolist, personal= main.by_info(gender, age)

    return render(request, 'info2.html')

def info3(request):
    room_name=request.GET.get('Rname')
    user_info.room_name = room_name

    return render(request, 'info3.html',{'room_name':room_name})

def info4(request):
    chk_fur1 = request.POST.getlist('chk_fur1[]')
    # 아무 가구도 없을 때
    if 'none' in chk_fur1:
        pic1=0 ; pic2=0; pic3=0;
        return render(request, 'recommend1.html',{'pic1': pic1,'pic2': pic2,'pic3': pic3})
    kname = []
    if 'restroom' in chk_fur1:
        kname4 = request.POST.getlist('Kname4[]')
        if (len(kname4) == 1):
            kname44 = list(map(int, kname4[0].split(',')))
            groupvalue = main.grouping(kname44)
            kname.append(kname44)
    if 'kitchen' in chk_fur1:
        kname1 = request.POST.getlist('Kname1[]')
        if (len(kname1) == 1):
            kname11 = list(map(int, kname1[0].split(',')))
            tagvalue = main.tagging(kname11,groupvalue)
            kname.append(kname11)
    #array1 = main.fixgenerate(chk_fur1, kname)
    lay.restLoca =groupvalue
    lay.kitchenLoca = tagvalue
    lay.save()
    return render(request, 'info4.html', {'array1': array1})

def recommend(request):
    groupid = lay.restLoca
    tagid = lay.kitchenLoca
    pic1, pic2, pic3 = main.pic(groupid, tagid)
    return render(request, 'recommend.html', {'pic1': pic1,'pic2': pic2,'pic3': pic3})


def loading(request):
    chk_fur2 = request.POST.getlist('chk_fur2[]')
    if len(chk_fur2)>=1:
        #array1 = main.addgenerate(chk_fur2)
        back = Image.open("back3.png")
        back.save("back1.png")
        print(array1)
        back = Image.new('RGB', (400, 400), '#AAAAAA')
        back.save("002.png")
        #main.show_image1(array1, "back1.png")
        image = Image.open("back1.png")
        image.save('추천.png')

    return render(request, 'loading.html')

def thanks(request):
    this = Tags.objects.latest('id')
    userob = Usertable.objects.get(pk=personal)
    userob.members+=1
    r1 = int(request.POST.get('chk_info1'))
    r2 = int(request.POST.get('chk_info2'))
    r3 = int(request.POST.get('chk_info3'))
    room1 = Rating()
    room1.tags = this
    room1.rating = r1
    room1.save()
    room2 = Rating()
    room2.tags = this
    room2.rating = r2
    room2.save()
    room3 = Rating()
    room3.tags = this
    room3.rating = r3
    room3.save()

    return render(request, 'thanks.html')


# 회원 가입
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            if request.POST['first_name'] is not None and request.POST['job'] \
                    is not None and request.POST['day'] is not None and request.POST['month'] is not None and \
                    request.POST['year'] is not None and request.POST['gender']:
                # user 객체를 새로 생성
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                                first_name=request.POST['first_name'])
                auth.login(request, user)
                userInfo = user_info()
                userInfo.gender = request.POST['gender']
                userInfo.user = request.user
                userInfo.job = request.POST['job']
                userInfo.year = request.POST['year']
                userInfo.month = request.POST['month']
                userInfo.day = request.POST['day']
                # userID = auth.authenticate(request, username='username', password='password')
                # userinfo = user_info.objects.all
                # userinfo = user_info(user_id=User.id, gender=request.POST['gender'], job=request.POST['job'])
                userInfo.save()
                # 로그인 한다
                auth.login(request, user)
                {'username': username}
                {'job': job}
                {'gender': gender}
                {'user': user}
                return redirect('/')

    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')


# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            {'user': user}
            {'username': username}

            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다
    else:
        return render(request, 'login.html')


# 로그 아웃
def logout(request):
    auth.logout(request)
    user = ''
    # {'user' : user}
    return redirect('/')
