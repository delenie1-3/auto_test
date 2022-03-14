from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

browser.get(link)

# говорим Selenium проверять в течение 5 секунд, пока 
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) 

button = browser.find_element_by_tag_name("button")
button.click()

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
num1 = browser.find_element_by_id('input_value')
n1 = num1.text
s = calc(n1)
input1 = browser.find_element_by_id('answer')
input1.send_keys(s)
button = browser.find_element_by_id("solve")
button.click()