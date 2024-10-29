'''
Author: Ms Rya
Version: 3.10
'''

import sqlite3

conn = sqlite3.connect('operations.db')
sth = conn.cursor()

sth.execute('''
CREATE TABLE IF NOT EXISTS results (
    integer_plus_ten INT,
    float_times_2_5 FLOAT,
    input_length INT
)
''')
print("Results table created!")

def arithmeticOperations(num_str):
    num_int = int(num_str)
    num_float = float(num_str)

    sum_result = num_int + 10
    product_result = num_float * 2.5
    input_length = len(num_str)

    print("Results of arithmetic operations:")
    print(f"Integer + 10: {sum_result}")
    print(f"Float * 2.5: {product_result}")
    print(f"Length of the input string: {input_length}")

    
    sth.execute('''
    INSERT INTO results(integer_plus_ten, float_times_2_5, input_length)
    VALUES (?, ?, ?)
    ''', (sum_result, product_result, input_length))

    conn.commit()
    print('Results are updated into the database')


num_str = input("Enter a number: ")
arithmeticOperations(num_str)


sth.execute('SELECT * FROM results')
records = sth.fetchall()

print("\nStored Results:")
for record in records:
    print(f"Integer + 10: {record[0]}, Float * 2.5: {record[1]}, Length: {record[2]}")


conn.close()
print("Database is closed")
