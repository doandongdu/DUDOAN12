from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import numpy as np
from keras.utils import img_to_array,load_img
from keras.models import load_model

top = Tk()
top.geometry('600x500+10+10')
top.title('Potato Pathology')

def image():
    global img
    filename = fd.askopenfilename(initialdir="/images",title='Choose image',filetypes=file_type)
    url['text'] = filename
    img = Image.open(filename)
    img = img.resize((200,200))
    img = ImageTk.PhotoImage(img)
    show_image['image'] = img

def predict():
    label = ['bệnh bạc lá','khỏe mạnh','bệnh sương mai']
    model = load_model('potato.h5')
    img= load_img(url.cget('text'),target_size=(200,200))
    img=img_to_array(img)
    img=img.astype('float32')
    img=img.reshape(1,200,200,3)
    img=img/255
    a= int(np.argmax(model.predict(img),axis=1))
    show_predict['text'] = label[a]


file_type = [('Tất cả file','.*'),('Ảnh','.png')]
title = Label(top,text='Nhận diện sâu bệnh',font=("time new roman",25),width=30)
title.grid(row=0,column=0)
url = Label(top,font=("time new roman",10),width=30)
url.grid(row=2,column=0)
button1 = Button(top,text='Tải ảnh lên',font=("time new roman",15),width=20,command=image)
button1.grid(row=3,column=0)
button2 = Button(top,text='Đoán',font=("time new roman",15),command=predict)
button2.grid(row=4,column=0)
show_image = Label(top)
show_image.grid(row=5,column=0)
show_predict = Label(top,font=("time new roman",15),text='',width=15)
show_predict.grid(row=6,column=0)

top.mainloop()
