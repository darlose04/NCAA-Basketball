import requests
from bs4 import BeautifulSoup

homeWins = []
homeLosses = []

season = 2018

while season > 2000:

    page = requests.get(
        "https://www.sports-reference.com/cbb/seasons/" + str(season) + "-school-stats.html")

    soup = BeautifulSoup(page.text, "html.parser")

    table = soup.find("tbody")

    for row in table.find_all("td", {"data-stat": "wins_home"}):
        homeWins.append(int(row.get_text()))

    for row in table.find_all("td", {"data-stat": "losses_home"}):
        homeLosses.append(int(row.get_text()))

    print(season)
    season -= 1

totalHomeWins = sum(homeWins)
print("Home Wins = " + str(totalHomeWins))
totalHomeLosses = sum(homeLosses)
print("Home Losses = " + str(totalHomeLosses))

totalHomeGames = totalHomeWins + totalHomeLosses
print("Total Home Games = " + str(totalHomeGames))

ratioWinsPerGame = totalHomeWins / totalHomeGames

print("Home Win % = " + "{:.2%}".format(ratioWinsPerGame))
