import unittest
from Back_end.working import *
class EmployeeTestCase(unittest.TestCase):
    '''
    This is a class that performs testing on sorting and searching algorithm.
    unittest.TestCase provides a base class which is used to create new test cases.
    '''
    def setUp(self):
        '''
        This method allows to define  instructions that will be executed before the each test method.
        :return: none
        '''
        self.con = Connection()
    def test_insert(self):
        '''
        This method allows to test insert function working
        :return: none
        '''
        query = "insert into staffs values(%s,%s,%s,%s,%s,%s,%s,%s);"
        values = (35,'Arya','18','Male','Baneshwor','arya@gmail.com','9841222','Head Chef')
        self.con.insert(query, values)
        query = "select * from staffs where staffID=%s;"
        values = (35,)
        actual = self.con.selectuser(query, values)
        expect = (35, 'Arya', '18', 'Male', 'Baneshwor', 'arya@gmail.com', '9841222', 'Head Chef')
        self.assertEqual(expect, actual)
    def test_update(self):
        '''
        This method allows to test update function working
        :return: none
        '''
        query = 'update staffs set Name=%s,age=%s,combo_gender=%s,Address=%s,email=%s, contact=%s ,post=%s WHERE staffID=%s;'
        values = ('Arya','20','Male','Baneshwor','arya@gmail.com','9841222','Chef', 35)
        self.con.update(query, values)
        query = "select * from staffs where staffID=%s;"
        values = (35,)
        actual = self.con.selectuser(query, values)
        expected = (35,'Arya','20','Male','Baneshwor','arya@gmail.com','9841222','Chef')
        self.assertEqual(expected,actual)
        query ="delete from staffs where staffID=%s;"
        self.con.delete(query,values)
    def tearDown(self):
        '''
        This method allows to define instructions that will be executed after each test method.
        :return: none
        '''
        self.con = None
        self.test_insert = None
        self.test_update = None
if __name__ == '__main__':
    unittest.main()
