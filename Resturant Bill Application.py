from tkinter import *
import random, math,os
from tkinter import messagebox
class Bill_App():
    def __init__(self,screen):
        self.screen = screen
        self.screen.geometry("1350x750+0+0")
        self.screen.title("Garlica Multicusine Restaurant")
        bg_colour = "deep sky blue"
        title = Label(self.screen,text = "Garlica Multicusine Restaurant",bd = 8,relief = GROOVE, bg = bg_colour , font = ("arial",30,"bold"),pady = 2).pack(fill = X)

        #########Variables######
        #-------Staters--------

        self.Tandoori = IntVar()
        self.Chilly_Chiken = IntVar()
        self.Majestic_Chiken = IntVar()
        self.Peper_Chiken = IntVar()
        self.Lollypop_Chiken = IntVar()
        self.Dry_Chilly = IntVar()

        # -------Main course--------

        self.Plain_Briyani = IntVar()
        self.Chiken_Briyani = IntVar()
        self.Mutton_Briyani = IntVar()
        self.Egg_Briyani = IntVar()
        self.Dry_CB = IntVar()
        self.Fried_Rice = IntVar()

        # -------Berverages--------

        self.Lassy = IntVar()
        self.Orange_Jucie= IntVar()
        self.Apple_Jucie = IntVar()
        self.Pepsi = IntVar()
        self.Thumpsup = IntVar()
        self.Fruit_Lassy = IntVar()

        # -------Total and Tax of the Iteams--------

        self.TStater = StringVar()
        self.TMcourse = StringVar()
        self.TBrav = StringVar()

        self.TaxStater = StringVar()
        self.TaxMcourse = StringVar()
        self.TaxBrav = StringVar()

        # -------Customer Details--------

        self.cname = StringVar()
        self.cphono = StringVar()

        self.cbillno = StringVar()
        x= random.randint(1000,9999)
        self.cbillno.set(str(x))

        self.search = StringVar()


        ###########Customer Label#######

        F1 = LabelFrame(self.screen, text = "Customer Details", bd = 10,font =("arial",15,"bold"),fg = "yellow",bg = bg_colour)
        F1.place(x = 0, y = 70, relwidth = 1)
        cnamelbl = Label(F1,text = "Customer Name",bg = bg_colour,font = ("arial",18,"bold")).grid(row = 0, column = 0)
        cnametxt = Entry(F1,font = ("arial",15,"bold"),textvariable = self.cname,bd = 7,relief = SUNKEN).grid(padx = 10,pady = 5,row = 0, column = 1)
        cphnolbl = Label(F1, text="Phone No", bg=bg_colour, font=("arial", 18, "bold")).grid(row=0,column=2)
        cphnotxt = Entry(F1, font=("arial", 15, "bold"),textvariable = self.cphono, bd=7, relief=SUNKEN).grid(padx=10, pady=5, row=0,column=3)
        cbillnolbl = Label(F1, text="Bill No", bg=bg_colour, font=("arial", 18, "bold")).grid(row=0,column=4)
        cbillnotxt = Entry(F1, font=("arial", 15, "bold"),textvariable = self.cbillno, bd=7, relief=SUNKEN).grid(padx=10, pady=5, row=0,column=5)
        searchbtn  = Button(F1,width = 10,text = "Search",command = self.search,font=("arial", 15, "bold"),bd = 8).grid(row = 0, column = 6,padx = 10,pady = 12)

        ###### Label 2 #####
        F2 = LabelFrame(self.screen, text="Staters", bd=10,relief = GROOVE,font=("arial", 15, "bold"), fg="yellow",bg=bg_colour)
        F2.place(x=5,y=185,width = 325,height = 380)
        Tlabel = Label(F2,text = "Tandoori",bg = bg_colour,font = ("arial",16  ,"bold")).grid(row = 0, column = 0)
        Ttxt = Entry(F2, width = 8,textvariable = self.Tandoori,font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=5, pady=10, row=0,column=1)

        Chilabel = Label(F2, text="Chilly Chiken", bg=bg_colour, font=("arial", 16, "bold")).grid(row=1, column=0)
        Chitxt = Entry(F2, width=8, textvariable = self.Chilly_Chiken,font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=1, column=1)

        Majlabel = Label(F2, text="Majestic Chiken", bg=bg_colour, font=("arial", 16, "bold")).grid(row=3,column=0)
        Majtxt = Entry(F2, width=8,textvariable = self.Majestic_Chiken,font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=3, column=1)

        peplabel = Label(F2, text="Peper Chiken", bg=bg_colour, font=("arial", 16, "bold")).grid(row=4,column=0)
        peptxt = Entry(F2, width=8,textvariable = self.Peper_Chiken, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=4, column=1)

        lollabel = Label(F2, text="Lollypop Chiken", bg=bg_colour, font=("arial", 16, "bold")).grid(row=5,column=0)
        loltxt = Entry(F2, width=8, textvariable = self.Lollypop_Chiken,font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=5, column=1)

        drylabel = Label(F2, text="Dry Chilly", bg=bg_colour, font=("arial", 16, "bold")).grid(row=6,column=0)
        drytxt = Entry(F2, width=8,textvariable = self.Dry_Chilly, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=6, column=1)

        ###### Label 3 #####
        F3 = LabelFrame(self.screen, text="Main Course", bd=10, relief=GROOVE, font=("arial", 15, "bold"),fg="yellow", bg=bg_colour)
        F3.place(x=340, y=185, width=325, height=380)
        Plabel = Label(F3, text="Plain Biriyani", bg=bg_colour, font=("arial", 16, "bold")).grid(row=0, column=0)
        Ptxt = Entry(F3, width=10,textvariable = self.Plain_Briyani, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=0, column=1)

        CBlabel = Label(F3, text="Chiken Biriyani", bg=bg_colour, font=("arial", 16, "bold")).grid(row=1,column=0)
        CBtxt = Entry(F3, width=10,textvariable = self.Chiken_Briyani, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=1, column=1)

        MBlabel = Label(F3, text="Mutton Biriyani", bg=bg_colour, font=("arial", 16, "bold")).grid(row=3,column=0)
        MBtxt = Entry(F3, width=10,textvariable = self.Mutton_Briyani, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=3, column=1)

        Egglabel = Label(F3, text="Egg Biriyani", bg=bg_colour, font=("arial", 16, "bold")).grid(row=4,column=0)
        Eggtxt = Entry(F3, width=10, textvariable = self.Egg_Briyani,font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=4, column=1)

        DCBlabel = Label(F3, text="Dry CB", bg=bg_colour, font=("arial", 16, "bold")).grid(row=5,column=0)
        DCBtxt = Entry(F3, width=10,textvariable = self.Dry_CB, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=5, column=1)

        frylabel = Label(F3, text="Fried Rice", bg=bg_colour, font=("arial", 16, "bold")).grid(row=6,column=0)
        frytxt = Entry(F3, width=10, textvariable = self.Fried_Rice,font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=6, column=1)

        ####### Label 4 ######
        F4 = LabelFrame(self.screen, text="Beverages", bd=10, relief=GROOVE, font=("arial", 15, "bold"),fg="yellow", bg=bg_colour)
        F4.place(x=670 , y=185, width=325, height=380)
        Laslabel = Label(F4, text="Lassy", bg=bg_colour, font=("arial", 16, "bold")).grid(row=0,column=0)
        Lastxt = Entry(F4, width=10,textvariable = self.Lassy, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=0, column=1)

        Orangelabel = Label(F4, text="Orange Juice", bg=bg_colour, font=("arial", 16, "bold")).grid(row=1,column=0)
        Orangetxt = Entry(F4, width=10,textvariable = self.Orange_Jucie, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=1, column=1)

        Applelabel = Label(F4, text="Apple Juice", bg=bg_colour, font=("arial", 16, "bold")).grid(row=3,column=0)
        Appletxt = Entry(F4, width=10, textvariable = self.Apple_Jucie,font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=3, column=1)

        Pepsilabel = Label(F4, text="Pepsi", bg=bg_colour, font=("arial", 16, "bold")).grid(row=4,column=0)
        Pepsitxt = Entry(F4, width=10, textvariable = self.Pepsi,font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=4, column=1)

        Thumblabel = Label(F4, text="Thumbsup", bg=bg_colour, font=("arial", 16, "bold")).grid(row=5, column=0)
        Thumbptxt = Entry(F4, width=10, textvariable = self.Thumpsup,font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=5, column=1)

        fruitlabel = Label(F4, text="Water Bottle", bg=bg_colour, font=("arial", 16, "bold")).grid(row=6,column=0)
        fruittxt = Entry(F4, width=10,textvariable = self.Fruit_Lassy, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(padx=10, pady=10,row=6, column=1)

        ##### Bill Area ######

        F5 = Frame(self.screen, bd=8, relief=GROOVE)
        F5.place(x=1010, y=185, width=350, height=380)
        bill_title = Label(F5,text = "Invoice",font = ("arial", 15, "bold"),bd = 7,relief = GROOVE).pack(fill = X)
        scrol_y = Scrollbar(F5,orient = VERTICAL)
        self.textarea = Text(F5,yscrollcommand = scrol_y.set)
        scrol_y.pack(side = RIGHT, fill = Y)
        scrol_y.config(command = self.textarea.yview)
        self.textarea.pack()

        ####### Button Frame #######
        F6 = LabelFrame(self.screen, text="Invoice Menu", bd=8, relief=GROOVE, font=("arial", 15, "bold"), fg="yellow",bg=bg_colour)
        F6.place(x=0, y=560, relwidth=1, height=140)
        TStarter = Label(F6, text = "Stater price",bg = bg_colour,font = ("arial",15,"bold")).grid(row= 0,column = 0,padx = 10,pady= 1,sticky = "w")
        TStartertxt = Entry(F6,width = 18,textvariable = self.TStater, font = ("arial",10,"bold"),bd = 6, relief=SUNKEN).grid(row = 0,column = 1,padx = 10,pady = 1)

        TMcourse = Label(F6, text="Main Course Price", bg=bg_colour, font=("arial", 15, "bold")).grid(row=1, column=0,padx=10, pady=1,sticky="w")
        TMcoursetxt = Entry(F6, width=18, textvariable = self.TMcourse,font=("arial", 10, "bold"), bd=6, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        TBrav = Label(F6, text="Beverages price", bg=bg_colour, font=("arial", 15, "bold")).grid(row=2, column=0,padx=10, pady=1,sticky="w")
        TBravtxt = Entry(F6, width=18, textvariable = self.TBrav,font=("arial", 10, "bold"), bd=6, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        TaxStarter = Label(F6, text="Stater Tax", bg=bg_colour, font=("arial", 15, "bold")).grid(row=0, column=4,padx=10, pady=1,sticky="w")
        TStartertxt = Entry(F6, width=18, textvariable = self.TaxStater,font=("arial", 10, "bold"), bd=6, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=1)

        TaxMcourse = Label(F6, text="Main Course Tax", bg=bg_colour, font=("arial", 15, "bold")).grid(row=1, column=4,padx=10, pady=1,sticky="w")
        TMcoursetxt = Entry(F6, width=18, textvariable = self.TaxMcourse,font=("arial", 10, "bold"), bd=6, relief=SUNKEN).grid(row=1, column=5, padx=10, pady=1)

        TaxBrav = Label(F6, text="Beverages Tax", bg=bg_colour, font=("arial", 15, "bold")).grid(row=2, column=4,padx=10, pady=1, sticky="w")
        TBravtxt = Entry(F6, width=18,textvariable = self.TaxBrav, font=("arial", 10, "bold"), bd=6, relief=SUNKEN).grid(row=2, column=5, padx=10, pady=1)

        btn_frame = Frame(F6,bd = 7, relief=GROOVE)
        btn_frame.place(x = 710,width = 620,height = 100)

        Tbtn = Button(btn_frame,command =self.total,text = "Total",font = ("arial",15,"bold"),fg = "white",bg = "grey",width = 10).grid(row = 0,column = 0,padx = 7,pady = 20)
        billbtn = Button(btn_frame, text="Bill Generate",command = self.bill_area, font=("arial", 15, "bold"), fg="white", bg="grey", width=12).grid(row=0,column=1,padx=7,pady=20)
        Clearbtn = Button(btn_frame, text="Clear",command = self.clear,font=("arial", 15, "bold"), fg="white", bg="grey",width=10).grid(row=0, column=2, padx=7, pady=20)
        Exitbtn = Button(btn_frame, text="Exit",command = self.exit, font=("arial", 15, "bold"), fg="white", bg="grey", width=10).grid(row=0, column=3, padx=7, pady=20)
        self.welcome_bill()
    def total(self):
        self.Tan = self.Tandoori.get()*250
        self.chi = self.Chilly_Chiken.get() * 180
        self.Maj =self.Majestic_Chiken.get() * 220
        self.pep = self.Peper_Chiken.get() * 230
        self.lol = self.Lollypop_Chiken.get() * 280
        self.dry = self.Dry_Chilly.get() * 180
        self.total_staters_price = float((self.Tan)+
                                    ( self.chi)+
                                    (self.Maj)+
                                    (self.pep)+
                                    (self.lol)+
                                    (self.dry)
                                   )
        self.TStater.set("Rs. "+str(self.total_staters_price))
        self.TTax = round((self.total_staters_price * 0.05),2)
        self.TaxStater.set("Rs. "+str(self.TTax))

        self.PB = self.Plain_Briyani.get() * 120
        self.CB = self.Chiken_Briyani.get() * 220
        self.MB = self.Mutton_Briyani.get() * 300
        self.EB = self.Egg_Briyani.get() * 150
        self.DB = self.Dry_CB.get() * 280
        self.FR = self.Fried_Rice.get() * 130

        self.total_Main_course_price = float((self.PB) +
                                         (self.CB) +
                                         (self.MB) +
                                         (self.EB) +
                                         (self.DB) +
                                         (self.FR)
                                         )
        self.TMcourse.set("Rs. "+str(self.total_Main_course_price))
        self.MTax =  round((self.total_Main_course_price * 0.05),2)
        self.TaxMcourse.set("Rs. " + str(self.MTax))

        self.Las = self.Lassy.get() * 70
        self.Ora = self.Orange_Jucie.get() * 80
        self.App = self.Apple_Jucie.get() * 100
        self.Pes = self.Pepsi.get() * 50
        self.Thum = self.Thumpsup.get() * 60
        self.Fru = self.Fruit_Lassy.get() * 50
        self.total_Berverage_price = float((self.Las) +
                                             (self.Ora) +
                                             (self.App) +
                                             (self.Pes) +
                                             (self.Thum) +
                                             (self.Fru)
                                             )
        self.TBrav.set("Rs. "+str(self.total_Berverage_price))
        self.Tbra = round((self.total_Berverage_price * 0.05),2)
        self.TaxBrav.set("Rs. " + str(self.Tbra))

        self.Total_Bill = float(self.total_staters_price+self.total_Main_course_price+self.total_Berverage_price+self.TTax+self.MTax+self.Tbra)

    def welcome_bill(self):
        self.textarea.delete("1.0",END)
        self.textarea.insert(END,"\t  Garlica Invoice")
        self.textarea.insert(END,f"\n Bill Number  : {self.cbillno.get()}")
        self.textarea.insert(END,f"\n Customer Name  : {self.cname.get()}")
        self.textarea.insert(END,f"\n Phone Number  : {self.cphono.get()}")
        self.textarea.insert(END, f"\n=======================================")
        self.textarea.insert(END, f"\n Iteams\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n=======================================")
    def bill_area(self):
        if self.cname.get() == "" or self.cphono.get() == "":
            messagebox.showerror("Customer Details"," Please enter customer details")
        else:
            self.welcome_bill()
            #-------- Staters for bill area
            if self.Tandoori.get()!=0:
                self.textarea.insert(END,f"\n Tandoori\t\t{self.Tandoori.get()}\t\t{self.Tan}")
            if self.Chilly_Chiken.get()!=0:
                self.textarea.insert(END,f"\n Chilly Chiken\t\t{self.Chilly_Chiken.get()}\t\t{self.chi}")
            if self.Majestic_Chiken.get()!=0:
                self.textarea.insert(END,f"\n Majestic Chiken\t\t{self.Majestic_Chiken.get()}\t\t{self.Maj}")
            if self.Peper_Chiken.get()!=0:
                self.textarea.insert(END,f"\n Peper Chiken\t\t{self.Peper_Chiken.get()}\t\t{self.pep}")
            if self.Dry_Chilly.get()!=0:
                self.textarea.insert(END,f"\n Dry Chilly\t\t{self.Dry_Chilly.get()}\t\t{self.dry}")
            if self.Lollypop_Chiken.get()!=0:
                self.textarea.insert(END,f"\n Lollypop Chiken\t\t{self.Lollypop_Chiken.get()}\t\t{self.lol}")

            # -------- Main Course for bill area
            if self.Plain_Briyani.get()!=0:
                self.textarea.insert(END,f"\n Plain Briyani\t\t{self.Plain_Briyani.get()}\t\t{self.PB}")
            if self.Chiken_Briyani.get()!=0:
                self.textarea.insert(END,f"\n Chiken Briyani\t\t{self.Chiken_Briyani.get()}\t\t{self.CB}")
            if self.Mutton_Briyani.get()!=0:
                self.textarea.insert(END,f"\n Mutton Briyani\t\t{self.Mutton_Briyani.get()}\t\t{self.MB}")
            if self.Egg_Briyani.get()!=0:
                self.textarea.insert(END,f"\n Egg Briyani\t\t{self.Egg_Briyani.get()}\t\t{self.EB}")
            if self.Dry_CB.get()!=0:
                self.textarea.insert(END,f"\n Dry CB\t\t{self.Dry_CB.get()}\t\t{self.DB}")
            if self.Fried_Rice.get()!=0:
                self.textarea.insert(END,f"\n Fried Rice\t\t{self.Fried_Rice.get()}\t\t{self.FR}")

            # -------- Berverages for bill area
            if self.Lassy.get() != 0:
                self.textarea.insert(END, f"\n Lassy\t\t{self.Lassy.get()}\t\t{self.Las}")
            if self.Orange_Jucie.get() != 0:
                self.textarea.insert(END, f"\n Orange Jucie\t\t{self.Orange_Jucie.get()}\t\t{self.Ora}")
            if self.Apple_Jucie.get() != 0:
                self.textarea.insert(END, f"\n Apple Jucie\t\t{self.Apple_Jucie.get()}\t\t{self.App}")
            if self.Pepsi.get() != 0:
                self.textarea.insert(END, f"\n Pepsi\t\t{self.Pepsi.get()}\t\t{self.Pes}")
            if self.Thumpsup.get() != 0:
                self.textarea.insert(END, f"\n Thumpsup\t\t{self.Thumpsup.get()}\t\t{self.Thum}")
            if self.Fruit_Lassy.get() != 0:
                self.textarea.insert(END, f"\n Fruit Lassy\t\t{self.Fruit_Lassy.get()}\t\t{self.Fru}")

            self.textarea.insert(END, f"\n--------------------------------------")
            if self.TaxStater.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Staters Tax\t\t\t{self.TaxStater.get()}")
            if self.TaxMcourse.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Main Course Tax \t\t\t{self.TaxMcourse.get()}")
            if self.TaxBrav.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Beverages Tax \t\t\t{self.TaxBrav.get()}")

            self.textarea.insert(END, f"\n--------------------------------------")
            self.textarea.insert(END,f"\n Total \t\t\t Rs. {self.Total_Bill}")
            self.textarea.insert(END, f"\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        key = messagebox.askyesno("Bill","Do you want to save the bill")
        if key > 0:
            self.billdata = self.textarea.get(1.0,END)
            file = open(r"C:\Users\Murugappa\Desktop\bills/"+str(self.cbillno.get())+".txt","w")
            file.write(self.billdata)
            file.close()
            messagebox.showinfo("Saved", f"Bill no : {self.cbillno.get()} saved successfully")
        else:
            return
    def search(self):
        for i in os.listdir(r"C:\Users\Murugappa\Desktop\bills/"):
            print(i)

    def clear(self):
        key = messagebox.askyesno("Clear","Do you want to clear?")
        if key > 0:
            self.Tandoori.set(0)
            self.Chilly_Chiken.set(0)
            self.Majestic_Chiken.set(0)
            self.Peper_Chiken.set(0)
            self.Lollypop_Chiken.set(0)
            self.Dry_Chilly.set(0)

            # -------Main course--------

            self.Plain_Briyani.set(0)
            self.Chiken_Briyani.set(0)
            self.Mutton_Briyani.set(0)
            self.Egg_Briyani.set(0)
            self.Dry_CB.set(0)
            self.Fried_Rice.set(0)

            # -------Berverages--------

            self.Lassy.set(0)
            self.Orange_Jucie.set(0)
            self.Apple_Jucie.set(0)
            self.Pepsi.set(0)
            self.Thumpsup.set(0)
            self.Fruit_Lassy.set(0)

            # -------Total and Tax of the Iteams--------

            self.TStater.set(" ")
            self.TMcourse.set(" ")
            self.TBrav.set(" ")

            self.TaxStater.set(" ")
            self.TaxMcourse.set(" ")
            self.TaxBrav.set(" ")

            # -------Customer Details--------

            self.cname.set(" ")
            self.cphono.set(" ")

            self.cbillno.set(" ")
            x = random.randint(1000, 9999)
            self.cbillno.set(str(x))

            self.search.set(" ")
        else:
            return
    def exit(self):
        key = messagebox.askyesno("Clear","Do you want to exit?")
        if key > 0:
            self.screen.destroy()
        else:
            return

screen = Tk()
object = Bill_App(screen)
screen.mainloop()