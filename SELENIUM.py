from selenium import webdriver

# need to make sure to have access to the chrome driver
# create a resourceFiles Subfolder and make sure chromedriver is there
chromeDriverLocation = 'resourceFiles/chromedriver'


driver = webdriver.Chrome(chromeDriverLocation)
driver.get("http://www.python.org")

elem = driver.find_element_by_id("submit")

elem.click()

# navigate back from the results page
driver.back()

# now try to grab some text on screen
elem = driver.find_element_by_xpath('//*[@id="dive-into-python"]/ul[2]/li[1]/div[2]/p')

# print it out
print(elem.text)
