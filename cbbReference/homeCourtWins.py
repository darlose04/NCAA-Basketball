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

# combine the dataframes in the list into one big dataframe (only one in list for now)
result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))], ignore_index=True)

# convert the pandas dataframe into JSON
json_records = result.to_json(orient='records')

# pretty print to CLI with tabulate
# converts to an ascii table
print(tabulate(result, headers=["Rk", "School",	"G",	"W",	"L",	"W-L %", "SRS", "SOS", "W", "L", "W", "L", "W", "L", "Tm.", "Opp.", "MP", "FG", "FGA", "FG %", "3P", "3PA", "3P %", "FT", "FTA", "FT %", "ORB", "TRB", "AST", "STL", "BLK", "TOV", "PF"], tablefmt='psql'))

