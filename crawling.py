# crawling.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time, os

import requests
from lxml import html


class EverytimeCrawler:

    def __init__(self, id: str, pw: str, major: str):
        """
        Crawling professors' evaluation on EveryTime.

        :params id:     EveryTime id
        :params pw:     EveryTime password
        :params major:  major name
        """

        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options)

        self.driver.implicitly_wait(15)
        # user's information
        self.id = id
        self.pw = pw
        self.major = major

    def crawling(self):
        self.login_everytime()
        self.get_evaluation()

        time.sleep(2)
        self.driver.quit()


    def login_everytime(self):
        """
        login function
        """
        self.driver.get("https://account.everytime.kr/login")
        login_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/div[1]/input[1]"))
        )
        login_btn.send_keys(self.id)

        time.sleep(1) # wait for 1 second.
        
        pw_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/div[1]/input[2]"))
        )
        pw_btn.send_keys(f"{self.pw}\n")


    def get_evaluation(self):
        """
        get professors' evaluations
        """
        # move to target page
        navigation = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='menu']/li[2]/a"))
        )
        navigation.click()

        # open and search major
        search_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='container']/ul/li[1]"))
        )
        search_btn.click()
        time.sleep(2)
        keyword_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='subjects']/div[1]/a[4]"))
        )
        keyword_btn.click()
        time.sleep(2)
        
        # search major
        search_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='subjectKeywordFilter']/div/input"))
        )
        search_input.send_keys(f"{self.major}\n")


        # //*[@id="subjects"]/div[2]/table/tbody/tr[1]/td[8]/a
        # //*[@id="subjects"]/div[2]/table/tbody/tr[2]/td[8]/a

        with requests.Session() as s:
            for cookie in self.driver.get_cookies():
                c = {cookie["name"]: cookie["value"]}
                s.cookies.update(c)
        headers = {'User-Agent': 'MyUserAgent/1.0'}
        url = 'https://everytime.kr/timetable'  # 여기에 실제 URL을 입력하세요
        response = s.get(url, headers=headers)
        print(response)

        # HTML 파싱
        tree = html.fromstring(response.content)

        # XPath를 사용하여 href 속성 추출
        xpath = '//*[@id="subjects"]/div[2]/table/tbody/tr[1]/td[8]/a'
        element = tree.xpath(xpath)

        if element:
            href = element[0].get('href')
            print(f"href: {href}")
        else:
            print("해당 XPath에 요소를 찾을 수 없습니다.")


if __name__=="__main__":
    load_dotenv()
    EVERY_ID = os.getenv("ID")
    EVERY_PW = os.getenv("PW")
    crawler = EverytimeCrawler(EVERY_ID, EVERY_PW, "객체지향프로그래밍1")
    crawler.crawling()
