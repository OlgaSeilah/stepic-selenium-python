from selenium import webdriver
import math

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_webElement = browser.find_element_by_id("input_value")
x = x_webElement.text

input = browser.find_element_by_id('answer')
input.send_keys(calc(x))

submitButton = browser.find_element_by_tag_name('button')
browser.execute_script("return arguments[0].scrollIntoView(true);", submitButton)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

radioButton = browser.find_element_by_id('robotsRule')
radioButton.click()

submitButton = browser.find_element_by_css_selector('.btn-default')
submitButton.click()



