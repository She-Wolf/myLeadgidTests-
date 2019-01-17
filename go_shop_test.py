from splinter import Browser
import variables
from datetime import date
''' Тест авторизации в админа -> партнера -> переход в магазин '''


def checkout_by_text(checkout_text, passed_text, failed_text):
    ''' Проверяет по наличию текста на странице, выводит результат проверки '''
    if browser.is_text_present(checkout_text):
        print (passed_text)
    else:
        print (failed_text)
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
    print(variables.passed_shop_popup)
else:
    print(variables.failed_shop_popup)
    browser.screenshot('downloads/{date.today()}.png')

# Переход в магазин
browser.find_by_css('.shopPopup__button').click()


#browser.quit()