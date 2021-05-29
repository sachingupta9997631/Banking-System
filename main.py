from tkinter import *
import sqlite3
import pyrebase

##############################variables declared#########################
firebaseConfig = {
    "apiKey": "AIzaSyDAwovZhuooQDzFJj6fJy4rbOjw38PoZ5A",
    "authDomain": "test-project-ae3e2.firebaseapp.com",
    "databaseURL": "https://test-project-ae3e2-default-rtdb.firebaseio.com",
    "projectId": "test-project-ae3e2",
    "storageBucket": "test-project-ae3e2.appspot.com",
    "messagingSenderId": "483863023492",
    "appId": "1:483863023492:web:87132bafb554750a8157d1"
}

firebase = pyrebase.initialize_app(firebaseConfig)
base = firebase.database()

db=sqlite3.connect("bank_data.db")
cur=db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS bank(id number NOT NULL,name text, father text, mother text,address text, phone text, amount number, pin number,PRIMARY KEY(id))")

#########################################################################

##############################Functions Defined##########################
def main_head(windows):
    main_lab=Label(windows,text="B a n k i n g   S y s t e m",font=("Bahnschrift Semifont",40))
    main_lab.pack(pady=10)
    credit=Label(windows,text="D e v e l o p e d   B y   S a c h i n   G u p t a",fg="red",font=("Bahnschrift Semifont",18))
    credit.pack(pady=10)

