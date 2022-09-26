from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

threeDots = self.driver.find_element(By.CSS_SELECTOR, "#more_horizontal_24__Mask")
            notInterested = self.driver.find_element(By.XPATH, "//*[@id='post-40498005_4370929']/div/div[1]/div[2]/div/div/div/div/a[1]")
#
            actions = ActionChains(self.driver)
            actions.move_to_element(threeDots).move_to_element(notInterested).click().perform()
