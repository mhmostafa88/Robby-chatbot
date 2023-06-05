import sqlite3

# Connect to the database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create the revenue_data table
create_table_query = '''
    CREATE TABLE revenue_data (
        month VARCHAR(20),
        revenue INT,
        budgeted_revenue INT,
        last_month_revenue INT,
        twelve_months_prior_revenue INT
    )
'''
cursor.execute(create_table_query)

# Insert the revenue data
insert_data_query = '''
    INSERT INTO revenue_data (month, revenue, budgeted_revenue, last_month_revenue, twelve_months_prior_revenue)
    VALUES ('Current Month', 86000, 75000, 73000, 50000)
'''
cursor.execute(insert_data_query)

# Commit the changes and close the connection
conn.commit()
conn.close()