def update_acc():
    win1=Toplevel()
    
    win1.title("Update Account Details")
    win1.config(bg="white")
    win1.geometry("1530x800+0+0")
    img1=PhotoImage(file="req_img\\options.png")
    lab1=Label(win1,image=img1)
    lab1.pack(side=LEFT)
    lab1.place(x=0,y=0)

    stat = StringVar()
    name,fname,mname,add,phone,pin=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
    
    main_lab=Label(win1,text="B a n k i n g   S y s t e m",font=("Bahnschrift Semifont",40))
    main_lab.pack(pady=10)
    credit=Label(win1,text="( D e v e l o p e d   B y   S a c h i n   G u p t a )",fg="red",font=("Bahnschrift Semifont",18))
    credit.pack(pady=10)
    main_tag=Label(win1,text="U p d a t e   A c c o u n t   D e t a i l s",fg="green",font=("Bahnschrift Semifont",20))
    main_tag.pack(pady=10)
    imp_tag=Label(win1,text="(All Fields are Mandatory)",font=("Bahnschrift Semifont",14))
    imp_tag.pack()
    imp_tag.place(x=350,y=370)
    
    lab_id=Label(win1,text="Account ID: ",font=("Bahnschrift Semifont",18))
    lab_id.pack()
    lab_id.place(x=175,y=400)

    ent_id=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_id.pack()
    ent_id.place(x=350,y=400)
    
    lab_pin=Label(win1,text="PIN Code: ",font=("Bahnschrift Semifont",18))
    lab_pin.pack()
    lab_pin.place(x=190,y=470)

    ent_pin=Entry(win1,font=("Bahnschrift Semifont",18),show="*",bg="lightcyan")
    ent_pin.pack()
    ent_pin.place(x=350,y=470)

    lab_stat=Label(win1,text="( S t a t u s )",font=("Bahnschrift Semifont",16))
    lab_stat.pack()
    lab_stat.place(x=310,y=630)
    
    stats=Entry(win1,font=("Bahnschrift Semifont",15),textvariable=stat,width=55,fg="red",bg="lightcyan")
    stats.pack()
    stats.place(x=90,y=670)    

    lab_det=Label(win1,text="Account Details",font=("Bahnschrift Semifont",14))
    lab_det.pack()
    lab_det.place(x=960,y=300)

    label1=Label(win1,text="Holder's Name: ",font=("Bahnschrift Semifont",16))
    label1.pack()
    label1.place(x=860,y=350)

    ent_upd_name=Entry(win1,textvariable=name,width=30,bg="lightcyan",font=("Bahnschrift Semifont",16))
    ent_upd_name.pack()
    ent_upd_name.place(x=1060,y=350)

    label2=Label(win1,text="Father's Name: ",font=("Bahnschrift Semifont",16))
    label2.pack()
    label2.place(x=860,y=400)

    ent_upd_fname=Entry(win1,textvariable=fname,width=30,bg="lightcyan",font=("Bahnschrift Semifont",16))
    ent_upd_fname.pack()
    ent_upd_fname.place(x=1060,y=400)
    
    label3=Label(win1,text="Mother's Name: ",font=("Bahnschrift Semifont",16))
    label3.pack()
    label3.place(x=860,y=450)

    ent_upd_mname=Entry(win1,textvariable=mname,width=30,bg="lightcyan",font=("Bahnschrift Semifont",16))
    ent_upd_mname.pack()
    ent_upd_mname.place(x=1060,y=450)
    
    label4=Label(win1,text="Address: ",font=("Bahnschrift Semifont",16))
    label4.pack()
    label4.place(x=860,y=500)

    ent_upd_add=Entry(win1,textvariable=add,width=30,bg="lightcyan",font=("Bahnschrift Semifont",16))
    ent_upd_add.pack()
    ent_upd_add.place(x=1060,y=500)

    label5=Label(win1,text="Contact No.: ",font=("Bahnschrift Semifont",16))
    label5.pack()
    label5.place(x=860,y=550)

    ent_upd_ph=Entry(win1,textvariable=phone,width=30,bg="lightcyan",font=("Bahnschrift Semifont",16))
    ent_upd_ph.pack()
    ent_upd_ph.place(x=1060,y=550)

    label6=Label(win1,text="PIN Password: ",font=("Bahnschrift Semifont",16))
    label6.pack()
    label6.place(x=860,y=600)

    ent_upd_pin=Entry(win1,textvariable=pin,width=30,bg="lightcyan",font=("Bahnschrift Semifont",16))
    ent_upd_pin.pack()
    ent_upd_pin.place(x=1060,y=600)
    
    ##########################functions##############################

    def clear_data():
        ent_id.delete(0,'end')
        ent_pin.delete(0,'end')
        stat.set(str(""))
        name.set(str(""))
        fname.set(str(""))
        mname.set(str(""))
        add.set(str(""))
        phone.set(str(""))
        pin.set(str(""))
    
    t_amt = str()
    t_id = str()
    def sear_det():
        global t_amt, t_id

        if str(ent_id.get())=="" and str(ent_pin.get())=="":
            stat.set(str(""))
            stat.set(str("No Data in the Fields were Found"))
        else:    
            data = base.child("Banking").get()
            for person in data.each():
                if person.val()["ID"]==str(ent_id.get()) and person.val()["PIN"]==str(ent_pin.get()):
                    t=person.val()
                    stat.set("Account found!")

                    name.set(str(t['NAME']))
                    fname.set(str(t['FATHER']))
                    mname.set(str(t['MOTHER']))
                    add.set(str(t['ADDRESS']))
                    phone.set(str(t['PHONE']))
                    pin.set(str(t['PIN']))
                    t_amt = str(t['AMOUNT'])
                    t_id = str(t['ID'])
                    
                    del t
                    return
            stat.set("No Account Found with these details")

    def upd_details():
        global t_amt, t_id
        
        a,b,c,d,e,f=str(ent_upd_name.get()),str(ent_upd_fname.get()),str(ent_upd_mname.get()),str(ent_upd_add.get()),str(ent_upd_ph.get()),str(ent_upd_pin.get())
        dat = {"ID": t_id, "NAME": a, "FATHER": b, "MOTHER": c, "ADDRESS": d, "PHONE": e, "AMOUNT": t_amt, "PIN": f}
        
        base.child("Banking").child(str(t_id+a)).update(dat)

        stat.set("The data was Successfully updated to the DataBase server...")
        del a,b,c,d,e,f
              
    #################################################################

    but_sear_det=Button(win1,text="Search Account ",font=("Bahnschrift Semifont",16),command=sear_det)
    but_sear_det.pack()
    but_sear_det.place(x=350,y=540)    

    but_upd=Button(win1,text="Update Details ",font=("Bahnschrift Semifont",16),command=upd_details)
    but_upd.pack()
    but_upd.place(x=890,y=700)    
    
    but_clear=Button(win1,text="Clear All Fields",font=("Bahnschrift Semifont",16),command=clear_data)
    but_clear.pack()
    but_clear.place(x=1090,y=700)
    
    but_home=Button(win1,text="Go to Home",font=("Bahnschrift Semifont",16),command=lambda:win1.destroy())
    but_home.pack()
    but_home.place(x=1290,y=700)
    
    win1.mainloop()


