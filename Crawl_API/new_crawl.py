from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service('C:\My Learning\laravel\web-scrapping\Crawl-website\chrome_driver')


def get_session():
    result = []
    driver = webdriver.Chrome(service=service)
    driver.get('http://stockboard.sbsc.com.vn/apps/StockBoard/SBSC/VN30INDEX.html')
    time.sleep(3)

    stock_list= ['ACB', 'BCM', 'BID', 'BVH', 'CTG', 'FPT', 'GAS', 'GVR', 'HDB', 'HPG']

    for item in stock_list:
        element = driver.find_element(By.XPATH,f'//td[contains(@id,"{item}-8")]')
        price = element.text
        
        temp = {"stock_code":item, 
                "current_price": price}
        
        result.append(temp)
    
    driver.quit()

    return result

