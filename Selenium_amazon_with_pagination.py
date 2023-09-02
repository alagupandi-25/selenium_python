import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def Web_scraping():
    try:
 
        driver = webdriver.Firefox()
        print("webdriver is open")

        driver.get("https://www.amazon.in/s?k=gaming+monitor&crid=3MHDYZB2OO82H&sprefix=gaming+monitor%2Caps%2C298 &ref=nb_sb_noss_1")
        
        i = 1
        
        while True:
            try:
                next_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator')))

                next_element.click()
                
                print("page : ",i)
                i = i + 1
                
            except TimeoutException:
                time.sleep(5)
                print("no next eleement")

    finally:
        driver.quit()
        print("webdriver is close")


if __name__ == "__main__":

    title = "Selenium Amazon Search Result"
    print(f"--------------------------------------{title}--------------------------------------")

    Web_scraping()
            

