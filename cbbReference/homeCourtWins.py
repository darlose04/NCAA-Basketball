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