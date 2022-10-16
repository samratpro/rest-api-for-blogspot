mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'}
    ],
    'exchnage_rate': 103.25
}
# example Output:
# Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT

#  Your Code Starts from here
import random

device_list = mobile_data.get('data')
exchange_rate = mobile_data.get("exchnage_rate")

for device in device_list:
    price_USD = device.get("price")
    price_only = price_USD.removesuffix("USD")     #remove USD suffix from the string value
    price_float = float(price_only)                #convert the string number to float number

    template = [
        f"{device.get('name')} is made in {device.get('made')}. The price is {price_only} USD which is almost equal to {round(price_float * exchange_rate)} BDT.",
        f"{device.get('name')} (made in {device.get('made')}) is realeased in USA.It Market value is {price_only} USD in USA. This phone is about {round(price_float * exchange_rate)} in Bangladeshi Taka.",
        f"This is {device.get('name')} {device.get('made')} varient.The price of this {device.get('name')} in Bangladesh is {round(price_float * exchange_rate)} BDT or about {price_only} USD.",
        f"Today we talk about {device.get('name')}.This device is made in {device.get('made')} and price is {price_only} USD. The value of this device in Bangladesh market is about {round(price_float * exchange_rate)} BDT.",
        f"Searching a device under {price_only} USD? This is new {device.get('name')} which is made in {device.get('made')} and the price is {price_only} USD. This phone is approximately {round(price_float * exchange_rate)} BDT in Bangladesh.",
        f"This {device.get('name')} {device.get('made')} varriant price  in USA is {price_only} USD. Which is almost equal to {round(price_float * exchange_rate)} BDT.",
        f"Want to buy a phone under {round(price_float * exchange_rate)} BDT? {device.get('name')} is approximately {round(price_float * exchange_rate)} BDT in Bangladesh. Which is equal to {price_only} USD and this device is made in {device.get('made')}."
    ]
    print(random.choice(template))