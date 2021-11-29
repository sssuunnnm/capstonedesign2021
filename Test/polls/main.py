# This is a sample Python script.
import random
import numpy as np
from PIL import ImageFont, ImageDraw, Image
array1 = np.zeros((20,20))
class user:
    def __init__ (self, age, gender, job):
        self.age = age
        self.gender = gender
        self.job = job
    def setdata (self, age, gender, job):
        self.age = age
        self.gender = gender
        self.job = job
    def getage(self):
        return self.age
    def getgender(self):
        return self.gender
    def getjob(self):
        return self.job

class bed:
    def __init__ (self, wsize,hsize,loca1,loca2,loca3,loca4,direction,location):
        self.wsize = 8
        self.hsize= 4
        self.loca1 = loca1
        self.loca2 = loca2
        self.loca3 = loca3
        self.loca4 = loca4
        self.direction = direction
        self.location=location
    def settag(self,tag):
        self.tag=1
    def gettag(self):
        return 1
    def setwsize(self,wsize):
        self.wsize = wsize
    def sethsize(self,hsize):
        self.hsize = hsize
    def getwsize(self):
        return self.wsize
    def gethsize(self):
        return self.hsize

    def setloca1(self,loca1):
        self.loca1 = loca1
    def setloca2(self, loca2):
        self.loca2 = loca2
    def setloca3(self,loca3):
        self.loca3 = loca3
    def setloca4(self,loca4):
        self.loca4 = loca4

    def getloca1(self):
        return self.loca1
    def getloca2(self):
        return self.loca2
    def getloca3(self):
        return self.loca3
    def getloca4(self):
        return self.loca4

    def setdirection(self,direction):
        self.direction=direction
    def getdirection(self):
        return self.direction
    def setlocation(self,location):
        self.location=location
    def getlocation(self):
        return self.location


class desk:
    def __init__ (self,wsize,hsize,loca1,loca2,loca3,loca4,direction,location):
        self.wsize = 8
        self.hsize = 3
        self.loca1 = loca1
        self.loca2 = loca2
        self.loca3 = loca3
        self.loca4 = loca4
        self.direction = direction
        self.location=location
    def settag(self):
        self.tag=2
    def gettag(self):
        return 2

    def setwsize(self, wsize):
        self.wsize = wsize
    def sethsize(self, hsize):
        self.hsize = hsize

    def getwsize(self):
        return self.wsize
    def gethsize(self):
        return self.hsize

    def setloca1(self, loca1):
        self.loca1 = loca1
    def setloca2(self, loca2):
        self.loca2 = loca2
    def setloca3(self, loca3):
        self.loca1 = loca3
    def setloca4(self, loca4):
        self.loca4 = loca4

    def getloca1(self):
        return self.loca1
    def getloca2(self):
        return self.loca2
    def getloca3(self):
        return self.loca3
    def getloca4(self):
        return self.loca4

    def setdirection(self,direction):
        self.direction=direction
    def getdirection(self):
        return self.direction

    def setlocation(self,location):
        self.location=location
    def getlocation(self):
        return self.location

class closet:
    def __init__ (self, wsize,hsize,loca1,loca2,loca3,loca4,direction,location):
        self.wsize = 4
        self.hsize = 2
        self.loca1 = loca1
        self.loca2 = loca2
        self.loca3 = loca3
        self.loca4 = loca4
        self.direction=direction
        self.location=location
    def settag(self):
        self.tag=3
    def gettag(self):
        return 3

    def setwsize(self, wsize):
        self.wsize = wsize
    def sethsize(self, hsize):
        self.hsize = hsize

    def getwsize(self):
        return self.wsize
    def gethsize(self):
        return self.hsize

    def setloca1(self, loca1):
        self.loca1 = loca1
    def setloca2(self, loca2):
        self.loca2 = loca2
    def setloca3(self, loca3):
        self.loca3 = loca3
    def setloca4(self, loca4):
        self.loca4 = loca4

    def getloca1(self):
        return self.loca1
    def getloca2(self):
        return self.loca2
    def getloca3(self):
        return self.loca3
    def getloca4(self):
        return self.loca4

    def setdirection(self,direction):
        self.direction=direction
    def getdirection(self):
        return self.direction

    def setlocation(self,location):
        self.location=location
    def getlocation(self):
        return self.location

