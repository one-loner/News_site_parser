import requests
import telebot
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
def pars(url,hashtag,lang):
   feed=''
   # Сюда пишем то, что не хотим видеть в выдаче
   excluded_values = [
       "mailto:support@glc.ru",
       "support@glc.ru",
       "mailto:yakovleva.a@glc.ru",
       "yakovleva.a@glc.ru",
       "https://qrator.net/ru/",
       "/about/",
       "Подписка для физлиц",
       "/corporate/",
       "/page/",
       "Подписка для юрлиц",
       "/advert/",
       "Реклама на «Хакере»",
       "/contact/",
       "Контакты",
       "https://xakep.ru/about-magazine/",
       "на годовую подписку",
       "https://xakep.ru/wp-login.php?redirect_to=https%3A%2F%2Fxakep.ru%2F",
       "Вход",
       "https://xakep.ru/",
       "https://xakep.ru/category/hack/",
       "Взлом",
       "https://xakep.ru/category/privacy/",
       "Приватность",
       "https://xakep.ru/category/tricks/",
       "Трюки",
       "https://xakep.ru/category/coding/",
       "Кодинг",
       "https://xakep.ru/category/admin/",
       "Админ",
       "https://xakep.ru/category/geek/",
       "Geek",
       "https://xakep.ru/pentest/",
       "Пентесты",
       "/wp-admin/users.php?page=paywall_subscribes&from=paywall_subscribe&subscribe=12_months",
       "Подписаться на материалы",
       "https://xakep.ru/tag/windows/",
       "Windows",
       "https://xakep.ru/tag/linux/",
       "Linux",
       "https://xakep.ru/tag/android/",
       "Android",
       "https://xakep.ru/tag/zhelezo/",
       "Железо",
       "https://xakep.ru/tag/hackthebox/",
       "Райтапы",
       "https://xakep.ru/tag/iskusstvennyj-intellekt/",
       "Нейросети",
       "https://xakep.ru/tag/python/",
       "Python",
       "https://xakep.ru/issues/xa/",
       "Все выпуски «Хакера»",
       "/issues",
       "https://xakep.ru/about",
       "ГодоваяподписканаХакер", "читателей",
       "авторов", "В мире",
       "редакции", "Бизнес-материалы", "Реклама", "Оппозиция", "Власть", "Общество", "Регионы", "Коррупция", "Экономика", "В СТРАНЕ", "Экология", "БЛОГИ", "Интервью", "Репортаж", "Обзор", "Опрос", "Контркультура", "По поводу", "Пятая колонка", "АВТОРЫ", "Образование", "Медицина", "Армия", "Полиция", "Тюрьмы", "Фото", "Видео", "Новости", "Политика", "Общество", "О нас", "Архив", "НОВОСТИ", "Оппозиция", "Власть", "Общество", "Регионы", "Коррупция", "Экономика", "В СТРАНЕ", "Экология", "СТАТЬИ", "Интервью", "Репортаж", "Обзор", "Контркультура", "Заметка", "БЛОГИ", "Все", "АВТОРЫ", "Все", "В", "Образование", "Медицина", "Армия", "Полиция", "Тюрьмы", "ГАЛЕРЕЯ", "Фото", "Видео", "ВОЙНА В УКРАИНЕ", "ЦЕНЗУРА", "ФОРУМ СВОБОДНОЙ РОССИИ",
       "			Read More Â»		", "Page2","Page3","Page4","Page5","Page6","Page7","Page8","Page9","Page10","Page11","Page12","Page13","Page14","Page15","Page16","Page17","Page18","Page19","Page20","Page21","Page22","Page23","Page24","Page25","Page26","Page27","Page28","Page29","Page30","Page31","Page32","Page33","Page34","Page35","Page36","Page37","Page38","Page39","Page40","Page41","Page42","Page43","Page44","Page45","Page46","Home","Products","Video","RebelNet","About","Contact","Resources","Home","Products","Video","RebelNet","About","Contact",
       "https://simplifiedprivacy.com/xmppsub/index.html", "https://simplex.chat/contact#/", "https://pvcsk5frxfyostm75nhyjneotxwpuldjy5ptdip24ut7w6lfgwha.arweave.net/fUUldLG5cOlNn-tPhLSOnez6LGnHXzGh-uUn-3llNY4/profile/zwYLgYCdECfO4S62oBMJXhvkVFL--24qJCa5E_-BnGM","https://simplifiedprivacy.com/xmppsub/index.html",
       "https://simplex.chat/contact#/?v=2-4&smp=smp%3A%2F%2FN_McQS3F9TGoh4ER0QstUf55kGnNSd-wXfNPZ7HukcM%3D%40smp19.simplex.im%2F-0fWTzXMJNobsaiaodOGLOfm0m9pq05I%23%2F%3Fv%3D1-2%26dh%3DMCowBQYDK2VuAyEAdfeJrGjuY_qKripG4E7xle6nTDWOWuBPtWmapW6pyEc%253D%26srv%3Di53bbtoqhlc365k6kxzwdp5w3cdt433s7bwh3y32rcbml2vztiyyz5id.onion&data=%7B%22type%22%3A%22group%22%2C%22groupLinkId%22%3A%22yhJzAfpfVkMynOUVxs412g%3D%3D%22%7D","https://simplex.chat/contact#/?v=2-4&smp=smp%3A%2F%2FN_McQS3F9TGoh4ER0QstUf55kGnNSd-wXfNPZ7HukcM%3D%40smp19.simplex.im%2F-0fWTzXMJNobsaiaodOGLOfm0m9pq05I%23%2F%3Fv%3D1-2%26dh%3DMCowBQYDK2VuAyEAdfeJrGjuY_qKripG4E7xle6nTDWOWuBPtWmapW6pyEc%253D%26srv%3Di53bbtoqhlc365k6kxzwdp5w3cdt433s7bwh3y32rcbml2vztiyyz5id.onion&data=%7B%22type%22%3A%22group%22%2C%22groupLinkId%22%3A%22yhJzAfpfVkMynOUVxs412g%3D%3D%22%7D","https://simplex.chat/contact#/?v=1-4&smp=smp%3A%2F%2Fh–vW7ZSkXPeOUpfxlFGgauQmXNFOzGoizak7Ult7cw%3D%40smp15.simplex.im%2FCCgaDX_IPqP9JsEom5c9bnnHPCKNOGu6%23%2F%3Fv%3D1-2%26dh%3DMCowBQYDK2VuAyEANTZYJwyYPKvDnhrd9Zs4Ez0RAOfsVKEzCjcK0kz0tEk%253D%26srv%3Doauu4bgijybyhczbnxtlggo6hiubahmeutaqineuyy23aojpih3dajad.onion&data=%7B%22type%22%3A%22group%22%2C%22groupLinkId%22%3A%22oZEDJ9yvqKBOfNufT3FnEQ%3D%3D%22%7D","https://simplex.chat/contact#/?v=1-4&smp=smp%3A%2F%2Fh--vW7ZSkXPeOUpfxlFGgauQmXNFOzGoizak7Ult7cw%3D%40smp15.simplex.im%2FCCgaDX_IPqP9JsEom5c9bnnHPCKNOGu6%23%2F%3Fv%3D1-2%26dh%3DMCowBQYDK2VuAyEANTZYJwyYPKvDnhrd9Zs4Ez0RAOfsVKEzCjcK0kz0tEk%253D%26srv%3Doauu4bgijybyhczbnxtlggo6hiubahmeutaqineuyy23aojpih3dajad.onion&data=%7B%22type%22%3A%22group%22%2C%22groupLinkId%22%3A%22oZEDJ9yvqKBOfNufT3FnEQ%3D%3D%22%7D","https://simplex.chat/contact#/?v=1-4&smp=smp%3A%2F%2FZKe4uxF4Z_aLJJOEsC-Y6hSkXgQS5-oc442JQGkyP8M%3D%40smp17.simplex.im%2FjlgwnohJoxn1yz9bhJ_3m6JhanIbgOME%23%2F%3Fv%3D1-2%26dh%3DMCowBQYDK2VuAyEArsSD2oa0yAYYTXuSKj_3uw5uQo0LU77i3jeoXtK6kjU%253D%26srv%3Dogtwfxyi3h2h5weftjjpjmxclhb5ugufa5rcyrmg7j4xlch7qsr5nuqd.onion","https://simplex.chat/contact#/?v=1-4&smp=smp%3A%2F%2FZKe4uxF4Z_aLJJOEsC-Y6hSkXgQS5-oc442JQGkyP8M%3D%40smp17.simplex.im%2FjlgwnohJoxn1yz9bhJ_3m6JhanIbgOME%23%2F%3Fv%3D1-2%26dh%3DMCowBQYDK2VuAyEArsSD2oa0yAYYTXuSKj_3uw5uQo0LU77i3jeoXtK6kjU%253D%26srv%3Dogtwfxyi3h2h5weftjjpjmxclhb5ugufa5rcyrmg7j4xlch7qsr5nuqd.onion","PublicXMPPGroup","https://simplifiedprivacy.com/xmppsub/index.html",
       "Skip to content", "About Us", "https://simplifiedprivacy.com/summary/index.html","https://simplifiedprivacy.com/pgp-directory/index.html","https://simplifiedprivacy.com/category/big-tech-is-evil/index.html","https://simplifiedprivacy.com/category/vpns-browsers/index.html","https://simplifiedprivacy.com/category/phones-service-2fa/index.html","https://simplifiedprivacy.com/category/cryptocurrency/index.html","https://simplifiedprivacy.com/category/agorism/index.html","https://simplifiedprivacy.com/category/virtual-machines/index.html","https://simplifiedprivacy.com/category/private-messengers-apps/index.html","https://simplifiedprivacy.com/category/tor/index.html","https://simplifiedprivacy.com/category/encryption-files/index.html","https://simplifiedprivacy.com/category/routers/index.html","https://simplifiedprivacy.com/category/censorship/index.html","https://simplifiedprivacy.com/category/nostr/index.html","https://simplifiedprivacy.com/category/sessionbot/index.html","https://simplifiedprivacy.com/category/email/index.html","https://simplifiedprivacy.com/category/security/index.html"

   ]


   response = requests.get(url)
   if response.status_code != 200:
           print(f"Ошибка при запросе страницы: {response.status_code}")
           exit()

   soup = BeautifulSoup(response.text, 'html.parser')

   a_tags = soup.find_all('a')

   for a_tag in a_tags:
       href = a_tag.get('href')
       text = a_tag.get_text()
       text = text.replace('\n','')
       if href not in excluded_values and text not in excluded_values:
            if text:
                 
                          if text.startswith("	"):
                              text=text.replace('	','')
                          if lang != 'ru':
                              text = GoogleTranslator(source=lang, target='ru').translate(text)
                          
                          href=href.replace('./',url)
                          href=href.replace('/material.php?id',url+'material.php?id')
                          href=href.replace(url+'.'+url+'.','')
                          feed=feed + '#' + hashtag + ' #' + lang + ' ' + text + ' ' + href + '\n'
#                          print(translated+' '+href)
#                              print(href)
#                          print('')
   return feed

def send_multiline_message(multiline_text):
    bot = telebot.TeleBot('YOUR_TOKEN')
    chat_id='YOUR_CHAT_ID'
    lines = multiline_variable.split('\n')
    for line in lines:
        bot.send_message(chat_id, line)



a=pars('https://example1.com','sp','en')
a=a+'\n'+pars('https://example2.com/','politic','ru')
print(a)
send_multiline_message(a)
