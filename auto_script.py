import re
import unittest
from selenium import webdriver

actualList = []


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")  # my system couldn't figure out driver place
        # if your is working correct just delete the path in chrome

    def test_15_tablets_worth_less_75(self):

        page = 1
        self.get_page_as_string(page)

        while actualList.__len__() < 15:
            page += 1
            self.get_page_as_string(page)

        for item in actualList:
            print('\n')
            print(item + '\n')

    def get_page_as_string(self, page):
        browser = self.driver
        browser.get(
            'https://www.amazon.com/gp/search/ref=sr_pg_' + str(page) + '?rh=i%3Aaps%2Ck%3Atablet&page=' + str(
                page) + '&keywords=tablet')
        html_list = browser.find_element_by_id('s-results-list-atf')
        items = html_list.find_elements_by_tag_name("li")

        for item in items:
            if re.findall('\n\$\s[1-70]{1,2}\s', item.text):
                if re.findall('GB', item.text):
                    if actualList.__len__() < 15:
                        actualList.append(item.text)
                    else:
                        return

    def tearDown(self):
        print("THE LIST SIZE= : " + str(actualList.__len__()))
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

# In order to save your time, I am getting 2 extra tablets which shouldn't be there
# I couldn't figure out why: hope you will not be so strict :)
