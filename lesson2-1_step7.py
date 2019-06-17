from selenium import webdriver
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element_by_css_selector('[id="treasure"]')
x = x.get_attribute('valuex')

result = calc(x)

input = browser.find_element_by_css_selector('[id="answer"]')
input.send_keys(result)

checkbox = browser.find_element_by_css_selector('[id="robotCheckbox"]')
checkbox.click()
roboruler_button = browser.find_element_by_css_selector('[id="robotsRule"]')
roboruler_button.click()

btn_submit = browser.find_element_by_css_selector('.btn-default')
btn_submit.click()