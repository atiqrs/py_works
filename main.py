# df.to_csv(‘existing.csv’, mode=’a’, index=False, header=False)

# Append Pandas DataFrame to Existing CSV File
# importing pandas module
import pandas as pd

# data of Player and their performance
data = {
	'Name': ['Mr. Y', 'Mr. X', 'Mr. Z'],
	'Age': [15,12,13],
	# 'Catch': [4, 2, 1]
}

# Make data frame of above data
df = pd.DataFrame(data, index=['1', '2', '3'])

# append data frame to CSV file
# df.to_csv('test.csv', mode='a',header= True, index=False,)
df.to_csv('test.csv', mode='a',header= False, index=True,)
# df.to_csv('res/csv/test.csv', mode='a', index=False, header=False)

# print message
print("Data appended successfully.")
