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

soup_level1 = BeautifulSoup(driver.page_source, 'lxml')

datalist = [] # empty list for storing tables

# grab the table on the page
table = soup_level1.find_all('table')[0]

# giving the html table to pandas to put in a dataframe
df = pd.read_html(str(table), header=0)

# store the dataframe in a list
datalist.append(df[0])

# end the browser session
driver.quit()