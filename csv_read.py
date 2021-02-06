import csv
import datetime
import matplotlib.pyplot as plt
import pandas as pd



t = datetime.datetime.today()
today = t.strftime('%Y-%m-%d')

hotel_ids = ["3011988","1000105081","1000105091", "3001372"]


f = open(f'{today}_{hotel_ids[0]}.csv')

data = csv.reader(f)
next(data)

my_date = []
my_type = []
my_price = []
for row in data:
    if '더블룸' in row[2]:
        my_date.append(row[1])
        my_type.append(row[2])

        if row[3] == '예약마감':
            my_price.append(0)
        else :
            my_price.append(int(row[3]))


f = open(f'{today}_{hotel_ids[1]}.csv')
data = csv.reader(f)
next(data)
comp1_date = []
comp1_type = []
comp1_price = []
for row in data:
    if '더블룸' in row[2]:
        comp1_date.append(row[1])
        comp1_type.append(row[2])

        if row[3] == '예약마감':
            comp1_price.append(0)
        else :
            comp1_price.append(int(row[3]))


f = open(f'{today}_{hotel_ids[2]}.csv')
data = csv.reader(f)
next(data)
comp2_date = []
comp2_type = []
comp2_price = []
for row in data:
    if '트윈룸' in row[2]:
        comp2_date.append(row[1])
        comp2_type.append(row[2])

        if row[3] == '예약마감':
            comp2_price.append(0)
        else :
            comp2_price.append(int(row[3]))


f = open(f'{today}_{hotel_ids[3]}.csv')
data = csv.reader(f)
next(data)
comp3_date = []
comp3_type = []
comp3_price = []
for row in data:
    if '디럭스 더블' in row[2]:
        comp3_date.append(row[1])
        comp3_type.append(row[2])

        if row[3] == '예약마감':
            comp3_price.append(0)
        else :
            comp3_price.append(int(row[3]))



print(len(my_date))
print(len(my_price))
print(len(comp1_price))
print(len(comp2_price))
print(len(comp3_price))


# 그래프 만들기


# print(plt.style.available)
# plt.style.use('dark_background')
plt.figure(figsize=(20,6))
plt.title('Rate Shopper')
plt.ylim(10000, 100000)
plt.xlabel('date')
plt.ylabel('price')

plt.plot(my_date, my_price, linestyle='-', marker='o', label='my hotel -- double room')
plt.plot(my_date, comp1_price, linestyle='-', marker='o', label='24guesthouse -- double room')
plt.plot(my_date, comp2_price, linestyle='-', marker='o', label='phlistay -- double room')
plt.plot(my_date, comp3_price, linestyle='-', marker='o', label='the designers -- twin room')
plt.legend()

# plt.show()
plt.savefig(f'static/{today}_graph.png')


# 테이블 만들기

df = pd.DataFrame()
df['date'] = my_date
df['user_96bunz'] = my_price
df['24guesthouse'] = comp1_price
df['philstay'] = comp2_price
df['the designers'] = comp3_price

df2 = df.set_index('date')
df2_trans = df2.transpose()
df2_trans.to_html(f'templates/{today}_table.html')
