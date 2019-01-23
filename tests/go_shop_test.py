from splinter import Browser
from tests import variables
''' Тест авторизации в админа -> партнера -> переход в магазин '''


def checkout_by_text(checkout_text: 'exist text', passed_text:'if detected', failed_text:' if failed'):
	''' Проверяет по наличию текста на странице, выводит результат проверки '''
	if browser.is_text_present(checkout_text):
		variables.green_text(passed_text)
	else:
		variables.green_text(failed_text)
		browser.screenshot('downloads/{date.today()}.png')

# Открытие главной сайта, попытка логина
browser = Browser()
browser.visit(variables.site)
browser.fill('login', variables.login)
browser.fill('password', variables.password)
browser.find_by_css('button').click()

# Проверка авторизации админа
checkout_by_text(variables.try_admin_logined, variables.passed_admin_login, variables.failed_admin_login)

#Попытка логина партнера
browser.fill('affiliate_id', '30003')
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

checkout_by_text(variables.try_shop, variables.passed_shop, variables.failed_shop)


#
# Следующий скрипт try_buy_test
#
#
#
#
# Проверка возможности выбрать товар
if browser.find_by_css('.shopItem').first.visible and browser.find_by_css('.shopButton').first.visible:
	browser.find_by_css('.shopButton').click()
else:
	print('Элементы недоступны. Проверьте не заказаны ли уже 3 товара')

checkout_by_text(variables.try_order,variables.passed_item_form, variables.failed_item_form)

# Заполнение формы минимально необходимыми значениями
# Личные данные
browser.find_by_text('L').click()
browser.find_by_id('surname').fill('Тест')
browser.find_by_id('firstname').fill('Тест')
browser.find_by_id('phone').fill('89000110011')
browser.find_by_id('email').fill('name@domain.com')
# Адрес доставки
browser.find_by_id('country').fill('Россия')
browser.find_by_id('region').fill('Иркутская область')
browser.find_by_id('city').fill('Иркутск')
browser.find_by_id('build').fill('Иркутская область')
browser.find_by_id('street').fill('Иркутская область')

#sleep(2)
#browser.quit()

