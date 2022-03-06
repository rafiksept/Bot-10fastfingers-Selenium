from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup



DRIVER_PATH = r'C:\Users\Downloads\chromedriver_win32/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://10fastfingers.com/typing-test/russian")

huruf = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#row1 span')))
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
coba = soup.select('span[wordnr]')
ketik = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="inputfield"]')))


for i in coba:
    waktu = driver.find_element(By.CSS_SELECTOR, '#timer').text
    if waktu == '0:00':
        ketik.send_keys(f'')
    else:
        for n in i.text:
            ketik.send_keys(f'{n}')
            time.sleep(0.001)
        ketik.send_keys(f' ')


