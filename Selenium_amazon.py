from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

try:
    
    title = "Selenium Amazon Search Result"

    print(f"--------------------------------------{title}--------------------------------------")

    driver = webdriver.Firefox()
    print("webdriver is open")

    driver.get("https://www.amazon.in/s?k=gaming+monitor&crid=3MHDYZB2OO82H&sprefix=gaming+monitor%2Caps%2C298&ref=nb_sb_noss_1")

    content = driver.find_elements(By.CSS_SELECTOR,"div.sg-col-20-of-24")

    print("\n")

    for ele in content:
        try:

            text_element = ele.find_element(By.XPATH,".//span[@class='a-size-medium a-color-base a-text-normal']")
            print("Product Name : ",text_element.text)
            
            text_element = ele.find_element(By.XPATH,".//span[@class='a-price-whole']")
            print("Product Price: ",text_element.text)

            print("\n")

        except:
            continue  

    sleep(4)

finally:
    driver.quit() 
    print("webdriver is close")


