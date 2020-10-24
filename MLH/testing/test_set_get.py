import unittest
from model_class.model import *
class FoodTestCase(unittest.TestCase):
    '''
    This is a class that performs testing on sorting and searching algorithm.
    unittest.TestCase provides a base class which is used to create new test cases.
    '''
    def setUp(self):
        '''
        This method allows to define  instructions that will be executed before the each test method.
        :return: none
        '''
        self.menu = Menu(1,'Pizza','300')
    def test_get_foodid(self):
        self.assertEqual(1, self.menu.get_food_id())
    def test_get_foodname(self):
        self.assertEqual('Pizza', self.menu.get_food_name())
    def test_get_foodprice(self):
        self.assertEqual('300', self.menu.get_food_price())
    def test_set_foodid(self):
        self.menu.set_food_id(4)
        self.assertEqual(4, self.menu.get_food_id())
    def test_set_foodname(self):
        self.menu.set_food_name('Popcorn')
        self.assertEqual('Popcorn', self.menu.get_food_name())
    def test_set_foodprice(self):
        self.menu.set_food_price('500')
        self.assertEqual('500', self.menu.get_food_price())
    def tearDown(self):
        self.menu= None
class FooddelTestCase(unittest.TestCase):
    '''
    This is a class that performs testing on sorting and searching algorithm.
    unittest.TestCase provides a base class which is used to create new test cases.
    '''
    def setUp(self):
        '''
        This method allows to define  instructions that will be executed before the each test method.
        :return: none
        '''
        self.del_menu = Del_Menu(1)
    def test_get_del_menu(self):
        self.assertEqual(1, self.del_menu.get_food_id())
    def test_set_del_menu(self):
        self.del_menu.set_food_id(2)
        self.assertEqual(2, self.del_menu.get_food_id())
    def tearDown(self):
        '''
        This method allows to define instructions that will be executed after each test method.
        :return: none
        '''
        self.del_menu = None
if __name__ == '__main__':
    unittest.main()