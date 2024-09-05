import unittest
from app import app
from faker import Faker

fake = Faker()

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_customers(self):
        id = fake.random_number(digits=3)
        name = fake.words(nb=2)
        email = fake.email(safe=True)
        phone = fake.phone_number()

        payload = {'id': id, 'name': name, 'email': email, 'phone': phone}
        response = self.app.post('/customers', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], data['result'])

    def test_customer_accounts(self):
        id = fake.random_number(digits=3)
        username = fake.words(nb=2)
        password = fake.password()
        customer_id = 1

        payload = {'id': id, 'username': username, 'password': password, 'customer_id': customer_id}
        response = self.app.post('/accounts', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], data['result'])

    def test_products(self):
        id = fake.random_number(digits=3)
        name = fake.words(nb=2)
        price = fake.random_number(digits=2)

        payload = {'id': id, 'name': name, 'price': price}
        response = self.app.post('/products', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], data['result'])

    def test_orders(self):
        id = fake.random_number(digits=3)
        customer_id = 1
        product_id = 1
        quantity = 1
        total_price = 10

        payload = {'id': id, 'customer_id': customer_id, 'product_id': product_id, 'quantity': quantity, 'total_price': total_price}
        response = self.app.post('/orders', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], data['result'])



if __name__ == '__main__':
    unittest.main()