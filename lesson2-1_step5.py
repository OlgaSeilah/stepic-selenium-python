from selenium import webdriver
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('[id="input_value"]')
x = x_element.text
y = calc(x)


input_result = browser.find_element_by_css_selector('.form-control')
input_result.send_keys(y)

checkbox = browser.find_element_by_css_selector('[id="robotCheckbox"]')
checkbox.click()
roboruler_button = browser.find_element_by_css_selector('[id="robotsRule"]')
roboruler_button.click()

btn_submit = browser.find_element_by_css_selector('.btn-default')
btn_submit.click()
