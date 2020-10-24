from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from Back_end.working import Connection
from model_class.model import *
import pygame
from string import *
class Main_interface():
    '''
    This is a class that configures and populates the main tkinter window.
    Attributes:
        root: This supports the Tk() {Toplevel window}
    '''
    def __init__(self,root):
        '''
        This constructor is for Main_interface class.
        :param
            root: It supports the Tk() {Toplevel window}
        '''
        self.wn = root
        self.wn.title("Restaurant Management System")
        self.wn.geometry('830x650+253+24')
        self.wn.attributes('-a',0.97)
        self.wn.resizable(0,0)
        self.wn.iconbitmap('index.ico')
        self.wn.config(bg="#eb3d34")
        self.normal_font = "-family Corbel -size 12"
        self.slogan_font = "-family {Tempus Sans ITC} -size 12"
        self.title_font = "-family {Century Gothic} -size 24 -slant italic"
        self.other_font = "-family Times -size 15"
        try:
            self.dbconnect = Connection()
        except Exception:
            messagebox.showerror('Error', 'Cannot connect to the database')
            self.wn.forget(root)
        else:
            self.getstarted= Frame(self.wn)
            self.getstarted.pack(fill=BOTH)
            self.photo1 = PhotoImage(file="getstart.png")
            getimage = Label(self.getstarted, image=self.photo1, background="#eb3d34", foreground="#eb3d34")
            getimage.pack(fill= BOTH)
            lblgetstarted= Label(self.getstarted, text="Get Started", background="#eb3d34", foreground="white"
                                 , cursor='hand1', font=self.other_font, width=300)
            lblgetstarted.bind("<Button-1>", self.validating)
            lblgetstarted.place(relx=0.800, rely=0.850, height=50, width=100)
            self.username = StringVar()
            self.password = StringVar()
            self.staffID = StringVar()
            self.Name = StringVar()
            self.staff_age = StringVar()
            self.gender = StringVar()
            self.Address = StringVar()
            self.email = StringVar()
            self.contact = StringVar()
            self.post = StringVar()
            self.foodID = StringVar()
            self.food1 = StringVar()
            self.foodprice1 = StringVar()
            self.customerID = StringVar()
            self.customer_name = StringVar()
            self.customer_Age = StringVar()
            self.combo_gender_customer_setting = StringVar()
            self.customer_address= StringVar()
            self.customer_email = StringVar()
            self.customer_contact= StringVar()
            self.foodchoice = StringVar()
            self.food_order_standard = StringVar()
            self.customer_order_standard = StringVar()
            self.staff_order_standard = StringVar()
            pygame.mixer.init()
            pygame.mixer.music.load('River Flows in You.mp3')
            pygame.mixer.music.play(-1)
    def validating(self, *args):
        """
        This deals with the validation of checking whether there are users or not.
        If there is it opens login page otherwise registration page gets opened.
        :return None
        """
        query = 'select * from users;'
        records1 = self.dbconnect.select(query)
        if records1:
            self.login_frame()
        else:
            self.admin_registration1()
    def login_frame(self, *args):
        """
        Login interface designing.
        :return None
        """
        entry ="-family Corbel -size 10"
        self.getstarted.pack_forget()
        self.main_frame = Frame(self.wn, bg="#eb3d34")
        self.main_frame.place(relx=0, rely=0, width=830, height=650)
        title = Label(self.main_frame, text="Restaurant Management System", bg="#eb3d34", font=self.title_font)
        title.pack(side=TOP)
        usern_lbl1 = Label(self.main_frame, text="Welcome", bg="#eb3d34",font= self.other_font, cursor= "xterm")
        usern_lbl1.place(relx=0.7, rely=0.400, height=49, width=151)
        usern_lbl2 = Label(self.main_frame, text='Username', bg="#eb3d34", font= self.normal_font, cursor="xterm")
        usern_lbl2.place(relx=0.651, rely=0.524, height=22, width=73)
        self.usern_ent2 = ttk.Entry(self.main_frame, font=entry, textvariable=self.username)
        self.usern_ent2.place(relx=0.760, rely=0.524,relheight=0.040, relwidth=0.200)
        self.usern_ent2.focus()
        pass_lbl3 = Label(self.main_frame, text="Password", bg="#eb3d34", font=self.normal_font, cursor="xterm")
        pass_lbl3.place(relx=0.656, rely=0.590, height=21, width=63)
        self.pass_ent3 = ttk.Entry(self.main_frame, show="*", font=entry, textvariable=self.password)
        self.pass_ent3.place(relx=0.760, rely=0.590,relheight=0.040, relwidth=0.200)
        trouble_login = Label(self.main_frame,text="Having Trouble?" ,cursor='hand2', bg="#eb3d34",
                              font = self.normal_font)
        trouble_login.bind("<Button-1>",self.help_window)
        trouble_login.place(relx=0.844, rely=0.646, height=31, width=110)
        loginbtn = ttk.Button(self.main_frame, text= "LOGIN", command= self.validation, takefocus='')
        loginbtn.place(relx=0.75, rely=0.720, height=45, width=186)
        loginbtn.bind('<Return>', lambda e: self.validation())
        self.logo = ImageTk.PhotoImage(Image.open("logo.png"))
        loginlbl1 = Label(self.main_frame, image=self.logo, bg="#eb3d34")
        loginlbl1.place(relx=0.676, rely=0.130, height=175, width=175)
        self.side = ImageTk.PhotoImage(Image.open("loginpage.png"))
        sidelbl = Label(self.main_frame, image=self.side, bg="#eb3d34")
        sidelbl.place(relx=0, rely=0.120, height=480, width=480)
        sloganlbl = Label(self.main_frame, text=
        'Only one thing can deal with bad day or mood swings? Just peek into look to our menu first 😍...', bg="#eb3d34"
                          ,font= self.other_font)
        sloganlbl.place(relx= 0, rely=0.908, width= 830)
    def clear_login(self):
        """Clearing login interface entries.
        :return None
        """
        self.username.set('')
        self.password.set('')
    def help_window(self, *args):
        """"Shows information for one who are in trouble to log in
        :return None
        """
        messagebox.showinfo("Contact !", "Please contact system administrator for help.")
    def validation(self):
        """For logging in by checking whether they are registered or not.
        :return None
        """
        a=self.usern_ent2.get()
        b=self.pass_ent3.get()
        query = "select * from users where username=%s;"
        values= (a,)
        records=self.dbconnect.selectuser(query,values)
        if records:
            if a==records[1] and b==records[2]:
                    messagebox.showinfo('Success','Login Successful')
                    self.dashboard()
                    self.clear_login()
            else:
                    messagebox.showinfo('Error','Invalid username and password')
                    self.clear_login()
        else:
            if a=="" or b=="":
                messagebox.showwarning("Warning", "Please enter the required credentials")
            else:
                messagebox.showinfo("Error",'No such username exists')
                self.clear_login()

    def admin_registration1(self):
        """Registration interface designing.
        :return None
        """
        entry = "-family Corbel -size 10"
        self.admin_registration_frame_first = Frame(self.wn, bg='#eb3d34')
        self.admin_registration_frame_first.place(relx=0, rely=0, width=830, height=650)
        lbl_heading_admin = Label(self.admin_registration_frame_first, text="ADMIN REGISTRATION", bg='#eb3d34',
                                  font=self.title_font)
        lbl_heading_admin.pack(side=TOP)
        lbl_userid = Label(self.admin_registration_frame_first, text='User ID', bg='#eb3d34', font=self.normal_font)
        lbl_userid.place(relx=0.020, rely=0.769, height=22, width=73)
        self.ent_userid1_first = ttk.Entry(self.admin_registration_frame_first, font=entry, takefocus="")
        self.ent_userid1_first.place(relx=0.096, rely=0.769, relheight=0.040, relwidth=0.200)
        self.ent_userid1_first.focus()
        lbl_username = Label(self.admin_registration_frame_first, text='Username', bg='#eb3d34', font=self.normal_font)
        lbl_username.place(relx=0.350, rely=0.769, height=22, width=73)
        self.ent_username1_first = ttk.Entry(self.admin_registration_frame_first, font=entry)
        self.ent_username1_first.place(relx=0.440, rely=0.769, relheight=0.040, relwidth=0.200)
        lbl_password = Label(self.admin_registration_frame_first, text='Password', bg="#eb3d34", font=self.normal_font)
        lbl_password.place(relx=0.688, rely=0.769, height=22, width=73)
        self.ent_password1_first = ttk.Entry(self.admin_registration_frame_first, font=entry, show='*')
        self.ent_password1_first.place(relx=0.780, rely=0.769, relheight=0.040, relwidth=0.200)
        btn_register = ttk.Button(self.admin_registration_frame_first, text='Register', command=self.add_admin_first)
        btn_register.place(relx=0.422, rely=0.830, height=35, width=106)
        photo_frame = Frame(self.admin_registration_frame_first, bg="#eb3d34")
        photo_frame.place(relx=0.108, rely=0.108, height=405, width=830)
        self.regframe_1 = PhotoImage(file="restaurant.png")
        bg_label = Label(self.admin_registration_frame_first, image=self.regframe_1, bg='#eb3d34')
        bg_label.pack(fill=BOTH)
    def clear1_first(self):
        """Clearing entries of admin registration.
        :return None
        """
        self.ent_userid1_first.delete(0, END)
        self.ent_username1_first.delete(0, END)
        self.ent_password1_first.delete(0, END)

    def add_admin_first(self):
        """Adding the admin into the database.
        :return None
        """
        admin = Admin(self.ent_userid1_first.get(), (self.ent_username1_first.get()), self.ent_password1_first.get())
        if self.ent_userid1_first.get() == '' or self.ent_username1_first.get() == '' or self.ent_password1_first.get() == '':
            messagebox.showwarning("Warning", "Please enter all credentials")
        elif not self.ent_userid1_first.get().isdigit():
            messagebox.showwarning("Warning", " ID should always be a number.")
            self.ent_userid1_first.delete(0, END)
        elif len(self.ent_userid1_first.get()) > 6:
            messagebox.showwarning("Warning", "User ID can only be 6 characters long.")
            self.ent_userid1_first.delete(0, END)
        elif len(self.ent_username1_first.get()) < 4 or len(self.ent_username1_first.get()) > 40:
            messagebox.showwarning("Warning", "Username must be atleast 4 to 40 characters long.")
            self.ent_username1_first.delete(0, END)
        elif len(self.ent_password1_first.get()) < 6 or len(self.ent_password1_first.get()) > 40:
            messagebox.showwarning("Warning", "Password must be atleast 6 to 40 characters long.")
            self.ent_password1_first.delete(0, END)
        elif re.search('[0-9]', self.ent_password1_first.get()) is None:
            messagebox.showwarning("Warning", "Password must contain a number.")
        elif re.search('[A-Z]', self.ent_password1_first.get()) is None:
            messagebox.showwarning("Warning", "Password must contain a capital letter.")
        elif re.search('[-=+_)(*&^%$#@!~`<>:.?,;]', self.ent_password1_first.get()) is None:
            messagebox.showwarning("Warning", "Password must contain a special symbol.")
        else:
            query = "select * from users where userid=%s;"
            values = (int(self.ent_userid1_first.get()),)
            records = self.dbconnect.selectuser(query, values)
            if records:
                messagebox.showwarning("Warning", "User ID already Exists. ")
                self.ent_userid1_first.delete(0, END)
            else:
                query = 'insert into users values(%s,%s,%s);'
                values = (int(admin.get_user_id()), admin.get_user_name1(), admin.get_password1())
                self.dbconnect.insert(query, values)
                messagebox.showinfo('Success', "Admin registered Successfully")
                self.login_frame()
                self.clear1_first()

    def dashboard(self):
        """
        Design of dashboard.
        :return None
        """
        self.main_frame.place_forget()
        self.dash_frame = Frame(self.wn, bg="#eb3d34")
        self.dash_frame.place(relx=0, rely=0, width=830, height=650)
        self.text_font = "-family Courier -size 10"
        self.dashboard_img = PhotoImage(file='dashboard1.png')
        label_dashboard_img = Label(self.dash_frame, bg="#eb3d34", image=self.dashboard_img)
        label_dashboard_img.place(relx=0.07, rely=0.08)
        title = Label(self.dash_frame, text="Welcome To The Dashboard", bg="#eb3d34", font=self.title_font)
        title.pack(side=TOP)
        self.customer = PhotoImage(file="customer.png")
        self.btn_customer = Button(self.dash_frame, text='Customer', font=self.slogan_font, image=self.customer,
                                   compound='top', bg="#eb3d34", command=self.customer_interface, border=0)
        self.btn_customer.place(relx=0.71, rely=0.06, height=195, width=227)
        self.backbtn = Button(self.dash_frame, text= 'Back', font=self.slogan_font, bg="#eb3d34", border=0, command=self.login_frame, cursor="hand2")
        self.backbtn.place(relx=0.02, rely=0.01)
        self.chef = PhotoImage(file="chef.png")
        self.btn_employee = Button(self.dash_frame, text='Employee', image=self.chef, compound="top", bg="#eb3d34",
                                   font=self.slogan_font, command=self.staffs_interface, border=0)
        self.btn_employee.place(relx=0.71, rely=0.37, height=195, width=227)
        self.menu = PhotoImage(file="menu.png")
        self.btn_menu = Button(self.dash_frame, text='Menu', font=self.slogan_font, image=self.menu, compound="top",
                               bg="#eb3d34", command=self.food_interface, border=0)
        self.btn_menu.place(relx=0.71, rely=0.69, height=195, width=227)
        self.regis = PhotoImage(file="regisbtn.png")
        self.btn_regis = Button(self.dash_frame, text='Admin Registration', font=self.slogan_font, image=self.regis, compound="top",
                               bg="#eb3d34", command=self.admin_registration, border=0)
        self.btn_regis.place(relx=0.440, rely=0.755, height=160, width=150)
    def admin_registration(self, *args):
        entry = "-family Corbel -size 10"
        self.admin_registration_frame = Frame(self.wn, bg='#eb3d34')
        self.admin_registration_frame.place(relx=0, rely=0, width=830, height=650)
        lbl_heading_admin = Label(self.admin_registration_frame, text="ADMIN REGISTRATION", bg='#eb3d34',
                                  font=self.title_font)
        lbl_heading_admin.pack(side= TOP)
        lbl_userid = Label(self.admin_registration_frame, text='User ID', bg='#eb3d34', font=self.normal_font)
        lbl_userid.place(relx=0.020, rely=0.769, height=22, width=73)
        self.ent_userid1 = ttk.Entry(self.admin_registration_frame, font=entry, takefocus="")
        self.ent_userid1.place(relx=0.096, rely=0.769,relheight=0.040, relwidth=0.200)
        self.ent_userid1.focus()
        lbl_username = Label(self.admin_registration_frame, text='Username', bg='#eb3d34', font=self.normal_font)
        lbl_username.place(relx=0.350, rely=0.769, height=22, width=73)
        self.ent_username1 = ttk.Entry(self.admin_registration_frame, font=entry)
        self.ent_username1.place(relx=0.440, rely=0.769,relheight=0.040, relwidth=0.200)
        lbl_password = Label(self.admin_registration_frame, text='Password', bg="#eb3d34", font=self.normal_font)
        lbl_password.place(relx=0.688, rely=0.769, height=22, width=73)
        self.ent_password1 = ttk.Entry(self.admin_registration_frame, font=entry, show='*')
        self.ent_password1.place(relx=0.780, rely=0.769,relheight=0.040, relwidth=0.200)
        btn_register = ttk.Button(self.admin_registration_frame, text='Register', command=self.add_admin)
        btn_register.place(relx=0.422, rely=0.830, height=35, width=106)
        photo_frame= Frame(self.admin_registration_frame, bg="#eb3d34")
        photo_frame.place(relx=0.108, rely=0.108, height=405, width=830)
        self.regframe_1 = PhotoImage(file="restaurant.png")
        bg_label = Label(self.admin_registration_frame, image=self.regframe_1, bg='#eb3d34')
        bg_label.pack(fill=BOTH)
        btn_exit_dept = ttk.Button(self.admin_registration_frame, text='Back',command=self.dashboard)
        btn_exit_dept.place(relx=0.006, rely=0.955)
    def clear1(self):
        self.ent_userid1.delete(0, END)
        self.ent_username1.delete(0, END)
        self.ent_password1.delete(0, END)
    def add_admin(self):
        admin = Admin(self.ent_userid1.get(), self.ent_username1.get(), self.ent_password1.get())
        if self.ent_userid1.get() == '' or self.ent_username1.get() == '' or self.ent_password1.get() == '':
            messagebox.showwarning("Warning", "Please enter all credentials")
        elif not self.ent_userid1.get().isdigit():
            messagebox.showwarning("Warning", " ID should always be a number.")
            self.ent_userid1.delete(0, END)
        elif len(self.ent_userid1.get()) > 6:
            messagebox.showwarning("Warning", "User ID can only be 6 characters long.")
            self.ent_userid1.delete(0, END)
        elif len(self.ent_username1.get()) < 4 or len(self.ent_username1.get()) > 40:
            messagebox.showwarning("Warning", "Username must be atleast 4 to 40 characters long.")
            self.ent_username1.delete(0, END)
        elif len(self.ent_password1.get()) < 6 or len(self.ent_password1.get()) > 40:
            messagebox.showwarning("Warning", "Password must be atleast 6 to 40 characters long.")
            self.ent_password1.delete(0, END)
        elif re.search('[0-9]', self.ent_password1.get()) is None:
            messagebox.showwarning("Warning", "Password must contain a number.")
        elif re.search('[A-Z]', self.ent_password1.get()) is None:
            messagebox.showwarning("Warning", "Password must contain a capital letter.")
        elif re.search('[-=+_)(*&^%$#@!~`<>:.?,;]', self.ent_password1.get()) is None:
            messagebox.showwarning("Warning", "Password must contain a special symbol.")
        else:
            query = "select * from users where userid=%s;"
            values = (int(self.ent_userid1.get()),)
            records = self.dbconnect.selectuser(query, values)
            if records:
                messagebox.showwarning("Warning", "User ID already Exists. ")
                self.ent_userid1.delete(0, END)
            else:
                query = 'insert into users values(%s,%s,%s);'
                values = (int(admin.get_user_id()), admin.get_user_name1(), admin.get_password1())
                self.dbconnect.insert(query, values)
                messagebox.showinfo('Success', "Admin registered Successfully")
                self.clear1()
    def staffs_interface(self):
        """
        Staffs/ Employee interface is designed here.
        :return None
        """
        self.emp_frame = Frame(self.wn, bg="#eb3d34")
        self.emp_frame.place(relx=0, rely=0, width=830, height=650)
        normal_font_staff= "-family Corbel -size 15"
        title_frame_staff = Frame(self.emp_frame, bg="#eb3d34")
        title_frame_staff.place(relx=-0.0, rely=0.0, relheight=0.131, relwidth=1.007)
        title_staff = Label(title_frame_staff, text="Staff Management", bg="#eb3d34", font=self.title_font)
        title_staff.place(relx=0.275, rely=0.110, height=71, width=434)
        self.staff_img = PhotoImage(file='staffs.png')
        label_staff_img = Label(self.emp_frame, bg="#eb3d34", image=self.staff_img)
        label_staff_img.place(relx=0.40, rely=0.30)
        detail_frame_staff= Frame(self.emp_frame,bg="#eb3d34")
        detail_frame_staff.place(relx = 0.0, rely = 0.138, relheight = 0.852, relwidth = 0.367)
        lbl_staffID = Label(detail_frame_staff, text='Staff ID', bg='#eb3d34', font=normal_font_staff)
        lbl_staffID.grid(row=0, column=0, padx=5, pady=10)
        self.ent_staffID = Entry(detail_frame_staff,width=15, font=normal_font_staff,textvariable=self.staffID)
        self.ent_staffID.grid(row=0, column=1, padx=5, pady=10)
        self.ent_staffID.focus()
        self.staffID.trace_variable("w", self.input_validation_staffid)
        lbl_Name = Label(detail_frame_staff, text='Name', bg='#eb3d34', font=normal_font_staff)
        lbl_Name.grid(row=1, column=0, padx=5, pady=10)
        self.ent_Name = Entry(detail_frame_staff,width=15, font=normal_font_staff,textvariable=self.Name)
        self.ent_Name.grid(row=1, column=1, padx=5, pady=10)
        self.Name.trace_variable("w", self.validation_staff_name)
        lbl_age = Label(detail_frame_staff, text='Age', bg='#eb3d34', font=normal_font_staff)
        lbl_age.grid(row=2, column=0, padx=5, pady=10)
        self.ent_staff_age = Entry(detail_frame_staff,width=15, font=normal_font_staff,textvariable=self.staff_age)
        self.ent_staff_age.grid(row=2, column=1, padx=5, pady=10)
        self.staff_age.trace_variable("w", self.input_validation_staff_age)
        lbl_Gender = Label(detail_frame_staff, text='Gender', bg='#eb3d34', font=normal_font_staff)
        lbl_Gender.grid(row=3, column=0, padx=5, pady=10)
        self.combo_gender = ttk.Combobox(detail_frame_staff,width=15, font=normal_font_staff, state='readonly',
                                         textvariable=self.gender)
        self.combo_gender['values'] = ('Male', 'Female', 'Others')
        self.combo_gender.grid(row=3, column=1, padx=5, pady=10)
        lbl_Address = Label(detail_frame_staff, text='Address', bg='#eb3d34', font=normal_font_staff)
        lbl_Address.grid(row=4, column=0, padx=5, pady=10)
        self.ent_Address = Entry(detail_frame_staff,width=15, font=normal_font_staff,textvariable=self.Address)
        self.ent_Address.grid(row=4, column=1, padx=5, pady=10)
        lbl_email = Label(detail_frame_staff, text='Email', bg='#eb3d34', font=normal_font_staff)
        lbl_email.grid(row=5, column=0, padx=5, pady=10)
        self.ent_email = Entry(detail_frame_staff,width=15, font=normal_font_staff,textvariable=self.email)
        self.ent_email.grid(row=5, column=1, padx=5, pady=10)
        lbl_contact = Label(detail_frame_staff, text='Number', bg='#eb3d34', font=normal_font_staff)
        lbl_contact.grid(row=6, column=0, padx=5, pady=10)
        self.ent_contact = Entry(detail_frame_staff,width=15, font=normal_font_staff,textvariable=self.contact)
        self.ent_contact.grid(row=6, column=1, padx=5, pady=10)
        self.contact.trace_variable("w", self.input_validation_contact)
        lbl_post = Label(detail_frame_staff, text='Post', bg='#eb3d34', font=normal_font_staff)
        lbl_post.grid(row=7, column=0, padx=5, pady=10)
        self.ent_post = Entry(detail_frame_staff,width=15, font=normal_font_staff,textvariable=self.post)
        self.ent_post.grid(row=7, column=1, padx=5, pady=10)
        self.post.trace_variable("w", self.validation_post_name)
        lbl_search_staff = Label(self.emp_frame, text= "Search",bg='#eb3d34', font= normal_font_staff)
        lbl_search_staff.place(relx=0.506, rely=0.138, height=21, width=60)
        lbl_search_from_staff= Label(self.emp_frame, text= "From",bg='#eb3d34', font= self.text_font)
        lbl_search_from_staff.place(relx=0.365, rely=0.185, height=25, width=72)
        self.staff_values = ['ID', 'Name']
        self.combo_staff_search_from= ttk.Combobox(self.emp_frame,width=15,state='readonly',values=self.staff_values,
                                                   font=self.text_font)
        self.combo_staff_search_from.place(relx=0.465, rely=0.185, relheight=0.032, relwidth=0.172)
        self.combo_staff_search_from.set('ID')
        lbl_searchby_staff = Label(self.emp_frame, text='By', bg='#eb3d34', font=self.text_font)
        lbl_searchby_staff.place(relx=0.360, rely=0.231, height=25, width=72)
        self.ent_search_from= Entry(self.emp_frame,width=15, font=self.text_font)
        self.ent_search_from.place(relx=0.465, rely=0.231,height=19, relwidth=0.173)
        search_staff_btn = ttk.Button(self.emp_frame,text='Search', command=self.search_staff)
        search_staff_btn.place(relx=0.495, rely=0.267, height=25, width=76)
        lbl_sort_staff= Label(self.emp_frame, text= "Sort",bg='#eb3d34', font= normal_font_staff)
        lbl_sort_staff.place(relx=0.840, rely=0.138, height=21, width=34)
        lbl_sort_from_staff= Label(self.emp_frame, text= "From",bg='#eb3d34', font= self.text_font)
        lbl_sort_from_staff.place(relx=0.699, rely=0.185, height=21, width=64)
        self.staff_sort_values = ['ID','Name']
        self.combo_staff_sort_from = ttk.Combobox(self.emp_frame, width=15,values=self.staff_sort_values,
                                                  state='readonly', font=self.text_font)
        self.combo_staff_sort_from.place(relx=0.783, rely=0.185, relheight=0.032, relwidth=0.172)
        self.combo_staff_sort_from.set('ID')
        lbl_searchby_staff = Label(self.emp_frame, text='By', bg='#eb3d34', font=self.text_font)
        lbl_searchby_staff.place(relx=0.698, rely=0.229, height=21, width=54)
        self.radio_staff_by_descend = Radiobutton(self.emp_frame, text="Descend",value='Descend', font=self.text_font,
                                                  bg='#eb3d34', variable= self.staff_order_standard)
        self.radio_staff_by_descend.place(relx=0.780, rely=0.231, width=75, height=21)
        self.radio_staff_by_ascend = Radiobutton(self.emp_frame, text="Ascend",value='Ascend', font=self.text_font,
                                                 bg='#eb3d34', variable= self.staff_order_standard)
        self.radio_staff_by_ascend.place(relx=0.875, rely=0.231, width=70, height=21)
        self.radio_staff_by_descend.invoke()
        sort_emp_sort_btn = ttk.Button(self.emp_frame, text='Sort', command= self.sort_employee)
        sort_emp_sort_btn.place(relx = 0.819, rely = 0.267, height = 25, width = 76)
        retrieve_again_staff = ttk.Button(self.emp_frame, text= "Retrieve", command= self.fetch_employee)
        retrieve_again_staff.place(relx=0.655, rely=0.268, height=24, width=57)
        add_staff= ttk.Button(detail_frame_staff, text='Add', command=self.add_employee)
        add_staff.place(relx=0.4, rely=0.741, height=34, width=67)
        remove_staff = ttk.Button(detail_frame_staff, text='Remove', command= self.delete_staff)
        remove_staff.place(relx=0.4, rely=0.885, height=34, width=67)
        update_staff = ttk.Button(detail_frame_staff, text='Update', command= self.update_employee)
        update_staff.place(relx=0.215, rely=0.813, height=34, width=67)
        clear_staff = ttk.Button(detail_frame_staff, text='Clear', command=self.clear_staff)
        clear_staff.place(relx=0.585, rely=0.813, height=34, width=67)
        backbutton_staff= ttk.Button(detail_frame_staff, text="Back", command= self.dashboard)
        backbutton_staff.place(relx=0.006, rely=0.955)
        treeframe=Frame(self.emp_frame)
        treeframe.place(relx=0.376, rely=0.617, relwidth=0.623, relheight=0.383)
        scroll_x = Scrollbar(treeframe, orient=HORIZONTAL)
        scroll_y = Scrollbar(treeframe, orient=VERTICAL)
        self.emp_tree= ttk.Treeview(treeframe,columns=("staffID", "Name","staff_age", "combo_gender","Address", "email",
                                    "contact","post"),xscrollcommand= scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.emp_tree.xview)
        scroll_y.config(command=self.emp_tree.yview)
        self.emp_tree.heading('staffID', text="Staff ID")
        self.emp_tree.heading('Name', text="Name")
        self.emp_tree.heading('staff_age', text="Age")
        self.emp_tree.heading('combo_gender', text="Gender")
        self.emp_tree.heading('Address', text="Address")
        self.emp_tree.heading('email', text="Email")
        self.emp_tree.heading('contact', text="Number")
        self.emp_tree.heading('post', text="Post")
        self.emp_tree['show'] = 'headings'
        self.emp_tree.pack(fill=BOTH, expand=1)
        self.emp_tree.bind('<ButtonRelease-1>',self.get_cursor_staff)
        self.fetch_employee()
    def add_employee(self, **kwargs):
        """
        Adding new employee into the database.
        :return None
        """
        emp = Staff(self.ent_staffID.get(), self.ent_Name.get(), self.ent_staff_age.get(),
                            self.combo_gender.get(), self.ent_Address.get(), self.ent_email.get(),
                            self.ent_contact.get(), self.ent_post.get())
        if self.ent_staffID.get() == '' or self.Name.get() == '' or self.ent_staff_age.get() == '' \
                or self.combo_gender.get() == '' or self.ent_Address.get() == '' or self.ent_email.get() == '' \
                or self.ent_contact.get() == '' or self.ent_post.get() == '':
            messagebox.showwarning("Warning", "Please enter all credentials")
        elif len(self.ent_Name.get()) < 3 or len(self.ent_Name.get()) > 40:
            messagebox.showwarning("Warning", "Staff name must be between 3-40 in length.")
        elif len(self.ent_post.get()) < 4 or len(self.ent_post.get()) > 20:
            messagebox.showwarning("Warning", "Post must be between 4-20 in length.")
        elif len(self.ent_Address.get()) < 4 or len(self.ent_Address.get()) > 42:
            messagebox.showwarning("Warning", "Staff address must be between 4-42 in length.")
        elif "@" not in self.ent_email.get():
            messagebox.showwarning("Warning", "Please enter a correct email which includes @")
        elif len(self.ent_contact.get()) < 7 or len(self.ent_contact.get()) > 15:
            messagebox.showwarning("Warning", "The staff contact number length must be between 7-15")
        else:
            query = 'select * from staffs where staffID=%s;'
            values = (int(self.ent_staffID.get()),)
            records = self.dbconnect.selectuser(query, values)
            if records:
                messagebox.showerror("Error", "Staff already exists")
                self.clear_staff()
            else:
                query = 'insert into staffs values(%s,%s,%s,%s,%s,%s,%s,%s);'
                values = (int(emp.get_staff_id()),capwords(emp.get_staff_name()), emp.get_staff_age(),
                          emp.get_staff_combo_gender(),emp.get_staff_address(),
                        emp.get_staff_email(), int(emp.get_staff_contact()), str(emp.get_staff_post()))
                self.dbconnect.insert(query, values)
                messagebox.showinfo('Success', "New employee added Successfully")
                self.fetch_employee()
                self.clear_staff()
    def fetch_employee(self):
        """
        Fetching the employee data from database to tree-view.
        :return None
        """
        query = 'select * from staffs;'
        records = self.dbconnect.select(query)
        self.emp_tree.delete(*self.emp_tree.get_children())
        for row in records:
            self.emp_tree.insert('', END, values=row)
    def update_employee(self):
        """
        Updating the employee data into the database.
        :return None
        """
        emp = Staff(self.ent_staffID.get(), self.ent_Name.get(), self.ent_staff_age.get(), self.combo_gender.get(),
                         self.ent_Address.get(), self.ent_email.get(), self.ent_contact.get(),self.ent_post.get())
        if self.ent_staffID.get() == '' or self.ent_Name.get() == '' or self.ent_staff_age.get() == '' \
                or self.combo_gender.get()== '' or self.ent_Address.get() == '' or self.ent_email.get() == ''or \
                self.ent_contact.get() == '' or self.ent_post.get() == '':
            messagebox.showwarning("Warning", "Please enter all credentials")
        elif len(self.ent_Name.get()) < 3 or len(self.ent_Name.get()) > 40:
            messagebox.showwarning("Warning", "Staff name must be between 3-40 in length.")
        elif len(self.ent_post.get()) < 4 or len(self.ent_post.get()) > 20:
            messagebox.showwarning("Warning", "Post must be between 4-20 in length.")
        elif len(self.ent_Address.get()) < 4 or len(self.ent_Address.get()) > 42:
            messagebox.showwarning("Warning", "Staff address must be between 4-42 in length.")
        elif "@" not in self.ent_email.get():
            messagebox.showwarning("Warning", "Please enter a correct email which includes @")
        elif len(self.ent_contact.get()) < 7 or len(self.ent_contact.get()) > 15:
            messagebox.showwarning("Warning", "The staff contact number length must be between 7-15")
        else:
            query= 'select * from staffs where staffID=%s;'
            values = (int(self.ent_staffID.get()),)
            records = self.dbconnect.selectuser(query, values)
            values = (int(emp.get_staff_id()),capwords(emp.get_staff_name()), emp.get_staff_age(),
                      emp.get_staff_combo_gender(), emp.get_staff_address(),emp.get_staff_email(),
                      str(emp.get_staff_contact()), str(emp.get_staff_post()))
            if records == values:
                messagebox.showwarning("Warning", "Employee data has nothing to update")
                self.clear_staff()
            elif records:
                query = 'update staffs set Name=%s,age=%s,combo_gender=%s,Address=%s,email=%s, contact=%s ,post=%s ' \
                        'WHERE staffID=%s;'
                values = (capwords(emp.get_staff_name()), emp.get_staff_age(), emp.get_staff_combo_gender(),
                          emp.get_staff_address(),emp.get_staff_email(), int(emp.get_staff_contact()),
                          str(emp.get_staff_post()), int(emp.get_staff_id()))
                self.dbconnect.update(query, values)
                messagebox.showinfo('Success', "Employee data updated Successfully")
                self.fetch_employee()
                self.clear_staff()
            else:
                messagebox.showerror('Error', 'No such staff exists')
    def delete_staff(self):
        """
        Deleting the employee data from the database.
        :return None
        """
        emp_delete = Del_Staff(self.ent_staffID.get())
        if self.ent_staffID.get()=="":
                messagebox.showwarning("Warning", "Staff ID cannot be empty")
        else:
            query = "select * from staffs where staffID=%s;"
            values = (int(self.ent_staffID.get()),)
            records = self.dbconnect.selectuser(query, values)
            if records:
                query = 'delete from staffs where staffID=%s;'
                values = (emp_delete.get_staff_id(),)
                self.dbconnect.delete(query, values)
                messagebox.showinfo("Delete", "Employee information Deleted successfully")
                self.fetch_employee()
                self.clear_staff()
            else:
                messagebox.showerror("Error", "No such staff id is available")
                self.clear_staff()
    def clear_staff(self):
        """Clearing the employee data from entries.
        :return None
        """
        if self.ent_staffID.get() == '' and self.ent_Name.get() == '' and self.ent_staff_age.get() == '' \
                and self.combo_gender.get()== '' \
                and self.ent_Address.get() == '' and self.ent_email.get() == '' and self.ent_contact.get() == '' \
                and self.ent_post.get() == '':
            messagebox.showwarning("Warning", "Nothing to clear")
        else:
            self.staffID.set('')
            self.Name.set('')
            self.staff_age.set('')
            self.gender.set('')
            self.Address.set('')
            self.email.set('')
            self.contact.set('')
            self.post.set('')
    def get_cursor_staff(self, *args):
        """
        Fetching the employee data from tree-view to entry.
        :return None
        """
        try:
            cursor_row=self.emp_tree.focus()
            contents=self.emp_tree.item(cursor_row)
            row= contents["values"]
            self.staffID.set(row[0])
            self.Name.set(row[1])
            self.staff_age.set(row[2])
            self.gender.set(row[3])
            self.Address.set(row[4])
            self.email.set(row[5])
            self.contact.set(row[6])
            self.post.set(row[7])
        except IndexError:
            pass
    def sort_employee(self):
        """Sorting the employee data in tree-view.
        :return None
        """
        try:
            a = self.combo_staff_sort_from.get()
            sort_by = self.staff_values.index(a)
            ascend = self.staff_order_standard.get()
            if a =="" or ascend =="":
                messagebox.showwarning("Warning",'Please Select a Employee data to sort from')
            else:
                query = 'select * from staffs'
                results = self.dbconnect.select(query)
                self.mergeSort(results, sort_by, ascend)
                self.emp_tree.delete(*self.emp_tree.get_children())
                for row in results:
                    self.emp_tree.insert('', 'end', values=row)
        except ValueError:
            messagebox.showerror("Error", "No employee data to sort")
    def food_interface(self):
        """
        Food/Menu interface is designed here.
        :return None
        """
        self.menuframe = Frame(self.wn,bg="#eb3d34")
        self.menuframe.place(relx=0, rely=0, width=830, height=650)
        normal_font_food = "-family Corbel -size 12"
        title_frame_food = Frame(self.menuframe, bg="#eb3d34")
        title_frame_food.place(relx=-0.0, rely=0.0, relheight=0.131, relwidth=1.007)
        title = Label(title_frame_food, text="Menu Management", bg="#eb3d34", font=self.title_font)
        title.place(relx=0.275, rely=0.118, height=71, width=434)
        detail_frame_food = Frame(self.menuframe, bg="#eb3d34")
        detail_frame_food.place(relx=0.0, rely=0.138, width=835, height=134)
        self.pizza_img = PhotoImage(file='pizza.png')
        label_pizza_img = Label(self.menuframe, bg="#eb3d34", image=self.pizza_img)
        label_pizza_img.place(relx=0.70, rely=0.40)
        self.dish_img = PhotoImage(file='dish.png')
        label_dish_img = Label(self.menuframe, bg="#eb3d34", image=self.dish_img)
        label_dish_img.place(relx=0.40, rely=0.40)
        self.food_img = PhotoImage(file='food.png')
        label_food_img = Label(self.menuframe, bg="#eb3d34", image=self.food_img)
        label_food_img.place(relx=0.05, rely=0.56)
        self.chowmin_img = PhotoImage(file='noodles.png')
        label_chowmin_img = Label(self.menuframe, bg="#eb3d34", image=self.chowmin_img)
        label_chowmin_img.place(relx=0.01, rely=0.37)
        lbl_foodID = Label(detail_frame_food, text='Food ID', bg='#eb3d34', font=normal_font_food)
        lbl_foodID.grid(row=0, column=0, padx=5, pady=10)
        self.ent_foodID = Entry(detail_frame_food, width=11, font=normal_font_food,textvariable=self.foodID)
        self.ent_foodID.grid(row=0, column=1, padx=5, pady=10)
        self.ent_foodID.focus()
        self.foodID.trace_variable("w", self.input_validation_food_id)
        lbl_food = Label(detail_frame_food, text='Food', bg='#eb3d34', font=normal_font_food)
        lbl_food.grid(row=0, column=2, padx=5, pady=10)
        self.ent_food = Entry(detail_frame_food, width=11, font=normal_font_food,textvariable=self.food1)
        self.ent_food.grid(row=0, column=3, padx=5, pady=10)
        lbl_foodPrice = Label(detail_frame_food, text='Price', bg='#eb3d34', font=normal_font_food)
        lbl_foodPrice.grid(row=0, column=4, padx=5, pady=10)
        self.ent_foodprice= Entry(detail_frame_food, width=11, font=normal_font_food,textvariable=self.foodprice1)
        self.ent_foodprice.grid(row=0, column=5, padx=5, pady=10)
        self.foodprice1.trace_variable("w", self.input_letter_validation_food_price)
        lbl_search_from_food = Label(detail_frame_food, text="From", bg='#eb3d34', font=self.text_font)
        lbl_search_from_food.place(relx=0.024, rely=0.764, height=21, width=34)
        self.food_values = ['ID', 'Name']
        self.combo_food_search_from = ttk.Combobox(detail_frame_food, width=15,values=self.food_values, state='readonly'
                                                   , font=self.text_font)
        self.combo_food_search_from.place(relx=0.072, rely=0.764, relheight=0.146, relwidth=0.171)
        self.combo_food_search_from.set('ID')
        lbl_searchby_food = Label(detail_frame_food, text='By', bg='#eb3d34', font=self.text_font)
        lbl_searchby_food.place(relx=0.275, rely=0.764, height=21, width=34)
        self.ent_search_from_food = Entry(detail_frame_food, width=15, font=self.text_font)
        self.ent_search_from_food.place(relx=0.311, rely=0.764,height=20, relwidth=0.113)
        self.ent_search_from_food.bind('<Return>', lambda e: self.search_food())
        search_food_btn = ttk.Button(detail_frame_food, text='Search', command=self.search_food)
        search_food_btn.place(relx=0.435, rely=0.75, height=25, width=76)
        lbl_sort_from_food = Label(detail_frame_food, text="From", bg='#eb3d34', font=self.text_font)
        lbl_sort_from_food.place(relx=0.630, rely=0.556, height=21, width=35)
        self.combofood_sort= ['ID','Name']
        self.combo_food_sort_from = ttk.Combobox(detail_frame_food, width=15,values=self.combofood_sort, state='readonly',
                                                 font=self.text_font)
        self.combo_food_sort_from.set('ID')
        self.combo_food_sort_from.place(relx=0.680, rely=0.556, relheight=0.146, relwidth=0.17)
        lbl_searchby_food = Label(detail_frame_food, text='By', bg='#eb3d34', font=self.text_font)
        lbl_searchby_food.place(relx=0.630, rely=0.764, height=21, width=35)
        self.radio_food_by_descending = Radiobutton(detail_frame_food, text="Descend",value='Descend', font=self.text_font,
                                                    bg='#eb3d34', variable=self.food_order_standard)
        self.radio_food_by_descending.place(relx=0.680, rely=0.764, width=75, height=21)
        self.radio_food_by_ascending = Radiobutton(detail_frame_food, text="Ascend", font=self.text_font,value='Ascend',
                                                   bg='#eb3d34',variable=self.food_order_standard)
        self.radio_food_by_ascending.place(relx=0.780, rely=0.764,width=70, height=21)
        self.radio_food_by_descending.invoke()
        sort_food_sort_btn = ttk.Button(detail_frame_food, text='Sort', command=self.sort_food)
        sort_food_sort_btn.place(relx=0.898, rely=0.764, height=25, width=76)
        retrieve_again_food = ttk.Button(detail_frame_food, text= "Retrieve", command= self.fetch_menu)
        retrieve_again_food.place(relx=0.539, rely=0.764, height=25, width=76)
        add_food = ttk.Button(detail_frame_food, text='Add', command=self.add_menu)
        add_food.grid(row=0, column=6, padx=5, pady=5)
        remove_food = ttk.Button(detail_frame_food, text='Remove', command=self.delete_food)
        remove_food.grid(row=0, column=7, padx=5, pady=5)
        update_food = ttk.Button(detail_frame_food, text='Update', command=self.update_menu)
        update_food.grid(row=0, column=9, padx=5, pady=5)
        clear_food = ttk.Button(detail_frame_food, text='Clear', command=self.clear_menu)
        clear_food.grid(row=0, column=10, padx=5, pady=5)
        backbutton_food = ttk.Button(self.menuframe, text="Back", command=self.dashboard)
        backbutton_food.place(relx=0.006, rely=0.955)
        treeframe_food= Frame(self.menuframe, bg="#eb3d34")
        treeframe_food.place(relx=0.487, rely=0.578, height=273, width=425)
        scroll_x = Scrollbar(treeframe_food, orient=HORIZONTAL)
        scroll_y = Scrollbar(treeframe_food, orient=VERTICAL)
        self.food_tree = ttk.Treeview(treeframe_food, columns=("foodID", "food", "foodprice"),
                                      xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.food_tree.xview)
        scroll_y.config(command=self.food_tree.yview)
        self.food_tree.heading('foodID', text="Food ID")
        self.food_tree.heading('food', text="Food")
        self.food_tree.heading('foodprice', text="Price")
        self.food_tree['show'] = 'headings'
        self.food_tree.column('foodID', width=120)
        self.food_tree.column('food', width=120)
        self.food_tree.column('foodprice', width=120)
        self.food_tree.pack(fill=BOTH, expand=1)
        self.food_tree.bind('<ButtonRelease-1>',self.get_cursor_menu)
        self.fetch_menu()
    def add_menu(self, **kwargs):
        """
        Adding new food item into the database.
        :return None
        """
        food = Menu(self.ent_foodID.get(), self.ent_food.get(), self.ent_foodprice.get())
        if self.ent_foodID.get() == '' or self.ent_food.get() == '' or self.ent_foodprice.get() == '':
            messagebox.showwarning("Warning", "Please enter all credentials")
        elif len(self.ent_food.get()) < 3 or len(self.ent_food.get()) > 40:
            messagebox.showwarning("Warning", "Food name must be between 3-40 in length.")
        else:
            query = 'select * from menu where foodID=%s;'
            values = (int(self.ent_foodID.get()),)
            records = self.dbconnect.selectuser(query, values)
            if records:
                messagebox.showerror("Error", "Food already exists")
                self.clear_menu()
            else:
                query = 'insert into menu values(%s,%s,%s);'
                values = (int(food.get_food_id()), capwords(food.get_food_name()), int(food.get_food_price()))
                self.dbconnect.insert(query, values)
                messagebox.showinfo('Success', "Food Added Successfully")
                self.fetch_menu()
                self.clear_menu()
    def fetch_menu(self):
        """
        Fetching the employee data from database to tree-view.
        :return None
        """
        query = 'select * from menu;'
        records = self.dbconnect.select(query)
        self.food_tree.delete(*self.food_tree.get_children())
        for row in records:
            self.food_tree.insert('', END, values=row)
    def update_menu(self):
        """
        Updating the employee data into the database.
        :return None
        """
        food = Menu(self.ent_foodID.get(), self.ent_food.get(), self.ent_foodprice.get())
        if self.ent_foodID.get() == '' or self.ent_food.get() == '' or self.ent_foodprice.get() == '':
            messagebox.showwarning("Error", "Please enter all credentials")
        elif len(self.ent_food.get()) < 3 or len(self.ent_food.get()) > 40:
            messagebox.showwarning("Warning", "Food name must be between 3-40 in length.")
        else:
            query= 'select * from menu where foodID=%s;'
            values = (int(self.ent_foodID.get()),)
            records = self.dbconnect.selectuser(query, values)
            values = (int(food.get_food_id()),capwords(food.get_food_name()), str(food.get_food_price()))
            if records == values:
                messagebox.showwarning("Warning", "Food data has nothing to update")
                self.clear_menu()
            elif records:
                query = 'update menu set food=%s,foodprice=%s WHERE foodID=%s;'
                values = (capwords(food.get_food_name()), int(food.get_food_price()), int(food.get_food_id()))
                self.dbconnect.update(query, values)
                messagebox.showinfo('Success', "Food data updated Successfully")
                self.fetch_menu()
                self.clear_menu()
            else:
                messagebox.showerror('Error', 'No such food exists')
    def delete_food(self):
        """
        Deleting the food data from the database.
        :return None
        """
        food = Del_Menu(self.ent_foodID.get())
        if self.ent_foodID.get() =="":
            messagebox.showwarning("Warning", "Food ID field is empty")
        else:
            query = "select * from menu where foodID=%s;"
            values= (int(self.ent_foodID.get()),)
            records= self.dbconnect.selectuser(query, values)
            if records:
                query = 'delete from menu where foodID=%s;'
                values = (food.get_food_id(),)
                self.dbconnect.delete(query, values)
                messagebox.showinfo("Delete", "Food data Deleted successfully")
                self.fetch_menu()
                self.clear_menu()
            else:
                messagebox.showerror("Error", "Food ID unavailable")
                self.clear_customer()
    def clear_menu(self):
        """
        Clearing the food data from entries.
        :return None
        """
        if self.ent_foodID.get() == '' and self.ent_food.get() == '' and self.ent_foodprice.get() == '':
            messagebox.showwarning("Warning", "Nothing to clear")
        else:
            self.foodID.set('')
            self.food1.set('')
            self.foodprice1.set('')
    def get_cursor_menu(self, *args):
        """
        Fetching the food data from tree-view to entry.
        :return None
        """
        try:
            cursor_row=self.food_tree.focus()
            contents=self.food_tree.item(cursor_row)
            row= contents["values"]
            self.foodID.set(row[0])
            self.food1.set(row[1])
            self.foodprice1.set(row[2])
        except IndexError:
            pass
    def sort_food(self):
        """Sorting the food data in tree-view.
        :return None
        """
        try:
            a = self.combo_food_sort_from.get()
            sort_by = self.food_values.index(a)
            ascend = self.food_order_standard.get()
            if a =="" or ascend =="":
                messagebox.showwarning("Warning",'Please select a food data to sort')
            else:
                query = 'select * from menu'
                results = self.dbconnect.select(query)
                self.mergeSort(results, sort_by, ascend)
                self.food_tree.delete(*self.food_tree.get_children())
                for row in results:
                    self.food_tree.insert('', 'end', values=row)
        except ValueError:
            messagebox.showerror("Error", "No food data to sort")
    def customer_interface(self):
        """Customer interface is designed here.
        :return None
        """
        self.customer_frame = Frame(self.wn, bg="#eb3d34")
        self.customer_frame.place(relx=0, rely=0, width=830, height=650)
        normal_font_customer = "-family Corbel -size 15"
        title_frame_customer = Frame(self.customer_frame, bg="#eb3d34")
        title_frame_customer.place(relx=-0.0, rely=0.0, relheight=0.131, relwidth=1.007)
        self.customer_img=PhotoImage(file='customerss.png')
        label_customer_img=Label(self.customer_frame,bg="#eb3d34",image=self.customer_img)
        label_customer_img.place(relx=0.40,rely=0.30)
        title_customer = Label(title_frame_customer, text="Customer Management", bg="#eb3d34", font=self.title_font)
        title_customer.place(relx=0.275, rely=0.118, height=71, width=434)
        detail_frame_customer = Frame(self.customer_frame, bg="#eb3d34")
        detail_frame_customer.place(relx=0.0, rely=0.138, relheight=0.852, relwidth=0.367)
        lbl_customerID = Label(detail_frame_customer, text='Customer ID', bg='#eb3d34', font=normal_font_customer)
        lbl_customerID.grid(row=0, column=0, padx=5, pady=10)
        self.ent_customerID = Entry(detail_frame_customer, width=15, font=normal_font_customer,
                                    textvariable=self.customerID)
        self.ent_customerID.grid(row=0, column=1, padx=5, pady=10)
        self.ent_customerID.focus()
        self.customerID.trace_variable("w", self.input_validation_customer_id)
        lbl_customer_name = Label(detail_frame_customer, text='Name', bg='#eb3d34', font=normal_font_customer)
        lbl_customer_name.grid(row=1, column=0, padx=5, pady=10)
        self.ent_customer_name = Entry(detail_frame_customer, width=15, font=normal_font_customer,
                                       textvariable=self.customer_name)
        self.ent_customer_name.grid(row=1, column=1, padx=5, pady=10)
        self.customer_name.trace_variable("w", self.validation_customer_name)
        lbl_customerAge = Label(detail_frame_customer, text='Age', bg='#eb3d34', font=normal_font_customer)
        lbl_customerAge.grid(row=2, column=0, padx=5, pady=10)
        self.ent_customer_Age = Entry(detail_frame_customer, width=15, font=normal_font_customer,
                                      textvariable=self.customer_Age)
        self.ent_customer_Age.grid(row=2, column=1, padx=5, pady=10)
        self.customer_Age.trace_variable("w", self.input_validation_customer_Age)
        lbl_customergender = Label(detail_frame_customer, text='Gender', bg='#eb3d34', font=normal_font_customer)
        lbl_customergender.grid(row=3, column=0, padx=5, pady=10)
        self.customer_combo_gender = ttk.Combobox(detail_frame_customer, width=15, font=normal_font_customer,
                                                  state='readonly',textvariable=self.combo_gender_customer_setting)
        self.customer_combo_gender['values'] = ('Male', 'Female', 'Others')
        self.customer_combo_gender.grid(row=3, column=1, padx=5, pady=10)
        lbl_customeraddress = Label(detail_frame_customer, text='Address', bg='#eb3d34', font=normal_font_customer)
        lbl_customeraddress.grid(row=4, column=0, padx=5, pady=10)
        self.ent_customer_address = Entry(detail_frame_customer, width=15, font=normal_font_customer,
                                          textvariable=self.customer_address)
        self.ent_customer_address.grid(row=4, column=1, padx=5, pady=10)
        lbl_customer_email = Label(detail_frame_customer, text='Email', bg='#eb3d34', font=normal_font_customer)
        lbl_customer_email.grid(row=5, column=0, padx=5, pady=10)
        self.ent_customer_email = Entry(detail_frame_customer, width=15, font=normal_font_customer,
                                        textvariable=self.customer_email)
        self.ent_customer_email.grid(row=5, column=1, padx=5, pady=10)
        lbl_customer_contact = Label(detail_frame_customer, text='Number', bg='#eb3d34', font=normal_font_customer)
        lbl_customer_contact.grid(row=6, column=0, padx=5, pady=10)
        self.ent_customer_contact = Entry(detail_frame_customer, width=15, font=normal_font_customer,
                                          textvariable=self.customer_contact)
        self.ent_customer_contact.grid(row=6, column=1, padx=5, pady=10)
        self.customer_contact.trace_variable("w", self.input_validation_customer_contact)
        lbl_foodchoice = Label(detail_frame_customer, text='Food ID', bg='#eb3d34', font=normal_font_customer)
        lbl_foodchoice.grid(row=7, column=0, padx=5, pady=10)
        self.ent_foodchoice = Entry(detail_frame_customer, width=15, font=normal_font_customer,
                                    textvariable=self.foodchoice)
        self.ent_foodchoice.grid(row=7, column=1, padx=5, pady=10)
        lbl_search_customer = Label(self.customer_frame, text="Search", bg='#eb3d34', font=normal_font_customer)
        lbl_search_customer.place(relx=0.506, rely=0.138, height=21, width=60)
        lbl_search_from_customer = Label(self.customer_frame, text="From", bg='#eb3d34', font=self.text_font)
        lbl_search_from_customer.place(relx=0.365, rely=0.185, height=25, width=72)
        self.combo_customer_search_from = ttk.Combobox(self.customer_frame, width=15, state='readonly',
                                                       font=self.text_font)
        self.combo_customer_search_from['values'] = ('ID', 'Name')
        self.combo_customer_search_from.set('ID')
        self.combo_customer_search_from.place(relx=0.465, rely=0.185, relheight=0.032, relwidth=0.172)
        lbl_searchby_customer = Label(self.customer_frame, text='By', bg='#eb3d34', font=self.text_font)
        lbl_searchby_customer.place(relx=0.360, rely=0.231, height=25, width=72)
        self.ent_customer_search_from = Entry(self.customer_frame, width=15, font=self.text_font)
        self.ent_customer_search_from.place(relx=0.465, rely=0.231, height=19, relwidth=0.173)
        search_customer_btn = ttk.Button(self.customer_frame, text='Search', command=self.search_customer)
        search_customer_btn.place(relx=0.495, rely=0.267, height=25, width=76)
        lbl_sort_customer = Label(self.customer_frame, text="Sort", bg='#eb3d34', font=normal_font_customer)
        lbl_sort_customer.place(relx=0.840, rely=0.138, height=21, width=34)
        lbl_sort_from_customer = Label(self.customer_frame, text="From", bg='#eb3d34', font=self.text_font)
        lbl_sort_from_customer.place(relx=0.699, rely=0.185, height=21, width=64)
        self.customer_values = ['ID','Name']
        self.combo_customer_sort_from = ttk.Combobox(self.customer_frame, width=15,values=self.customer_values,
                                                     state='readonly', font=self.text_font)
        self.combo_customer_sort_from.place(relx=0.783, rely=0.185, relheight=0.032, relwidth=0.172)
        self.combo_customer_sort_from.set('ID')
        lbl_searchby_customer = Label(self.customer_frame, text='By', bg='#eb3d34', font=self.text_font)
        lbl_searchby_customer.place(relx=0.698, rely=0.229, height=21, width=54)
        self.radio_customer_by_descending = Radiobutton(self.customer_frame, text="Descend", value="Descend" ,
                                        font=self.text_font, bg='#eb3d34',variable= self.customer_order_standard)
        self.radio_customer_by_descending.place(relx=0.780, rely=0.231, width=75, height=21)
        self.radio_customer_by_ascending = Radiobutton(self.customer_frame, text="Ascend",value="Ascend",
                                        font=self.text_font, bg='#eb3d34', variable=self.customer_order_standard)
        self.radio_customer_by_ascending.place(relx=0.875, rely=0.231, width=70, height=21)
        self.radio_customer_by_descending.invoke()
        sort_customer_btn = ttk.Button(self.customer_frame, text='Sort', command=self.sort_customer)
        sort_customer_btn.place(relx = 0.819, rely = 0.267, height = 25, width = 76)
        retrieve_again_customer = ttk.Button(self.customer_frame, text= "Retrieve", command= self.fetch_customer)
        retrieve_again_customer.place(relx=0.655, rely=0.268, height=24, width=57)
        add_customer = ttk.Button(detail_frame_customer, text='Add',command= self.add_customers)
        add_customer.place(relx=0.4, rely=0.741, height=34, width=67)
        remove_customer = ttk.Button(detail_frame_customer, text='Remove',command= self.delete_customer)
        remove_customer.place(relx=0.4, rely=0.885, height=34, width=67)
        update_customer = ttk.Button(detail_frame_customer, text='Update',command= self.update_customer)
        update_customer.place(relx=0.215, rely=0.813, height=34, width=67)
        clear_customer = ttk.Button(detail_frame_customer, text='Clear',command=self.clear_customer)
        clear_customer.place(relx=0.585, rely=0.813, height=34, width=67)
        backbutton_customer = ttk.Button(detail_frame_customer, text="Back", command=self.dashboard)
        backbutton_customer.place(relx=0.006, rely=0.955)
        treeframe_customer = Frame(self.customer_frame)
        treeframe_customer.place(relx=0.376, rely=0.617, relwidth=0.623, relheight=0.383)
        scroll_x = Scrollbar(treeframe_customer, orient=HORIZONTAL)
        scroll_y = Scrollbar(treeframe_customer, orient=VERTICAL)
        self.customer_tree = ttk.Treeview(treeframe_customer, columns=("customerID", "customer_name", "customer_Age",
                                        "customer_combo_gender", "customer_address",
                                        "customer_email", "customer_contact", "foodchoice"), xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.customer_tree.xview)
        scroll_y.config(command=self.customer_tree.yview)
        self.customer_tree.heading('customerID', text="Customer ID")
        self.customer_tree.heading('customer_name', text="Name")
        self.customer_tree.heading('customer_Age', text="Age")
        self.customer_tree.heading('customer_combo_gender', text="Gender")
        self.customer_tree.heading('customer_address', text="Address")
        self.customer_tree.heading('customer_email', text="Email")
        self.customer_tree.heading('customer_contact', text="Number")
        self.customer_tree.heading('foodchoice', text="Food")
        self.customer_tree['show'] = 'headings'
        self.customer_tree.pack(fill=BOTH, expand=1)
        self.customer_tree.bind('<ButtonRelease-1>',self.get_cursor_customer)
        self.fetch_customer()
    def add_customers(self, **kwargs):
        """
        Adding new customer into the database.
        :return None
        """
        a = self.ent_foodchoice.get()
        query_check = "select * from menu where foodID=%s;"
        value_check = (a, )
        records_check = self.dbconnect.selectuser(query_check, value_check)
        if records_check:
            cus = Customer(self.ent_customerID.get(), self.ent_customer_name.get(), self.ent_customer_Age.get(),
                           self.customer_combo_gender.get(),self.ent_customer_address.get(), self.ent_customer_email.get(),
                           self.ent_customer_contact.get(), self.ent_foodchoice.get())
            if self.ent_customerID.get() == '' or self.ent_customer_name.get() == '' or self.ent_customer_Age.get() == '' \
                    or self.customer_combo_gender.get()== '' or self.ent_customer_address.get() == '' or \
                    self.ent_customer_email.get() == ''or self.ent_customer_contact.get() == ''or \
                    self.ent_foodchoice.get() == '' :
                messagebox.showwarning("Warning", "Please enter all credentials")
            elif len(self.customer_name.get()) < 3 or len(self.customer_name.get()) > 40:
                messagebox.showwarning("Warning", "Customer name must be between 3-40 in length.")
            elif not self.ent_foodchoice.get().isdigit():
                    messagebox.showerror('Error', "Customer food should contain number only.")
            elif len(self.ent_customer_address.get()) < 4 or len(self.ent_customer_address.get()) > 42:
                messagebox.showwarning("Warning", "Customer address must be between 4 - 42 in length.")
            elif "@" not in self.ent_customer_email.get():
                messagebox.showwarning("Warning", "Please enter a correct email which includes @")
            elif len(self.ent_customer_contact.get()) < 7 or len(self.ent_customer_contact.get()) > 15:
                messagebox.showwarning("Warning", "The customer contact number length must be between 7-15")
            else:
                query = "select * from customers where customerID=%s;"
                values = (int(self.ent_customerID.get()),)
                records = self.dbconnect.selectuser(query, values)
                if records:
                    messagebox.showerror("Error", "Customer already exists")
                    self.clear_customer()
                else:
                    query = 'insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s);'
                    values = (int(cus.get_customer_ID()), capwords(cus.get_customer_name()),
                              int(cus.get_customer_Age()),cus.get_customer_combo_gender(),cus.get_customer_address(),
                              cus.get_customer_email(),int(cus.get_customer_contact()),cus.get_foodchoice())
                    self.dbconnect.insert(query, values)
                    messagebox.showinfo('Success', "New Customer Added Successfully")
                    self.fetch_customer()
                    self.clear_customer()
        else:
            if not self.ent_foodchoice.get().isdigit():
                messagebox.showerror('Error', "Customer food choice should contain number only.")
            else:
                messagebox.showerror("Error", "Enter a valid Food ID")
    def update_customer(self):
        """
        Updating the customer data into the database.
        :return None
        """
        cus = Customer(self.ent_customerID.get(), self.ent_customer_name.get(), self.ent_customer_Age.get(),
                       self.customer_combo_gender.get(), self.ent_customer_address.get(),
                       self.ent_customer_email.get(), self.ent_customer_contact.get(), self.ent_foodchoice.get())
        a = self.ent_foodchoice.get()
        query_check = "select * from menu where foodID=%s;"
        value_check = (a,)
        records_check = self.dbconnect.selectuser(query_check, value_check)

        if self.ent_customerID.get() == '' or self.ent_customer_name.get() == '' or self.ent_customer_Age.get() == '' \
                or self.customer_combo_gender.get() == '' \
                or self.ent_customer_address.get() == '' or self.ent_customer_email.get() == '' \
                or self.ent_customer_contact.get() == '' or self.ent_foodchoice.get() == '':
            messagebox.showwarning("Warning", "Please enter all credentials")
        else:
            if records_check:

                if not self.ent_foodchoice.get().isdigit():
                    messagebox.showerror('Error', "Id should contain number only.")
                elif "@" not in self.ent_customer_email.get():
                    messagebox.showwarning("Warning", "Please enter a correct email which contains @")
                elif len(self.customer_name.get()) < 3 or len(self.customer_name.get()) > 40:
                    messagebox.showwarning("Warning", "Customer name must be between 3-40 in length.")
                elif len(self.ent_customer_address.get()) < 4 or len(self.ent_customer_address.get()) > 42:
                    messagebox.showwarning("Warning", "Customer address must be between 4 - 42 in length.")
                elif len(self.ent_customer_contact.get()) < 7 or len(self.ent_customer_contact.get()) > 15:
                    messagebox.showwarning("Warning", "The customer contact number length must be between 7-15")
                else:
                    customer_update = int(self.ent_customerID.get())
                    query= 'select * from customers where customerID=%s;'
                    values = (customer_update,)
                    records = self.dbconnect.selectuser(query, values)
                    values = (int(cus.get_customer_ID()), capwords(cus.get_customer_name()),
                              str(cus.get_customer_Age()), cus.get_customer_combo_gender(),cus.get_customer_address(),
                              cus.get_customer_email(), str(cus.get_customer_contact()),int(cus.get_foodchoice()))
                    if records == values:
                        messagebox.showwarning("Warning", "Customer data has nothing to update")
                        self.clear_customer()
                    elif records:
                        query = 'update customers set customer_name=%s,customer_Age=%s,customer_combo_gender=%s,' \
                                'customer_address=%s,customer_email=%s, customer_contact=%s,foodID=%s WHERE customerID=%s;'
                        values = (capwords(cus.get_customer_name()), int(cus.get_customer_Age()), cus.get_customer_combo_gender(),
                                  cus.get_customer_address(), cus.get_customer_email(), int(cus.get_customer_contact()),
                                  cus.get_foodchoice(), int(cus.get_customer_ID()))
                        self.dbconnect.update(query, values)
                        messagebox.showinfo('Success', "Customer data updated Successfully")
                        self.fetch_customer()
                        self.clear_customer()
                    else:
                        messagebox.showerror('Error', 'No such customer exists')
            else:
                if not self.ent_foodchoice.get().isdigit():
                    messagebox.showerror('Error', "Customer food choice should contain number only.")
                else:
                    messagebox.showerror("Error", "Such food does not exist.")
    def fetch_customer(self):
        """
        Fetching the customer data from database to tree-view with joined table.
        :return None
        """
        query = 'select customers.customerID, customers.customer_name, customers.customer_Age, ' \
                'customers.customer_combo_gender,customers.customer_address, customers.customer_email, ' \
                'customers.customer_contact, menu.food from menu inner join customers on menu.foodID=customers.foodID;'
        records = self.dbconnect.select(query)
        self.customer_tree.delete(*self.customer_tree.get_children())
        for row in records:
            self.customer_tree.insert('', END, values=row)
    def delete_customer(self):
        """
        Deleting the customer from the database.
        :return None
        """
        customer_delete = Del_Customer(self.ent_customerID.get())
        if self.ent_customerID.get() =="":
            messagebox.showwarning("Warning", "Customer ID field is empty")
        else:
            query = "select * from customers where customerID=%s;"
            values= (int(self.ent_customerID.get()),)
            records= self.dbconnect.selectuser(query, values)
            if records:
                query = 'delete from customers where customerID=%s;'
                values = (customer_delete.get_customer_ID(),)
                self.dbconnect.delete(query, values)
                messagebox.showinfo("Delete", "Customer information deleted successfully")
                self.fetch_customer()
                self.clear_customer()
            else:
                messagebox.showerror("Error", "No such customer id available")
                self.clear_customer()
    def clear_customer(self):
        """
        Clearing the customer from entries.
        :return None
        """
        if self.ent_customerID.get() == '' and self.ent_customer_name.get() == '' and self.ent_customer_Age.get() == ''\
                and self.customer_combo_gender.get()== '' and self.ent_customer_address.get() == '' and \
                self.ent_customer_email.get() == '' and self.ent_customer_contact.get() == '' and \
                self.ent_foodchoice.get() == '':
            messagebox.showwarning('Warning', 'Nothing to clear')
        else:
            self.customerID.set('')
            self.customer_name.set('')
            self.customer_Age.set('')
            self.combo_gender_customer_setting.set('')
            self.customer_address.set('')
            self.customer_email.set('')
            self.customer_contact.set('')
            self.foodchoice.set('')
    def get_cursor_customer(self,*args):
        """
        Fetching the customer data from tree-view to entry.
        :return None
        """
        try:
            cursor_row=self.customer_tree.focus()
            contents=self.customer_tree.item(cursor_row)
            row= contents["values"]
            value=(row[0],)
            query ='select * from customers where customerID=%s'
            records = self.dbconnect.selectuser(query,value)
            self.customerID.set(records[0])
            self.customer_name.set(records[1])
            self.customer_Age.set(records[2])
            self.combo_gender_customer_setting.set(records[3])
            self.customer_address.set(records[4])
            self.customer_email.set(records[5])
            self.customer_contact.set(records[6])
            self.foodchoice.set(records[7])
        except IndexError:
            pass
    def search_customer(self, list=None):
        """
        Searching the customer data from tree-view.
        :return new_list contains the final result
        :param list - It checks result is in list or not if not it
        """
        search_by_customer = self.combo_customer_search_from.get()
        item = capwords(self.ent_customer_search_from.get())
        if search_by_customer == "" or item ==  "":
            messagebox.showerror("Error", "No customer data to search from")
        else:
            if not list:
                query = 'select * from customers;'
                result = self.dbconnect.select(query)
            else:
                result = list
            self.customer_tree.delete(*self.customer_tree.get_children())
            if search_by_customer == "ID":
                column = 0
                if item.isdigit():
                    item = int(item)
                elif self.combo_customer_search_from.get() == " " or self.ent_customer_search_from == " ":
                    messagebox.showwarning("Warning", "Enter values to search from")
                else:
                    messagebox.showerror('Error', "Customer Id must be a number.")
                    self.fetch_customer()
                    return
            elif search_by_customer == "Name":
                column = 1
            else:
                return
            new_list = self.searching(result, column, item)
            self.customer_tree.delete(*self.customer_tree.get_children())
            for row in new_list:
                self.customer_tree.insert('', 'end', values=row)
            if not new_list:
                messagebox.showinfo('Not found', "Customer does not exist.")
                self.fetch_customer()
            return new_list
    def search_food(self, list=None):
        """
        Searching the food data from tree-view.
        :return new_list
        """
        search_by_food = self.combo_food_search_from.get()
        item = capwords(self.ent_search_from_food.get())
        if search_by_food == "" or item== "":
            messagebox.showerror("Error", "No food information to search from")
        else:
            if not list:
                query = 'select * from menu;'
                result = self.dbconnect.select(query)
            else:
                result = list
            self.food_tree.delete(*self.food_tree.get_children())
            if search_by_food == "ID":
                column = 0
                if item.isdigit():
                    item = int(item)
                else:
                    messagebox.showerror('Error', "Food Id must be number.")
                    self.fetch_menu()
                    return
            elif search_by_food == "Name":
                column = 1
            else:
                return
            new_list = self.searching(result, column, item)
            self.food_tree.delete(*self.food_tree.get_children())
            for row in new_list:
                self.food_tree.insert('', 'end', values=row)
            if not new_list:
                messagebox.showinfo('Not found', "Food does not exist.")
                self.fetch_menu()
            return new_list
    def search_staff(self, list=None):
        """
        Searching the staff data from tree-view.
        :return new_list
        """
        search_by_staff = self.combo_staff_search_from.get()
        item = capwords(self.ent_search_from.get())
        if search_by_staff== "" or item =="":
            messagebox.showerror("Error", "No staff data to search from")
        else:
            if not list:
                query = 'select * from staffs;'
                result = self.dbconnect.select(query)
            else:
                result = list
            self.emp_tree.delete(*self.emp_tree.get_children())
            if search_by_staff == "ID":
                column = 0
                if item.isdigit():
                    item = int(item)
                else:
                    messagebox.showerror('Error', "Employee Id must be number.")
                    self.fetch_employee()
                    return
            elif search_by_staff == "Name":
                column = 1
            else:
                return
            new_list = self.searching(result, column, item)
            self.emp_tree.delete(*self.emp_tree.get_children())
            for row in new_list:
                self.emp_tree.insert('', 'end', values=row)
            if not new_list:
                messagebox.showinfo('Not found', "Staff does not exist.")
                self.fetch_employee()
            return new_list
    def sort_customer(self):
        """
        Sorting the customer data in tree-view.
        :return None
        """
        try:
            a= self.combo_customer_sort_from.get()
            sort_by = self.customer_values.index(a)
            ascend = self.customer_order_standard.get()
            if a =="" or ascend =="":
                messagebox.showwarning("Warning",'Please select a value to sort the customers')
            else:
                query ='select customers.customerID, customers.customer_name, customers.customer_Age, ' \
                    'customers.customer_combo_gender,customers.customer_address, customers.customer_email, ' \
                'customers.customer_contact, menu.food from menu inner join customers on menu.foodID=customers.foodID;'
                results = self.dbconnect.select(query)
                self.mergeSort(results, sort_by, ascend)
                self.customer_tree.delete(*self.customer_tree.get_children())
                for row in results:
                    self.customer_tree.insert('', 'end', values=row)
        except ValueError:
            messagebox.showerror("Error", "No customer data to sort from")

    def input_validation_contact(self,*args):
        """
        Stopping user from entering alphabets in contact entry of staffs.
        :return None
        """
        a = self.contact.get()
        try:
            b = int(a)
            if b > 9999999999999:
                self.contact.set(a[:-1])
        except Exception:
            self.contact.set(a[:-1])
    def input_validation_staffid(self,*args):
        """
        Stopping user from entering alphabets in staff's id entry.
        :return None
        """
        a = self.staffID.get()
        try:
            b = int(a)
            if b > 9999999:
                self.staffID.set(a[:-1])
        except Exception:
            self.staffID.set(a[:-1])
    def input_validation_customer_contact(self,*args):
        """
        Stopping user from entering alphabets in contact entry of customer.
        :return None
        """
        a = self.customer_contact.get()
        try:
            b = int(a)
            if b > 9999999999999:
                self.customer_contact.set(a[:-1])
        except Exception:
            self.customer_contact.set(a[:-1])
    def input_validation_staff_age(self,*args):
        """
        Stopping user from entering alphabets in age entry of staffs.
        :return None
        """
        a = self.staff_age.get()
        try:
            b = int(a)
            if b > 99:
                self.staff_age.set(a[:-1])
        except Exception:
            self.staff_age.set(a[:-1])
    def input_validation_customer_Age(self,*args):
        """
        Stopping user from entering alphabets in age entry of customer.
        :return None
        """
        a = self.customer_Age.get()
        try:
            b = int(a)
            if b > 99:
                self.customer_Age.set(a[:-1])
        except Exception:
            self.customer_Age.set(a[:-1])
    def input_validation_customer_id(self,*args):
        """
        Stopping user from entering alphabets in customer's id entry.
        :return None
        """
        a = self.customerID.get()
        try:
            b = int(a)
            if b > 9999999:
                self.customerID.set(a[:-1])
        except Exception:
            self.customerID.set(a[:-1])
    def input_validation_food_id(self,*args):
        """Stopping user from entering alphabets in food's id entry.
        :return None
        """
        a = self.foodID.get()
        try:
            b = int(a)
            if b > 9999999:
                self.foodID.set(a[:-1])
        except Exception:
            self.foodID.set(a[:-1])
    def input_letter_validation_food_price(self,*args):
        """
        Stopping user from entering alphabets in customer's id entry.
        :return None
        """
        a = self.foodprice1.get()
        try:
            b = int(a)
            if b > 99999:
                self.foodprice1.set(a[:-1])
        except Exception:
            self.foodprice1.set(a[:-1])
    def validation_customer_name(self, *args):
        """
        Stopping user from entering numbers and special characters in customer's name entry.
        :return None
        """
        test_name_customer = self.customer_name.get()
        for i in "1234567890-=+_)(*&^%$#@!~`<>?:{}|\/*[]:'.?,;":
            if i in test_name_customer:
                test_name_customer = test_name_customer[:-1]
                self.customer_name.set(test_name_customer)
    def validation_staff_name(self, *args):
        """
        Stopping user from entering numbers and special characters in staff's name entry.
        :return None
                """
        test_name_staff = self.Name.get()
        for i in "1234567890-=+_)(*&^%$#@!~`<>?:{}|\/*[]:'.?,;":
            if i in test_name_staff:
                test_name_staff = test_name_staff[:-1]
                self.Name.set(test_name_staff)
    def validation_post_name(self, *args):
        """
        Stopping user from entering numbers and special characters in staff's post entry.
        :return None
        """
        test_name_post = self.post.get()
        for i in "1234567890-=+_)(*&^%$#@!~`<>?:{}|\/*[]:'.?,;":
            if i in test_name_post:
                test_name_post = test_name_post[:-1]
                self.post.set(test_name_post)

    @classmethod
    def mergeSort(cls, result, sort_by, ascend):
        """
        Mergesort algorithm for sorting data
        :param
                   sort_by - This parameter is for either sorting in ascending or descending order
                   ascend - This is for ascending order
        :return result - This returns the final sorted data
        """
        if len(result) > 1:
            mid = len(result) // 2
            left = result[:mid]
            right = result[mid:]
            cls.mergeSort(left, sort_by, ascend)
            cls.mergeSort(right, sort_by, ascend)
            x, y, z = 0, 0, 0
            while x < len(left) and y < len(right):
                if ascend == 'Ascend':
                    if left[x][sort_by] >= right[y][sort_by]:
                        result[z] = right[y]
                        y = y + 1
                    else:
                        result[z] = left[x]
                        x = x + 1
                    z = z + 1
                else:
                    if left[x][sort_by] <= right[y][sort_by]:
                        result[z] = right[y]
                        y = y + 1
                    else:
                        result[z] = left[x]
                        x = x + 1
                    z = z + 1
            while x < len(left):
                result[z] = left[x]
                x = x + 1
                z = z + 1
            while y < len(right):
                result[z] = right[y]
                y = y + 1
                z = z + 1
            return result

    @staticmethod
    def searching(result, search_by, item):
        """
        Linear search algorithm is for searching data
        :param
                search_by - This parameter is to specify what to search from.
                item - This parameter is used to specify the exact data.
        :return new_list - This returns the searched data.
        """
        new_list = []
        for value in result:
            if value[search_by] == item:
                new_list.append(value)
        return new_list
if __name__ == '__main__':
    root = Tk()
    Main_interface(root)
    root.mainloop()