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

# start with 2018 season
seasons = 2018
# x and y variables are for the driver click method. 
x = 16
y = 17

# these are used to keep track of the number of home games
homeWins = 0
homeLosses = 0



'''
Instead of using this while loop in this fashion, I could probably create while loop that 
changes the season year in the URL. This may result in cleaner code, so it's something
I'll need to look into. Possibly with Puppeteer and JS.
'''

# loop through seasons going back to the 03-04 season
while seasons > 2003:
  # use Beautiful soup to pull info from tables
  soup_level1 = BeautifulSoup(driver.page_source, 'html.parser')

  

  # these if statements add leading zeroes to the x and y values once they go below 10 (with zfill()). 
  # this is necessary because of the link_text in the html
  if x < 10:
    x = str(x).zfill(2)
  if y < 10:
    y = str(y).zfill(2)

  # finds the proper button for the driver to click in order to go to previous season's page
  season_button = driver.find_element_by_link_text('« 20' + str(x) + '-' + str(y) + ' Season')
  season_button.click()

  # decrement seasons, x, and y by 1
  seasons -= 1
  x = int(x)
  x -= 1
  y = int(y)
  y -= 1





# end the browser session
driver.quit()

# finding the total number of home games and then the ratio of wins to games
totalHomeGames = homeLosses + homeWins
ratio = homeWins / totalHomeGames



# «
