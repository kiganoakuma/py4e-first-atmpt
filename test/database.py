import sqlite3
from tabulate import tabulate

# Connect to the database
conn = sqlite3.connect('/Users/devil/Desktop/lrn.mng.sys.db')
cursor = conn.cursor()

# Execute the query to retrieve the combined and sorted data
query = '''
select User.name, Member.role, Course.title
From User join Member join Course on 
Member.user_id = User.id and Member.course_id = Course.id
Order by User.name, Member.role, Course.title
'''
cursor.execute(query)

# Fetch all rows from the result
rows = cursor.fetchall()

# Define the column headers
headers = ['Name', 'Member', 'Course']

# Display the combined and sorted data in organized columns
print(tabulate(rows, headers=headers, tablefmt='pipe'))

# Close the database connection
conn.close()