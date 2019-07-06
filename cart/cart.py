from decimal import Decimal
from django.conf import settings
from shop.models import Product


# session data structure
"""

self.cart = {'product_id':{'quantity': 1, 'price':'10', 'product': model(product)},
				 }

"""


class Cart():

    def __init__(self, request):
        "this class get the arg from the browser session and instantiate "
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):

        product_id = str(product.id)
        if not product_id in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):

        self.session[settings.CART_SESSION_ID] = self.cart

        self.session.modified = True

    def remove(self, product):

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        "get the corresponding product model from cart keys (product.id)"

        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
                # adding new keys to the product id
            self.cart[str(product.id)]['product'] = product

        # adding total_price key to the cart dict

        for item in self.cart.values():

            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        "counting all items in the cart"

        return sum([item['quantity'] for item in self.cart.values()])

    def get_total_price(self):

        return sum([item['price'] * item['quantity'] for item in self.cart.values()])

    def clear(self):

        del self.session[settings.CART_SESSION_ID]
        self.save()
