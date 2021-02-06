import datetime
import requests
from bs4 import BeautifulSoup
import csv
import time
import schedule


def yanolja_crawling() :
    hotel_ids = ["3011988","1000105081","1000105091", "3001372" ]
    t = datetime.datetime.today()
    today = t.strftime('%Y-%m-%d')
    for hotel_id in hotel_ids:
        file = open("%s_%s.csv" % (today, hotel_id), "w", encoding='ansi', newline='')
        wr = csv.writer(file, delimiter=",")
        wr.writerow(["호텔코드", "날짜", "객실타입", "가격"])
        for i in range(3) :
            check_in_date = t + datetime.timedelta(days=i)
            check_out_date = check_in_date + datetime.timedelta(days=1)
            check_in = check_in_dates.strftime('%Y-%m-%d')
            check_out = check_out_date.strftime('%Y-%m-%d')

            url = "https://www.yanolja.com/guest-house/%s?checkinDate=%s&checkoutDate=%s&capacityAdult=2&capacityChild=0" % (hotel_id, check_in, check_out)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

            # time.sleep(3)
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            rooms = soup.select('section._2YIQKY > div._3mKfF6 > div._2la8ZA')
            # if(len(rooms) == 0):
            #     wr.writerow([hotel_id, check_in, "", 0])

            for room in rooms:

                type = room.select_one("h2._3vmdHa").text
                p = room.select_one("span.price").text
                price = p.split('원')[0].split('%')[-1].replace(',','')
                print([hotel_id, check_in, type, price])
                wr.writerow([hotel_id, check_in, type, price])

                # file.write("%s\t%s\t%s" % (check_in, type, price))

        file.close()

    time.sleep(3)

     import csv_read


def job():

    yanolja_crawling()

job()

def run():
    schedule.every().days.at("08:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run()












# 객실이 없는 날짜에는 모든 객실 0원으로 설정 어떻게?

# 그래프 그리는데다가 한글로 입력하는 방법

# pandas 표를 이미지 파일로 받아오는 법