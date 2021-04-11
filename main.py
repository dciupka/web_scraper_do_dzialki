from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
PATH="C:/znajdywacz_dzialki/geckodriver.exe"

driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://www.olx.pl/nieruchomosci/dzialki/sprzedaz/?search%5Bfilter_enum_type%5D%5B0%5D=dzialki-budowlane&search%5Bfilter_float_price%3Ato%5D=200000&search%5Bdescription%5D=1")
time.sleep(2)
ciasteczka=driver.find_element_by_id("onetrust-accept-btn-handler").click()

miasta=["Chrząstawa Mała"]

element=driver.find_element_by_id("cityField")
element.clear()
element.send_keys("Chrząstawa Mała")
element.send_keys(Keys.RETURN)
time.sleep(2)
lokalizacja=driver.find_element_by_css_selector(".suggestgeo li:first-child").click() #wybranie miasta
distance=driver.find_element_by_class_name("topLink").click()  #otworzenie listy odległości od

km=3 #30km 4-10km 3-5km
odleglosc_od_lokalizacji = driver.find_element_by_xpath(f"//ul[@class='hidden']/li[{km}]").click() #wybranie odległości od