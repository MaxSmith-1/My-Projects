#Troll software
#use vpn for security if your saying something provocative
#Breaks for posts with comments turned off, and some video posts
#Breaks just after making second comment on ideal run
from selenium import webdriver
from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
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



        #navigate/load page
        try:
            self.actions = ActionChains(self.driver)
            self.ignore = self.driver.find_element(By.CLASS_NAME, "PostHeaderActionsButtonMoreIcon")
        except StaleElementReferenceException:
            self.actions = ActionChains(self.driver)
            self.ignore = self.driver.find_element(By.CLASS_NAME, "PostHeaderActionsButtonMoreIcon")


        def comment():
            # click


            #comment
            try:

                sleep(4)
                self.driver.find_element(By.CLASS_NAME, "reply_field").send_keys("привет")
#"дети Украины ;( https://www.youtube.com/watch?v=_fFOYnKT4lg")

                self.driver.find_element(By.CLASS_NAME, "reply_field").send_keys(Keys.ENTER)

                sleep(1)
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                #self.driver.find_element(By.CLASS_NAME, "pv_close_btn").click()


            except StaleElementReferenceException:
                sleep(1)
                self.driver.find_element(By.CLASS_NAME, "reply_field").send_keys("привет")
            # "дети Украины ;( https://www.youtube.com/watch?v=_fFOYnKT4lg")

                self.driver.find_element(By.CLASS_NAME, "reply_field").send_keys(Keys.ENTER)

                sleep(1)
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            except NoSuchElementException:
                sleep(1)
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                #self.driver.find_element(By.CLASS_NAME, "pv_close_btn").click()
                self.actions.move_to_element(self.ignore).perform()
                self.driver.find_element(By.LINK_TEXT, 'Not interesting').click()
                sleep(2)
                self.driver.refresh()


            # exit

            #sleep(2)
            #self.driver.find_element(By.CLASS_NAME, "PostHeaderActionsUiActionMenu").click()
            #sleep(2)
            #self.driver.find_element(By.LINK_TEXT, "Not interesting").click()
            # refresh


        a = True
        while a:
            sleep(2)

            try:
                self.driver.find_element(By.CLASS_NAME, "wall_post_cont").click()

            except StaleElementReferenceException:
                b = self.driver.find_element(By.CLASS_NAME, "wall_post_cont")
                b.click()



            #self.driver.find_element(By.CLASS_NAME, "wall_post_cont")


            try:
                comment()
            except StaleElementReferenceException:
                comment()

            try:
                self.actions.move_to_element(self.ignore).perform()
                self.driver.find_element(By.LINK_TEXT, 'Not interesting').click()
                sleep(2)
                self.driver.refresh()
            except StaleElementReferenceException:
                self.actions.move_to_element(self.ignore).perform()
                self.driver.find_element(By.LINK_TEXT, 'Not interesting').click()
                sleep(2)
                self.driver.refresh()

            #self.driver.find_element(By.CLASS_NAME, "wall_post_cont").click()
            #sleep(2)







#pv_nav_btn, pv_nav_btn_show

#exicutable file

#reply_fakebox
count = 0

b = True
while b:
    VkBot("your phone number", "your password")





