from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
y=input("ENTER THE NAME WHOM YOU WANT TO SEND MSG:")
print("ENTER THE TEXT TO BE SENT")
x=sys.stdin.readlines()

path="C:\Program Files\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://web.whatsapp.com/")
time.sleep(10)
search=driver.find_element_by_xpath("//span[@title='{}']".format(y))
search.click()
msg=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
time.sleep(10)
for i in x:
    msg.send_keys(i)
    msg.send_keys(Keys.RETURN)
# driver.quit()
