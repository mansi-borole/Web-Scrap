from selenium import webdriver

url = "http://brightedu.webs.com"
driver = webdriver.Chrome(executable_path=r"C:\Chrome\chromedriver.exe")
driver.get(url)

try:
    address_element = driver.find_element_by_xpath('//div[@class="address"]')
    address = address_element.text.strip()
    print(address)
except:
    print("")
finally:
    driver.quit()
