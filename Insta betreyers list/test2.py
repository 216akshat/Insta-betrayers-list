from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
username=input("enter the username: ")
password=input("enter the password: ")
followercount=int(input("enter numbers of followers: "))
followingcount=int(input("enter numbers of following: "))
# ChromeDriver ka path set karein using webdriver-manager (automatically driver ko manage karega)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Instagram login page par jaayein
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the page to load
time.sleep(3)

# Instagram ID aur password ke fields ko locate karein
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

# Apna username aur password daalein
username_field.send_keys(username)
password_field.send_keys(password)

# Login button ko locate karke click karein
password_field.send_keys(Keys.RETURN)

# Wait for login to complete
time.sleep(5)

# Followers list ko open karein
driver.get(f"https://www.instagram.com/{username}/followers/")
driver.maximize_window()

# Wait for the page to load
time.sleep(3)
follower_name_field=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span")
follower_name_field.click()
time.sleep(3)

followers = []
for i in range(1,followercount+1):
 follower_name = driver.find_element(By.CSS_SELECTOR,f"body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 > div:nth-child(1) > div > div:nth-child({i}) > div > div > div > div.x9f619.x1ja2u2z.x78zum5.x1n2onr6.x1iyjqo2.xs83m0k.xeuugli.x1qughib.x6s0dn4.x1a02dak.x1q0g3np.xdl72j9 > div > div > span").text
 if(i%10==0):
     time.sleep(2)
  
 followers.append(follower_name)
time.sleep(3)
x=driver.find_element(By.CSS_SELECTOR,"body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.x1qjc9v5.x78zum5.xdt5ytf > div > div._ac7b._ac7d > div > button > div > svg")
x.click()
time.sleep(3)
following_name_field=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span")
following_name_field.click()
time.sleep(3)
following=[]
for i in range(1,followingcount+1):
 following_name=driver.find_element(By.CSS_SELECTOR,f"body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 > div:nth-child(1) > div > div:nth-child({i}) > div > div > div > div.x9f619.x1ja2u2z.x78zum5.x1n2onr6.x1iyjqo2.xs83m0k.xeuugli.x1qughib.x6s0dn4.x1a02dak.x1q0g3np.xdl72j9 > div > div > span > span").text
 if(i%10==0):
        
        time.sleep(2)
 following.append(following_name)
time.sleep(3)    
 



betrayers=[]
for i in following:
    if i not in followers:
        betrayers.append(i)
print(f"betrayers list: {betrayers}")       
