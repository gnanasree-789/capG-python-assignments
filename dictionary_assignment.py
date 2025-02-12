# 1) calculate count the item frequency from the below products and store it in dictionary

products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
list=products.split()
item_freq={}
for item in list:
    if item in item_freq:
        item_freq[item]+=1
    else:
        item_freq[item]=1
print(item_freq)
print()


# 2) Store management
#calculate the current stock and display current stock

initial_stock = {"apple": 50,"banana": 100,"orange": 75}
sold_item = {"apple": 10, "banana": 20, "orange": 15}
curr_stock={}
for item in sold_item:
    curr_stock[item]=initial_stock[item]-sold_item[item]
print(curr_stock)
print()


# 3) You have sales data for different regions and want to calculate the total sales for each region.

sales_data = [
    {"region": "North", "sales": 15000},
    {"region": "South", "sales": 8000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000}
]
total_sales={}
for data in sales_data:
    region=data["region"]
    sales=data["sales"]
    if region in total_sales:
        total_sales[region]+=sales
    else:
        total_sales[region]=sales
print(total_sales)
print()


# 4) take input of your mobile number and display it in word format
# 234= two three four

digit_to_word={'0':'Zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
word_format=[]
n=input("ENter the number: ")
for digit in n:
    word_format.append(digit_to_word[digit])
print(' '.join(word_format))