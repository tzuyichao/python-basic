def apply_discount(product, discount):
    price = product['price'] * discount
    assert 0 < price <= product['price']
    return price


if __name__ == "__main__":
    shoes = {'name': '潮鞋', 'price': 149}
    print(shoes, apply_discount(shoes, 0.75))
    print(shoes, apply_discount(shoes, -0.5))
