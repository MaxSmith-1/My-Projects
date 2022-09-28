#Troll software
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyautogui

class VkBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://vk.com/")
        self.driver.maximize_window()

        sleep(2)


        #login
        self.driver.find_element(By.ID, "index_email").send_keys(username)
        self.driver.find_element(By.ID, "index_pass").send_keys(password)
        self.driver.find_element(By.ID, "index_login_button").click()

        sleep(2)
        #navigate/load page




        def comment():
            # click
            self.driver.find_element(By.CLASS_NAME, "wall_post_cont").click()
            #text = self.driver.find_element(By.CLASS_NAME, "wall_post_text")

            sleep(2)
            #comment
            self.driver.find_element(By.CLASS_NAME, "reply_field").send_keys("Путин платит за то, чтобы люди ходили на его митинги :(")

            self.driver.find_element(By.CLASS_NAME, "reply_field").send_keys(Keys.ENTER)
            sleep(2)
            # exit
            self.driver.find_element(By.CLASS_NAME, "pv_close_btn").click()
            sleep(2)

            threeDots = self.driver.find_element(By.CSS_SELECTOR, "#more_horizontal_24__Mask")

            actions = ActionChains(self.driver)
            actions.move_to_element(threeDots).perform()

            sleep(2)
            pyautogui.click(x=1100, y=450)


            sleep(2)

        a = 1
        while a > 0:
            comment()






#pv_nav_btn, pv_nav_btn_show

#exicutable file

#reply_fakebox
count = 0

VkBot("your phone number", "your password")


