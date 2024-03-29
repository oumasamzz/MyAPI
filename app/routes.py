from flask import jsonify
from app.models import Product

# Define routes
@app.route('/products')
def get_products():
    # Fetch products from the database
    products = Product.query.all()

    # Convert products to JSON
    result = []
    for product in products:
        result.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'sku': product.sku,
            'quantity': product.quantity,
            'price': product.price,
            'image_url': product.image_url
        })

    return jsonify(result)
