import unittest
from front_end.interface import *
class Search_Sort_TestCase(unittest.TestCase):
    '''
    This is a class that performs testing on sorting and searching algorithm.
    unittest.TestCase provides a base class which is used to create new test cases.
    '''
    def setUp(self):
        '''
        This method allows to define  instructions that will be executed before the each test method.
        :return: none
        '''
        pass
    def test_customer_sort(self):
        '''
        This method allows to sort values according to mergesort algorithm
        :return:None
        '''
        test_array = [(102, 'Baka', '18', 'Male', 'Baneshwor', 'arya@', '9876543', 2),
                      (101, 'Arya', '18', 'Male', 'Baneshwor', 'arya@', '9876543', 2)]
        sort_by = 0
        ascend = 'Ascend'
        expected = [(101, 'Arya', '18', 'Male', 'Baneshwor', 'arya@', '9876543', 2),
                    (102, 'Baka', '18', 'Male', 'Baneshwor', 'arya@', '9876543', 2)]
        a = Main_interface.mergeSort(test_array, sort_by , ascend)
        self.assertEqual(a, expected)
    def test_customer_searching(self):
        '''
        This method allows to search values according to Linear Search algorithm
        :return:None
        '''
        test_array = [(102, 'Baka', '18', 'Male', 'Baneshwor', 'arya@', '9876543', 2),
                      (101, 'Arya', '18', 'Male', 'Baneshwor', 'arya@', '9876543', 2)]
        search_by = 0
        item = 101
        expected = [(101, 'Arya', '18', 'Male', 'Baneshwor', 'arya@', '9876543', 2)]
        a= Main_interface.searching(test_array, search_by, item)
        self.assertEqual(a, expected)
    def tearDown(self):
        '''
        This method allows to define instructions that will be executed after each test method.
        :return: none
        '''
        self.test_customer_sort = None
        self.test_customer_searching = None
if __name__ == '__main__':
    unittest.main()
