import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id('input_value')
    n1 = num1.text
    s = calc(n1)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(s)

    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    
    option2 = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()