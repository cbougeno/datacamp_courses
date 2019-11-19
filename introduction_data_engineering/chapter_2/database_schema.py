import pandas as pd

# Complete the SELECT statement
data = pd.read_sql("""
SELECT first_name, ____ FROM "____"
ORDER BY ____, ____
""", db_engine)

# Show the first 3 rows of the DataFrame
print(data.head(____))

# Show the info of the DataFrame
print(data.____())