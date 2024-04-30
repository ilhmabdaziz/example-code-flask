# Conditions on flask : 
y = 20

if y > 20:
    print("y is greater than 10")
elif y == 20:
    print('y is equal to 10')
else:
    print('y is less than 20')

print('===========================================')

# Lopping :
for i in range(10):
    print(i)

print('===========================================')

# While:
i = 0
while i < 10:
    print(i)
    i += 1

print('===========================================')

# Aritmatic operations:
x = 50
y = 20

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)

print('===========================================')

# Database connection using MYSQL and query:

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database_name"
)

cursor = conn.cursor()

# Create table:
create_query_table = "CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT)"
cursor.execute(create_query_table)

# Insert data:
insert_query = "INSERT INTO products (name, price) VALUES ('Product 1', 100)"
cursor.execute(insert_query)
conn.commit()

# Select data:
select_query = "SELECT * FROM products"
cursor.execute(select_query)
result = cursor.fetchall()
for row in result:
    print(row)

# Update data:
update_query = "UPDATE products SET price = 200 WHERE id = 1"
cursor.execute(update_query)
conn.commit()

# Delete data:
delete_query = "DELETE FROM products WHERE id = 1"
cursor.execute(delete_query)
conn.commit()


# Closing the cursor and connection:
cursor.close()
conn.close()


print('===========================================')

# Flask:
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_product():
    return jsonify({'message': 'data retrievedsuccessfully', 'data': [{"id":1, "name": "Make up", "price": 100}], "error": 0})

@app.route('/api', methods=['POST'])
def post_product():
    data = request.json
    name = data['name']
    price = data['price']
    return jsonify({'message': 'data inserted successfully', 'data': {"id": 2, "name": name, "price": price}, "error":0})

if __name__ == '__main__':
    app.run(debug=True)

