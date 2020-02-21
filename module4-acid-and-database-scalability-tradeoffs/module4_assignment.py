import sqlite3

connection = sqlite3.connect('titanic.db')
cursor = connection.cursor()

q1 = '''
SELECT COUNT(DISTINCT"name")
FROM passengers 
WHERE survived=TRUE
'''
result1 = cursor.execute(q1).fetchall()
print(f'How many passengers survived, and how many died? {result1}')

q2 = '''
SELECT pclass,COUNT(id)
FROM passengers 
GROUP BY pclass
'''
result2 = cursor.execute(q2).fetchall()
print(f'How many passengers were in each class? {result2}')

q3 = '''
SELECT pclass,COUNT(id)
FROM passengers 
WHERE survived=TRUE 
GROUP BY pclass
'''
result3 = cursor.execute(q3).fetchall()
print(f'How many passengers survived/died within each class? {result3}')

q4 = '''
SELECT survived,AVG(age)
FROM passengers 
GROUP BY survived
'''
result4 = cursor.execute(q4).fetchall()
print(f'What was the average age of survivors vs nonsurvivors? {result4}')

q5 = '''
SELECT pclass,AVG(age)
FROM passengers 
GROUP BY pclass
'''
result5 = cursor.execute(q5).fetchall()
print(f'What was the average age of each passenger class? {result5}')

q6 = '''
SELECT pclass,survived,AVG(fare)
FROM passengers 
GROUP BY pclass,survived 
ORDER BY pclass,survived DESC
'''
result6 = cursor.execute(q6).fetchall()
print(f'What was the average fare by passenger class? By survival? {result6}')

q7 = '''
SELECT pclass,survived,AVG(sib_spouse_count)
FROM passengers 
GROUP BY pclass,survived 
ORDER BY pclass,survived DESC
'''
result7 = cursor.execute(q7).fetchall()
print(f'How many siblings/spouses aboard on average, by passenger class? By 
survival? {result7}')

q8 = '''
SELECT pclass,survived,AVG(parent_child_count)
FROM passengers 
GROUP BY pclass,survived 
ORDER BY pclass,survived DESC
'''
result8 = cursor.execute(q8).fetchall()
print(f'How many parents/children aboard on average, by passenger class? By 
survival? {result8}')

q9 = '''
SELECT"name",count("name")
FROM passengers 
GROUP BY"name" 
HAVING COUNT(*)>1
'''
result9 = cursor.execute(q9).fetchall()
print(f'Do any passengers have the same name? {result9}')

connection.commit()