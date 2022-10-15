#Troll software
#use vpn for security if your saying something provocative
#Breaks for posts with comments turned off, and some video posts
from selenium import webdriver
from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, \
    ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

from webdriver_manager.chrome import ChromeDriverManager


class VkBot:
    def __init__(self, username, password):

        self.ser = Service("C:\\webdrivers_\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.ser)
        self.driver.get("https://vk.com/")
        self.driver.maximize_window()

        sleep(2)


        #login


        self.driver.find_element(By.ID, "index_email").send_keys(username)

        self.driver.find_element(By.CLASS_NAME, "VkIdForm__signInButton").click()
        sleep(11)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "vkuiButton__in").click()
        sleep(15)

        self.rows = []
        self.rows = self.driver.find_elements(By.CLASS_NAME, "feed_row")




        print(self.rows)
        self.num = 0

        for self.i in self.rows:
            self.i.click()


            try:
            #self.driver.find_element(By.CLASS_NAME, "wall_post_cont").click()

                sleep(1)
                self.driver.find_element(By.CLASS_NAME, "reply_field").send_keys("дети Украины ;( https://www.youtube.com/watch?v=_fFOYnKT4lg")


                self.driver.find_element(By.CLASS_NAME, "reply_field").send_keys(Keys.ENTER)

                sleep(1)
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            # self.driver.find_element(By.CLASS_NAME, "pv_close_btn").click()
                sleep(1)
            except NoSuchElementException:
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                sleep(1)
            except ElementNotInteractableException:
                self.num+=1



VkBot("+your phone number", "your password")