def delete_acc():
    win1=Toplevel()
    
    win1.title("Delete Account")
    win1.config(bg="white")
    win1.geometry("1530x800+0+0")
    img1=PhotoImage(file="req_img\\options.png")
    lab1=Label(win1,image=img1)
    lab1.pack(side=LEFT)
    lab1.place(x=0,y=0)

    stat = StringVar()
    stat.set(str(" "))

    main_lab=Label(win1,text="B a n k i n g   S y s t e m",font=("Bahnschrift Semifont",40))
    main_lab.pack()
    credit=Label(win1,text="( D e v e l o p e d   B y   S a c h i n   G u p t a )",fg="red",font=("Bahnschrift Semifont",18))
    credit.pack(pady=10)
    main_tag=Label(win1,text="D e l e t e   T h e   A c c o u n t",fg="green",font=("Bahnschrift Semifont",20))
    main_tag.pack(pady=10)
    imp_tag=Label(win1,text="(All Fields are Mandatory)",font=("Bahnschrift Semifont",14))
    imp_tag.pack()
    imp_tag.place(x=350,y=350)
    
    lab_id=Label(win1,text="Account ID: ",font=("Bahnschrift Semifont",18))
    lab_id.pack()
    lab_id.place(x=175,y=400)

    ent_id=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_id.pack()
    ent_id.place(x=350,y=400)
    
    lab_pin=Label(win1,text="PIN Code: ",font=("Bahnschrift Semifont",18))
    lab_pin.pack()
    lab_pin.place(x=190,y=470)

    ent_pin=Entry(win1,font=("Bahnschrift Semifont",18),show="*",bg="lightcyan")
    ent_pin.pack()
    ent_pin.place(x=350,y=470)

    lab_stat=Label(win1,text="( S t a t u s )",font=("Bahnschrift Semifont",16))
    lab_stat.pack()
    lab_stat.place(x=1090,y=300)
    
    stats=Entry(win1,font=("Bahnschrift Semifont",15),textvariable=stat,width=50,fg="red",bg="lightcyan")
    stats.pack()
    stats.place(x=860,y=340)    

    text=Text(win1,font=("Bahnschrift Semifont",15),width=50,height=12,bg="lightcyan")
    text.pack()
    text.place(x=860,y=380)

    ##########################functions##############################
    def clear_data():
        text.delete(1.0,'end')
        ent_id.delete(0,'end')
        ent_pin.delete(0,'end')
        stat.set(str(""))

    def del_rec():
        data = base.child("Banking").get()
        for person in data.each():
            if person.val()["ID"]==str(ent_id.get()) and person.val()["PIN"]==str(ent_pin.get()):
                base.child("Banking").child(person.key()).remove()
                stat.set("The Account was deleted Successfully!")
                text.delete(1.0,'end')
                return
        stat.set("No Account Found with these details")
    
    def sear_det():
        if str(ent_id.get())=="" and str(ent_pin.get())=="":
            text.delete(1.0,'end')
            stat.set(str(""))
            stat.set(str("No Data in the Fields were Found"))
        else:    
            data = base.child("Banking").get()
            for person in data.each():
                if person.val()["ID"]==str(ent_id.get()) and person.val()["PIN"]==str(ent_pin.get()):
                    t=person.val()
                    stat.set("Account found!")
                    text.delete(1.0,'end')

                    text.insert(INSERT,str("\n\n       Account ID : " + str(t['ID'])))
                    text.insert(INSERT,str("\n    Holder Name : " + str(t['NAME'])))
                    text.insert(INSERT,str("\n  Father's Name : " + str(t['FATHER'])))
                    text.insert(INSERT,str("\n Mother's Name : " + str(t['MOTHER'])))
                    text.insert(INSERT,str("\n           Address : " + str(t['ADDRESS'])))
                    text.insert(INSERT,str("\nContact Number : " + str(t['PHONE'])))
                    text.insert(INSERT,str("\n Current Amount : " + str(t['AMOUNT'])))

                    del t
                    return
            stat.set("No Account Found with these details")
    #################################################################

    but_upd_det=Button(win1,text="Search Account ",font=("Bahnschrift Semifont",16),command=sear_det)
    but_upd_det.pack()
    but_upd_det.place(x=350,y=540)    

    del_acc=Button(win1,text="Delete Account ",font=("Bahnschrift Semifont",16),command=del_rec)
    del_acc.pack()
    del_acc.place(x=350,y=610)
    
    but_clear=Button(win1,text="Clear All Fields",font=("Bahnschrift Semifont",16),command=clear_data)
    but_clear.pack()
    but_clear.place(x=1090,y=700)
    
    but_home=Button(win1,text="Go to Home",font=("Bahnschrift Semifont",16),command=lambda:win1.destroy())
    but_home.pack()
    but_home.place(x=1290,y=700)
    
    win1.mainloop()


