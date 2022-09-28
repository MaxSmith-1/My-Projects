from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyautogui

url = 'https://vk.com/'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

#login
driver.find_element(By.ID, "index_email").send_keys("your phone number")
driver.find_element(By.ID, "index_pass").send_keys("your password")
driver.find_element(By.ID, "index_login_button").click()

sleep(2)

def type():
#comment
    driver.find_element(By.CLASS_NAME, "wall_post_cont").click()

# exit
    sleep(2)
    driver.find_element(By.CLASS_NAME, "pv_close_btn").click()
    sleep(2)

#notInterested ;)
    threeDots = driver.find_element(By.CSS_SELECTOR, "#more_horizontal_24__Mask")

    actions = ActionChains(driver)
    actions.move_to_element(threeDots).perform()

    #pyautogui.click(x=1075, y=507)
#notInteresting = driver.find_element(By.XPATH, '//*[@id="post-40498005_4364290"]/div/div[1]/div[2]/div/div/div/div/a[1]')


a = 1

while a > 0:
    type()





