    from selenium import webdriver
import time

url = ('https://krunker.io')

driver = webdriver.Chrome('/Users/YOURLOGINUSERNAMEHERE/Downloads/chromedriver')
driver.get(url)

driver.find_element_by_class_name("Register").click()

time.sleep(2)

///if you want to make more random accs, just put whatever you want, then put a comma and put whatever you want again. :)

driver.find_element_by_id('accName').send_keys('YOURTEXTHERE')
driver.find_element_by_id('accPass').send_keys('YOURTEXTHERE')


driver.find_element_by_class_name("accountButton").click()

end
end
