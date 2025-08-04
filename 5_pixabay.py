from selenium import webdriver
from urllib.request import Request, urlopen

driver = webdriver.Chrome()
url = 'https://pixabay.com/ko/images/search/강아지/'
driver.get(url)

image_xpath = '/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div/a/img'
image_url = driver.find_element('xpath', image_xpath).get_attribute('src')
print('image_url:', image_url)

image_byte = Request(image_url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})

f = open('dog.jpg', 'wb')
f.write(urlopen(image_byte).read())
f.close()