import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id('num1')
    n1 = num1.text
    num2 = browser.find_element_by_id('num2')
    n2 = num2.text
    s = str(int(n1) + int(n2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()