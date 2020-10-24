class Management():
    '''
    This class gets required data for validating user login.
    Attributes:
        user: It gets the username from interface entry box
        password: It gets the password from interface entry box
    '''
    def __init__(self, user, password):
        '''
        This constructor is for Management class.
        :param
            user    : It gets the username from interface entry box
            password: It gets the password from interface entry box
        '''
        self.__user = user
        self.__passwd = password
    def get_user(self):
        return self.__user
    def get_passwd(self):
        return self.__passwd
class Admin():
    '''
    This class sets and gets required data for registering admin.
    Attributes:
        userid (int): It sets and gets the userid from interface entry box
        username    : It sets and gets the username from interface entry box
        password    : It sets and gets the password from interface entry box
    '''
    def __init__(self, userid, username, password):
        '''
        This is a constructor for Admin class.
        :param
            userid (int) : It sets and gets the userid from interface entry box
            username    : It sets and gets the username from interface entry box
            password    : It sets and gets the password from interface entry box
        '''
        self.__userid = userid
        self.__username = username
        self.__password = password
    def set_user_id(self, userid):
        self.__userid = userid
    def get_user_id(self):
        return self.__userid
    def set_user_name1(self, username):
        self.__username = username
    def get_user_name1(self):
        return self.__username
    def set_password1(self, password):
        self.__password = password
    def get_password1(self):
        return self.__password
class Staff():
    '''
    This class gets required data from staff table.
    Attributes:
        staffID (int)   : The staff id from interface entry box
        Name            : The staff name from interface entry box
        age             : The staff age from interface entry box
        combo_gender    : The staff gender from interface entry box
        Address         : The staff address from interface entry box
        contact         : The staff contact from interface entry box
        post            : The staff post from interface entry box
    '''
    def __init__(self,staffID,Name,age,combo_gender,Address,email,contact,post):
        '''
        This constructor is of class Staff.
        :param
            staffID (int)   : The staff id from interface entry box
            Name            : The staff name from interface entry box
            age             : The staff age from interface entry box
            combo_gender    : The staff gender from interface entry box
            email           : The staff email from interface entry box
            Address         : The staff address from interface entry box
            contact         : The staff contact from interface entry box
            post            : The staff post from interface entry box
        '''
        self.__staffID= staffID
        self.__Name= Name
        self.__age= age
        self.combo_gender= combo_gender
        self.__Address= Address
        self.__email= email
        self.__contact= contact
        self.__post = post
    def set_staff_id(self,staffID):
        self.__staffID= staffID
    def get_staff_id(self):
        return self.__staffID
    def set_staff_name(self,Name):
        self.__Name= Name
    def get_staff_name(self):
        return self.__Name
    def set_staff_age(self,age):
        self.__age= age
    def get_staff_age(self):
        return self.__age
    def set_staff_combo_gender(self,combo_gender):
        self.combo_gender= combo_gender
    def get_staff_combo_gender(self):
        return self.combo_gender
    def set_staff_address(self,Address):
        self.__Address= Address
    def get_staff_address(self):
        return self.__Address
    def set_staff_email(self,email):
        self.__email= email
    def get_staff_email(self):
        return self.__email
    def set_staff_contact(self,contact):
        self.__contact= contact
    def get_staff_contact(self):
        return self.__contact
    def set_staff_post(self,post):
        self.__post= post
    def get_staff_post(self):
        return self.__post
class Menu():
    '''
    This class gets required data for food table.
    Attributes:
        foodID (int): The food id from interface entry box
        food        : The food name from interface entry box
        foodprice   : The foodprice from interface entry box
    '''
    def __init__(self, foodID, food, foodprice):
        '''
        This constructor is for Menu class.
            :param
                food_id (int)   : The food id from interface entry box
                food            : The food name from interface entry box
                foodprice       : The foodprice from interface entry box
        '''
        self.__foodID = foodID
        self.__food = food
        self.__foodprice = foodprice
    def set_food_id(self, foodID):
        self.__foodID = foodID
    def get_food_id(self):
        return self.__foodID
    def set_food_name(self, food):
        self.__food = food
    def get_food_name(self):
        return self.__food
    def set_food_price(self, foodprice):
        self.__foodprice = foodprice
    def get_food_price(self):
        return self.__foodprice
