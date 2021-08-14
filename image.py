from PIL import Image,ImageDraw
import numpy as np
import matplotlib.pylab as plt

data = np.zeros((20,20))
data[5][3]=1
data[10][7]=1

'''
배율 = 이미지 크기 / 배열 크기
좌표 = 인덱스 * 배율
'''

#배율
s = 300//10
#이미지 크기
h, w = 400,400

#외곽선 굵기
t = 2

#가구 이미지 크기
sh, sw = 40,40

#배경 이미지
background = Image.new('RGB', (h+(t*2), w+(t*2)), '#000000')
back = Image.new('RGB', (h, w), '#FFFFFF')
background.paste(back, (t, t))
#가구 이미지

img1 = Image.new('RGB', ((sh, sw)), 300000)

#가구 이미지 넣기

#인덱스
arridx = np.where(data >0)
for i in range(len(arridx[0])):
    a = int(arridx[0][i])
    y = a * s
    b = int(arridx[1][i])
    x = b * s
    background.paste(img1, (x+t, y+t))

background.save('fur.png')