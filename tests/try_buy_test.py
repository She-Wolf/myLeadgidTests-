from time import sleep
from splinter import Browser

browser = Browser()

# Проверка возможности выбрать товар
if browser.find_by_tag('shopItem').first.visible and browser.find_by_css('.shopButton').first.visible:
	browser.find_by_css('.shopButton').click()
else:
	print('Элементы недоступны. Проверьте не заказаны ли уже 3 товара')

browser.find_by_text('ОФОРМЛЕНИЕ ЗАКАЗА')
browser.find_by_value('L').click()

sleep(2)
