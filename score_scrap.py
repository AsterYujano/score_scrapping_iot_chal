import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

domain_name = 'https://www.iotchallengekeysight.com'
project_urls = []
votes = []

print('---------------------------------------')
print('-  Starting project URL gathering...  -')
print('---------------------------------------')
for page in range(0, 180, 12):
	print('[+] Crawling around the '+str(page)+'th entry...')
	url = 'https://www.iotchallengekeysight.com/2019/entries?start='+str(page)

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	cards = soup.find_all('div', attrs={'class': 'card', 'itemprop': 'blogPost'})

	for card in cards:
		link_url = card.find('a', href=True, itemprop='url')['href']
		project_urls.append(link_url)
		#time.sleep(0.5)
print('[o] Complete')

print('-------------------------------')
print('-  Starting Vote fetching...  -')
print('-------------------------------')
count = 1
for project_url in project_urls:
	#counter
	print(str(count) + ' / ' + str(len(project_urls)), end='')
	print('\r', end='')
	count = count + 1

	url = domain_name+project_url

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	header = soup.find('div', attrs={'class': 'page-header'})
	vote_string = header.find('h5').text
	vote = int(re.sub("[^0-9]", "", vote_string))
	votes.append(vote)
print('[o] Complete')
print()
print('votes :')
print(votes)
print()

print('Highest : ' + str(max(votes)) + 'votes')
print('Lowest : ' + str(min(votes)) + 'votes')

sum = 0
for vote in votes:
	sum = sum + vote
result = sum / len(votes)
print('average vote number per project : ', result)
