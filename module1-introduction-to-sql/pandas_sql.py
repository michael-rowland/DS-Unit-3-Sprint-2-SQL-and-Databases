import os
import pandas as pd
import sqlite3

CSV_PATH = os.getcwd()+'/buddymove_holidayiq.csv'

connection = sqlite3.connect('BuddyMove.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

df = pd.read_csv(CSV_PATH)
# ONLY NEEDS TO BE RUN ONCE
# df.to_sql('sample_export', con=connection)

'''
Q1: Count how many rows you have - it should be 249!
'''
q1 = '''
SELECT
    COUNT(DISTINCT "index")
FROM
    sample_export
'''

result = cursor.execute(q1).fetchall()
print('QUERY 1 RESULT:', result[0][0])


'''
Q2: How many users who reviewed at least 100 Nature in the category also 
reviewed at least 100 in the Shopping category?
'''
q2 = '''
SELECT
    COUNT(DISTINCT "User Id")
FROM
    sample_export
WHERE
    Nature >= 100
    AND Shopping >= 100
'''

# THIS ALSO WORKS
# result2 = cursor.execute(q2).fetchone()
# print(result2['COUNT(DISTINCT "User Id")'])
result2 = cursor.execute(q2).fetchone()
print('QUERY 2 RESULT:', result2[0])
