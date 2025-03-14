import mysql.connector

# Connect to MySQL Database
conn = mysql.connector.connect(
    host="localhost",       # Change if using a remote MySQL server
    user="root",            # Replace with your MySQL username
    password="mHl0000!@#$",# Replace with your MySQL password
    database="openmind"     # Ensure the database exists
)

# Create a cursor object
cursor = conn.cursor()

# Define the SQL query to create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS smedia_usage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Platform VARCHAR(100),
    Year INT,
    Total_Users INT,
    Male_Users INT,
    Female_Users INT,
    Percentage_Total_Population DECIMAL(5,2),
    Percentage_Internet_Users DECIMAL(5,2),
    Average_TimeSpent_PerDay DECIMAL(5,2)
);
"""

# Execute the query
cursor.execute(create_table_query)

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()

print("✅ Table 'smedia_usage' created successfully in 'openmind' database!")
