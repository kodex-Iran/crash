from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
from selenium.webdriver.common.keys import Keys
from instaLogin import instaLogins
from mysql import connector
from randoms import randompy
perday = 1
maxlikes = 680
maxComment = 170
maxfallow = 130 
username = "cobco_perfume_ca"
password = "perfumec0rp0ratio"


"""
--------------------------------------------
|
|
|       MY SQL CONNECTION 
|-------------------------------------------
"""
mydb = connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_instabot"
)
mycursor = mydb.cursor()
excutable = mydb.cursor(dictionary=True)

"""
--------------------------------------------
|
|
|       LOG IN TO INSTAGRAM 
|-------------------------------------------
"""
# browser = webdriver.Chrome("chromedriver.exe")
# browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
# browser.maximize_window()
# find_serial = browser.find_element_by_css_selector("[name='username']")
# find_serial.send_keys(username)
# find_serial = browser.find_element_by_css_selector("[name='password']")
# find_serial.send_keys(password)
# find_serial = browser.find_element_by_css_selector("[type='submit']")
# find_serial.click()
# clickurl = str("https://www.instagram.com/accounts/onetap/?next=%2F")
# while (browser.current_url != clickurl):
#     time.sleep(10) # Delay for 1 minute (60 seconds).
#     print("10 sec pass")
# print ("while ended")
# find_serial = browser.find_element_by_css_selector(".sqdOP.L3NKy.y3zKF")
# find_serial.click()
# time.sleep(10)
# find_serial = browser.find_element_by_css_selector(".aOOlW.bIiDR")
# find_serial.click()
# print ("alow btn clicked")
sql = "Select * from urls where(description = 'posts')"
excutable.execute(sql)
myresult = excutable.fetchall()
try:
    print("row count")
    print(excutable.rowcount)
except:
    print('lo')
def liking():    
    for x in myresult:
        randnum =  randompy.likerandom()
        print(randnum)  

liking()        