class wmachine:
    def __init__(self, wsize,hsize, loca1,loca2,loca3,loca4,direction,location):
        self.wsize = 3
        self.hsize = 3
        self.loca1 = loca1
        self.loca2 = loca2
        self.loca3 = loca3
        self.loca4 = loca4
        self.direction = '가로'
        self.location=location

    def settag(self):
        self.tag = 4
    def gettag(self):
        return 4

    def setwsize(self, wsize):
        self.wsize = 8
    def sethsize(self, hsize):
        self.hsize = 4
    def getwsize(self):
        return self.wsize
    def gethsize(self):
        return self.hsize

    def setloca1(self, loca1):
        self.loca1 = loca1
    def setloca2(self, loca2):
        self.loca2 = loca2
    def setloca3(self, loca3):
        self.loca3 = loca3
    def setloca4(self, loca4):
        self.loca4 = loca4

    def getloca1(self):
        return self.loca1
    def getloca2(self):
        return self.loca2
    def getloca3(self):
        return self.loca3
    def getloca4(self):
        return self.loca4
    def setdirection(self,direction):
        self.direction=direction
    def getdirection(self):
        return self.direction
    def setlocation(self,location):
        self.location=location
    def getlocation(self):
        return self.location

class restroom:
    def __init__(self, wsize,hsize, loca1,loca2,loca3,loca4,direction,location):
        self.wsize = 3
        self.hsize = 3
        self.loca1 = loca1
        self.loca2 = loca2
        self.loca3 = loca3
        self.loca4 = loca4
        self.direction = '가로'
        self.location=location

    def settag(self):
        self.tag = 5
    def gettag(self):
        return 5

    def setwsize(self, wsize):
        self.wsize = wsize
    def sethsize(self, hsize):
        self.hsize = hsize

    def getwsize(self):
        return self.wsize
    def gethsize(self):
        return self.hsize

    def setloca1(self, loca1):
        self.loca1 = loca1
    def setloca2(self, loca2):
        self.loca2 = loca2
    def setloca3(self, loca3):
        self.loca3 = loca3
    def setloca4(self, loca4):
        self.loca4 = loca4

    def getloca1(self):
        return self.loca1
    def getloca2(self):
        return self.loca2
    def getloca3(self):
        return self.loca3
    def getloca4(self):
        return self.loca4

    def setdirection(self,direction):
        self.direction=direction
    def getdirection(self):
        return self.direction

    def setlocation(self,location):
        self.location=location
    def getlocation(self):
        return self.location

class storage:
    def __init__(self, wsize,hsize, loca1,loca2,loca3,loca4,direction,location):
        self.wsize = 4
        self.hsize = 4
        self.loca1 = loca1
        self.loca2 = loca2
        self.loca3 = loca3
        self.loca4 = loca4
        self.direction=direction
        self.location=location

    def settag(self):
        self.tag = 6
    def gettag(self):
        return 6

    def setwsize(self, wsize):
        self.wsize = wsize
    def sethsize(self, hsize):
        self.hsize = hsize

    def getwsize(self):
        return self.wsize
    def gethsize(self):
        return self.hsize

    def setloca1(self, loca1):
        self.loca1 = loca1
    def setloca2(self, loca2):
        self.loca2 = loca2
    def setloca3(self, loca3):
        self.loca3 = loca3
    def setloca4(self, loca4):
        self.loca4 = loca4

    def getloca1(self):
        return self.loca1
    def getloca2(self):
        return self.loca2
    def getloca3(self):
        return self.loca3
    def getloca4(self):
        return self.loca4

    def setdirection(self,direction):
        self.direction=direction
    def getdirection(self):
        return self.direction
    def setlocation(self,location):
        self.location=location
    def getlocation(self):
        return self.location

