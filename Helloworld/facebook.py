from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import csv
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option, executable_path='D:/chromedriver_win32/chromedriver.exe')
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.find_element_by_id("twotabsearchtextbox").send_keys('nokia')
driver.find_element_by_id("nav-search-submit-button").click()
content = driver.find_elements_by_xpath("//a[@class='a-link-normal a-text-normal']")
stars = driver.find_elements_by_xpath("//span[@class='a-declarative']/a/i/span")
prices = driver.find_elements_by_xpath("//span[@class='a-price']")
mobilename =[]
cost=[]
for i in content:
    mobilename.append(i.text)
print('***************************')
for price in prices:
    cost.append(price.text)

print(mobilename)
print(cost)


with open('C://Users//AL3500//Desktop//amazon.csv','w',encoding="utf-8", newline='') as f:
    w = csv.writer(f)
    w.writerow(["productname","price"])
    for mobile in range(len(mobilename)):
        for costs in range(len(cost)):
            if(mobile == costs):
                w.writerow([mobilename[mobile], cost[costs]])
                break

print('i think its working fine')





