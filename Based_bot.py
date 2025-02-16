from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
# Настройки Chrome
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\Александр\\AppData\\Local\\Google\\Chrome\\Si")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
def buy(i):
    button = driver.find_element(By.XPATH, '//div[contains(text(), "Купить")]')
    button.click()
    time.sleep(3)
    input_field = driver.find_element(By.XPATH, '//input[@placeholder="от 1 лота"]')
    input_field.clear()
    input_field.send_keys(i)
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://appweb.broker.vtb.ru/mob/WebApp/Main/Portfel/PortfelAccount_11037764")
    time.sleep(500)
    button = driver.find_element(By.XPATH, '//div[contains(text(), "Китайский юань")]')
    button.click()
    time.sleep(1)
    Yuan_rub = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'МОСБИРЖА')]"))
    )
    print("Элемент найден:", Yuan_rub.text)
    possible_xpaths2 = [
        "following-sibling::div",  # Возможно, число в соседнем div
        "following-sibling::span",  # Иногда в span
        "parent::div/following-sibling::div",  # Число в соседнем блоке
        "ancestor::div/following-sibling::div",  # Число выше в структуре
    ]
    price_text = None
    for xpath in possible_xpaths2:
        try:
            price_element = Yuan_rub.find_element(By.XPATH, xpath)
            price_text_Yuan = price_element.text.strip()
            if price_text_Yuan:
                print("Найдено число:", price_text_Yuan)
                break
        except:
            continue
    price_text_Yuan = price_text_Yuan.split('Y')[1].strip()
    Cost_Yuan_Rub = price_text_Yuan.split('₽')[0].strip()
    Change_Yuan_Rub = price_text_Yuan.split('₽')[1].strip()
    Cost_Yuan_Rub = float(Cost_Yuan_Rub.replace(' ', '').replace(',', '.'))
    Change_Yuan_Rub = float(Change_Yuan_Rub.replace(' ', '').replace(',', '.'))
    print (Cost_Yuan_Rub, Change_Yuan_Rub)
    Cl_price_yaun = Cost_Yuan_Rub - Change_Yuan_Rub
    print(Cl_price_yaun)
    #----------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------------------
    driver.get("https://appweb.broker.vtb.ru/mob/WebApp/Main/Portfel/PortfelAccount_11037764")
    time.sleep(4)
    #button = driver.find_element(By.XPATH, '//div[contains(text(), "Акрон Б1P4")]')
    #button.click()
    #time.sleep(3)
    rubles = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[contains(@style, 'translateX(0px)') and contains(text(), '₽')]"
        ))
    )
    #<div dir="auto" class="css-901oao css-nfaoni r-kgv7a8 r-1i10wst r-majxgm r-10yl4k r-1ut4w64 r-1vl6mv8" style="transform: translateX(0px);">116,59&nbsp;₽</div>
    #<div dir="auto" class="css-901oao css-nfaoni r-kgv7a8 r-1i10wst r-majxgm r-10yl4k r-1ut4w64 r-1vl6mv8" style="transform: translateX(0px);">342,25&nbsp;¥</div>
    yuan = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[contains(@style, 'translateX(0px)') and contains(text(), '¥')]"
        ))
    )
    rub_num = rubles.text.strip()
    yuan_num = yuan.text.strip()
    print("Рублей:", rub_num)
    print("Юаней:", yuan_num)

    #<div dir="auto" class="css-901oao css-nfaoni r-kgv7a8 r-1i10wst r-majxgm r-10yl4k r-1ut4w64 r-1vl6mv8" style="transform: translateX(0px);">44&nbsp;121,0&nbsp;₽</div>
    button = driver.find_element(By.XPATH, '//div[contains(text(), "Акрон Б1P4")]')
    button.click()
    time.sleep(1)
    buttons = driver.find_elements(By.CLASS_NAME, "css-1dbjc4n")
    for button in buttons[::-1]:
        text = button.text.strip()
        if "RUB" not in text and "Акрон Б1P4" in text:  
            button.click()
            break
    buy_cost = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Купить')]"))
    )
    print("Элемент найден:", buy_cost.text)
    possible_xpaths = ["following-sibling::div", "following-sibling::span", "parent::div/following-sibling::div", "ancestor::div/following-sibling::div",]
    price_text = None
    for xpath in possible_xpaths:
        try:
            price_element = buy_cost.find_element(By.XPATH, xpath)
            price_text = price_element.text.strip()
            if price_text:
                print("Найдено число:", price_text)
                break
        except:
            continue
    buy(5)

finally:
    # Закрыть браузер
    time.sleep(120)  # Подождите, чтобы увидеть результат
    driver.quit()
    print("Браузер закрыт.")