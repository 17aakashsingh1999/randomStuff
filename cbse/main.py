from selenium import webdriver

c = webdriver.Chrome()
url = 'http://cbseresults.nic.in/class12zpq/class12th18.htm'
c.get(url)

reg = 5858420

while True:
    c.find_element_by_name('regno').send_keys(str(reg))
    c.find_element_by_name('sch').send_keys('09025')
    c.find_element_by_name('cno').send_keys('5756')
    c.find_element_by_name('B2').click()
    input('')
    reg+=1
    c.back()
