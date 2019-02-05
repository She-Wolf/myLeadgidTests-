site = 'http://my-db.leadgid.space/affiliate/spystore/'
login = 'e.dubitskaya@leadgid.ru'
password = 'Wolfy023'

try_admin_logined = 'Войти как партнёр'
passed_admin_login = "Залогинились в партнера"
failed_admin_login = "Скорее всего уже админ залогинен или что-то сломалось"
try_partner_logined = 'Ваши баллы по конкурсу Миссия: Panamera'

passed_partner_login = "Вошли в ЛК партнера № 30003"
failed_partner_login = "Где-то упало на этапе входа в партнера"

passed_shop_popup = 'Боковая панель магазина отображается'
failed_shop_popup = 'Что-то не так с панелью магазина'

try_shop = 'Добро пожаловать в наш шпионский магазин, веб-агент.'
passed_shop = 'Магазин успешно открылся'
failed_shop = 'Магазин сломан'
try_order = 'ОФОРМЛЕНИЕ ЗАКАЗА'
passed_item_form = 'Форма Заказа товара открылась'
failed_item_form = 'Форма заказа не отобразилась '
try_ordered = 'Спасибо за заказ!'
passed_ordered = 'Заказ оформлен, следует проверить письмо из магазина в почте.\n ТЕСТ ПРОЙДЕН УСПЕШНО :)'
failed_ordered = 'Заказ не оформлен'



def red_text(txt):
	print('\033[91m' + txt +  '\033[0m')

def green_text(txt):
	print('\033[96m' + txt +  '\033[0m')