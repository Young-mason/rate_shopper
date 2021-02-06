import requests
from bs4 import BeautifulSoup
import pymongo
client = pymongo.MongoClient("mongodb+srv://user:0615@cluster0-cfvlo.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.booking

import datetime
t = datetime.datetime.today()
today = t.strftime('%Y-%m-%d')
later = t + datetime.timedelta(days=60)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.booking.com/hotel/kr/96-bunz-travellers-lodge.ko.html?label=gen173nr-1FCAEoggI46AdIM1gEaH2IAQGYARe4ARjIAQzYAQHoAQH4AQuIAgGoAgTYAgE;sid=4c39997eedb9cd5480e633c725b00532;all_sr_blocks=177786902_91037544_0_0_0;checkin=2020-06-23;checkout=2020-06-24;dest_id=-716583;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=177786902_91037544_0_0_0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=177786902_91037544_0_0_0__5269999;srepoch=1592108378;srpvid=7c051e6d0c0c0067;type=total;ucfs=1&#hotelTmpl', headers=headers)

# today, today+1
# today+1, today+2
# today+2, today+3
# ......
# today +59, today+60


soup = BeautifulSoup(data.text, "html.parser")
rooms = soup.select("tbody tr")
#
# print(rooms)

for room in rooms:
    type = room.select_one("span.hprt-roomtype-icon-link")
    price = room.select_one("div.bui-price-display__value")
    if type and price is not None:
        type_removed = type.text.strip()
        price_removed = int(price.text.strip().split('₩')[1].replace(',', ''))
        print(type_removed, price_removed)


#질문1 : 숫자에서 콤마 없애는법, 파이썬 parse int



#질문2 : 오늘부터 향후 60일의 데이터를 크롤링 해야하는 것을 어떻게 코드로 표현해야 할지?
#
# datetime 검색
# yyyy-mm-dd 포맷
#
# 포문으로
# hotels = ["asdasd","3ke3kek"]
# for hotel in hotels:
#     "https://www.booking.com/%s.htm?from=%s&to=%s" % (hotel,"2020-06-20", "2020-07-20")


# request 앞에 time.sleep()