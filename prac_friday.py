import time
import selenium
import os
import random
from PIL import Image , ImageEnhance
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

byfly_link = "https://issaold.beltelecom.by/main.html"





class Parcer():

    def __init__(self, byfly_link , captcha_solve_link , login , password, listOurInformation):
        self.byfly_link = byfly_link
        self.captcha_solve_link = captcha_solve_link
        self.login = login
        self.password = password
        self.listOutInformation = listOurInformation


    def registrate(self):
        driver = webdriver.Chrome()
        driver.get(self.byfly_link)

        login_field = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/form/div/div[1]/input")
        login_field.click()
        login_field.clear()
        login_field.send_keys("12")



        password_field = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/form/div/div[2]/input")

        password_field.click()
        password_field.clear()
        password_field.send_keys("34")

        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

        chapth_imd = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/form/div/div[3]/img")

        captcha_path = 'screenshots/captcha.png'
        chapth_imd.screenshot(captcha_path)


        time.sleep(10)

        driver.quit()



    def changeImage(self):
        image = Image.open('screenshots/captcha.png')


if __name__ == "__main__":
    my_parser = Parcer(
        byfly_link = "https://issaold.beltelecom.by/main.html" ,
        captcha_solve_link="ссылка_на_капчу",
        login="12",
        password="34",
        listOurInformation=[]
    )


    my_parser.registrate()
    my_parser.changeImage   

