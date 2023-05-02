from flask import Flask,redirect
from flask import render_template
from flask import request
from flask import session
import database as db
import authentication
import logging
import ordermanagement as om


app = Flask(__name__)

# Set the secret key to some random bytes. 
# Keep this really secret!
app.secret_key = b's@g@d@c0ff33!'

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    return render_template('index.html', page="Index")

@app.route('/products')
def products():
    product_list = db.get_products()
    return render_template('products.html', page="Products", product_list=product_list)

@app.route('/productdetails')
def productdetails():
    code = request.args.get('code', '')
    product = db.get_product(int(code))
    return render_template('productdetails.html', code=code, product=product)

@app.route('/branches')
def branches():
    branch_list = db.get_branches()
    return render_template('branches.html', page="Branches", branch_list=branch_list)

@app.route('/branchdetails')
def branchdetails():
    code = request.args.get('code', '')
    branch = db.get_branch(int(code))
    return render_template('branchdetails.html', branch=branch)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', page="About Us")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    is_successful, user_or_error = authentication.login(username, password)
    
    if is_successful:
        session['user'] = user_or_error
        return redirect('/')
    else:
        error_message = user_or_error
        return render_template('login.html', error=error_message)
    
@app.route('/logout')
def logout():
    session.pop("user",None)
    session.pop("cart",None)
    return redirect('/')

@app.route('/addtocart')

def addtocart():
    code = request.args.get('code', '')
    product = db.get_product(int(code))
    item=dict()
    # A click to add a product translates to a 
    # quantity of 1 for now

    item["qty"] = 1
    item["code"] = code  # add a code property to the item
    item["name"] = product["name"]
    item["price"] = product["price"]
    item["subtotal"] = product["price"]*item["qty"]

    if(session.get("cart") is None):
        session["cart"]={}

    cart = session["cart"]
    cart[code]=item
    session["cart"]=cart
    return redirect('/cart')


@app.route('/cart')
def cart():
    if session.get("cart") is None:
        session["cart"] = {}

    cart = session["cart"]
    cart_copy = cart.copy()  # create a copy of the cart dictionary

    for code, item in cart_copy.items():
        if request.form.get(f"{code}_qty"):
            qty = int(request.form.get(f"{code}_qty"))
            item["qty"] = qty
            item["subtotal"] = item["price"] * item["qty"]
            cart[code] = item
        elif request.form.get(f"{code}_code"):
            del cart[code]  # remove the item from the cart

    session["cart"] = cart
    total = sum(item["subtotal"] for item in cart.values())

    return render_template('cart.html', cart=cart, total=total)

@app.route('/updatecart', methods=['POST'])
def updatecart():
    cart = session.get('cart', {})
    for code, item in cart.items():
        qty = int(request.form.get(f'{code}_qty', 0))
        if qty > 0:
            item['qty'] = qty
            item['subtotal'] = item['price'] * qty
        else:
            del cart[code]
    session['cart'] = cart
    return redirect('/cart')

@app.route('/removeitem/<code>', methods=["POST"])
def remove_item(code):
    if session.get("cart") is None:
        return redirect('/cart')

    cart = session["cart"]
    if code in cart:
        del cart[code]

    if not cart:
        session.pop("cart", None)
    else:
        session["cart"] = cart

    return redirect('/cart')
@app.route('/clearcart', methods=['POST'])
def clear_cart():
    session.pop('cart', None)
    return redirect('/cart')

@app.route('/orders')
def orders():
    if "user" not in session:
        return redirect("/login")

    email = session["user"]["email"]
    order_list = db.get_orders(email)

    return render_template('orders.html', order_list=order_list)
@app.route('/checkout')
def checkout():
    # clear cart in session memory upon checkout
    om.create_order_from_cart()
    session.pop("cart",None)
    return redirect('/ordercomplete')

@app.route('/ordercomplete')
def ordercomplete():
    return render_template('ordercomplete.html')

@app.route('/changepassword', methods=['GET', 'POST'])
def changepassword():
    if "user" not in session:
        return redirect("/login")

    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if new_password != confirm_password:
            error_message = "New password and confirmed password do not match."
            return render_template('changepassword.html', error=error_message)

        email = session["user"]["email"]
        is_successful = db.change_password(email, old_password, new_password)

        if is_successful:
            success_message = "Password updated successfully!"
            return render_template('changepassword.html', success=success_message)
        else:
            error_message = "Old password is incorrect."
            return render_template('changepassword.html', error=error_message)

    return render_template('changepassword.html')