import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import time
         
         
def Write_image(id_element : int ,image_response,page_number : int) -> None:

    image_folder = os.getcwd() + "\Amazon_result_image"

    if os.path.exists(image_folder) == False:
        os.mkdir(image_folder)
                
    if image_response.status_code == 200:
        with open(f'{image_folder}\\{page_number}-{id_element}.png', 'wb') as image_file:
            image_file.write(image_response.content)
                        
    else:
        print(f'Failed to download image-{id_element}')

def Web_scraping() -> None:
    
    try:
        
        options = Options() 
        options.add_argument("-headless") 
        driver = webdriver.Firefox(options=options)
        print("webdriver is open")

        driver.get("https://www.amazon.in/")

        input_var = str(input("Enter the Keyword to extract in amazon : "))

        search_bar =  WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located(
                                (By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
                            )
                        )
        search_bar.send_keys(input_var)
        search_bar.send_keys(Keys.RETURN)

        time.sleep(5)
        
        driver.get("https://www.amazon.in/s?k=gaming+monitor&crid=3MHDYZB2OO82H&sprefix=gaming+monitor%2Caps%2C298 &ref=nb_sb_noss_1")
        
        page_number : int = 1
          
        try:

            while True:
                
                with open("Amazon_result.txt", "a+", encoding="utf-8") as file:
                    print("Started to the file")
                    
                    content =  WebDriverWait(driver, 5).until(
                                    EC.presence_of_all_elements_located(
                                        (By.CSS_SELECTOR, "div.sg-col-20-of-24.s-result-item.s-asin.sg-col-0-of-12.sg-col-16-of-20")
                                    )
                                )

                    file.write("\n")

                    id_element : int = 0
                
                    for ele in content:

                        try:

                            name_element = ele.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text
                            file.write(f"Product Name({page_number} : {id_element}) : "+ name_element+"\n")
                                    
                            image_element = ele.find_element(By.XPATH, ".//img[@class='s-image']").get_attribute("src")
                            file.write("Image url: "+image_element+"\n")

                            price_element = ele.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
                            file.write("Product Price: "+ price_element+"\n") 
                            
                            image_response = requests.get(image_element)
                            Write_image(id_element ,image_response ,page_number)             
                                            
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