def deposit():
    win1=Toplevel()
    
    win1.title("Deposit")
    win1.config(bg="white")
    win1.geometry("1530x800+0+0")
    img1=PhotoImage(file="req_img\\options.png")
    lab1=Label(win1,image=img1)
    lab1.pack(side=LEFT)
    lab1.place(x=0,y=0)

    stat = StringVar()
    stat.set(str(" "))

    main_lab=Label(win1,text="B a n k i n g   S y s t e m",font=("Bahnschrift Semifont",40))
    main_lab.pack()
    credit=Label(win1,text="( D e v e l o p e d   B y   S a c h i n   G u p t a )",fg="red",font=("Bahnschrift Semifont",18))
    credit.pack(pady=10)
    main_tag=Label(win1,text="D e p o s i t   F r o m   A c c o u n t",fg="green",font=("Bahnschrift Semifont",20))
    main_tag.pack(pady=10)
    imp_tag=Label(win1,text="(All Fields are Mandatory)",font=("Bahnschrift Semifont",14))
    imp_tag.pack()
    imp_tag.place(x=350,y=350)
    
    lab_id=Label(win1,text="Account ID: ",font=("Bahnschrift Semifont",18))
    lab_id.pack()
    lab_id.place(x=175,y=400)

    ent_id=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_id.pack()
    ent_id.place(x=350,y=400)
    
    lab_pin=Label(win1,text="PIN Code: ",font=("Bahnschrift Semifont",18))
    lab_pin.pack()
    lab_pin.place(x=190,y=470)

    ent_pin=Entry(win1,font=("Bahnschrift Semifont",18),show="*",bg="lightcyan")
    ent_pin.pack()
    ent_pin.place(x=350,y=470)

    dep_amt=Label(win1,text="Deposit Amount: ",font=("Bahnschrift Semifont",18))
    dep_amt.pack()
    dep_amt.place(x=120,y=540)

    ent_dep=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_dep.pack()
    ent_dep.place(x=350,y=540)

    lab_stat=Label(win1,text="( S t a t u s )",font=("Bahnschrift Semifont",16))
    lab_stat.pack()
    lab_stat.place(x=1090,y=400)
    
    stats=Entry(win1,font=("Bahnschrift Semifont",15),textvariable=stat,width=50,fg="red",bg="lightcyan")
    stats.pack()
    stats.place(x=860,y=440)    

    ##########################functions##############################
    def clear_data():    
        ent_id.delete(0,'end')
        ent_pin.delete(0,'end')
        ent_dep.delete(0,'end')

    def upd_det():
        data = base.child("Banking").get()
        for person in data.each():
            if person.val()["ID"]==str(ent_id.get()) and person.val()["PIN"]==str(ent_pin.get()):
                t = int(person.val()["AMOUNT"])
                t+= int(ent_dep.get())
                base.child("Banking").child(person.key()).update({"AMOUNT": t})
                stat.set("The Amount was Successfully Updated to the bank...")
                return
        stat.set("No Account Found with these details")

    def upd_det():
        cur.execute("select * from bank where id=?",str(ent_id.get()))  
        a=cur.fetchall()
        if a==[]:
            stat.set(str("No Account Found... Either the ID or the PIN was Invalid"))
        else:
            cur.execute("UPDATE bank set amount=amount+(?) where id=? and pin=?",(str(ent_dep.get()),str(ent_id.get()),str(ent_pin.get())))
            db.commit()
            stat.set(str("The Amount was Successfully Updated"))

    #################################################################

    but_upd_det=Button(win1,text="Update Account ",font=("Bahnschrift Semifont",16),command=upd_det)
    but_upd_det.pack()
    but_upd_det.place(x=350,y=610)    

    but_clear=Button(win1,text="Clear All Fields",font=("Bahnschrift Semifont",16),command=clear_data)
    but_clear.pack()
    but_clear.place(x=1290,y=630)
    
    but_home=Button(win1,text="Go to Home",font=("Bahnschrift Semifont",16),command=lambda:win1.destroy())
    but_home.pack()
    but_home.place(x=1290,y=700)
    
    win1.mainloop()


