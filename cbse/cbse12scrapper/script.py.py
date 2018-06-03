from selenium import webdriver
from bs4 import BeautifulSoup as bs

c = webdriver.Chrome()
url = 'http://cbseresults.nic.in/class12zpq/class12th18.htm'
c.get(url)                                                                                       #opens the website in Chrome

reg = 5858371                                                                                    #starting roll no

while True:
    c.find_element_by_name('regno').send_keys(str(reg))
    c.find_element_by_name('sch').send_keys('09025')
    c.find_element_by_name('cno').send_keys('5756')
    c.find_element_by_name('B2').click()                                                         #fills in data and submits the form
    s=0
    soup = bs(c.page_source)                                                                     #parses the html to extract marks and name
    print(soup.find_all('table')[4].find_all('tr')[1].find_all('td')[1].text.strip())            #name
    for i in range(1,6):
        s+=int(soup.find_all('table')[5].find_all('tr')[i].find_all('td')[4].text)               #sum
        print(int(soup.find_all('table')[5].find_all('tr')[i].find_all('td')[4].text),end=' ')   #print marks
    print('\nPercentage: ',s/5,'%')                                                              #print percentage
    #print(reg)
    reg+=1
    c.back()

