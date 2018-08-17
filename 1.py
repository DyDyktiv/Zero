import requests
import time


testhttp = ('https://ficbook.net/find',
            'https://ficbook.net/popular',
            'https://ficbook.net/find?title=&fandom_filter=fandom&fandom_group_id=1&fandom_ids%5B%5D=6186&fandom_exclude_ids%5B%5D=98&fandom_exclude_ids%5B%5D=183&fandom_exclude_ids%5B%5D=3276&fandom_exclude_ids%5B%5D=1691&fandom_exclude_ids%5B%5D=7509&fandom_exclude_ids%5B%5D=2541&sizes%5B%5D=3&sizes%5B%5D=4&pages_min=15&pages_max=&ratings%5B%5D=5&ratings%5B%5D=6&ratings%5B%5D=7&ratings%5B%5D=8&ratings%5B%5D=9&transl=&status=&directions%5B%5D=1&directions%5B%5D=2&directions%5B%5D=7&genres_ignore%5B%5D=49&genres_ignore%5B%5D=53&genres_ignore%5B%5D=57&genres_ignore%5B%5D=58&genres_ignore%5B%5D=68&genres_ignore%5B%5D=63&genres_ignore%5B%5D=66&warnings_ignore%5B%5D=25&warnings_ignore%5B%5D=28&warnings_ignore%5B%5D=69&warnings_ignore%5B%5D=60&warnings_ignore%5B%5D=16&warnings_ignore%5B%5D=86&likes_min=&likes_max=&creating_date_min_day=18&creating_date_min_month=7&creating_date_min_year=2018&creating_date_max_day=18&creating_date_max_month=8&creating_date_max_year=2018&date=2&updating_date_min_day=16&updating_date_min_month=8&updating_date_min_year=2018&updating_date_max_day=18&updating_date_max_month=8&updating_date_max_year=2018&sort=marks&rnd=241152267&find=Найти%21#result')


def httptotext(http, savemode=False):
    t = requests.get(http).text
    mainstart = t.rfind('<main id="main" role="main">')
    mainend = t.find('</main>')
    if mainstart==-1 or mainend==-1:
        f = open('D:\YandexDisk\Project\Zero\ErrorHTTP\{}.txt'.format(int(time.time())), 'w', encoding='utf-8')
        f.write('http:\n{}\nhtml:\n'.format(http))
        f.write(t)
        f.close()
        return ''
    else:
        t = t[mainstart + 29: mainend -1]
        if savemode:
            httptime = int(time.time())
            f = open('{}.txt'.format(httptime), 'w', encoding='utf-8')
            f.write('http:\n{}\nhtml:\n'.format(http))
            f.write(t)
            f.close()
        return (httptime, t)


t = httptotext('https://yandex.ru', True)
print(t.__sizeof__())
