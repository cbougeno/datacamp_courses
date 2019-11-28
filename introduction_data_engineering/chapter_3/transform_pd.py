import pandas as pd

# Pandas DataFrame with customer data
customer = {"customer_id": 1, "email": "jane.doe@theweb.com"}
customer_df = pd.DataFrame.from_dict(customer)
# +- customer_id -+-             email      -+
# +---------------+--------------------------|
# |  1            |     jane.doe@theweb.com  |
# +---------------+--------------------------|

# Split email column into 2 columns on the '@' symbol
split_email = customer_df['email'].str.split('@', expand=True)
# At this point, split_email will hace 2 columns, a first one whith everything before '@', and a second one with after @

# Create 2 new columns using the resulting DataFrame
customer_df = customer_df.assign(
    username=split_email[0],
    domain=split_email[1]
)

print(customer_df)
