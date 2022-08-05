"""
This is classwork for lesson 3
Author: Evgeniy
"""

from datetime import datetime


name = "Bob"
age = 42

now = datetime.now()
print("My name is %(a)s. I am is %(b)d yars old. %(a)s is good name" % {"a": name, "b": age})
spend_time_1 = datetime.now() - now

now = datetime.now()
print("My name is {}. I am is {} yars old. {} is good name".format(name, age, name))
spend_time_2 = datetime.now() - now

now = datetime.now()
print("My name is {0}. I am is {1} yars old. {0} is good name".format(name, age))
spend_time_3 = datetime.now() - now

now = datetime.now()
print("My name is {a}. I am is {b} yars old. {a} is good name".format(a=name, b=age))
spend_time_4 = datetime.now() - now

now = datetime.now()
print(f"My name is {name}. I am is {age} yars old. {name} is good name")
spend_time_5 = datetime.now() - now

print('spend_time_1:', spend_time_1)
print('spend_time_2:', spend_time_2)
print('spend_time_3:', spend_time_3)
print('spend_time_4:', spend_time_4)
print('spend_time_5:', spend_time_5)


sales_tax_10 = 1.10
