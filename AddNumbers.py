import pandas
df = pandas.read_csv('../data/data.data',
                         sep = "\t",
                         header = None)

sum1 = df.sum()
print(sum1) 
#print(df)
