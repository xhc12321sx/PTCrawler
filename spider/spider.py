import time
import urllib
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import re

class spider(object):
    def __init__(self, headless=True, dtLoadPicture=True, disableGPU=True):
        self.chrome_option = webdriver.ChromeOptions()

        if dtLoadPicture == True:
            prefs = {"profile.managed_default_content_settings.images":2}
            self.chrome_option.add_experimental_option("prefs",prefs)
        if headless == True:
            self.chrome_option.add_argument("--headless")
        if disableGPU == True:
            self.chrome_option.add_argument("--disable-gpu")
        

        self.chrome_option.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1')

        self.browser = None

        self.start_browser()

    def boot_up_browser(self):
        self.browser = webdriver.Chrome(options=self.chrome_option)
        self.browser.implicitly_wait(10)

    def start_browser(self):
        self.boot_up_browser()
        pass

    def get_url(self, url):
        pass

    def img_tag(self):
        pass

    def download(self, urls, filenames, path):
        print("Start downloading...")
        l = len(urls)

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1')]
        urllib.request.install_opener(opener)

        for i in range(l):
            print("  page {0:03d}/{1}".format(i + 1, l))        
            urllib.request.urlretrieve(urls[i], path + "/" + filenames[i])
        pass


class u2spider(spider):
    def __init__(self, cookie, headless=True, dtLoadPicture=True, disableGPU=True):
        super().__init__(headless=headless, dtLoadPicture=dtLoadPicture, disableGPU=disableGPU)
        self.cookie = cookie
        print("Getting torrent page...")
        url = "https://u2.dmhy.org/torrents.php"
        self.browser.get(url)
        for cookie in self.cookie:
            self.browser.add_cookie(cookie)
        self.browser.get(url)

    def get_torrent_page(self):
        print("Getting torrent page...")
        url = "https://u2.dmhy.org/torrents.php"
        self.browser.get(url)
        for cookie in self.cookie:
            self.browser.add_cookie(cookie)
        self.browser.get(url)

    def parse_page(self):
        self.parse_note()
        self.parse_torrents()
        pass

    def parse_note(self):
        refresh = self.browser.find_element_by_id("sh_refresh")
        refresh.click()

        iframe = self.browser.find_element_by_id("scrollee").find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        soup = BeautifulSoup(self.browser.page_source, "lxml")
        # all notes with 魔法
        note_list_all = soup.select("td[class='shoutrow']")[0].find_all(self.my_tag)
        note_list = [None] * len(note_list_all)
        for i in range(len(note_list_all)):
            note_list[i] = note_list_all[i].select("bdo")[0].text
            pass

        print("魔法：")
        for i in note_list:
            print("  {0}".format(i))
            pass

        self.browser.switch_to.default_content()
        # note_list = note_list.find_e
        pass

    @staticmethod
    def my_tag(tag):
        return tag.name == "div" and re.match("魔法使", tag.select("bdo")[0].text)

    def parse_torrents(self):
        # torrent_list = self.browser.find_element_by_class_name("torrents").find_element_by_tag_name("tbody").find_elements_by_xpath("./*")
        pass


if __name__ == "__main__":
    cookie = [
        {
            "domain": "u2.dmhy.org",
            "name": "PHPSESSID",
            "value": "683e9ca68ec7e23ec6d6711d0ab40ab4",
            }, 
            {
                "domain": ".dmhy.org",
                "name": "__cfduid",
                "value": "ddf8e87e35543daaa82a7a8642e93c5ec1575669957",
            }, 
            {
                "domain": "u2.dmhy.org",
                "name": "nexusphp_u2",
                "value": "668a2ede564b45e05daa400b17d288ec983642f1a64626bd79a2ce222aecd5ce624612cbae43aa6b0e7cd0bddd3281a1",
            }
            ]
    a = u2spider(headless=False, dtLoadPicture=False, cookie=cookie)
    a.parse_page()
    pass