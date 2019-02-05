from splinter import Browser
import unittest
from tests import variables
''' Тест покупки спонсорства на конференции FinAdTech Киев 2019'''
browser = Browser()

# RU Версия

browser.visit('http://2019kyiv.leadgid.space/ua')
def test_fill_sponsor_form(sponsor):
	browser.find_by_text(sponsor).click()
	browser.find_by_name('sponsor[fullName]').fill('Тест ФИО можливіст HFISj')
	browser.find_by_id('general_sponsor_company').fill('ТестCompany')
	browser.find_by_id('general_sponsor_email').fill('name@domain.com')
	browser.find_by_id('general_sponsor_phone').fill('89000110011')

try:
	browser.find_by_css('.shopButton').click()
except Exception:
	print('Ошибка не выводится')

	# browser.quit()
# Адрес доставки

fill_sponsor_form('ГЕНЕРАЛЬНИЙ СПОНСОР')

if __name__=='__main__':
	unittest.main()