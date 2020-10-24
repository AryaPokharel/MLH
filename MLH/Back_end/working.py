import mysql.connector
class Connection():
        '''
        This class configures the connection object for interface along with backend works with
        creation of database and tables required.
        '''
        def __init__(self):
            '''
            This constructor is for Connection class.
            '''
            self.con= mysql.connector.connect(host='localhost', user='root',password='Pokharelaryapass1.')
            self.cursor=self.con.cursor()
            self.cursor.execute('create database if not exists restaurantmanagement;')
            self.cursor.execute('USE restaurantmanagement;')
            self.cursor.execute(
                'create table if not exists users(userid int not null, username varchar(45) not null,'
                'password varchar(45) not null, primary key (userid));')
            self.cursor.execute(
                'create table if not exists menu(foodID int not null, food varchar(45) not null,'
                'foodprice varchar(10) not null, primary key (foodID));')
            self.cursor.execute(
                'create table if not exists customers(customerID int not null, customer_name varchar(45) not null,'
                'customer_Age varchar(5) not null, customer_combo_gender varchar(20)  not null,'
                'customer_address varchar(45) not null,customer_email varchar(45) not null,'
                'customer_contact varchar (20) not null,foodID int not null, primary key (customerID));')
            self.cursor.execute(
                'create table if not exists staffs(staffID int not null, Name varchar(45) not null,'
                'age varchar(5) not null, combo_gender varchar(20) not null,Address varchar(45) not null, '
                'email varchar(45) not null,contact varchar (20) not null, post varchar(45) not null, primary key (staffID));')
        def selectuser(self, query, values):
            """Select particular data from the database
            :param
                query : This parameter is to specify the query for execution.
                values : This parameter is used to store the data to be selected.
            :return records:This returns the selected data
                    """
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()
            return records
        def insert(self, query, values):
            """Insert data in the database
                    :param
                        query : This parameter is to specify the query for execution.
                        values : This parameter is used to store the data.
                    :return None
            """
            self.cursor.execute(query, values)
            self.con.commit()

        def update(self, query, values):
            """Update the data in the database
            :param
                query : This parameter is to specify the query for execution.
                values : This parameter is used to store the entered data.
            :return None
                    """
            self.cursor.execute(query, values)
            self.con.commit()

        def delete(self, query, values):
            """Delete the data in the database
                :param
                    query : This parameter is to specify the query for execution.
                    values : This parameter is used to store the entered data.
                :return None
            """
            self.cursor.execute(query, values)
            self.con.commit()

        def select(self, query):
            """Select all data from the database
            :param
                query : This parameter is to specify the query for execution.
                values : This parameter is used to store the data.
            :return records:This returns the data
                    """
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            self.con.commit()
            return records
        def destroy(self):
            """Closing the cursor and connection objects
                        :return None
            """
            if self.cursor:
                self.cursor.close()
            if self.con:
                self.con.close()