from selenium import webdriver

username = "alikhandkk81"
password = "123456"

url = "https://www.facebook.com/"

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")

driver.get(url)


driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()
