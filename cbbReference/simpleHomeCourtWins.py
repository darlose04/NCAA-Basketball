import requests
from bs4 import BeautifulSoup

# create empty lists to store the number of home wins and losses from each team listed 
# in the table
homeWins = []
homeLosses = []

# use this season variable to parse through each url for seasons with available data
season = 2018

# this loop go through each page that has the necessary data, which is from 00-01 to present day
while season > 2000:

  # request each page for the seasons
  page = requests.get(
      "https://www.sports-reference.com/cbb/seasons/" + str(season) + "-school-stats.html")

  # create Beautiful Soup object
  soup = BeautifulSoup(page.text, "html.parser")

  #find the tbody element on the page
  table = soup.find("tbody")

  # for each row in the table, find the tds that contain the home wins and losses
  for row in table.find_all("td", {"data-stat": "wins_home"}):
      homeWins.append(int(row.get_text()))

  for row in table.find_all("td", {"data-stat": "losses_home"}):
      homeLosses.append(int(row.get_text()))

  print(season)
  # decrement the season variable
  season -= 1

# determine the total number of home wins and losses over the time span
totalHomeWins = sum(homeWins)
print("Home Wins = " + str(totalHomeWins))
totalHomeLosses = sum(homeLosses)
print("Home Losses = " + str(totalHomeLosses))

totalHomeGames = totalHomeWins + totalHomeLosses
print("Total Home Games = " + str(totalHomeGames))

# calculate the ratio of total wins per total games
ratioWinsPerGame = totalHomeWins / totalHomeGames

print("Home Win % = " + "{:.2%}".format(ratioWinsPerGame))
