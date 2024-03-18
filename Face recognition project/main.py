from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        
        # first image
        img=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\Top.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\top1.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\top3.jpg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img3=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\bg.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman", 35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\student.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b2=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b2.place(x=200,y=300,width=220,height=40)


         #detect face button
        img5=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\face.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b2=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=300,width=220,height=40)


          #Attendance face button
        img6=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\attendance.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b2=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b2.place(x=800,y=300,width=220,height=40)


          #Help desk button
        img7=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\help.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b2=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1100,y=300,width=220,height=40)


          #train face button
        img8=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\train_data.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b2=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b2.place(x=200,y=600,width=220,height=40)


          #Photos button
        img9=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\photo.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b2=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=600,width=220,height=40)


          #Developer button
        img10=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\developer.jpg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b2=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b2.place(x=800,y=600,width=220,height=40)


          #Exit
        img11=Image.open(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\College_images\exit.jpg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b2=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1100,y=600,width=220,height=40)











if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()