from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

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
homeWins = []
homeLosses = []

# loop through seasons going back to the specified season
while seasons > 2014:
  # use Beautiful soup to pull info from tables
  soup = BeautifulSoup(driver.page_source, 'html.parser')

  table = soup.find("tbody")
  
  for row in table.find_all("td", {"data-stat": "wins_home"}):
    homeWins.append(int(row.get_text()))

  for row in table.find_all("td", {"data-stat": "losses_home"}):
    homeLosses.append(int(row.get_text()))
   
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
totalHomeWins = sum(homeWins)
print("Home Wins = " + str(totalHomeWins))
totalHomeLosses = sum(homeLosses)
print("Home Losses = " + str(totalHomeLosses))

totalHomeGames = totalHomeWins + totalHomeLosses
print("Total Home Games = " + str(totalHomeGames))

ratioWinsPerGame = totalHomeWins / totalHomeGames

print("Home Win % = " + "{:.2%}".format(ratioWinsPerGame))