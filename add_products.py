from app import app, db
from app.models import Product

def add_sample_products():
    # Create sample products
    product1 = Product(name='Product 1', description='Description for Product 1', sku='SKU001', quantity=10, price=20.0, image_url='https://example.com/product1.jpg')
    product2 = Product(name='Product 2', description='Description for Product 2', sku='SKU002', quantity=15, price=25.0, image_url='https://example.com/product2.jpg')

    # Add products to the database
    with app.app_context():
        db.session.add(product1)
        db.session.add(product2)
        db.session.commit()

if __name__ == "__main__":
    add_sample_products()