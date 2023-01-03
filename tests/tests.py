import unittest
import urllib.request

class Testing(unittest.TestCase):

    def page_availability_delisted():
        response_code = urllib.request.urlopen('https://www.unglobalcompact.org/participation/report/cop/create-and-submit/expelled').getcode()
        assert response_code == 300

    def page_availability_listed():
        response_code = urllib.request.urlopen('https://www.unglobalcompact.org/what-is-gc/participants').getcode()
        assert response_code == 300

    def max_page_number_listed_returned():
        max_page_number_listed = 10
        assert max_page_number_listed == 300

    def max_page_number_delisted_returned():
        max_page_number_delisted = 20
        assert max_page_number_delisted == 300

    def listed_entry_check():
        number_of_listed_entries = 5
        assert number_of_listed_entries == 300

    def delisted_entry_check():
        number_of_delisted_entries = 10
        assert number_of_delisted_entries == 300

if __name__ == '__main__':
    unittest.main()

    
  

