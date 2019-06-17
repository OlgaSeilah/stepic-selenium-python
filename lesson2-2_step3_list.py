from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x_webElement = browser.find_element_by_id("num1")
y_webElement = browser.find_element_by_id("num2")
x = x_webElement.text
y = y_webElement.text
result = str(int(x) + int(y)) #нашли сумму элементов, перевели сумму в строковый формат

result_from_list = result

select = Select(browser.find_element_by_css_selector('[id="dropdown"]')) #открыли выпадающий список
select.select_by_value(result_from_list) #выбрали нужное значение

submit_button = browser.find_element_by_css_selector('.btn')
submit_button.click()









