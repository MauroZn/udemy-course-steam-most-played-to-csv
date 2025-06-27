import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

current_date = datetime.datetime.now()
url = "https://steamdb.info/"

driver = webdriver.Chrome()
driver.get(url)

row = driver.find_element(By.XPATH, "/html/body/div[@class='body-wrap']/div[@id='main']/div[@class='container container-products'][1]")
first_div = row.find_element(By.XPATH, "./div[1]")
table = first_div.find_element(By.XPATH, ".//table[contains(@class, 'table') and contains(@class, 'table-hover')]")
games = table.find_elements(By.XPATH, ".//tr[@class='app']")

data = []

for game in games:
    name = game.find_element(By.XPATH, "./td[3]")
    current_players = game.find_element(By.XPATH, "./td[4]")
    peak_players_day = game.find_element(By.XPATH, "./td[5]")
    list_game = []
    list_game.append(name.text)
    list_game.append(current_players.text)
    list_game.append(peak_players_day.text)
    data.append(list_game)

columns = ['Name', 'Current Players', 'Peak 24h players']
df = pandas.DataFrame(data, columns=columns)
df.to_csv(f'{current_date.strftime("%Y-%m-%d")}_most_played_games_data.csv', index=True)