class Customer():
    '''
    This class gets required data from customer table.
    Attributes:
        customerID (int)         : The customer id from interface entry box
        customer_name            : The customer name from interface entry box
        customer_Age             : The customer age from interface entry box
        customer_combo_gender    : The customer gender from interface entry box
        customer_address         : The customer address from interface entry box
        customer_email           : The customer email from interface entry box
        customer_contact         : The customer contact from interface entry box
        foodID (int)             : The foodID from interface entry box
    '''
    def __init__(self, customerID, customer_name, customer_Age, customer_combo_gender, customer_address, customer_email,
                 customer_contact, foodID):
        '''
        This constructor is of class Customer.
        :param
            customerID (int)         : The customer id from interface entry box
            customer_name            : The customer name from interface entry box
            customer_Age             : The customer age from interface entry box
            customer_combo_gender    : The customer gender from interface entry box
            customer_address         : The customer address from interface entry box
            customer_email           : The customer email from interface entry box
            customer_contact         : The customer contact from interface entry box
            foodID (int)             : The foodID from interface entry box
        '''
        self.__customerID = customerID
        self.__customer_name = customer_name
        self.__customer_Age = customer_Age
        self.customer_combo_gender = customer_combo_gender
        self.__customer_address = customer_address
        self.__customer_email = customer_email
        self.__customer_contact = customer_contact
        self.__foodID = foodID
    def set_customer_ID(self, customerID):
        self.__customerID = customerID
    def get_customer_ID(self):
        return self.__customerID
    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name
    def get_customer_name(self):
        return self.__customer_name
    def set_customer_Age(self, customer_Age):
        self.__customer_Age = customer_Age
    def get_customer_Age(self):
        return self.__customer_Age
    def set_customer_combo_gender(self, customer_combo_gender):
        self.customer_combo_gender = customer_combo_gender
    def get_customer_combo_gender(self):
        return self.customer_combo_gender
    def set_customer_address(self, customer_address):
        self.__customer_address = customer_address
    def get_customer_address(self):
        return self.__customer_address
    def set_customer_email(self, customer_email):
        self.__customer_email = customer_email
    def get_customer_email(self):
        return self.__customer_email
    def set_customer_contact(self, customer_contact):
        self.__customer_contact = customer_contact
    def get_customer_contact(self):
        return self.__customer_contact
    def set_foodchoice(self, foodID):
        self.__foodID = foodID
    def get_foodchoice(self):
        return self.__foodID
class Del_Customer():
    '''
    This class gets required data to delete from customer table.
    Attributes:
        customerID: The customer id to delete from interface entry box
    '''
    def __init__(self, customerID):
        '''
        This constructor is for Delete_Customer class.
        :param
            customerID: The customer id to delete from interface entry box
        '''
        self.__customerID = customerID
    def set_customer_ID(self, customerID):
        self.__customerID = customerID
    def get_customer_ID(self):
        return self.__customerID
class Del_Staff():
    '''
    This class gets required data to delete from staff table.
    Attributes:
        staffID: The staff id to delete from interface entry box
    '''
    def __init__(self, staffID):
        '''
        This constructor is for Delete_Staff class.
        :param
            staffID: The staff id to delete from interface entry box
        '''
        self.__staffID= staffID
    def set_staff_id(self,staffID):
        self.__staffID= staffID
    def get_staff_id(self):
        return self.__staffID
class Del_Menu():
    '''
    This class gets required data to delete from staff table.
    Attributes:
        foodID: The food id to delete from interface entry box
    '''
    def __init__(self, foodID):
        '''
        This constructor is for Delete_Menu class.
        :param
            foodID: The food id to delete from interface entry box
        '''
        self.__foodID = foodID
    def set_food_id(self, foodID):
        self.__foodID = foodID
    def get_food_id(self):
        return self.__foodID