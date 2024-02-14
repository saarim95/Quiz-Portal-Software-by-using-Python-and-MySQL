import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
t=tkinter.Tk()
t.geometry("1270x1080+0+0")
t.title("Quiz Portal")

def Admin():
     b=Toplevel(t)
     b.geometry("1270x1080+0+0")
     b.title("Admin Side")
     
     def Login():
         name=y1.get()
         pwd=x1.get()
         
         if name=="root" and pwd=="root":
            a=Toplevel(b)
            a.geometry("1270x1080+0+0")
            a.title("Admin Login")
            
            def Ques_inf():
                c=Toplevel(a)
                c.geometry("1270x1080+0+0")
                c.title("Questions Information")
                
                def Insert_Question():
                    m=Toplevel(a)
                    m.geometry("1270x1080+0+0")
                    m.title("Insert_Question")
                    
                    def one():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                        cur=db.cursor()
                        m22=str(m4.get())
                        m23=int(m6.get())
                        m24=str(m8.get())
                        m25=str(m10.get())
                        m26=str(m12.get())
                        m27=str(m14.get())
                        m28=str(m16.get())
                        m29=str(m18.get())
                        sql="insert into questions values('%s','%d','%s','%s','%s','%s','%s','%s')"%(m22,m23,m24,m25,m26,m27,m28,m29)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Saved')
                 
                    def one_close():
                        m.destroy()
                 
                    def one_clear():
                        m4.delete(0,100)
                        m6.delete(0,100)
                        m8.delete(0,100)
                        m10.delete(0,100)
                        m12.delete(0,100)
                        m14.delete(0,100)
                        m16.delete(0,100)
                        m18.delete(0,100)
                    
                    m22=Canvas(m,width=2970,height=2080,bg='light blue')
                    m22.place(x=0,y=0)
                    m2=Label(m,text="Insert Questions",bg='yellow',fg='Blue',width=300,height=2,font=('Aeries',30))
                    m2.pack()
             
                    m3=Label(m,text="Subject_Id",font=10)
                    m3.place(x=450,y=120)
                    
                    lt=['C01','C02','M01','P01']
                    m4=ttk.Combobox(m)
                    m4['values']=lt
                    m4.place(x=600,y=120)
                    
             
                    m5=Label(m,text="Ques_no",font=10)
                    m5.place(x=450,y=170)
                    m6=Entry(m,width=30)
                    m6.place(x=600,y=170)
             
                    m7=Label(m,text="Ques_name",font=10)
                    m7.place(x=450,y=220)
                    m8=Entry(m,width=90)
                    m8.place(x=600,y=220)
             
                    m9=Label(m,text="Option_1",font=10)
                    m9.place(x=450,y=270)
                    m10=Entry(m,width=50)
                    m10.place(x=600,y=270)
             
                    m11=Label(m,text="Option_2",font=10)
                    m11.place(x=450,y=320)
                    m12=Entry(m,width=50)
                    m12.place(x=600,y=320)
                
                    m13=Label(m,text="Option_3",font=10)
                    m13.place(x=450,y=370)
                    m14=Entry(m,width=50)
                    m14.place(x=600,y=370)
                
                    m15=Label(m,text="Option_4",font=10)
                    m15.place(x=450,y=420)
                    m16=Entry(m,width=50)
                    m16.place(x=600,y=420)
                    
                    m17=Label(m,text="Answers",font=10)
                    m17.place(x=450,y=470)
                    m18=Entry(m,width=50)
                    m18.place(x=600,y=470)
             
                    m19=Button(m,text="Insert",width=10,font=10,bg="blue",fg="white",command=one)
                    m19.place(x=450,y=520)
             
                    m20=Button(m,text="Clear",width=10,font=10,bg="blue",fg="white",command=one_clear)
                    m20.place(x=670,y=520)
             
                    m21=Button(m,text="Back",width=10,font=10,bg="red",fg="black",command=one_close)
                    m21.place(x=560,y=570)
                    
                    m.mainloop()
                    
                def Update_Questions():
                    n=Toplevel(a)
                    n.geometry("1270x1080+0+0")
                    n.title("Insert_Question")
                    
                    def two():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                        cur=db.cursor()
                        n22=str(n4.get())
                        n23=int(n6.get())
                        n24=str(n8.get())
                        n25=str(n10.get())
                        n26=str(n12.get())
                        n27=str(n14.get())
                        n28=str(n16.get())
                        n29=str(n18.get())
                        sql=("update questions set Ques_name='%s',Opt_1='%s',Opt_2='%s',Opt_3='%s',Opt_4='%s',Answers='%s' where sub_id='%s' and Ques_no='%d'")%(n24,n25,n26,n27,n28,n29,n22,n23)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Updated')
                        
                    def find_2():
                         db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                         cur=db.cursor()
                         x=str(n4.get())
                         y=int(n6.get())
                         sql="select Ques_name,Opt_1,Opt_2,Opt_3,Opt_4,Answers from questions where sub_id='%s' and Ques_no='%d'"%(x,y)
                         cur.execute(sql)
                         data=cur.fetchall()
                         if len(data)==0:
                             messagebox.showinfo('STATUS',"No records found")
                         else:
                             for res in data:
                                 n8.insert(0,str(res[0]))
                                 n10.insert(0,str(res[1]))
                                 n12.insert(0,str(res[2]))
                                 n14.insert(0,str(res[3]))
                                 n16.insert(0,str(res[4]))
                                 n18.insert(0,str(res[5]))
                         db.close()
                 
                    def two_close():
                        n.destroy()
                 
                    def two_clear():
                        n4.delete(0,100)
                        n6.delete(0,100)
                        n8.delete(0,100)
                        n10.delete(0,100)
                        n12.delete(0,100)
                        n14.delete(0,100)
                        n16.delete(0,100)
                        n18.delete(0,100)
                        
                    n22=Canvas(n,width=2270,height=2080,bg='light blue')
                    n22.place(x=0,y=0)
                 
                    n2=Label(n,text="Update Questions",bg='yellow',fg='Blue',width=300,height=2,font=('Aeries',30))
                    n2.pack()
             
                    n3=Label(n,text="Subject_Id",font=10)
                    n3.place(x=450,y=120)
                    lt=['C01','C02','M01','P01']
                    n4=ttk.Combobox(n)
                    n4['values']=lt
                    n4.place(x=600,y=120)
             
                    n5=Label(n,text="Ques_no",font=10)
                    n5.place(x=450,y=170)
                    n6=Entry(n,width=30)
                    n6.place(x=600,y=170)
                    
                    n7=Label(n,text="Ques_name",font=10)
                    n7.place(x=450,y=220)
                    n8=Entry(n,width=90)
                    n8.place(x=600,y=220)
             
                    n9=Label(n,text="Option_1",font=10)
                    n9.place(x=450,y=270)
                    n10=Entry(n,width=50)
                    n10.place(x=600,y=270)
             
                    n11=Label(n,text="Option_2",font=10)
                    n11.place(x=450,y=320)
                    n12=Entry(n,width=50)
                    n12.place(x=600,y=320)
                
                    n13=Label(n,text="Option_3",font=10)
                    n13.place(x=450,y=370)
                    n14=Entry(n,width=50)
                    n14.place(x=600,y=370)
                
                    n15=Label(n,text="Option_4",font=10)
                    n15.place(x=450,y=420)
                    n16=Entry(n,width=50)
                    n16.place(x=600,y=420)
                
                    n17=Label(n,text="Answers",font=10)
                    n17.place(x=450,y=470)
                    n18=Entry(n,width=50)
                    n18.place(x=600,y=470)
             
                    n19=Button(n,text="Update",width=10,font=10,bg="blue",fg="white",command=two)
                    n19.place(x=450,y=520)
             
                    n20=Button(n,text="Clear",width=10,font=10,bg="blue",fg="white",command=two_clear)
                    n20.place(x=670,y=520)
             
                    n21=Button(n,text="Back",width=10,font=10,bg="red",fg="black",command=two_close)
                    n21.place(x=560,y=570)
                    
                    n30=Button(n,text="Find",width=10,font=10,bg="blue",fg="white",command=find_2)
                    n30.place(x=850,y=150)
                
                    n.mainloop()
                    
                def Delete_Questions():
                    k=Toplevel(a)
                    k.geometry("1270x1080+0+0")
                    k.title("Delete Questions")
                
                    def three():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                        cur=db.cursor()
                        k10=str(k4.get())
                        k11=int(k6.get())
                        sql="delete from questions where sub_id='%s'and Ques_no='%d'"%(k10,k11)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo("STATUS",'DELETED')
                
                    def three_clear():
                        k4.delete(0,100)
                        k6.delete(0,100)
                        
                    def three_close():
                        k.destroy()
                        
                    k10=Canvas(k,width=2270,height=2080,bg='light blue')
                    k10.place(x=0,y=0)
                    
                    k2=Label(k,text="Delete Questions",bg='yellow',fg='Blue',width=300,height=2,font=('Aeries',30))
                    k2.pack()
             
                    k3=Label(k,text="Subject_Id",font=10)
                    k3.place(x=450,y=200)
                    lt=['C01','C02','M01','P01']
                    k4=ttk.Combobox(k)
                    k4['values']=lt
                    k4.place(x=600,y=200)
             
                    k5=Label(k,text="Ques_no",font=10)
                    k5.place(x=450,y=250)
                    k6=Entry(k,width=30)
                    k6.place(x=600,y=250)
                
                    k7=Button(k,text="Delete",width=10,font=10,bg="blue",fg="white",command=three)
                    k7.place(x=450,y=350)
                    
                    k8=Button(k,text="Clear",width=10,font=10,bg="blue",fg="white",command=three_clear)
                    k8.place(x=670,y=350)
             
                    k9=Button(k,text="Back",width=10,font=10,bg="red",fg="black",command=three_close)
                    k9.place(x=560,y=400)
                
                    k.mainloop()
                    
                def Find_Questions():
                    l=Toplevel(a)
                    l.geometry("1270x1080+0+0")
                    l.title("find Questions")
                    
                    def find_1():
                         db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                         cur=db.cursor()
                         x=str(l4.get())
                         y=int(l6.get())
                         sql="select Ques_name,Opt_1,Opt_2,Opt_3,Opt_4,Answers from questions where sub_id='%s' and Ques_no='%d'"%(x,y)
                         cur.execute(sql)
                         data=cur.fetchall()
                         if len(data)==0:
                             messagebox.showinfo('STATUS',"No records found")
                         else:
                             for res in data:
                                 l8.insert(0,str(res[0]))
                                 l10.insert(0,str(res[1]))
                                 l12.insert(0,str(res[2]))
                                 l14.insert(0,str(res[3]))
                                 l16.insert(0,str(res[4]))
                                 l18.insert(0,str(res[5]))
                         db.close()
                         
                    def two_clearr():
                        l4.delete(0,100)
                        l6.delete(0,100)
                        l8.delete(0,100)
                        l10.delete(0,100)
                        l12.delete(0,100)
                        l14.delete(0,100)
                        l16.delete(0,100)
                        l18.delete(0,100)
                         
                    def close_l():
                        l.destroy()
                        
                        
                    l22=Canvas(l,width=2270,height=2080,bg='light blue')
                    l22.place(x=0,y=0)
                 
                    l2=Label(l,text="Find Questions",bg='yellow',fg='Blue',width=300,height=2,font=('Aeries',30))
                    l2.pack()
             
                    l3=Label(l,text="Subject_Id",font=10)
                    l3.place(x=450,y=120)
                    lt=['C01','C02','M01','P01']
                    l4=ttk.Combobox(l)
                    l4['values']=lt
                    l4.place(x=600,y=120)
             
                    l5=Label(l,text="Ques_no",font=10)
                    l5.place(x=450,y=170)
                    l6=Entry(l,width=30)
                    l6.place(x=600,y=170)
                    
                    l7=Label(l,text="Ques_name",font=10)
                    l7.place(x=450,y=220)
                    l8=Entry(l,width=90)
                    l8.place(x=600,y=220)
             
                    l9=Label(l,text="Option_1",font=10)
                    l9.place(x=450,y=270)
                    l10=Entry(l,width=50)
                    l10.place(x=600,y=270)
             
                    l11=Label(l,text="Option_2",font=10)
                    l11.place(x=450,y=320)
                    l12=Entry(l,width=50)
                    l12.place(x=600,y=320)
                
                    l13=Label(l,text="Option_3",font=10)
                    l13.place(x=450,y=370)
                    l14=Entry(l,width=50)
                    l14.place(x=600,y=370)
                
                    l15=Label(l,text="Option_4",font=10)
                    l15.place(x=450,y=420)
                    l16=Entry(l,width=50)
                    l16.place(x=600,y=420)
                
                    l17=Label(l,text="Answers",font=10)
                    l17.place(x=450,y=470)
                    l18=Entry(l,width=50)
                    l18.place(x=600,y=470)
             
                    l19=Button(l,text="Find",width=10,font=10,bg="blue",fg="white",command=find_1)
                    l19.place(x=450,y=520)
             
                    l20=Button(l,text="Clear",width=10,font=10,bg="blue",fg="white",command= two_clearr)
                    l20.place(x=670,y=520)
             
                    l21=Button(l,text="Back",width=10,font=10,bg="red",fg="black",command=close_l)
                    l21.place(x=560,y=570)
                
                    l.mainloop()
                    
                def back_1():
                    c.destroy()
                
                c1=Canvas(c,width=200,height=1080,bg='blue')
                c1.place(x=0,y=0)
         
                c3=Button(c1,text="Insert Question",width=15,font=10,bg='light green',fg='black',command=Insert_Question)
                c3.place(x=10,y=20)
         
                c4=Button(c1,text="Update Question",width=15,font=10,bg='light green',fg='black',command=Update_Questions)
                c4.place(x=10,y=120)
         
                c5=Button(c1,text="Find Question",width=15,font=10,bg='light green',fg='black',command=Find_Questions)
                c5.place(x=10,y=220)
                
                c6=Button(c1,text="Delete Question",width=15,font=10,bg='light green',fg='black',command= Delete_Questions)
                c6.place(x=10,y=320)
         
                c7=Button(c1,text="Back",width=15,font=10,bg='light green',fg='black',command=back_1)
                c7.place(x=10,y=420)
         
                c2=Canvas(c,width=2270,height=2080,bg='light blue')
                c2.place(x=200,y=0)
         
                c8=Label(c2,text="Questions Information",bg='yellow',fg='blue',width=50,height=3,font=('Aeries',30))
                c8.place(x=0,y=0)
                
                c.mainloop()
                
            def User_info():
                e=Toplevel(a)
                e.geometry("1270x1080+0+0")
                e.title("User Information")
                
                def Insert_details():
                    j=Toplevel(e)
                    j.geometry("1270x1080+0+0")
                    j.title("Insert Details")
                    
                    def one():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                        cur=db.cursor()
                        j16=str(j4.get())
                        j17=str(j6.get())
                        j18=str(j8.get())
                        j19=str(j10.get())
                        j20=str(j12.get())
                        sql="insert into userinformation values('%s','%s','%s','%s','%s')"%(j16,j17,j18,j19,j20)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Saved')
                 
                    def one_close():
                        j.destroy()
                 
                    def one_clear():
                        j4.delete(0,100)
                        j6.delete(0,100)
                        j8.delete(0,100)
                        j10.delete(0,100)
                        j12.delete(0,100)
                        
                    c11=Canvas(j,width=2270,height=2080,bg='light blue')
                    c11.place(x=0,y=0)
                 
                    j2=Label(j,text="Insertion",bg='yellow',fg='Blue',width=300,height=3,font=('Aeries',30))
                    j2.pack()
             
                    j3=Label(j,text="User_Id",font=10)
                    j3.place(x=450,y=180)
                    j4=Entry(j,width=30)
                    j4.place(x=600,y=180)
             
                    j5=Label(j,text="User_Name",font=10)
                    j5.place(x=450,y=230)
                    j6=Entry(j,width=30)
                    j6.place(x=600,y=230)
             
                    j7=Label(j,text="E_Mail",font=10)
                    j7.place(x=450,y=280)
                    j8=Entry(j,width=30)
                    j8.place(x=600,y=280)
             
                    j9=Label(j,text="City",font=10)
                    j9.place(x=450,y=330)
                    j10=Entry(j,width=30)
                    j10.place(x=600,y=330)
             
                    j11=Label(j,text="Password",font=10)
                    j11.place(x=450,y=380)
                    j12=Entry(j,width=30)
                    j12.place(x=600,y=380)
             
                    j13=Button(j,text="Insert",width=10,font=10,bg="blue",fg="white",command=one)
                    j13.place(x=450,y=430)
             
                    j14=Button(j,text="Clear",width=10,font=10,bg="blue",fg="white",command=one_clear)
                    j14.place(x=670,y=430)
             
                    j15=Button(j,text="Back",width=10,font=10,bg="red",fg="black",command=one_close)
                    j15.place(x=560,y=500)
             
                    j.mainloop()
                    
                def Update_details():
                    k=Toplevel(e)
                    k.geometry("1270x1080+0+0")
                    k.title("Update Details")
                    
                    def two():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                        cur=db.cursor()
                        k16=str(k4.get())
                        k17=str(k6.get())
                        k18=str(k8.get())
                        k19=str(k10.get())
                        k20=str(k12.get())
                        sql=("update userinformation set User_Name='%s',E_Mail='%s',City='%s',Password='%s' where User_Id='%s'")%(k17,k18,k19,k20,k16)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Updated')
                        
                    def three_1():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                        cur=db.cursor()
                        x=k4.get()
                        sql="select User_Name,E_Mail,City,Password from userinformation where User_Id='%s'"%(x)
                        cur.execute(sql)
                        data=cur.fetchall()
                        if len(data)==0:
                            messagebox.showinfo('STATUS',"No records found")
                        else:
                            for res in data:
                                k6.insert(0,str(res[0]))
                                k8.insert(0,str(res[1]))
                                k10.insert(0,str(res[2]))
                                k12.insert(0,str(res[3]))
                        db.close()
                 
                    def two_clear():
                        k4.delete(0,100)
                        k6.delete(0,100)
                        k8.delete(0,100)
                        k10.delete(0,100)
                        k12.delete(0,100)
                 
                    def two_close():
                        k.destroy()
                        
                    c22=Canvas(k,width=2270,height=2080,bg='light blue')
                    c22.place(x=0,y=0)
                 
                    k2=Label(k,text="Modification",bg='yellow',fg='Blue',width=300,height=3,font=('Aeries',30))
                    k2.pack()
             
                    k3=Label(k,text="User_Id",font=10)
                    k3.place(x=450,y=180)
                    k4=Entry(k,width=30)
                    k4.place(x=600,y=180)
             
                    k5=Label(k,text="User_Name",font=10)
                    k5.place(x=450,y=230)
                    k6=Entry(k,width=30)
                    k6.place(x=600,y=230)
             
                    k7=Label(k,text="E_Mail",font=10)
                    k7.place(x=450,y=280)
                    k8=Entry(k,width=30)
                    k8.place(x=600,y=280)
             
                    k9=Label(k,text="City",font=10)
                    k9.place(x=450,y=330)
                    k10=Entry(k,width=30)
                    k10.place(x=600,y=330)
             
                    k11=Label(k,text="Password",font=10)
                    k11.place(x=450,y=380)
                    k12=Entry(k,width=30)
                    k12.place(x=600,y=380)
             
                    k13=Button(k,text="Update",width=10,font=10,bg="blue",fg="white",command=two)
                    k13.place(x=450,y=430)
             
                    k14=Button(k,text="Clear",width=10,font=10,bg="blue",fg="white",command=two_clear)
                    k14.place(x=670,y=430)
             
                    k15=Button(k,text="Back",width=10,font=10,bg="red",fg="black",command=two_close)
                    k15.place(x=560,y=500)
                    
                    k20=Button(k,text="Find",width=10,font=10,bg="blue",fg="white",command=three_1)
                    k20.place(x=850,y=170)
             
                    k.mainloop()
                    
                def Find_details():
                    o=Toplevel(e)
                    o.geometry("1270x1080+0+0")
                    o.title("Find Details")
                    
                    def three():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                        cur=db.cursor()
                        x=o4.get()
                        sql="select User_Name,E_Mail,City,Password from userinformation where User_Id='%s'"%(x)
                        cur.execute(sql)
                        data=cur.fetchall()
                        if len(data)==0:
                            messagebox.showinfo('STATUS',"No records found")
                        else:
                            for res in data:
                                o6.insert(0,str(res[0]))
                                o8.insert(0,str(res[1]))
                                o10.insert(0,str(res[2]))
                                o12.insert(0,str(res[3]))
                        db.close()
                 
                    def three_close():
                        o.destroy()
                 
                    def three_clear():
                        o4.delete(0,100)
                        o6.delete(0,100)
                        o8.delete(0,100)
                        o10.delete(0,100)
                        o12.delete(0,100)
                         
                    c33=Canvas(o,width=2270,height=2080,bg='light blue')
                    c33.place(x=0,y=0)
             
                    o2=Label(o,text="Find Data",bg='yellow',fg='Blue',width=300,height=3,font=('Aeries',30))
                    o2.pack()
             
                    o3=Label(o,text="User_Id",font=10)
                    o3.place(x=450,y=180)
                    o4=Entry(o,width=30)
                    o4.place(x=600,y=180)
             
                    o5=Label(o,text="User_Name",font=10)
                    o5.place(x=450,y=230)
                    o6=Entry(o,width=30)
                    o6.place(x=600,y=230)
             
                    o7=Label(o,text="E_Mail",font=10)
                    o7.place(x=450,y=280)
                    o8=Entry(o,width=30)
                    o8.place(x=600,y=280)
             
                    o9=Label(o,text="City",font=10)
                    o9.place(x=450,y=330)
                    o10=Entry(o,width=30)
                    o10.place(x=600,y=330)
             
                    o11=Label(o,text="Password",font=10)
                    o11.place(x=450,y=380)
                    o12=Entry(o,width=30)
                    o12.place(x=600,y=380)
             
                    o13=Button(o,text="Find",width=10,font=10,bg="blue",fg="white",command=three)
                    o13.place(x=450,y=430)
             
                    o14=Button(o,text="Clear",width=10,font=10,bg="blue",fg="white",command=three_clear)
                    o14.place(x=670,y=430)
             
                    o15=Button(o,text="Back",width=10,font=10,bg="red",fg="black",command=three_close)
                    o15.place(x=560,y=500)
             
                    o.mainloop()
                    
                def delete_data():
                    q=Toplevel(e)
                    q.geometry("1270x1080+0+0")
                    q.title("Delete Details")
                    
                    def four():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                        cur=db.cursor()
                        q8=str(h4.get())
                        sql="delete from userinformation where User_Id='%s'"%(q8)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo("STATUS",'DELETED')
                
                    def four_clear():
                        q4.delete(0,100)
                 
                    def four_close():
                        q.destroy()
                 
                    c334=Canvas(q,width=2270,height=2080,bg='light blue')
                    c334.place(x=0,y=0)
              
                    q2=Label(q,text="Deletion",bg='yellow',fg='Blue',width=300,height=3,font=('Aeries',30))
                    q2.pack()
             
                    q3=Label(q,text="User_Id",font=10)
                    q3.place(x=450,y=280)
                    q4=Entry(q,width=30)
                    q4.place(x=600,y=280)
             
                    q5=Button(q,text="Delete",width=10,font=10,bg="blue",fg="white",command=four)
                    q5.place(x=450,y=430)
             
                    q6=Button(q,text="Clear",width=10,font=10,bg="blue",fg="white",command=four_clear)
                    q6.place(x=670,y=430)
             
                    q7=Button(q,text="Back",width=10,font=10,bg="red",fg="black",command=four_close)
                    q7.place(x=560,y=500)
                    
                    q.mainloop()
                    
                def ch_close_1():
                    e.destroy()
                    
             
                e1=Canvas(e,width=200,height=1080,bg='blue')
                e1.place(x=0,y=0)
         
                e3=Button(e1,text="Insert Details",width=15,font=10,bg='light green',fg='black',command=Insert_details)
                e3.place(x=10,y=20)
         
                e4=Button(e1,text="Update Details",width=15,font=10,bg='light green',fg='black',command=Update_details)
                e4.place(x=10,y=120)
         
                e5=Button(e1,text="Find Details",width=15,font=10,bg='light green',fg='black',command=Find_details)
                e5.place(x=10,y=220)
                
                e6=Button(e1,text="Delete Details",width=15,font=10,bg='light green',fg='black',command=delete_data)
                e6.place(x=10,y=320)
         
                e7=Button(e1,text="Back",width=15,font=10,bg='light green',fg='black',command=ch_close_1)
                e7.place(x=10,y=420)
         
                e2=Canvas(e,width=1070,height=1080,bg='light blue')
                e2.place(x=200,y=0)
         
                e8=Label(e2,text="User Information",bg='yellow',fg='blue',width=50,height=3,font=('Aeries',30))
                e8.place(x=0,y=0)
                
                e.mainloop()
                
            
            def close_a():
                a.destroy()
            
            c2=Canvas(a,width=2270,height=2080,bg='light blue')
            c2.place(x=0,y=0)

            welcome=Label(a,text="Welcome to Admin Side",bg='yellow',fg='Blue',width=300,height=3,font=('Aeries',30))
            welcome.pack()

            admin=Button(a,text="User Information",width=15,font=15,bg="Blue",fg="white",command=User_info)
            admin.place(x=480,y=350)

            user=Button(a,text="Questions",width=15,font=15,bg="Blue",fg="white",command=Ques_inf)
            user.place(x=660,y=350)

            create_exp=Label(a,text='select any one of them.',bg="light blue",font=('Aeries',16))
            create_exp.place(x=510,y=410)

            close_a=Button(a,text='Back',width=10,font=10,bg='red',fg='black',command=close_a)
            close_a.place(x=1080,y=550)
            
            a.mainloop()
     
     
     
     
     def chclose():
         b.destroy()
          
     c1=Canvas(b,width=2270,height=2080,bg='light blue')
     c1.place(x=0,y=0)

     z=Label(b,text="Admin Login",bg="yellow",fg="blue",width=300,height=3,font=('Aerial',30))
     z.pack()

     y=Label(b,text="Admin Name",font=5)
     y.place(x=500,y=200)
     y1=Entry(b,width=30)
     y1.place(x=700,y=200)

     x=Label(b,text="Password",font=5)
     x.place(x=500,y=250)
     x1=Entry(b,width=30,show='*')
     x1.place(x=700,y=250)

     z1=Button(b,text="Login",width=10,font=10,bg="blue",fg="white",command=Login)
     z1.place(x=500,y=350)

     z3=Button(b,text="Back",width=10,font=5,bg="red",fg="black",command=chclose)
     z3.place(x=750,y=350)
     
     b.mainloop()

