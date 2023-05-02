from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
dbase = client.products
branch_col = dbase.branches

order_dbase = client.order_management
order_col = order_dbase.orders
products_db = client["products"]
order_management_db = client["order_management"]
users_db = client["users"]
users_col = users_db["users"]


products = {
    100: {"name":"Americano","price":125},
    200: {"name":"Brewed Coffee","price":100},
    300: {"name":"Cappuccino","price":120},
    400: {"name":"Espresso","price":120},
    500: {"name":"Latte","price":140},
    600: {"name":"Cold Brew","price":200},
    1000: {"name":"Tiramisu","price":150},
    1100: {"name":"Red Velvet","price":130},
    1200: {"name":"Mango Cream Pie","price":200},
}

branches = {
    1: {"name":"Katipunan","phonenumber":"09179990000"},
    2: {"name":"Tomas Morato","phonenumber":"09179990001"},
    3: {"name":"Eastwood","phonenumber":"09179990002"},
    4: {"name":"Tiendesitas","phonenumber":"09179990003"},
    5: {"name":"Arcovia","phonenumber":"09179990004"},
}

users = {
    "chums@example.com":{"username":"chums@example.com",
                         "password":"Ch@ng3m3!",
                         "first_name":"Matthew",
                         "last_name":"Uy"},
    "joben@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joben",
                         "last_name":"Ilagan"},
    "bong@example.com":{"password":"Ch@ng3m3!",
                        "first_name":"Bong",
                        "last_name":"Olpoc"},
    "joaqs@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joaqs",
                         "last_name":"Gonzales"},
    "gihoe@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Gio",
                         "last_name":"Hernandez"},
    "vic@example.com":{"password":"Ch@ng3m3!",
                       "first_name":"Vic",
                       "last_name":"Reventar"},
    "joe@example.com":{"password":"Ch@ng3m3!",
                       "first_name":"Joe",
                       "last_name":"Ilagan"},
}
  
def get_product(code):
    products_coll = products_db["products"]

    product = products_coll.find_one({"code":code})

    return product


def get_products():
    product_list = []

    products_coll = products_db["products"]

    for p in products_coll.find({}):
        product_list.append(p)

    return product_list


def get_branch(code):
    return branch_col.find_one({"code": code}, {"_id": 0})

def get_branches():
    branch_list = list(branch_col.find({}, {"_id": 0}))
    return branch_list

def get_user(email):
    return users[email]

def get_users():
    user_list = []

    for user in users_col.find({}):
        user_list.append(user)

    return user_list

def get_user(username):
    user = users_col.find_one({"username": username})
    return user


def get_orders(email):
    order_list = list(order_col.find({"email": email}))
    return order_list
def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)
