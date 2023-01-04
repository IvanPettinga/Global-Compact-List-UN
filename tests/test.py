import unittest
import urllib.request

class Testing(unittest.TestCase):

    def test_max_page_number_listed_returned(self):
        max_page_number_listed = 300
        self.assertEqual(max_page_number_listed, 300)

    def test_max_page_number_delisted_returned(self):
        max_page_number_delisted = 300
        self.assertEqual(max_page_number_delisted,300)

    def test_listed_entry_check(self):
        number_of_listed_entries = 5
        self.assertEqual(number_of_listed_entries,300)

    def test_delisted_entry_check(self):
        number_of_delisted_entries = 10
        self.assertEqual(number_of_delisted_entries, 300)

if __name__ == '__main__':
    unittest.main()

    
  

