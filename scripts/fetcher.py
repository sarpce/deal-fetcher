import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Fetcher:
    def __init__(self):
        service = Service('../util/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def get_page_html(self, url):
        try:
            self.driver.get(url)
            self.driver.refresh()
            time.sleep(0.5)
            inner_html = self.driver.execute_script(
                "return document.getElementsByTagName('html')[0].innerHTML")
            return inner_html
        except Exception:
            return None
