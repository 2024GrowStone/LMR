# crawling.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time, os


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
                    EC.presence_of_element_located((By.XPATH, "//*[@id='majors']/div[1]/a[4]"))
        )
        keyword_btn.click()
        time.sleep(2)
        # search
        search_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form[5]/div/input"))
        )
        search_input.send_keys(f"{self.major}\n")

        evaluation_page = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='majors']/div[2]/table/tbody/tr[1]/td[8]"))
        )
        evaluation_page.click()


if __name__=="__main__":
    load_dotenv()
    EVERY_ID = os.getenv("ID")
    EVERY_PW = os.getenv("PW")
    crawler = EverytimeCrawler(EVERY_ID, EVERY_PW, "객체지향프로그래밍1")
    crawler.crawling()
