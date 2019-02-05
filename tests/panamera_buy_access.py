from splinter import Browser
from selenium import webdriver
import unittest
from tests import variables

browser = Browser()

def checkout_by_text(checkout_text: 'exist text', passed_text:'if detected', failed_text:' if failed'):
	''' Проверяет по наличию текста на странице, выводит результат проверки '''
	if browser.is_text_present(checkout_text):
		variables.green_text(passed_text)
	else:
		variables.red_text(failed_text)
		browser.screenshot('downloads/{date.today()}.png')
		browser.quit()


class PanameraDenied(unittest.TestCase) :

	def test_01(self):
		browser.visit('http://my-db.leadgid.space/')
		browser.fill('login', variables.login)
		browser.fill('password', variables.password)
		browser.find_by_css('button').click()

		# Проверка авторизации админа
		checkout_by_text(variables.try_admin_logined, variables.passed_admin_login, variables.failed_admin_login)

		partners = {'21390', '22033', '22819', '22737', '28617', '24623', '21062', '21487', '24965', '25261', '25615', '25393', '26067', '38317',
		            '38319', '27835', '22457', '37669', '25845', '32083', '33573', '32883', '36463', '25465', '32055', '36301', '25487', '24057',
		            '25319', '30799', '28357', '29301', '25577', '32543', '23083', '24193', '21366', '24489', '25021', '25045', '25065', '27765',
		            '29485', '25725', '31447', '26197', '28019', '27537', '27539', '33367', '34495', '34905', '37971'}

		for each in str(partners):
			# Попытка логина партнера
			browser.fill('affiliate_id', '')
			browser.find_by_css('button.btn').click()

			# Проверка авторизации партнера
			checkout_by_text(variables.try_partner_logined, variables.passed_partner_login, variables.failed_partner_login)

			# Открытие боковой панели магазина
			browser.find_by_css('.shopHeaderButton__link.out').click()

			# Проверка отображения панели
			if browser.find_by_css('.shopPopup.selected').visible:
				variables.green_text(variables.passed_shop_popup)
			else:
				variables.red_text(variables.failed_shop_popup)
				browser.screenshot('downloads/{date.today()}.png')

			# Переход в магазин
			browser.find_by_css('.shopPopup__button').click()

			# Проверка кнопки
			browser.find_by_link('http://my-db.leadgid.space/affiliate/spystore/order_ticket/1').click()