def view():
    win1=Toplevel()
    
    win1.title("View Account Details")
    win1.config(bg="white")
    win1.geometry("1530x800+0+0")
    img1=PhotoImage(file="req_img\\options.png")
    lab1=Label(win1,image=img1)
    lab1.pack(side=LEFT)
    lab1.place(x=0,y=0)

    stat = StringVar()
    stat.set(str(" "))

    main_lab=Label(win1,text="B a n k i n g   S y s t e m",font=("Bahnschrift Semifont",40))
    main_lab.pack()
    credit=Label(win1,text="( D e v e l o p e d   B y   S a c h i n   G u p t a )",fg="red",font=("Bahnschrift Semifont",18))
    credit.pack(pady=10)
    main_tag=Label(win1,text="V i e w   A c c o u n t   D e t a i l s",fg="green",font=("Bahnschrift Semifont",20))
    main_tag.pack(pady=10)
    imp_tag=Label(win1,text="(All Fields are Mandatory)",font=("Bahnschrift Semifont",14))
    imp_tag.pack()
    imp_tag.place(x=350,y=370)
    
    lab_id=Label(win1,text="Account ID: ",font=("Bahnschrift Semifont",18))
    lab_id.pack()
    lab_id.place(x=175,y=400)

    ent_id=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_id.pack()
    ent_id.place(x=350,y=400)
    
    lab_pin=Label(win1,text="PIN Code: ",font=("Bahnschrift Semifont",18))
    lab_pin.pack()
    lab_pin.place(x=190,y=470)

    ent_pin=Entry(win1,font=("Bahnschrift Semifont",18),show="*",bg="lightcyan")
    ent_pin.pack()
    ent_pin.place(x=350,y=470)

    lab_stat=Label(win1,text="( S t a t u s )",font=("Bahnschrift Semifont",16))
    lab_stat.pack()
    lab_stat.place(x=310,y=630)
    
    stats=Entry(win1,font=("Bahnschrift Semifont",15),textvariable=stat,width=55,fg="red",bg="lightcyan")
    stats.pack()
    stats.place(x=90,y=670)    

    lab_det=Label(win1,text="Account Details",font=("Bahnschrift Semifont",14))
    lab_det.pack()
    lab_det.place(x=860,y=300)
    
    text=Text(win1,font=("Bahnschrift Semifont",18),width=50,height=12,bg="lightcyan")
    text.pack()
    text.place(x=860,y=330)

    ##########################functions##############################
    def clear_data():
        text.delete(1.0,'end')
        ent_id.delete(0,'end')
        ent_pin.delete(0,'end')
        stat.set(str(""))
    
    def sear_det():
        if str(ent_id.get())=="" and str(ent_pin.get())=="":
            text.delete(1.0,'end')
            stat.set(str(""))
            stat.set(str("No Data in the Fields were Found"))
        else:    
            data = base.child("Banking").get()
            for person in data.each():
                if person.val()["ID"]==str(ent_id.get()) and person.val()["PIN"]==str(ent_pin.get()):
                    t=person.val()
                    stat.set("Account found!")
                    text.delete(1.0,'end')

                    text.insert(INSERT,str("\n\n       Account ID : " + str(t['ID'])))
                    text.insert(INSERT,str("\n    Holder Name : " + str(t['NAME'])))
                    text.insert(INSERT,str("\n  Father's Name : " + str(t['FATHER'])))
                    text.insert(INSERT,str("\n Mother's Name : " + str(t['MOTHER'])))
                    text.insert(INSERT,str("\n           Address : " + str(t['ADDRESS'])))
                    text.insert(INSERT,str("\nContact Number : " + str(t['PHONE'])))
                    text.insert(INSERT,str("\n Current Amount : " + str(t['AMOUNT'])))

                    del t
                    return
            stat.set("No Account Found with these details")

    #################################################################

    but_upd_det=Button(win1,text="Search Account ",font=("Bahnschrift Semifont",16),command=sear_det)
    but_upd_det.pack()
    but_upd_det.place(x=350,y=540)    

    but_clear=Button(win1,text="Clear All Fields",font=("Bahnschrift Semifont",16),command=clear_data)
    but_clear.pack()
    but_clear.place(x=1090,y=700)
    
    but_home=Button(win1,text="Go to Home",font=("Bahnschrift Semifont",16),command=lambda:win1.destroy())
    but_home.pack()
    but_home.place(x=1290,y=700)
    
    win1.mainloop()


