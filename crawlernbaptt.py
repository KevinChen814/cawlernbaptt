import requests
from bs4 import BeautifulSoup
import time

today = time.strftime('%m/%d').lstrip('0')   # lstrip 移除字串左邊文字

def pttNBA(url,num):
	resp = requests.get(url)
	if resp.status_code != 200:
		print('URL Error')
		return
	run = 0	
	page(url, num,run)

def page(url, num, run):
	if run >= num:
		return
		
	resp = requests.get(url)
	soup = BeautifulSoup(resp.text, 'html5lib')
	paging = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']
	articles = []
	rents = soup.find_all('div', 'r-ent')
	for rent in rents:
		title = rent.find('div', 'title').text.strip()
		count = rent.find('div', 'nrec').text.strip()
		date = rent.find('div', 'meta').find('div','date').text.strip()
		article = '%s %s:%s' % (date, count, title)
		  
		try:
			if int(count) > 10:
				articles.append(article)
		except:
			if count == '爆':
				articles.append(article)

	for article in articles:
			print(article)					
	url = 'https://www.ptt.cc' + paging		
	page(url, num, run+1)
	return 
	


pttNBA('https://www.ptt.cc/bbs/NBA/index.html',5)