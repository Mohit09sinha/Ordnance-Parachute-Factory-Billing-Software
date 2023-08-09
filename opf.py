from ast import Delete
from ipaddress import collapse_addresses
from time import strftime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import COLUMN
from PIL import Image,ImageTk
import random,os
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Ordnance Parachute Factory Billing Software")
        
        #Variables
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.com_name=StringVar()
        self.c_ord=StringVar()
        self.c_del=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
       
        
        #Product Categories List
        self.category=["Select Option","Parachute","Boat","Clothes"]
        
        #SubCatClothing
        self.SubCatParachute=["Man_Carrying_Parachutes","Cargo_Parachutes","Brake_Parachutes","Pilot_Parachutes","Other_Parachutes"]
        
        self.Man_Carrying_Parachutes=["PTA_M","PTA_R","PTR_R","High_Altitude_Parachute","Ram_Air_9_Cell_Para"]
        self.price_PTA_M=20000
        self.price_PTA_R=21000
        self.price_PTR_R=22000
        self.price_High_Altitude_Parachute=19000
        self.price_Ram_Air_9_Cell_Para=18000
        
        self.Cargo_Parachutes=["Supply_Drop_Parachute","Heavy_Drop_Parachute"]
        self.price_Supply_Drop_Parachute=15000
        self.price_Heavy_Drop_Parachute=18000
        
        self.Brake_Parachutes=["SU30_Aircraft","MiG21_Aircraft","MiG23_Aircraft","MiG29_Aircraft","Jaguar_Aircraft"]
        self.price_SU30_Aircraft=21000
        self.price_MiG21_Aircraft=27000
        self.price_MiG23_Aircraft=18000
        self.price_MiG29_Aircraft=19000
        self.price_Jaguar_Aircraft=20000
        
        self.Pilot_Parachutes=["Kiran_Aircraft"]
        self.price_Kiran_Aircraft=15000
        
        self.Other_Parachutes=["Parasail","Illuminating_Ammunition"]
        self.price_Parasail=16000
        self.price_Illuminating_Ammunition=18000
        
        
        #SubCatLifeStyle
        self.SubCatBoat=["BAPLW","KM_Float","Gemini_Craft"]
        
        self.BAPLW=["BAPLW"]
        self.price_BAPLW=25000
        
        self.KM_Float=["KM_Float"]
        self.price_KM_Float=18000
        
        self.Gemini_Craft=["Gemini_Craft"]
        self.price_Gemini_Craft=19000
       
        self.SubCatClothes=["Danger_Building_Coat","Danger_Building_Trouser","Pohcho_Glacier","NBC_Suit","Waterproof_Rain_Poncho"]
        
        self.Danger_Building_Coat=["Danger_Building_Coat"]
        self.price_Danger_Building_Coat=15000
        
        self.Danger_Building_Trouser=["Danger_Building_Trouser"]
        self.price_Danger_Building_Trouser=15000
        self.Pohcho_Glacier=["Pohcho_Glacier"]
        self.price_Pohcho_Glacier=22000
        self.NBC_Suit=["NBC_Suit"]
        self.price_NBC_Suit=20000
        self.Waterproof_Rain_Poncho=["Waterproof_Rain_Poncho"]
        self.price_Waterproof_Rain_Poncho=18000
        
        #ofbsymbol
        img01=Image.open("Images/ofb.webp")
        img01=img01.resize((125,140),Image.ANTIALIAS)
        self.photoimage01=ImageTk.PhotoImage(img01)
        lbl_img01=Label(self.root,image=self.photoimage01)
        lbl_img01.place(x=0,y=0,width=125,height=140)
        
        #gliders
        img=Image.open("Images/opf.png")
        img=img.resize((1525,140),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimage)
        lbl_img.place(x=125,y=0,width=1250,height=140)
        
        #opf
        img_12=Image.open("Images/parac.jpg")
        img_12=img_12.resize((155,140),Image.ANTIALIAS)
        self.photoimage_12=ImageTk.PhotoImage(img_12)
        lbl_img_12=Label(self.root,image=self.photoimage_12)
        lbl_img_12.place(x=1375,y=0,width=155,height=140)
        
        lbl_title=Label(self.root,text="ORDNANCE PARACHUTE FACTORY BILLING SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=140,width=1525,height=33)
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(lbl_title,font=('times new roman',16,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-8),width=120,height=45)
        time()
        
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)
        
        #Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",15,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=355,height=245)
        
        self.lblCustname=Label(Cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCustname.grid(row=0,column=0,stick=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=1,column=0,stick=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=1,column=1)
        
        self.lblEmail=Label(Cust_Frame,text="Email id.",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)
        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        self.lblCompname=Label(Cust_Frame,text="Company Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCompname.grid(row=3,column=0,stick=W,padx=5,pady=2)
        self.txtCompname=ttk.Entry(Cust_Frame,textvariable=self.com_name,font=("arial",10,"bold"),width=24)
        self.txtCompname.grid(row=3,column=1,sticky=W,padx=5,pady=2)
        
        self.lblOrdate=Label(Cust_Frame,text="Order Date",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblOrdate.grid(row=4,column=0,stick=W,padx=5,pady=2)
        self.txtOrdate=ttk.Entry(Cust_Frame,textvariable=self.c_ord,font=("arial",10,"bold"),width=24)
        self.txtOrdate.grid(row=4,column=1,sticky=W,padx=5,pady=2)
        
        self.lblDeldate=Label(Cust_Frame,text="Delivery Date",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblDeldate.grid(row=5,column=0,stick=W,padx=5,pady=2)
        self.txtDeldate=ttk.Entry(Cust_Frame,textvariable=self.c_del,font=("arial",10,"bold"),width=24)
        self.txtDeldate.grid(row=5,column=1,sticky=W,padx=5,pady=2)
        
        #Product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",15,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=245)
        
        #Category
        self.lblCategory=Label(Product_Frame,text="Select Categories",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)        
        
        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)        
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)
        
        #Sub Category
        self.lblSubCategory=Label(Product_Frame,text="Subcategory",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)        
        
        self.Combo_SubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)        
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)
        
        #Product Name
        self.lblproduct=Label(Product_Frame,text="Product Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)        
        
        self.Combo_Product=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Product.grid(row=2,column=1,sticky=W,padx=5,pady=2)        
        self.Combo_Product.bind("<<ComboboxSelected>>",self.Price)
        
        #Price
        self.lblPrice=Label(Product_Frame,text="Price",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)        
        
        self.Combo_Price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Price.grid(row=0,column=3,sticky=W,padx=5,pady=2)        
        
        #Qty
        self.lblQty=Label(Product_Frame,text="Qty",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)        
        
        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)        
                
        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10,bg="orange")
        MiddleFrame.place(x=10,y=252,width=979,height=250)
        
        #Image1
        img71=Image.open("Images/indpara1.jpg")
        img71=img71.resize((218,225),Image.ANTIALIAS)
        self.photoimage71=ImageTk.PhotoImage(img71)
        lbl_img71=Label(MiddleFrame,image=self.photoimage71)
        lbl_img71.place(x=-6.5,y=-4.5,width=218,height=225)

        #Image2
        img11=Image.open("Images/make.jpg")
        img11=img11.resize((531,225),Image.ANTIALIAS)
        self.photoimage11=ImageTk.PhotoImage(img11)
        lbl_img11=Label(MiddleFrame,image=self.photoimage11)
        lbl_img11.place(x=213.5,y=-4.5,width=531,height=225)
        
        #Image3
        img_22=Image.open("Images/indpara2.jpg")
        img_22=img_22.resize((218,225),Image.ANTIALIAS)
        self.photoimage_22=ImageTk.PhotoImage(img_22)
        lbl_img_22=Label(MiddleFrame,image=self.photoimage_22)
        lbl_img_22.place(x=747.5,y=-4.5,width=218,height=225)
    
        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=15,width=500,height=40)
        
        self.lblBill=Label(Search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)        
        
        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)
        
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)
        
        #RightFrame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)
        
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        #Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)
        
        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)        
        
        self.EntySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=24)
        self.EntySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        self.lbl_Tax=Label(Bottom_Frame,text="Gov. Tax",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_Tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)        
        
        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.lblAmountTotal=Label(Bottom_Frame,text="Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)        
        
        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",10,"bold"),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)
        
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)
        
        self.BtnGenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnGenerate_bill.grid(row=0,column=1)
        
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)
        
        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)
        
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)
        
        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()
        
        self.l=[]
     #================Function Declaration==========================
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t               Ordnance Parachute Factory       ")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()} ")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()} ")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")
        self.textarea.insert(END,f"\n Company Name:{self.com_name.get()}")
        self.textarea.insert(END,f"\n Order Date:{self.c_ord.get()}")
        self.textarea.insert(END,f"\n Delivery Date:{self.c_del.get()}")
        self.textarea.insert(END,"\n==============================================")
        self.textarea.insert(END,f"\n Products\t\t\tQty\t\tPrice")
        self.textarea.insert(END,"\n==============================================\n")
    
    def AddItem(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select The Product Name")
        else:
            Tax=1
            self.n=self.prices.get()
            self.m=self.qty.get()*self.n
            self.l.append(self.m)
            self.textarea.insert(END,f"\n{self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))            
            self.total.set(str("Rs.%.2f"%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100))))) 
    
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add Product To The Cart")
        else:
            text=self.textarea.get(13.0,(13.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ==============================================")
            self.textarea.insert(END,f"\n Sub Amount: \t\t\t{self.sub_total.get()} ")
            self.textarea.insert(END,f"\n Tax Amount: \t\t\t{self.tax_input.get()} ")
            self.textarea.insert(END,f"\n Total Amount: \t\t\t{self.total.get()} ")
            self.textarea.insert(END,"\n==============================================")
            
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Want To Save The Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill no:{self.bill_no.get()} Saved Successfully")
        
            f1.close()
              
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
        
    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
                messagebox.showerror("Error","Invalid Bill No.")
    
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(x)
        self.c_email.set("")
        self.com_name.set("")
        self.c_ord.set("")
        self.c_del.set("")
        self.search_bill.set("")
        self.product.set("")
        self.l=[0]
        self.prices.set("")
        self.qty.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome() 
    
    def Categories(self,event=""):
        
        if self.Combo_Category.get()=="Parachute":
            self.Combo_SubCategory.config(value=self.SubCatParachute)
            self.Combo_SubCategory.current(0)
        
        if self.Combo_Category.get()=="Boat":
            self.Combo_SubCategory.config(value=self.SubCatBoat)
            self.Combo_SubCategory.current(0)
        
        if self.Combo_Category.get()=="Clothes":
            self.Combo_SubCategory.config(value=self.SubCatClothes)
            self.Combo_SubCategory.current(0)     
            
    def Product_add(self,event=""):
        if self.Combo_SubCategory.get()=="Man_Carrying_Parachutes":
            self.Combo_Product.config(value=self.Man_Carrying_Parachutes)
            self.Combo_Product.current(0)
            
        if self.Combo_SubCategory.get()=="Cargo_Parachutes":
            self.Combo_Product.config(value=self.Cargo_Parachutes)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Brake_Parachutes":
            self.Combo_Product.config(value=self.Brake_Parachutes)
            self.Combo_Product.current(0)
            
        if self.Combo_SubCategory.get()=="Pilot_Parachutes":
            self.Combo_Product.config(value=self.Pilot_Parachutes)
            self.Combo_Product.current(0)
            
        if self.Combo_SubCategory.get()=="Other_Parachutes":
            self.Combo_Product.config(value=self.Other_Parachutes)
            self.Combo_Product.current(0)
            
        if self.Combo_SubCategory.get()=="BAPLW":
            self.Combo_Product.config(value=self.BAPLW)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="KM_Float":
            self.Combo_Product.config(value=self.KM_Float)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Gemini_Craft":
            self.Combo_Product.config(value=self.Gemini_Craft)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Danger_Building_Coat":
            self.Combo_Product.config(value=self.Danger_Building_Coat)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Danger_Building_Trouser":
            self.Combo_Product.config(value=self.Danger_Building_Trouser)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Pohcho_Glacier":
            self.Combo_Product.config(value=self.Pohcho_Glacier)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="NBC_Suit":
            self.Combo_Product.config(value=self.NBC_Suit)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Waterproof_Rain_Poncho":
            self.Combo_Product.config(value=self.Waterproof_Rain_Poncho)
            self.Combo_Product.current(0)
             
    def Price(self,event=""):
        if self.Combo_Product.get()=="PTA_M":
            self.Combo_Price.config(value=self.price_PTA_M)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="PTA_R":
            self.Combo_Price.config(value=self.price_PTA_R)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="PTR_R":
            self.Combo_Price.config(value=self.price_PTR_R)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="High_Altitude_Parachute":
            self.Combo_Price.config(value=self.price_High_Altitude_Parachute)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Ram_Air_9_Cell_Para":
            self.Combo_Price.config(value=self.price_Ram_Air_9_Cell_Para)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Supply_Drop_Parachute":
            self.Combo_Price.config(value=self.price_Supply_Drop_Parachute)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Heavy_Drop_Parachute":
            self.Combo_Price.config(value=self.price_Heavy_Drop_Parachute)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="SU30_Aircraft":
            self.Combo_Price.config(value=self.price_SU30_Aircraft)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="MiG21_Aircraft":
            self.Combo_Price.config(value=self.price_MiG21_Aircraft)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="MiG23_Aircraft":
            self.Combo_Price.config(value=self.price_MiG23_Aircraft)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="MiG29_Aircraft":
            self.Combo_Price.config(value=self.price_MiG29_Aircraft)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Jaguar_Aircraft":
            self.Combo_Price.config(value=self.price_Jaguar_Aircraft)
            self.Combo_Price.current(0)
            self.qty.set(1)
         
        if self.Combo_Product.get()=="Kiran_Aircraft":
            self.Combo_Price.config(value=self.price_Kiran_Aircraft)
            self.Combo_Price.current(0)
            self.qty.set(1)
          
        if self.Combo_Product.get()=="Parasail":
            self.Combo_Price.config(value=self.price_Parasail)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Illuminating_Ammunition":
            self.Combo_Price.config(value=self.price_Illuminating_Ammunition)
            self.Combo_Price.current(0)
            self.qty.set(1)
             
        if self.Combo_Product.get()=="BAPLW":
            self.Combo_Price.config(value=self.price_BAPLW)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="KM_Float":
            self.Combo_Price.config(value=self.price_KM_Float)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Gemini_Craft":
            self.Combo_Price.config(value=self.price_Gemini_Craft)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_Product.get()=="Danger_Building_Coat":
            self.Combo_Price.config(value=self.price_Danger_Building_Coat)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Danger_Building_Trouser":
            self.Combo_Price.config(value=self.price_Danger_Building_Trouser)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Pohcho_Glacier":
            self.Combo_Price.config(value=self.price_Pohcho_Glacier)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="NBC_Suit":
            self.Combo_Price.config(value=self.price_NBC_Suit)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Waterproof_Rain_Poncho":
            self.Combo_Price.config(value=self.price_Waterproof_Rain_Poncho)
            self.Combo_Price.current(0)
            self.qty.set(1)   
        
if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
    