def draw_amt():
    win1=Toplevel()
    
    win1.title("Withdraw")
    win1.config(bg="white")
    win1.geometry("1530x800+0+0")
    img1=PhotoImage(file="req_img\\options.png")
    lab1=Label(win1,image=img1)
    lab1.pack(side=LEFT)
    lab1.place(x=0,y=0)

    stat = StringVar()
    stat.set(str(" "))

    main_lab=Label(win1,text="B a n k i n g   S y s t e m",font=("Bahnschrift Semifont",40))
    main_lab.pack()
    credit=Label(win1,text="( D e v e l o p e d   B y   S a c h i n   G u p t a )",fg="red",font=("Bahnschrift Semifont",18))
    credit.pack(pady=10)
    main_tag=Label(win1,text="W i t h d r a w   F r o m   A c c o u n t",fg="green",font=("Bahnschrift Semifont",20))
    main_tag.pack(pady=10)
    imp_tag=Label(win1,text="(All Fields are Mandatory)",font=("Bahnschrift Semifont",14))
    imp_tag.pack()
    imp_tag.place(x=350,y=350)
    
    lab_id=Label(win1,text="Account ID: ",font=("Bahnschrift Semifont",18))
    lab_id.pack()
    lab_id.place(x=175,y=400)

    ent_id=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_id.pack()
    ent_id.place(x=350,y=400)
    
    lab_pin=Label(win1,text="PIN Code: ",font=("Bahnschrift Semifont",18))
    lab_pin.pack()
    lab_pin.place(x=190,y=470)

    ent_pin=Entry(win1,font=("Bahnschrift Semifont",18),show="*",bg="lightcyan")
    ent_pin.pack()
    ent_pin.place(x=350,y=470)

    draw_amt=Label(win1,text="Withdraw Amount: ",font=("Bahnschrift Semifont",18))
    draw_amt.pack()
    draw_amt.place(x=100,y=540)

    ent_draw=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_draw.pack()
    ent_draw.place(x=350,y=540)

    lab_stat=Label(win1,text="( S t a t u s )",font=("Bahnschrift Semifont",16))
    lab_stat.pack()
    lab_stat.place(x=1090,y=400)
    
    stats=Entry(win1,font=("Bahnschrift Semifont",15),textvariable=stat,width=50,fg="red",bg="lightcyan")
    stats.pack()
    stats.place(x=860,y=440)    

    ##########################functions##############################
    def clear_data():    
        ent_id.delete(0,'end')
        ent_pin.delete(0,'end')
        ent_draw.delete(0,'end')

    def upd_det():
        data = base.child("Banking").get()
        for person in data.each():
            if person.val()["ID"]==str(ent_id.get()) and person.val()["PIN"]==str(ent_pin.get()):
                t = int(person.val()["AMOUNT"])
                t-= int(ent_draw.get())
                base.child("Banking").child(person.key()).update({"AMOUNT": t})
                stat.set("The Amount was Successfully Updated to the bank...")
                return
        stat.set("No Account Found with these details")

    #################################################################

    but_upd_det=Button(win1,text="W i t h d r a w ",font=("Bahnschrift Semifont",16),command=upd_det)
    but_upd_det.pack()
    but_upd_det.place(x=350,y=610)    

    but_clear=Button(win1,text="Clear All Fields",font=("Bahnschrift Semifont",16),command=clear_data)
    but_clear.pack()
    but_clear.place(x=1290,y=630)
    
    but_home=Button(win1,text="Go to Home",font=("Bahnschrift Semifont",16),command=lambda:win1.destroy())
    but_home.pack()
    but_home.place(x=1290,y=700)
    
    win1.mainloop()


