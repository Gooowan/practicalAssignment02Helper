import random
import datetime


# Function to generate random date
def random_date(start, end):
    return start + datetime.timedelta(days=random.randint(0, (end - start).days))


# Function to generate client IDs for opt_clients table
def generate_client_ids(num_clients):
    return [f"'{''.join(random.choices('abcdef0123456789-', k=36))}'" for _ in range(num_clients)]


# Function to generate product IDs for opt_products table
def generate_product_ids(num_products):
    return list(range(1, num_products + 1))


# Function to generate single insert for opt_clients
def generate_single_insert_opt_clients(num_clients):
    client_ids = generate_client_ids(num_clients)
    values = []
    statuses = ['active', 'inactive']
    for client_id in client_ids:
        name = f"'{''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))}'"
        surname = f"'{''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))}'"
        email = f"'{name[1:-1]}.{surname[1:-1]}@example.com'"
        phone = f"'{random.randint(1000000000, 9999999999)}'"
        address = f"'{''.join(random.choices('abcdefghijklmnopqrstuvwxyz ', k=50))}'"
        status = f"'{random.choice(statuses)}'"
        values.append(f"({client_id}, {name}, {surname}, {email}, {phone}, {address}, {status})")

    insert_statement = f"INSERT INTO opt_clients (id, name, surname, email, phone, address, status) VALUES {', '.join(values)};"
    return insert_statement, client_ids


# Function to generate single insert for opt_products
def generate_single_insert_opt_products(num_products):
    product_ids = generate_product_ids(num_products)
    values = []
    categories = ['Category1', 'Category2', 'Category3', 'Category4', 'Category5']
    for product_id in product_ids:
        product_name = f"'{''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))}'"
        product_category = f"'{random.choice(categories)}'"
        description = f"'{''.join(random.choices('abcdefghijklmnopqrstuvwxyz ', k=50))}'"
        values.append(f"({product_id}, {product_name}, {product_category}, {description})")

    insert_statement = f"INSERT INTO opt_products (product_id, product_name, product_category, description) VALUES {', '.join(values)};"
    return insert_statement, product_ids


# Function to generate single insert for opt_orders
def generate_single_insert_opt_orders(num_orders, client_ids, product_ids):
    values = []
    for _ in range(num_orders):
        order_date = f"'{random_date(datetime.date(2022, 1, 1), datetime.date(2024, 1, 1))}'"
        client_id = random.choice(client_ids)
        product_id = random.choice(product_ids)
        values.append(f"({order_date}, {client_id}, {product_id})")

    insert_statement = f"INSERT INTO opt_orders (order_date, client_id, product_id) VALUES {', '.join(values)};"
    return insert_statement


# Main function to generate all inserts
def generate_all_inserts():
    num_clients = 10000
    num_products = 10000
    num_orders = 10000

    # Generate inserts for opt_clients
    opt_clients_insert, client_ids = generate_single_insert_opt_clients(num_clients)

    # Generate inserts for opt_products
    opt_products_insert, product_ids = generate_single_insert_opt_products(num_products)

    # Generate inserts for opt_orders
    opt_orders_insert = generate_single_insert_opt_orders(num_orders, client_ids, product_ids)

    # Write the inserts to files
    with open('opt_clients_inserts.sql', 'w') as f:
        f.write(opt_clients_insert)

    with open('opt_products_inserts.sql', 'w') as f:
        f.write(opt_products_insert)

    with open('opt_orders_inserts.sql', 'w') as f:
        f.write(opt_orders_insert)


# Call the main function to generate the inserts
generate_all_inserts()