class refri:
    def __init__(self, wsize,hsize, loca1,loca2,loca3,loca4,direction,location):
        self.wsize = 3
        self.hsize= 3
        self.loca1 = loca1
        self.loca2 = loca2
        self.loca3 = loca3
        self.loca4 = loca4
        self.direction=direction
        self.location=location

    def settag(self):
        self.tag = 7

    def gettag(self):
        return 7

    def setwsize(self, wsize):
        self.wsize = wsize

    def sethsize(self, hsize):
        self.hsize = hsize

    def getwsize(self):
        return self.wsize

    def gethsize(self):
        return self.hsize

    def setloca1(self, loca1):
        self.loca1 = loca1

    def setloca2(self, loca2):
        self.loca2 = loca2

    def setloca3(self, loca3):
        self.loca3 = loca3

    def setloca4(self, loca4):
        self.loca4 = loca4

    def getloca1(self):
        return self.loca1
    def getloca2(self):
        return self.loca2
    def getloca3(self):
        return self.loca3
    def getloca4(self):
        return self.loca4

    def setdirection(self,direction):
        self.direction=direction
    def getdirection(self):
        return self.direction
    def setlocation(self,location):
        self.location=location
    def getlocation(self):
        return self.location

class kitchen:
    def __init__(self, wsize,hsize, loca1,loca2,loca3,loca4,direction,location):
        self.wsize = 6
        self.hsize= 3
        self.loca1 = loca1
        self.loca2 = loca2
        self.loca3 = loca3
        self.loca4 = loca4
        self.direction=direction
        self.location=location

    def settag(self):
        self.tag = 8

    def gettag(self):
        return 8

    def setwsize(self, wsize):
        self.wsize = wsize

    def sethsize(self, hsize):
        self.hsize = hsize

    def getwsize(self):
        return self.wsize

    def gethsize(self):
        return self.hsize

    def setloca1(self, loca1):
        self.loca1 = loca1

    def setloca2(self, loca2):
        self.loca2 = loca2

    def setloca3(self, loca3):
        self.loca3 = loca3

    def setloca4(self, loca4):
        self.loca4 = loca4

    def getloca1(self):
        return self.loca1
    def getloca2(self):
        return self.loca2
    def getloca3(self):
        return self.loca3
    def getloca4(self):
        return self.loca4

    def setdirection(self,direction):
        self.direction=direction
    def getdirection(self):
        return self.direction

    def setlocation(self,location):
        self.location=location
    def getlocation(self):
        return self.location

class front:
    def __init__(self, wsize,hsize, loca1,loca2,loca3,loca4,direction,location):
        self.wsize = 2
        self.hsize= 2
        self.loca1 = loca1
        self.loca2 = loca2
        self.loca3 = loca3
        self.loca4 = loca4
        self.direction=direction
        self.location=location

    def settag(self):
        self.tag = 9

    def gettag(self):
        return 9

    def setwsize(self, wsize):
        self.wsize = wsize

    def sethsize(self, hsize):
        self.hsize = hsize

    def getwsize(self):
        return self.wsize

    def gethsize(self):
        return self.hsize

    def setloca1(self, loca1):
        self.loca1 = loca1

    def setloca2(self, loca2):
        self.loca2 = loca2

    def setloca3(self, loca3):
        self.loca3 = loca3

    def setloca4(self, loca4):
        self.loca4 = loca4

    def getloca1(self):
        return self.loca1
    def getloca2(self):
        return self.loca2
    def getloca3(self):
        return self.loca3
    def getloca4(self):
        return self.loca4

    def setdirection(self,direction):
        self.direction=direction
    def getdirection(self):
        return self.direction

    def setlocation(self,location):
        self.location=location
    def getlocation(self):
        return self.location

class table:
    def __init__(self, wsize,hsize, loca1,loca2,loca3,loca4,direction,location):
        self.wsize = 2
        self.hsize= 2
        self.loca1 = loca1
        self.loca2 = loca2
        self.loca3 = loca3
        self.loca4 = loca4
        self.direction='가로'
        self.location=location

    def settag(self):
        self.tag = 10

    def gettag(self):
        return 10

    def setwsize(self, wsize):
        self.wsize = wsize

    def sethsize(self, hsize):
        self.hsize = hsize

    def getwsize(self):
        return self.wsize

    def gethsize(self):
        return self.hsize

    def setloca1(self, loca1):
        self.loca1 = loca1

    def setloca2(self, loca2):
        self.loca2 = loca2

    def setloca3(self, loca3):
        self.loca3 = loca3

    def setloca4(self, loca4):
        self.loca4 = loca4

    def getloca1(self):
        return self.loca1
    def getloca2(self):
        return self.loca2
    def getloca3(self):
        return self.loca3
    def getloca4(self):
        return self.loca4

    def setdirection(self,direction):
        self.direction=direction
    def getdirection(self):
        return self.direction

    def setlocation(self,location):
        self.location=location
    def getlocation(self):
        return self.location


