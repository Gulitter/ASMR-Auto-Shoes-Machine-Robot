import sys, os
import numpy as np
import time
import firebase_admin
from uuid import uuid4
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import cv2
import RPi.GPIO as GPIO
 
 
GPIO.setmode(GPIO.BCM)
x1e=2
x1s=3
x1d=4

x2e=17
x2s=27
x2d=22

x3e=10
x3s=9
x3d=11

x4e=5
x4s=6
x4d=13

z1e=14
z1s=15
z1d=18

z2e=16
z2s=20
z2d=21

y1e=25
y1s=8
y1d=7
 
GPIO.setup(x1e,GPIO.OUT)
GPIO.setup(x1s,GPIO.OUT)
GPIO.setup(x1d,GPIO.OUT)

GPIO.setup(x2e,GPIO.OUT)
GPIO.setup(x2s,GPIO.OUT)
GPIO.setup(x2d,GPIO.OUT)
 
GPIO.setup(x3e,GPIO.OUT)
GPIO.setup(x3s,GPIO.OUT)
GPIO.setup(x3d,GPIO.OUT)

GPIO.setup(x4e,GPIO.OUT)
GPIO.setup(x4s,GPIO.OUT)
GPIO.setup(x4d,GPIO.OUT)

GPIO.setup(z1e,GPIO.OUT)
GPIO.setup(z1s,GPIO.OUT)
GPIO.setup(z1d,GPIO.OUT)

GPIO.setup(z2e,GPIO.OUT)
GPIO.setup(z2s,GPIO.OUT)
GPIO.setup(z2d,GPIO.OUT)

GPIO.setup(y1e,GPIO.OUT)
GPIO.setup(y1s,GPIO.OUT)
GPIO.setup(y1d,GPIO.OUT)

GPIO.output(x1e,False)
GPIO.output(x2e,False)
GPIO.output(x3e,False)
GPIO.output(x4e,False)
GPIO.output(z1e,False)
GPIO.output(z2e,False)
GPIO.output(y1e,False)
#print "First calibrate by giving some +ve and -ve values....."
front=1
back=0
up=1
down=0
left=1
right=0
def xd(a):
    if a==1:
        GPIO.output(x1d, True)#front
        GPIO.output(x2d, True)#front
        GPIO.output(x3d, False)#front
        GPIO.output(x4d, False)#front
    elif a==0:
        GPIO.output(x1d, False)#back
        GPIO.output(x2d, False)#back
        GPIO.output(x3d, True)#back
        GPIO.output(x4d, True)#back
        
def yd(a):
    if a==1:
        GPIO.output(y1d, True)#front
    elif a==0:
        GPIO.output(y1d, False)#front
        
def zd(a):
    if a==1:
        GPIO.output(z1d, True)#up
        GPIO.output(z2d, True)#up
    elif a==0:
        GPIO.output(z1d, False)#down
        GPIO.output(z2d, False)#down

def x(a):
    for Index in range(0,a):
        GPIO.output(x1s,True)
        GPIO.output(x2s,True)
        GPIO.output(x3s,True)
        GPIO.output(x4s,True)
        time.sleep(0.00022)
        GPIO.output(x3s,False)
        GPIO.output(x4s,False)
        time.sleep(0.00022)
        GPIO.output(x3s,True)
        GPIO.output(x4s,True)
        time.sleep(0.00022)
        GPIO.output(x3s,False)
        GPIO.output(x4s,False)
        time.sleep(0.00022)
        GPIO.output(x1s,False)
        GPIO.output(x2s,False)
        GPIO.output(x3s,True)
        GPIO.output(x4s,True)
        time.sleep(0.00022)
        GPIO.output(x3s,False)
        GPIO.output(x4s,False)
        time.sleep(0.00022)
        GPIO.output(x3s,True)
        GPIO.output(x4s,True)
        time.sleep(0.00022)
        GPIO.output(x3s,False)
        GPIO.output(x4s,False)
        time.sleep(0.00022)
def x1(a):
    for Index in range(0,a):
        GPIO.output(x1s,True)
        time.sleep(0.00022)
        GPIO.output(x1s,False)
        time.sleep(0.00022)
def x2(a):
    for Index in range(0,a):
        GPIO.output(x2s,True)
        time.sleep(0.00022)
        GPIO.output(x2s,False)
        time.sleep(0.00022)
