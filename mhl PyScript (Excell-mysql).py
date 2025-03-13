import pandas as pd
import mysql.connector

# Connect to MySQL Workbench Database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mHl0000!@#$",
    database="openmind"
)
cursor = conn.cursor()

# Load Excel File
df = pd.read_excel("social media usage of youthGenbd (2023-24).xlsx")  # Ensure the file is in the same directory or provide full path

# Insert Data into MySQL
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO smedia_usage (
        Platform, Year, Total_Users, Male_Users, Female_Users, 
        Percentage_Total_Population, Percentage_Internet_Users, Average_TimeSpent_PerDay) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("Data imported successfully!")