def new_acc():
    win1=Toplevel()
    
    win1.title("Create New Account")
    win1.config(bg="white")
    win1.geometry("1530x800+0+0")
    img1=PhotoImage(file="req_img\\options.png")
    lab1=Label(win1,image=img1)
    lab1.pack(side=LEFT)
    lab1.place(x=0,y=0)

    stat = StringVar()
    stat.set(str(" "))

    main_lab=Label(win1,text="B a n k i n g   S y s t e m",font=("Bahnschrift Semifont",40))
    main_lab.pack()
    credit=Label(win1,text="( D e v e l o p e d   B y   S a c h i n   G u p t a )",fg="red",font=("Bahnschrift Semifont",18))
    credit.pack(pady=10)
    main_tag=Label(win1,text="C r e a t e   N e w   A c c o u n t",fg="green",font=("Bahnschrift Semifont",20))
    main_tag.pack(pady=10)
    imp_tag=Label(win1,text="(All Fields are Mandatory)",font=("Bahnschrift Semifont",14))
    imp_tag.pack()
    imp_tag.place(x=350,y=250)
    
    lab_id=Label(win1,text="Account ID: ",font=("Bahnschrift Semifont",18))
    lab_id.pack()
    lab_id.place(x=150,y=300)

    ent_id=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_id.pack()
    ent_id.place(x=350,y=300)
    
    lab_name=Label(win1,text="Account Holder: ",font=("Bahnschrift Semifont",18))
    lab_name.pack()
    lab_name.place(x=100,y=370)

    ent_name=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_name.pack()
    ent_name.place(x=350,y=370)

    lab_father=Label(win1,text="Father's Name: ",font=("Bahnschrift Semifont",18))
    lab_father.pack()
    lab_father.place(x=100,y=440)

    ent_father=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_father.pack()
    ent_father.place(x=350,y=440)

    lab_mother=Label(win1,text="Mother's Name: ",font=("Bahnschrift Semifont",18))
    lab_mother.pack()
    lab_mother.place(x=100,y=510)

    ent_mother=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_mother.pack()
    ent_mother.place(x=350,y=510)
    
    lab_add=Label(win1,text="Address: ",font=("Bahnschrift Semifont",18))
    lab_add.pack()
    lab_add.place(x=170,y=580)

    ent_add=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_add.pack()
    ent_add.place(x=350,y=580)
    
    lab_phone=Label(win1,text="Phone: ",font=("Bahnschrift Semifont",18))
    lab_phone.pack()
    lab_phone.place(x=190,y=650)

    ent_phone=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_phone.pack()
    ent_phone.place(x=350,y=650)
    
    lab_amt=Label(win1,text="Initial Amount: ",font=("Bahnschrift Semifont",18))
    lab_amt.pack()
    lab_amt.place(x=110,y=720)

    ent_amt=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_amt.pack()
    ent_amt.place(x=350,y=720)

    lab_date=Label(win1,text="(the current date will be automatically added)",font=("bahnschrift semibold",18),fg="red")
    lab_date.pack()
    lab_date.place(x=900,y=500)

    lab_pin=Label(win1,text="PIN Password: ",font=("Bahnschrift Semifont",18))
    lab_pin.pack()
    lab_pin.place(x=900,y=320)

    ent_pin=Entry(win1,font=("Bahnschrift Semifont",18),bg="lightcyan")
    ent_pin.pack()
    ent_pin.place(x=1150,y=320)

    lab_stat=Label(win1,text="( S t a t u s )",font=("Bahnschrift Semifont",16))
    lab_stat.pack()
    lab_stat.place(x=1090,y=400)
    
    stats=Entry(win1,font=("Bahnschrift Semifont",15),textvariable=stat,width=50,fg="red",bg="lightcyan")
    stats.pack()
    stats.place(x=860,y=440)

    ##########################functions##############################
    def clear_data():    
        ent_id.delete(0,'end')
        ent_name.delete(0,'end')
        ent_father.delete(0,'end')
        ent_mother.delete(0,'end')
        ent_phone.delete(0,'end')
        ent_add.delete(0,'end')
        ent_amt.delete(0,'end')
        ent_pin.delete(0,'end')

    def save_data():
        a,b,c,d,e,f,g,h=str(ent_id.get()),str(ent_name.get()),str(ent_father.get()),str(ent_mother.get()),str(ent_add.get()),str(ent_phone.get()),str(ent_amt.get()),str(ent_pin.get())

        dat = {"ID": a, "NAME": b, "FATHER": c, "MOTHER": d, "ADDRESS": e, "PHONE": f, "AMOUNT": g, "PIN": h}
        
        base.child("Banking").child(str(a+b)).set(dat)

        stat.set("The data was Successfully saved to the DataBase...")
        del a,b,c,d,e,f,g,h
        
    #################################################################

    but_save=Button(win1,text="Save Account Details",font=("Bahnschrift Semifont",16),command=save_data)
    but_save.pack()
    but_save.place(x=900,y=620)    

    but_clear=Button(win1,text="Clear Everything",font=("Bahnschrift Semifont",16),command=clear_data)
    but_clear.pack()
    but_clear.place(x=1200,y=620)
    
    but_home=Button(win1,text="Go to Home",font=("Bahnschrift Semifont",16),command=lambda:win1.destroy())
    but_home.pack()
    but_home.place(x=1090,y=700)
    
    win1.mainloop()

