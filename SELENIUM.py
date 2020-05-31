from selenium import webdriver

# need to make sure to have access to the chrome driver
chromeDriverLocation = '..//resourceFiles/chromedriver'
driver = webdriver.Chrome(chromeDriverLocation)
driver.get("http://www.python.org")

elem = driver.find_element_by_xpath('//*[@id="id-search-field"]')

elem.click()

elem.send_keys("Search String")
elem.submit()

# navigate back from the results page
driver.back()

# now try to grab some text on screen
elem = driver.find_element_by_xpath('//*[@id="dive-into-python"]/ul[2]/li[1]/div[2]/p')

# print it out
print(elem.text)
