
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
from pystyle import *
import time
import random
import string
import requests
import fade



#email = "".join(random.choices(string.ascii_letters + string.digits, k=8)) + "@gmail.com"
password = "0xBotterEveryware"
usr = "".join(random.choices(string.ascii_letters + string.digits, k=8))

os.system("cls")
os.system('title Disckid ^| by KirawzWeb')

text = """
██████╗ ██╗███████╗ ██████╗██╗  ██╗██╗██████╗ 
██╔══██╗██║██╔════╝██╔════╝██║ ██╔╝██║██╔══██╗
██║  ██║██║███████╗██║     █████╔╝ ██║██║  ██║
██║  ██║██║╚════██║██║     ██╔═██╗ ██║██║  ██║
██████╔╝██║███████║╚██████╗██║  ██╗██║██████╔╝
╚═════╝ ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═════╝      
"""
faded_text = fade.purplepink(text)
print(faded_text)


print(Colorate.Horizontal(Colors.blue_to_purple, "https://github.com/KirawzWeb", 1))
time.sleep(3)
os.system("cls")

print(Colors.purple + "         [" + Colors.pink + "+" + Colors.purple + "]" + Colors.orange + " starting up.")
time.sleep(1)
os.system("cls")
print(Colors.purple + "         [" + Colors.pink + "+" + Colors.purple + "]" + Colors.orange + " starting up..")
time.sleep(1)
os.system("cls")
print(Colors.purple + "         [" + Colors.pink + "+" + Colors.purple + "]" + Colors.orange + " starting up...")
time.sleep(1)
os.system("cls")
print(Colors.purple + "         [" + Colors.pink + "DONE" + Colors.purple + "]")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.roblox.com/")
time.sleep(1.2)
driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[2]/div/div/button[2]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[1]/select/option[5]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[2]/select/option[6]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[3]/select/option[40]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/input").clear() 
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/input").send_keys(usr)
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[3]/input").send_keys(password)
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[4]/div/div/button[1]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div/div/div/div[1]/button").click()
time.sleep(0.1)
print(Colorate.Horizontal(Colors.blue_to_purple, " >> click on listen is completed manually << ", 1))
time.sleep(75) ##setting here
with open("accounts.txt", "a") as f:
    f.write(f"Email: {email}\nPassword: {password}\n\n")







