from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from chromedriver_py import binary_path


options = Options()
options.add_argument('--headless')
options.add_argument("--log-level=3")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = ChromeService(binary_path)

def get_session():
    result = []
    driver = webdriver.Chrome(options=options,service=service)
    driver.get('http://stockboard.sbsc.com.vn/apps/StockBoard/SBSC/VN30INDEX.html')
    delay = 3

    try:
        myElem = WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, '//td[contains(@id,"ACB-8")]')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
        driver.close()
        return None

    stock_list= ['ACB', 'BCM', 'BID', 'BVH', 'CTG', 'FPT', 'GAS', 'GVR', 'HDB', 'HPG']

    for item in stock_list:
    # Gia khop lenh lien tuc co duoi la 8 || The price of the stock code has the ending of -8
        element = driver.find_element(By.XPATH,f'//td[contains(@id,"{item}-8")]')
        price = element.text
        temp = {"stock_code":item, 
        "current_price": price}
        result.append(temp)

    driver.close()
    return result

if __name__ == '__main__':
    get_session()
