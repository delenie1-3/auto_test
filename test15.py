import math
from selenium import webdriver
import time


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    num1 = browser.find_element_by_id('input_value')
    n1 = num1.text
    s = calc(n1)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(s)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()