#########################################################################

win=Tk()
win.title("Banking System")
win.config(bg="white")
win.geometry("1530x800+0+0")
img=PhotoImage(file="req_img\\2.png")
lab=Label(win,image=img)
lab.pack(side=LEFT)
win.resizable(False, False)
lab.place(x=0,y=0)

imglogo=PhotoImage(file="req_img\\logo.png")
lab=Label(win,image=imglogo)
lab.pack(side=LEFT)
lab.place(x=600,y=300)

main_head(win)

new_but=Button(win,text="Create New Account",font=("Bahnschrift Semifont",18),background="white",command=new_acc)
new_but.pack()
new_but.place(x=150,y=350)

draw_but=Button(win,text="Withdraw Amount",font=("Bahnschrift Semifont",18),background="white",command=draw_amt)
draw_but.pack()
draw_but.place(x=150,y=450)

dep_but=Button(win,text="Deposit Amount",font=("Bahnschrift Semifont",18),background="white",command=deposit)
dep_but.pack()
dep_but.place(x=150,y=550)

upd_but=Button(win,text="Update Account Details",font=("Bahnschrift Semifont",18),background="white",command=update_acc)
upd_but.pack()
upd_but.place(x=150,y=650)

desc=Label(win,text="Your Trust is Our Resposibility",font=("Bahnschrift Semifont",24),background="white")
desc.pack()
desc.place(x=540,y=630)

view_but=Button(win,text="View Account Details",font=("Bahnschrift Semifont",18),background="white",command=view)
view_but.pack()
view_but.place(x=1100,y=350)

del_but=Button(win,text="Delete Account",font=("Bahnschrift Semifont",18),background="white",command=delete_acc)
del_but.pack()
del_but.place(x=1100,y=450)

quit_but=Button(win,text="Quit to Windows",font=("Bahnschrift Semifont",18),background="white",command=lambda:win.destroy())
quit_but.pack()
quit_but.place(x=1100,y=550)

win.mainloop()
