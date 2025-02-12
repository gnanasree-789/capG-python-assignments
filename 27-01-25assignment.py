#Calclate the total amount based on price and quantity as input 

# def cal_total():
#     quantity=int(input("enter the quantity of product: "))
#     price=int(input("Enter the price: "))
#     res=lambda x,y : x*y
#     print(f"Total amount to be paid: {res(quantity,price)}")
# cal_total()


#1) convert the prices in USD & Euro using appropriate function

PricesList_inr =[3000,56000,45000,2300]
PricesList_usd=map(lambda x:x*0.012, PricesList_inr)
print(f"Prices in USD: {list(PricesList_usd)}")
PricesList_euro=map(lambda x:x*0.011, PricesList_inr)
print(f"Prices in Euro: {list(PricesList_euro)}")



# 2) List the name which has more than 6 characters as lone_names list using appropriate function

student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]
lone_names=filter(lambda x:len(x)>6, student_name_list)
print(f"Lone_names: {list(lone_names)}")



# 3) Display the Product in ascending order based on the price of the product

products = [
    {"name": "Laptop", "price": 92000},
    {"name": "Smartphone", "price": 48000},
    {"name": "Tablet", "price": 20000},
    {"name": "Monitor", "price": 8000}
    ]
sorted_product=sorted(products,key=lambda x:x["price"])
print(f"Product in ascending order based on the price of the product: {sorted_product}")



# 4) You have a list of numbers. Filter out the odd ones, double the even numbers, and sort them in ascending order

numbers=[3,7,2,5,9,4,6]
odd_ones=filter(lambda x:x%2 != 0,numbers)
sorted_odd_ones=lambda x:sorted(x)
print(f"List of Odd ones in ascending order: {sorted_odd_ones(odd_ones)}")
double_even=map(lambda x:x if x%2 != 0 else x*2,numbers)
list_double_even=list(double_even)
print(f" List of Doubled even numbers in ascending order: {list_double_even}")



# 5) You have a list of cities with their population data. Sort the cities in descending order of their population.
   
cities = [
    {"name": "New York", "population": 8419600},
    {"name": "Los Angeles", "population": 3980400},
    {"name": "Chicago", "population": 2716000},
    {"name": "Houston", "population": 2328000}
]
sort_cities=sorted(cities,key=lambda x: -x["population"])
print(f"cities in descending order of their population: {sort_cities}")



# 6) Extract Emails of Verified Users
# You have a list of user records with email and a verification status. Extract the emails of verified users.

users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
	 ]
verified_users=filter(lambda x:x["verified"]==True, users)
print(f"emails of verified users: {list(verified_users)}")



# 7) Calculate Discounts for Products
#You have a list of products with their prices. Apply a 20% discount to products costing more than $100 and
#                                                      #return the updated prices.
#list out discounted products

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
   ]
disount_produ=filter(lambda x:x["price"]>100,products)
disount_produ_lis=list(disount_produ)
final_price = map(lambda x:x["price"]*0.8,disount_produ_lis)
print(f"updated prices: {list(final_price)}")



# 8)sort Words by Length
#Sort them in ascending order of their lengths.

words = ["apple", "banana", "cherry", "date", "fig"]
sorted_len=sorted(words,key=lambda x:len(x))
print(f"Words in ascending order of their lengths: {sorted_len}")



# 9)write a program to remove the duplicates in the list

numbers3=[2,2,4,6,3,4,6,1]
new_lis=[]
for num in numbers3:
    if num not in new_lis:
        new_lis.append(num)
    else:
        pass
print(f"List without duplicates: {new_lis}")