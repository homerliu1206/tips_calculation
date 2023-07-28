price = input('今日帳單總金額為：')
people = input('今日的用餐人數為：')
tip = input('今日用餐的服務費為多少百分比：')

price = int(price)
people = int(people)
tip = int(tip)


tip_price = price * (tip / 100)
total_price = price + tip_price
avg_price = total_price / people
print (
    '在費率', tip, '%的狀況下，小費為', 
    tip_price, '元，總金額', total_price, 
    '元，每人平均消費',avg_price, '元')