def x3(a):
    for Index in range(0,a):
        GPIO.output(x3s,True)
        time.sleep(0.00022)
        GPIO.output(x3s,False)
        time.sleep(0.00022)
def x4(a):
    for Index in range(0,a):
        GPIO.output(x4s,True)
        time.sleep(0.00022)
        GPIO.output(x4s,False)
        time.sleep(0.00022)
    
def z(a):
    for Index in range(0,a):
        GPIO.output(z1s,True)
        GPIO.output(z2s,True)
        time.sleep(0.00018)
        GPIO.output(z1s,False)
        GPIO.output(z2s,False)
        time.sleep(0.00018)

def y(a):
    for Index in range(0,a):
        GPIO.output(y1s,True)
        time.sleep(0.00018)
        GPIO.output(y1s,False)
        time.sleep(0.00018)
        
def z1(a):
    for Index in range(0,a):
        GPIO.output(z1s,True)
        time.sleep(0.00018)
        GPIO.output(z1s,False)
        time.sleep(0.00018)

def z2(a):
    for Index in range(0,a):
        GPIO.output(z2s,True)
        time.sleep(0.00018)
        GPIO.output(z2s,False)
        time.sleep(0.00018)
def y1(a):
    for Index in range(0,a):
        GPIO.output(y1s,True)
        time.sleep(0.00018)
        GPIO.output(y1s,False)
        time.sleep(0.00018)
    
def clog11():
    zd(up)
    z(22000)
    time.sleep(2)
    xd(front)
    x(9400)
    time.sleep(2)
    zd(down)
    z(3000)
    time.sleep(2)
    xd(back)
    x(9500)
    time.sleep(2)
    zd(down)
    z(19500)
        
def sandal11():
    zd(up)
    z(11000)
    yd(left)
    y(4000)
    xd(front)
    x(9000)
    zd(down)
    z(7000)
    xd(back)
    x(9000)
    yd(right)
    y(4000)
    zd(down)
    z(5000)
def running11():
    zd(up)
    z(3500)
    time.sleep(2)
    xd(front)
    x(9400)
    time.sleep(2)
    zd(down)
    z(4000)
    time.sleep(2)
    xd(back)
    x(9500)
def clog21():
    yd(left)
    y(16000)
    zd(up)
    z(22000)
    time.sleep(2)
    xd(front)
    x(9400)
    time.sleep(2)
    zd(down)
    z(3000)
    time.sleep(2)
    xd(back)
    x(9500)
    time.sleep(2)
    zd(down)
    z(19500)
    yd(right)
    y(18000)
def sandal21():
    yd(left)
    y(16000)
    zd(up)
    z(11600)
    time.sleep(2)
    xd(front)
    x(9400)
    time.sleep(2)
    zd(down)
    z(3000)
    time.sleep(2)
    xd(back)
    x(9500)
    time.sleep(2)
    zd(down)
    z(9100)
    yd(right)
    y(18000)
def running21():
    yd(left)
    y(16000)
    zd(up)
    z(3500)
    time.sleep(2)
    xd(front)
    x(9400)
    time.sleep(2)
    zd(down)
    z(4000)
    time.sleep(2)
    xd(back)
    x(9500)
    time.sleep(2)
    yd(right)
    y(16000)


    
def clog12():
    zd(up)
    z(13000)
    yd(right)
    y(8000)
    xd(front)
    x(9000)
    zd(up)
    z(6000)
    xd(back)
    x(9000)
    yd(left)
    y(8000)
    zd(down)
    z(19000)
        
def sandal12():
    zd(up)
    z(6000)
    yd(left)
    y(4000)
    xd(front)
    x(9000)
    zd(up)
    z(6000)
    xd(back)
    x(9000)
    yd(right)
    y(4000)
    zd(down)
    z(13000)  
def running12():
    xd(front)
    x(9400)
    time.sleep(2)
    zd(up)
    z(3500)
    time.sleep(2)
    xd(back)
    x(9500)
    time.sleep(2)
    zd(down)
    z(4000)
def clog22():
    zd(up)
    z(13000)
    yd(right)
    y(8000)
    xd(front)
    x(9000)
    zd(up)
    z(6000)
    xd(back)
    x(9000)
    yd(left)
    y(8000)
    zd(down)
    z(19000)
