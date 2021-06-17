import requests
from bs4 import BeautifulSoup

forcastArray = []

page = requests.get("https://azdeq.gov/PHOENIX/Forecast")
soup = BeautifulSoup(page.content, 'html.parser')

ozone = soup.select_one('#day2 > div:nth-child(4) > div.display_gauges > div > strong')
pm10 = soup.select_one('#day2 > div:nth-child(6) > div.display_gauges > div > strong')
pm25 = soup.select_one('#day2 > div:nth-child(8) > div.display_gauges > div > strong')
forcastTable = soup.select_one('#node-5065 > div > div > div > div > div.divPoll > div')
updatedAT = soup.select_one('#node-5065 > div > div > div > div > div.submitted')
highAlert = soup.select_one('#day1 > div.divAlerts > div > div > div.divAlertsCellHPA')

for x in range(1, 5):
  tempArray = []
  for i in range(1, 6):
    tempArray.append(forcastTable.contents[x].contents[i].contents[0])
  forcastArray.append(tempArray)

ozoneValue = (ozone.contents[0].split(" "))[0]
pm10Value = (pm10.contents[0].split(" "))[0]
pm25Value = (pm25.contents[0].split(" "))[0]

print('')
print(f'Current: @{updatedAT.contents[0][12:]}')
print('-' * 40)
print(f'Ozone:\t{ozoneValue}')
print(f'PM10:\t{pm10Value}')
print(f'PM2.5:\t{pm25Value}')
print('')
if len(highAlert.contents[0]) >=1:
  print(f'{highAlert.contents[0]}\n')
print(f'\t{forcastArray[0][1][0:3]}\t{forcastArray[0][2][0:3]}\t{forcastArray[0][3][0:3]}\t{forcastArray[0][4][0:3]}')
print(f'Ozone:\t{forcastArray[1][1]}\t{forcastArray[1][2]}\t{forcastArray[1][3]}\t{forcastArray[1][4]}')
print(f'PM10:\t{forcastArray[2][1]}\t{forcastArray[2][2]}\t{forcastArray[2][3]}\t{forcastArray[2][4]}')
print(f'PM2.5:\t{forcastArray[3][1]}\t{forcastArray[3][2]}\t{forcastArray[3][3]}\t{forcastArray[3][4]}')