from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

url = 'https://vk.com/'

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()

#login
driver.find_element(By.ID, "index_email").send_keys("your phone number")
driver.find_element(By.ID, "index_pass").send_keys("your password")
driver.find_element(By.ID, "index_login_button").click()

sleep(2)

def andMayGodBlessTheseUnitedStatesOfAmerica():
    #comment
    driver.find_element(By.CLASS_NAME, "wall_post_cont").click()
    driver.find_element(By.CLASS_NAME, "reply_field").send_keys("Путин платит за то, чтобы люди ходили на его митинги :(")
    driver.find_element(By.CLASS_NAME, "reply_field").send_keys(Keys.ENTER)
    sleep(2)

    # exit
    driver.find_element(By.CLASS_NAME, "pv_close_btn").click()
    sleep(2)

    #notInterested ;)
    threeDots = driver.find_element(By.CSS_SELECTOR, "#more_horizontal_24__Mask")
    notInterested = driver.find_element(By.XPATH, "//*[@id='post-40498005_4370929']/div/div[1]/div[2]/div/div/div/div/a[1]")

    actions = ActionChains(driver)
    actions.move_to_element(threeDots).move_to_element(notInterested).click().perform()

a = 0

while a < 1:
    andMayGodBlessTheseUnitedStatesOfAmerica()
