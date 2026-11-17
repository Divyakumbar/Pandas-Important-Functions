import pandas as pd
data={
    "Name":["Divya","Akshay","Rahul","Ramya","Vinay","kumari","Keerthi","tanu"],
    "Marks":[100,80,76,89,100,None ,74,39]
}
df=pd.DataFrame(data)
print(df)
print("First 5 rows")
print(df.head())            # first 5 rows
print("Last 5 rows")
print(df.tail())            # last 5 rows
print(df.shape)             # number of rows and col
print(df.columns)           # displays col names
print(df.isnull())          # checks missing values
print(df.sort_values(by="Marks"))    #sorts