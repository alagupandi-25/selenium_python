import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
         

def Web_scraping() -> None:
    
    try:
        
        options = Options() 
        options.add_argument("-headless") 
        driver = webdriver.Firefox(options=options)
        print("webdriver is open")

        driver.get("https://www.amazon.in/s?k=gaming+monitor&crid=3MHDYZB2OO82H&sprefix=gaming+monitor%2Caps%2C298 &ref=nb_sb_noss_1")
        
        page_number : int = 1
          
        try:

            while True:
                
                with open("Amazon_result.txt", "a", encoding="utf-8") as file:
                    print("Started to the file")
                    
                    content =  WebDriverWait(driver, 5).until(
                                    EC.presence_of_all_elements_located(
                                        (By.CSS_SELECTOR, "div.sg-col-20-of-24")
                                    )
                                )

                    file.write("\n")

                    id_element : int = 0
                
                    for ele in content:

                        try:
                            
                            name_element = ele.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text
                            file.write(f"Product Name({id_element}) : "+ name_element+"\n")
                                    
                            image_element = ele.find_element(By.XPATH, ".//img[@class='s-image']").get_attribute("src")
                            file.write("Image url: "+image_element+"\n")

                            price_element = ele.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
                            file.write("Product Price: "+ price_element+"\n")              
                                        
                            id_element += 1
                                
                        except:
                            continue
                
                next_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator')
                    )
                )
                next_element.click()
                
                
                print("page : ",page_number)
                page_number = page_number + 1
                
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
            