#가구태그값채우기 5*5
def locationcal(a):
    if a.getlocation()>=1 and a.getlocation()<=5:
        for i in range((a.getlocation()-1)*4,a.getlocation()*4):
            array1[0][i]=a.gettag()
            array1[1][i]=a.gettag()
            array1[2][i] = a.gettag()
            array1[3][i] = a.gettag()

    if a.getlocation() >= 6 and a.getlocation()<=10:
        for i in range((a.getlocation()-6)*4,(a.getlocation()-5)*4):
            array1[4][i] = a.gettag()
            array1[5][i] = a.gettag()
            array1[6][i] = a.gettag()
            array1[7][i] = a.gettag()
    if a.getlocation() >= 11 and a.getlocation()<=15:
        for i in range((a.getlocation()-11)*4,(a.getlocation()-10)*4):
            array1[8][i] = a.gettag()
            array1[9][i] = a.gettag()
            array1[10][i] = a.gettag()
            array1[11][i] = a.gettag()
    if a.getlocation() >= 16 and a.getlocation()<=20:
        for i in range((a.getlocation()-16)*4,(a.getlocation()-15)*4):
            array1[12][i] = a.gettag()
            array1[13][i] = a.gettag()
            array1[14][i] = a.gettag()
            array1[15][i] = a.gettag()
    if a.getlocation() >= 21 and a.getlocation()<=25:
        for i in range((a.getlocation()-21)*4,(a.getlocation()-20)*4):
            array1[16][i] = a.gettag()
            array1[17][i] = a.gettag()
            array1[18][i] = a.gettag()
            array1[19][i] = a.gettag()
    return array1

def initial(a,index1,index2):
    a.setloca1(index1)
    a.setloca2(index2)
    if (a.direction == '가로'):
        a.setloca3(index1 + a.hsize)
        a.setloca4(index2 + a.wsize)
        for i in range(index1, index1 + a.hsize):
            for j in range(index2, index2 + a.wsize):
                array1[i][j] = a.gettag()
    if (a.direction == '세로'):
        a.setloca3(index1 + a.wsize)
        a.setloca4(index2 + a.hsize)
        for i in range(index1, index1 + a.wsize):
            for j in range(index2, index2 + a.hsize):
                array1[i][j] = a.gettag()


def find_index6(array1, a):
    arridx = np.where(array1 == 0)
    in1 = 0
    in2 = 0
    while(1):
        cont = 0
        pow = random.choice([1, 2])
        if pow == 1:
            while(1):
                cont = 0
                in1 = random.choice([0, 14 - a.hsize])
                in2 = random.randint(0, 14 - a.wsize)
                for i in range(in1, in1 + a.hsize):
                    for j in range(in2, in2 + a.wsize):
                        if array1[i][j] != 0:
                            cont = 1
                if cont == 0:
                    break
        else:
            while (1):
                cont = 0
                in2 = random.choice([0, 14 - a.wsize])
                in1 = random.randint(0, 14 - a.hsize)
                for i in range(in1, in1 + a.hsize):
                    for j in range(in2, in2 + a.wsize):
                        if array1[i][j] != 0:
                            cont = 1
                if cont == 0:
                    break
        if array1[in1][in2] == 0:
            break
    initial(a, in1, in2)


