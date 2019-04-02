# import driver

def send_keys(driver,xpath,text):
    username = driver.find_element_by_xpath(xpath)
    username.clear()
    username.send_keys(text)

#
#
def click (driver,xpath):
    djej = driver.find_element_by_xpath(xpath)
    djej.click()