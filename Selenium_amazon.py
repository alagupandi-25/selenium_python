import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def Web_scraping():
    try:
        driver = webdriver.Firefox()
        print("webdriver is open")

        with open("Search_result.txt", "w", encoding="utf-8") as file:
            print("Started to the file")

            file.write("""--------------------------------------Selenium Amazon Search Result--------------------------------------""")

            driver.get("""https://www.amazon.in/s?k=gaming+monitor&crid=3MHDYZB2OO82H&sprefix=gaming+monitor%2Caps
            %2C298 &ref=nb_sb_noss_1""")
            content = driver.find_elements(By.CSS_SELECTOR, "div.sg-col-20-of-24")

            file.write("\n\n")
            
            for ele in content:
                try:

                    text_element = ele.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
                    file.write("Product Name : "+ text_element.text+"\n")

                    text_element = ele.find_element(By.XPATH, ".//span[@class='a-price-whole']")
                    file.write("Product Price: "+ text_element.text+"\n")

                    file.write("\n")

                except:
                    continue

            print("Completed the writing file.")
            print("File located at ", os.path.realpath(file.name))

    except:
        print("Error Occurred.....")

    finally:
        driver.quit()
        print("webdriver is close")


if __name__ == "__main__":

    try:
        while True:
            title = "Selenium Amazon Search Result"
            print(f"--------------------------------------{title}--------------------------------------")

            var = input("To run or stop program : ").lower()

            match var:
                case "run":
                    Web_scraping()
                case "stop":
                    raise KeyboardInterrupt
                case _:
                    print("Invalid input.The available input Run or Stop.")
                    continue

    except KeyboardInterrupt:
        print(" End of Program.")