def fixgenerate(chk,k):
    listchk = []
    listloca=[]
    for i in range(len(chk)):
        if chk[i] == 'kitchen':
            if(len(k[i])>1):
                if(k[i][1]-k[i][0]==1):
                    listchk.append(kitchen(6, 3, 0, 0, 0, 0, '가로', k[i][0]))
            else:
                listchk.append(kitchen(6, 3, 0, 0, 0, 0, '세로', k[i][0]))
            listloca.append(k[i])
        elif chk[i] == 'front':
            listchk.append(front(3, 3, 0, 0, 0, 0, '가로', k[i][0]))
            listloca.append(k[i])
        elif chk[i] == 'refri':
            listchk.append(refri(3, 3, 0, 0, 0, 0, '가로', k[i][0]))
            listloca.append(k[i])
        elif chk[i] == 'restroom':
            listchk.append(restroom(3, 3, 0, 0, 0, 0, '가로', k[i][0]))
            listloca.append(k[i])
        elif chk[i] == 'bed':
            if(len(k[i])>1):
                if(k[i][1]-k[i][0]==1):
                    listchk.append(bed(8, 4, 0, 0, 0, 0, '가로', k[i][0]))
            else:
                listchk.append(bed(8, 4, 0, 0, 0, 0, '세로', k[i][0]))
            listloca.append(k[i])
        elif chk[i] == 'closet':
            if(len(k[i])>1):
                if(k[i][1]-k[i][0]==1):
                    listchk.append(closet(4, 2, 0, 0, 0, 0, '가로', k[i][0]))
            else:
                listchk.append(closet(4, 2, 0, 0, 0, 0, '세로', k[i][0]))
            listloca.append(k[i])
        elif chk[i] == 'wmachine':
            listchk.append(wmachine(3, 3, 0, 0, 0, 0, '가로', k[i][0]))
            listloca.append(k[i])
    for i in range(len(listchk)):
        for i in range(len(listloca)):
            for j in range(len(listloca[i])):
                listchk[i].setlocation(listloca[i][j])
                locationcal(listchk[i])
    return array1

def addgenerate(chk):
    listchk=[]
    for i in range(len(chk)):
        if chk[i]=='bed':
            listchk.append(bed(8,4,0,0,0,0,'가로',0))
        elif chk[i] == 'wmachine':
            listchk.append(wmachine(3, 3, 0, 0, 0, 0, '가로', 0))
        elif chk[i] == 'desk':
            listchk.append(desk(8, 3, 0, 0, 0, 0, '세로', 0))
        elif chk[i]=='closet':
            listchk.append(closet(4,2,0,0,0,0,'세로',0))
        elif chk[i]=='storage':
            listchk.append(storage(4,4,0,0,0,0,'가로',0))
        elif chk[i]=='refri':
            listchk.append(refri(6,6,0,0,0,0,'가로',0))
        elif chk[i]=='table':
            listchk.append(table(2,2,0,0,0,0,'가로',0))
    for i in range(len(listchk)):
        find_index6(array1,listchk[i])
    return array1


def show_image1(array1,background):
    # 2차원 배열, 텍스트, 가구 코드, 배경 이미지
    # 배열에 가구코드가 있을 시 실행
    print(array1)
    for i in range(1, 11):
        if i == 1:
            furniture_image = Image.open("bed.png")
        elif i == 2:
            furniture_image = Image.open("desk.png")
        elif i == 3:
            furniture_image = Image.open("closet.png")
        elif i == 4:
            furniture_image = Image.open("wmachine.png")
        elif i == 5:
            furniture_image = Image.open("restroom.png")
        elif i == 6:
            furniture_image = Image.open("storage.png")
        elif i == 7:
            furniture_image = Image.open("refri.png")
        elif i == 8:
            furniture_image = Image.open("kitchen.png")
        elif i == 9:
            furniture_image = Image.open("front.png")
        elif i == 10:
            furniture_image = Image.open("table.png")

        if np.any(array1 == i):
            back = Image.open(background)
            image_size = back.size[0]

            s = image_size // int((np.shape(array1))[0])
            # 인덱스
            # #배열에 가구코드가 하나 이상 들어갔을때를 구분
            arridx = np.where(array1 == i)
            if len(arridx[0]) == 1:
                a = int(arridx[0])
                b = int(arridx[1])
            else:
                a = int(arridx[0][0])
                b = int(arridx[1][0])

            # 가구 이미지 크기
            temp = arridx[0][0]
            count = 0
            for j in arridx[0]:
                if temp == j:
                    count += 1
            # x 길이
            f_size_x = count
            ytemp = arridx[1][0]
            ycount = 0
            for j in arridx[1]:
                if ytemp == j:
                    ycount += 1
            # y 길이
            f_size_y = ycount

            # 좌표
            y = a * s
            x = b * s

            # 가구 이미지 생성
            draw = furniture_image.resize(((s * f_size_x), (s * f_size_y)))
            # 배경 이미지에 가구 이미지 붙여넣기
            back.paste(draw, (x, y))
            back.save(background)


def func1(job, age):
    j = job; a = age;
    newlist = []
    if( j == 'students' or j == 'students' or a == '10s'):
        newlist.append('desk')


    return newlist

def func2(furlist):
    alist = []
    alist.append('desk')
    # 침대 없으면 무조건 침대 추가


    return alist