def sandal22():
    yd(left)
    y(16000)
    zd(up)
    z(11600)
    time.sleep(2)
    xd(front)
    x(9400)
    time.sleep(2)
    zd(up)
    z(3000)
    time.sleep(2)
    xd(back)
    x(9500)
    time.sleep(2)
    zd(down)
    z(15100)
    yd(right)
    y(16000)
def running22():
    yd(left)
    y(16000)
    time.sleep(2)
    xd(front)
    x(9400)
    time.sleep(2)
    zd(up)
    z(3500)
    time.sleep(2)
    xd(back)
    x(9500)
    time.sleep(2)
    zd(down)
    z(4000)
    yd(right)
    y(16000)


#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('/home/pi/shoe-427b3-firebase-adminsdk-38ew3-2c9b8d59a2.json')
firebase_admin.initialize_app(cred,{'storageBucket' : 'shoe-427b3.appspot.com','databaseURL' : "https://shoe-427b3-default-rtdb.firebaseio.com/"})
bucket = storage.bucket()
dir = db.reference()
cap = cv2.VideoCapture(0) #카메라 열기
if not cap.isOpened():
   print('camera open failed')
   sys.exit()
# Load network
net = cv2.dnn.readNet('/home/pi/bvlc_googlenet.caffemodel', '/home/pi/deploy.prototxt') #비교해줄 데이터(네트워크)를 불러옴
sandal=[0,0]
clog=[0,0]
running=[0,0]
while True:
   if(db.reference('모터').get()=="clog1"):
       #모터작동
       clog[0]=0
       print("크록스1을 꺼냅니다.")
       dir.update({'모터':'motor'})
       
       blob = bucket.blob("image/clog1.jpg")

               
       new_token = uuid4()
       metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
       blob.metadata = metadata
               #upload file
       blob.upload_from_filename(filename='/home/pi/images/black.jpg', content_type='image/jpeg')
       clog12()
       dir.update({'신발':'clog1'})  
       time.sleep(10)
   elif(db.reference('모터').get()=="clog2"):
       clog[1]=0
       print("크록스2을 꺼냅니다.")
       dir.update({'모터':'motor'})        
       blob = bucket.blob("image/clog2.jpg")
               
               
       new_token = uuid4()
       metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
       blob.metadata = metadata
               #upload file
       blob.upload_from_filename(filename='/home/pi/images/black.jpg', content_type='image/jpeg')
       clog22()
       dir.update({'신발':'clog2'})        
       time.sleep(10)
   elif(db.reference('모터').get()=="sandal1"):
       sandal[0]=0
       print("샌달1를 꺼냅니다.")
       dir.update({'모터':'motor'})        
       blob = bucket.blob("image/sandal1.jpg")
               
               
       new_token = uuid4()
       metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
       blob.metadata = metadata
               #upload file
       blob.upload_from_filename(filename='/home/pi/images/black.jpg', content_type='image/jpeg')
       sandal12()
       dir.update({'신발':'sandal1'})        
       time.sleep(10)
   elif(db.reference('모터').get()=="sandal2"):
       sandal[1]=0
       print("샌달2를 꺼냅니다.")
       dir.update({'모터':'motor'})        
       blob = bucket.blob("image/sandal2.jpg")
               
               
       new_token = uuid4()
       metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
       blob.metadata = metadata
               #upload file
       blob.upload_from_filename(filename='/home/pi/images/black.jpg', content_type='image/jpeg')
       sandal22()
       dir.update({'신발':'sandal2'})
       time.sleep(10)
   elif(db.reference('모터').get()=="running1"):
       running[0]=0
       print("운동화1을 꺼냅니다.")
       dir.update({'모터':'motor'})        
       blob = bucket.blob("image/running1.jpg")
               
               
       new_token = uuid4()
       metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
       blob.metadata = metadata
               #upload file
       blob.upload_from_filename(filename='/home/pi/images/black.jpg', content_type='image/jpeg')
       running12()       
       dir.update({'신발':'running1'})        
       time.sleep(10)
   elif(db.reference('모터').get()=="running2"):
       running[1]=0
       print("운동화2를 꺼냅니다.")
       dir.update({'모터':'motor'})        
       blob = bucket.blob("image/running2.jpg")
               
               
       new_token = uuid4()
       metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
       blob.metadata = metadata
               #upload file
       blob.upload_from_filename(filename='/home/pi/images/black.jpg', content_type='image/jpeg')
       running22()       
       dir.update({'신발':'running2'})        
       time.sleep(10)
   ret, img = cap.read() #프레임하나를 변수에 저장함
   inputBlob = cv2.dnn.blobFromImage(img, 1, (224, 224), (104, 117, 123)) #사진을 네트워크에 맞는 형식으로 바꿈
   net.setInput(inputBlob) #네트워크에 사진을 넣음
   prob = net.forward() # 1행 1000열의 데이터 행렬
   out = prob.flatten() #행렬 1차원으로 펴기
   classId = np.argmax(out) #비교 했을때 값이 가장 큰 인덱스(배열번호)
   confidence = out[classId] #변수값에 배열값(일치확률) 넣음
   
   if not ret:
       break
   
   print(classId)
   print(confidence*100)
   cv2.imshow('img', img)
   if cv2.waitKey(200) == 27:
       break
   elif classId == 774:
       #샌달층 빈칸 쪽으로 모터작동
       if (confidence*100>10):
           if sandal[0]==0:
               print('샌달')
               cv2.imwrite('/home/pi/images/sandal1.jpg',img)
               blob = bucket.blob("image/sandal1.jpg")
               
               
               new_token = uuid4()
               metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
               blob.metadata = metadata
               #upload file
               blob.upload_from_filename(filename='/home/pi/images/sandal1.jpg', content_type='image/jpeg')
               sandal11()
               dir.update({'신발':'sandal1'})
               sandal[0]=1
           elif sandal[1] ==0:
               
               cv2.imwrite('/home/pi/images/sandal2.jpg',img)
               blob = bucket.blob("image/sandal2.jpg")
               
               new_token = uuid4()
               metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
               blob.metadata = metadata
               #upload file
               blob.upload_from_filename(filename='/home/pi/images/sandal2.jpg', content_type='image/jpeg')
               sandal21()
               dir.update({'신발':'sandal2'})
               sandal[1]=1
           else:
              print("신발장이 꽉찼습니다.")    
           print('샌달')
           time.sleep(10)
       else:
           pass
   elif classId == 770:
       if (confidence*100>70):
           if running[0]==0:
               print('운동화')
               
               cv2.imwrite('/home/pi/images/running1.jpg',img)
               blob = bucket.blob("image/running1.jpg")
               
               
               new_token = uuid4()
               metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
               blob.metadata = metadata
               #upload file
               blob.upload_from_filename(filename='/home/pi/images/running1.jpg', content_type='image/jpeg')
               running11()
               dir.update({'신발':'running1'})
               running[0]=1
           elif (running[1]==0):
               
               cv2.imwrite('/home/pi/images/running2.jpg',img)
               blob = bucket.blob("image/running2.jpg")
               
               new_token = uuid4()
               metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
               blob.metadata = metadata
               #upload file
               blob.upload_from_filename(filename='/home/pi/images/running2.jpg', content_type='image/jpeg')
               running21()
               dir.update({'신발':'running2'})
               running[1]=1
           else:
              print("신발장이 꽉찼습니다.")  
           print('운동화')
           time.sleep(10)
       else:
           pass
   elif classId == 502:
       #크록스층 빈칸 쪽으로 모터작동
       if (confidence*100>50):
           if clog[0] ==0:
               print('크록스')
               
               cv2.imwrite('/home/pi/images/clog1.jpg',img)
               blob = bucket.blob("image/clog1.jpg")
               
               
               new_token = uuid4()
               metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
               blob.metadata = metadata
               #upload file
               blob.upload_from_filename(filename='/home/pi/images/clog1.jpg', content_type='image/jpeg')
               dir.update({'신발':'clog1'})
               clog[0] = 1
           elif clog[1] ==0:
               
               cv2.imwrite('/home/pi/images/clog2.jpg',img)
               blob = bucket.blob("image/clog2.jpg")
               
               new_token = uuid4()
               metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
               blob.metadata = metadata
               #upload file
               blob.upload_from_filename(filename='/home/pi/images/clog2.jpg', content_type='image/jpeg')
               clog21
               dir.update({'신발':'clog2'})
               clog[1] = 1
           else:
               print("신발장이 꽉 찼습니다.")
           print('크록스')
           time.sleep(10)
       else:
           pass    
cap.release()
cv2.destroyAllWindows()
