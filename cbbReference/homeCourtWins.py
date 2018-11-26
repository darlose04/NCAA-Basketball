from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os



url = "https://www.sports-reference.com/cbb/seasons/2018-school-stats.html"

# create a new chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

seasons = 2018
x = 16
y = 17

while seasons > 2003:
  if x < 10:
    x = str(x).zfill(2)
  if y < 10:
    y = str(y).zfill(2)

  season_button = driver.find_element_by_link_text('« 20' + str(x) + '-' + str(y) + ' Season')
  season_button.click()

  seasons -= 1
  x = int(x)
  x -= 1
  y = int(y)
  y -= 1

# soup_level1 = BeautifulSoup(driver.page_source, 'html.parser')



# end the browser session
driver.quit()









# «
