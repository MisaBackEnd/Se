from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options=webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Remote(
    command_executor='http://localhost:4444',
    options=options
)
driver.get("http://www.python.org")
assert "Python" in driver.title
print(driver.title)
driver.save_screenshot("fromgrid2.png")
print(driver.capabilities['browserVersion'])
print(driver.capabilities)
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()