def close_bb():
    t.destroy()
    
def User():
    z=Toplevel(t)
    z.geometry("1270x1080+0+0")
    z.title("User Side")
    
    def Login_2():
        name=y1.get()
        password=x1.get()
        db=pymysql.connect(host='localhost',user='root',password='root',database="Quiz_Portal")
        cur=db.cursor()
        sql="select User_Id ,Password from userinformation where User_Id='%s'"%(name)
        cur.execute(sql)
        result=cur.fetchone()
        db.close()
        print("yes")
        print(result)
        if result is not None and name==result[0] and password==result[1]:
            h1=Toplevel(z)
            h1.geometry("1270x1080+0+0")
            h1.title("Login User")
            
            def chemistry():
                h=Toplevel(h1)
                h.geometry("1270x1080+0+0")
                h.title("Chemistry")
   
                question=[]
                global i 
                global score
                answer=[]
                option1=[]
                option2=[]
                option3=[]
                option4=[]
                optans=''
                ans1,ans2,ans3,ans4='','','',''
                cans=''
                i=0
                score=0
                def loaddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                    cur=db.cursor()
                    sql="select Ques_name,Answers,Opt_1,Opt_2,Opt_3,Opt_4 from questions where sub_id='C01' "
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        question.append(res[0])
                        answer.append(res[1])
                        option1.append(res[2])
                        option2.append(res[3])
                        option3.append(res[4])
                        option4.append(res[5])
                def filldata():
                    a.config(text=question[i])
                    b.config(text=answer[i])  
                def nextdata():
                     global i
                     i=i+1
                     if i < len(question):
                         x.set(0)


                         a.config(text=question[i])
                         b.config(text=answer[i])
                         filloptions()
                         
                     else:
                         global score
                         a.config(text="**** END OF QUIZ******")
                         b.config(text='')
                         r1.destroy()
                         r2.destroy()
                         r3.destroy()
                         r4.destroy()
                         bt.destroy()
                         bt1.destroy()
                         checkresult.destroy()
                         score_lbl.destroy()
                         if score == len(question):
                             message = f"Congratulations! You got all the answers correct \n Your Total Score is {score}"
                         else:
                             message = f"You got {score} out of {len(question)} questions correct. Keep it up!"
                             result_message = Label(h, text=message, font=("Aerial", 20), fg="black")
                             result_message.place(x=300, y=300)
                             closebt = Button(h, text="CLOSE", width=10,font=10, bg="red",fg="black", command=closeall)
                             closebt.place(x=470, y=500)
                             
                def filloptions():
                    r1.config(text=option1[i])
                    r2.config(text=option2[i])
                    r3.config(text=option3[i])
                    r4.config(text=option4[i])
                    # rsc.config(text=score)
                    checkresult.config(text=score)
             
                    ans1=r1['text']
                    ans2=r2['text']
                    ans3=r3['text']
                    ans4=r4['text']
                    
                def choose1():
                      global optans
                      optans=r1['text']
             
                def choose2():
                    global optans
                    optans=r2['text']
                    
                def choose3():
                     global optans
                     optans=r3['text']
                     
                def choose4():
                    global optans
                    optans=r4['text']
                    
                def checkanswer():
    
                    w=b['text']
                    global optans
                    if w==optans:
                         a=Label(h,text="Correct Answer",width=40,font="impack 15 bold").place(x=650,y=500)
                         global score
                
                         score=score+1
                         
                    else:
                        c=Label(h,text="Wrong Answer",width=40,font="impack 15 bold").place(x=650,y=500)
            
                def putans():
                    ww=int(x.get())
                    if ww==1:
                        ansjava.append()  
                
                def closeall():
                    h.destroy()
                    
                loaddata()
                
                a=Label(h,font=("Times new Roman",25),fg="black")
                a.place(x=100,y=150)
                
                checkresult=Label(h,width=10,font=("areial",20),bg="light blue")
        
                checkresult.place(x=1200,y=85)
                x=IntVar()
            
                c1=Canvas(h,height=60,width=1700,bg='yellow')
                c1.place(x=0,y=0)
                welcome_label=Label(c1,text="WELCOME TO QUIZ PORTAL",font=("areial",28),bg="yellow",fg="blue")
                welcome_label.place(x=500,y=3)
                r1=Radiobutton(h,font=("Areial",15),variable=x,value=1,command=choose1)
                r1.place(x=100,y=250)
                r2=Radiobutton(h,font=("Areial",15),variable=x,value=2,command=choose2)
                r2.place(x=100,y=300)
                r3=Radiobutton(h,font=("Areial",15),variable=x,value=3,command=choose3)
                r3.place(x=100,y=350)
                r4=Radiobutton(h,font=("Areial",15),variable=x,value=4,command=choose4)
                r4.place(x=100,y=400)
                b=Label(h,bg="skyblue")
                b.place(x=1300,y=750)
                filloptions()
                
                filldata()
            
                bt=Button(h,text="Next",width=10,height=2,bg="yellow",command=nextdata)
                bt.place(x=300,y=500)
                bt1=Button(h,text="Check",width=10,height=2,bg="yellow",command=checkanswer)
                bt1.place(x=500,y=500)
                
                score_lbl=Label(h,text="SCORE:",width=10,height=2,font=("areial",15),bg="#5e65a1",fg="white")
                score_lbl.place(x=1100,y=80)
                
                h.mainloop()
                
            def physics():
                h2=Toplevel(h1)
                h2.geometry("1270x1080+0+0")
                h2.title("Chemistry")
                
                question=[]
                global i 
                global score
                answer=[]
                option1=[]
                option2=[]
                option3=[]
                option4=[]
                optans=''
                ans1,ans2,ans3,ans4='','','',''
                cans=''
                i=0
                score=0
                def loaddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                    cur=db.cursor()
                    sql="select Ques_name,Answers,Opt_1,Opt_2,Opt_3,Opt_4 from questions where sub_id='P01' "
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        question.append(res[0])
                        answer.append(res[1])
                        option1.append(res[2])
                        option2.append(res[3])
                        option3.append(res[4])
                        option4.append(res[5])
                def filldata():
                    a.config(text=question[i])
                    b.config(text=answer[i])
                    
                def nextdata():
                     global i
                     i=i+1
                     if i < len(question):
                         x.set(0)


                         a.config(text=question[i])
                         b.config(text=answer[i])
                         filloptions()
                     else:
                         global score
                         a.config(text="**** END OF QUIZ******")
                         b.config(text='')
                         r1.destroy()
                         r2.destroy()
                         r3.destroy()
                         r4.destroy()
                         bt.destroy()
                         bt1.destroy()
                         checkresult.destroy()
                         score_lbl.destroy() 
                         if score == len(question):
                             message = f"Congratulations! You got all the answers correct \n Your Total Score is {score}"
                         else:
                             message = f"You got {score} out of {len(question)} questions correct. Keep it up!"
                             result_message = Label(h2, text=message, font=("Aerial", 20), fg="black")
                             result_message.place(x=300, y=300)
                             closebt = Button(h2, text="CLOSE", width=10,font=10, bg="red",fg="black", command=closeall)
                             closebt.place(x=470, y=500)
                 
                def filloptions():
                    r1.config(text=option1[i])
                    r2.config(text=option2[i])
                    r3.config(text=option3[i])
                    r4.config(text=option4[i])
        
                    checkresult.config(text=score)
             
                    ans1=r1['text']
                    ans2=r2['text']
                    ans3=r3['text']
                    ans4=r4['text']
                    
                def choose1():
                    global optans
                    optans=r1['text']
             
                def choose2():
                    global optans
                    optans=r2['text']
             
                def choose3():
                    global optans
                    optans=r3['text']
             
                def choose4():
                    global optans
                    optans=r4['text']
                    
                def checkanswer():
    
                    w=b['text']
                    global optans
                    if w==optans:
                 
                        a=Label(h2,text="Correct Answer",width=40,font="impack 15 bold").place(x=650,y=500)
                        global score
                
                        score=score+1
                 
                    else:
                        c=Label(h2,text="Wrong Answer",width=40,font="impack 15 bold").place(x=650,y=500)
                 
                def putans():
                    ww=int(x.get())
                    if ww==1:
                        ansjava.append()

                def closeall():
                    h2.destroy()
                    
                loaddata()
                
                a=Label(h2,font=("Times new Roman",25),fg="black")
                a.place(x=100,y=150)
                
                checkresult=Label(h2,width=10,font=("areial",20),bg="light blue")
        
                checkresult.place(x=1200,y=85)
                x=IntVar()
            
                c1=Canvas(h2,height=60,width=1700,bg='yellow')
                c1.place(x=0,y=0)
                welcome_label=Label(c1,text="WELCOME TO QUIZ PORTAL",font=("areial",28),bg="yellow",fg="blue")
                welcome_label.place(x=500,y=3)
                r1=Radiobutton(h2,font=("Areial",15),variable=x,value=1,command=choose1)
                r1.place(x=100,y=250)
                r2=Radiobutton(h2,font=("Areial",15),variable=x,value=2,command=choose2)
                r2.place(x=100,y=300)
                r3=Radiobutton(h2,font=("Areial",15),variable=x,value=3,command=choose3)
                r3.place(x=100,y=350)
                r4=Radiobutton(h2,font=("Areial",15),variable=x,value=4,command=choose4)
                r4.place(x=100,y=400)
                b=Label(h2,bg="skyblue")
                b.place(x=1300,y=750)
                filloptions()
                
                filldata()
            
                bt=Button(h2,text="Next",width=10,height=2,bg="yellow",command=nextdata)
                bt.place(x=300,y=500)
                bt1=Button(h2,text="Check",width=10,height=2,bg="yellow",command=checkanswer)
                bt1.place(x=500,y=500)
         
                score_lbl=Label(h2,text="SCORE:",width=10,height=2,font=("areial",15),fg="black")
                score_lbl.place(x=1100,y=80)
                
                h2.mainloop()
                
            def computer():
                h3=Toplevel(h1)
                h3.geometry("1270x1080+0+0")
                h3.title("Chemistry")
   
                question=[]
                global i 
                global score
                answer=[]
                option1=[]
                option2=[]
                option3=[]
                option4=[]
                optans=''
                ans1,ans2,ans3,ans4='','','',''
                cans=''
                i=0
                score=0
                def loaddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                    cur=db.cursor()
                    sql="select Ques_name,Answers,Opt_1,Opt_2,Opt_3,Opt_4 from questions where sub_id='C02' "
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        question.append(res[0])
                        answer.append(res[1])
                        option1.append(res[2])
                        option2.append(res[3])
                        option3.append(res[4])
                        option4.append(res[5])
                def filldata():
                    a.config(text=question[i])
                    b.config(text=answer[i])
                def nextdata():
                    global i
                    i=i+1
                    if i < len(question):
                        x.set(0)
                        
                        a.config(text=question[i])
                        b.config(text=answer[i])
                        filloptions()
                        
                    else:
                        global score
                        a.config(text="**** END OF QUIZ******")
                        b.config(text='')
                        r1.destroy()
                        r2.destroy()
                        r3.destroy()
                        r4.destroy()
                        bt.destroy()
                        bt1.destroy()
                        checkresult.destroy()
                        score_lbl.destroy()
                        if score == len(question):
                            message = f"Congratulations! You got all the answers correct \n Your Total Score is {score}"
                        else:
                            message = f"You got {score} out of {len(question)} questions correct. Keep it up!"
                            result_message = Label(h3, text=message, font=("Aerial", 20), fg="black")
                            result_message.place(x=300, y=300)
                            closebt = Button(h3, text="CLOSE", width=10,font=10, bg="red",fg="black", command=closeall)
                            closebt.place(x=470, y=500)
                            
                def filloptions():
                    r1.config(text=option1[i])
                    r2.config(text=option2[i])
                    r3.config(text=option3[i])
                    r4.config(text=option4[i])
                    # rsc.config(text=score)
                    checkresult.config(text=score)
                
                    ans1=r1['text']
                    ans2=r2['text']
                    ans3=r3['text']
                    ans4=r4['text']
                    
                def choose1():
                    global optans
                    optans=r1['text']
                    # checkanswer()
                def choose2():
                    global optans
                    optans=r2['text']
                    # checkanswer()
                def choose3():
                    global optans
                    optans=r3['text']
                    # checkanswer()
                def choose4():
                    global optans
                    optans=r4['text']
                    # checkanswer()
                    
                def checkanswer():
    
                    w=b['text']
                    global optans
                    if w==optans:
                 
                        a=Label(h3,text="Correct Answer",width=40,font="impack 15 bold").place(x=650,y=500)
                        global score
                
                        score=score+1
                        
                    else:
                        c=Label(h3,text="Wrong Answer",width=40,font="impack 15 bold").place(x=650,y=500)
                        
                        
                def putans():
                    ww=int(x.get())
                    if ww==1:
                        ansjava.append()

                def closeall():
                    h3.destroy()
                    
                loaddata()
                
                a=Label(h3,font=("Times new Roman",25),fg="black")
                a.place(x=100,y=150)
                # rsc=Label(t,width=20,height=2)
                # rsc.place(x=1200,y=20)
            
                checkresult=Label(h3,width=10,font=("areial",20),bg="light blue")
        
                checkresult.place(x=1200,y=85)
                x=IntVar()
                
                          
                c1=Canvas(h3,height=60,width=1700,bg='yellow')
                c1.place(x=0,y=0)
                welcome_label=Label(c1,text="WELCOME TO QUIZ PORTAL",font=("areial",28),bg="yellow",fg="blue")
                welcome_label.place(x=500,y=3)
                r1=Radiobutton(h3,font=("Areial",15),variable=x,value=1,command=choose1)
                r1.place(x=100,y=250)
                r2=Radiobutton(h3,font=("Areial",15),variable=x,value=2,command=choose2)
                r2.place(x=100,y=300)
                r3=Radiobutton(h3,font=("Areial",15),variable=x,value=3,command=choose3)
                r3.place(x=100,y=350)
                r4=Radiobutton(h3,font=("Areial",15),variable=x,value=4,command=choose4)
                r4.place(x=100,y=400)
                b=Label(h3,bg="skyblue")
                b.place(x=1300,y=750)
                filloptions()
                
                filldata()
            
                bt=Button(h3,text="Next",width=10,height=2,bg="yellow",command=nextdata)
                bt.place(x=300,y=500)
                bt1=Button(h3,text="Check",width=10,height=2,bg="yellow",command=checkanswer)
                bt1.place(x=500,y=500)
         
                score_lbl=Label(h3,text="SCORE:",width=10,height=2,font=("areial",15),bg="#5e65a1",fg="white")
                score_lbl.place(x=1100,y=80)
                
                
                h3.mainloop()
                
            def maths():
                h4=Toplevel(h1)
                h4.geometry("1270x1080+0+0")
                h4.title("Chemistry")
   
                question=[]
                global i 
                global score
                answer=[]
                option1=[]
                option2=[]
                option3=[]
                option4=[]
                optans=''
                ans1,ans2,ans3,ans4='','','',''
                cans=''
                i=0
                score=0
                def loaddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='Quiz_Portal')
                    cur=db.cursor()
                    sql="select Ques_name,Answers,Opt_1,Opt_2,Opt_3,Opt_4 from questions where sub_id='M01' "
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        question.append(res[0])
                        answer.append(res[1])
                        option1.append(res[2])
                        option2.append(res[3])
                        option3.append(res[4])
                        option4.append(res[5])
                def filldata():
                    a.config(text=question[i])
                    b.config(text=answer[i])
                def nextdata():
                    global i
                    i=i+1
                    if i < len(question):
                        x.set(0)
                        a.config(text=question[i])
                        b.config(text=answer[i])
                        filloptions()
                            
                    else:
                        global score
                        a.config(text="**** END OF QUIZ******")
                        b.config(text='')
                        r1.destroy()
                        r2.destroy()
                        r3.destroy()
                        r4.destroy()
                        bt.destroy()
                        bt1.destroy()
                        checkresult.destroy()
                        score_lbl.destroy()
                        if score == len(question):
                            message = f"Congratulations! You got all the answers correct \n Your Total Score is {score}"
                        else:
                            message = f"You got {score} out of {len(question)} questions correct. Keep it up!"
                            result_message = Label(h4, text=message, font=("Aerial", 20), fg="black")
                            result_message.place(x=300, y=300)
                            closebt = Button(h4, text="CLOSE", width=10,font=10, bg="red",fg="black", command=closeall)
                            closebt.place(x=470, y=500)
                    
                def filloptions():
                    r1.config(text=option1[i])
                    r2.config(text=option2[i])
                    r3.config(text=option3[i])
                    r4.config(text=option4[i])
                   
                    checkresult.config(text=score)
             
                    ans1=r1['text']
                    ans2=r2['text']
                    ans3=r3['text']
                    ans4=r4['text']
                        
                def choose1():
                    global optans
                    optans=r1['text']
                    # checkanswer()
                def choose2():
                    global optans
                    optans=r2['text']
                    # checkanswer()
                def choose3():
                    global optans
                    optans=r3['text']
                    # checkanswer()
                def choose4():
                    global optans
                    optans=r4['text']
                    # checkanswer()
                        
                def checkanswer():
    
                    w=b['text']
                    global optans
                    if w==optans:
                 
                        a=Label(h4,text="Correct Answer",width=40,font="impack 15 bold").place(x=650,y=500)
                        global score
                
                        score=score+1
                        # checkresult.config(text=score)
    
                    else:
                        c=Label(h4,text="Wrong Answer",width=40,font="impack 15 bold").place(x=650,y=500)
                        #     score=0
        
                def putans():
                    ww=int(x.get())
                    if ww==1:
                        ansjava.append()

                def closeall():
                    h4.destroy()
                        
                loaddata()
                
                a=Label(h4,font=("Times new Roman",25),fg="black")
                a.place(x=100,y=150)
                
                checkresult=Label(h4,width=10,font=("areial",20),bg="light blue")
        
                checkresult.place(x=1200,y=85)
                x=IntVar()
                    
                             
                c1=Canvas(h4,height=60,width=1700,bg='yellow')
                c1.place(x=0,y=0)
                welcome_label=Label(c1,text="WELCOME TO QUIZ PORTAL",font=("areial",28),bg="yellow",fg="blue")
                welcome_label.place(x=500,y=3)
                r1=Radiobutton(h4,font=("Areial",15),variable=x,value=1,command=choose1)
                r1.place(x=100,y=250)
                r2=Radiobutton(h4,font=("Areial",15),variable=x,value=2,command=choose2)
                r2.place(x=100,y=300)
                r3=Radiobutton(h4,font=("Areial",15),variable=x,value=3,command=choose3)
                r3.place(x=100,y=350)
                r4=Radiobutton(h4,font=("Areial",15),variable=x,value=4,command=choose4)
                r4.place(x=100,y=400)
                b=Label(h4,bg="skyblue")
                b.place(x=1300,y=750)
                filloptions()
                    
                filldata()
            
                bt=Button(h4,text="Next",width=10,height=2,bg="yellow",command=nextdata)
                bt.place(x=300,y=500)
                bt1=Button(h4,text="Check",width=10,height=2,bg="yellow",command=checkanswer)
                bt1.place(x=500,y=500)
         
                score_lbl=Label(h4,text="SCORE:",width=10,height=2,font=("areial",15),bg="black")
                score_lbl.place(x=1100,y=80)
               
                h4.mainloop()
                
            def closeab():
                h1.destroy()
                    
            h11=Canvas(h1,width=2270,height=2080,bg='light blue')
            h11.place(x=0,y=0)

            question=Label(h1,text="Questions",bg='yellow',fg='Blue',width=300,height=3,font=('Aeries',30))
            question.pack()

            chemistry=Button(h1,text="Chemistry",width=10,font=10,bg='Blue',fg='White',command=chemistry)
            chemistry.place(x=250,y=250)

            computer=Button(h1,text="Computer",width=10,font=10,bg='Blue',fg='White',command=computer)
            computer.place(x=450,y=350)

            maths=Button(h1,text="Maths",width=10,font=10,bg='Blue',fg='White',command=maths)
            maths.place(x=650,y=250)

            physics=Button(h1,text="Physics",width=10,font=10,bg='Blue',fg='White',command=physics)
            physics.place(x=850,y=350)

            back=Button(h1,text="Back",width=10,font=10,bg='red',fg='black',command=closeab)
            back.place(x=1080,y=550)
            
            h1.mainloop()
        
        else:
            messagebox.showinfo("STATUS","WRONG DETAILS")
            
    def closeabc():
        z.destroy()
        
    z4=Canvas(z,width=2270,height=2080,bg='light blue')
    z4.place(x=0,y=0)

    z5=Label(z,text="User Login",bg="yellow",fg="blue",width=300,height=3,font=('Aerial',30))
    z5.pack()
    
    y=Label(z,text="User Name",font=5)
    y.place(x=500,y=200)
    y1=Entry(z,width=30)
    y1.place(x=700,y=200)

    x=Label(z,text="Password",font=5)
    x.place(x=500,y=250)
    x1=Entry(z,width=30,show='*')
    x1.place(x=700,y=250)

    z1=Button(z,text="Login",width=10,font=10,bg="blue",fg="white",command=Login_2)
    z1.place(x=500,y=350)

    z3=Button(z,text="Back",width=10,font=5,bg="red",fg="black",command=closeabc)
    z3.place(x=750,y=350)
    
    z.mainloop()
  
c=Canvas(t,width=2270,height=2080,bg='light blue')
c.place(x=0,y=0)

welcome=Label(t,text="Welcome to Quiz Portal",bg='yellow',fg='Blue',width=300,height=3,font=('Aeries',30))
welcome.pack()

admin=Button(t,text="Admin",width=10,font=10,bg="Blue",fg="white",command=Admin)
admin.place(x=480,y=350)

user=Button(t,text="User",width=10,font=10,bg="Blue",fg="white",command=User)
user.place(x=650,y=350)

create_exp=Label(t,text='select any one of them.',bg="light blue",font=('Aeries',16))
create_exp.place(x=510,y=410)

close_b=Button(t,text='Close',width=10,font=10,bg='red',fg='black',command=close_bb)
close_b.place(x=1080,y=550)

t.mainloop()