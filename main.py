# df.to_csv(‘existing.csv’, mode=’a’, index=False, header=False)

# Append Pandas DataFrame to Existing CSV File
# importing pandas module
import pandas as pd

# data of Player and their performance
data = {
	'omr_val_sl': 'AFSD284A',
	'omr_val_roll': 10202,
	'omr_val_qr': 'AFSD284A',
	'omr_val_start_time': '2019-01-01 01:17:49',
	'omr_val_end_time': '2019-01-01 01:18:10', # time stamp
}

# i feel i can be fit for your team and i will be happy to be your player.

# Make data frame of above data
df = pd.DataFrame(data, index=[0])

# append data frame to CSV file
# df.to_csv('test.csv', mode='a',header= True, index=False,)
df.to_csv('test.csv', mode='a',header= False,)
# df.to_csv('res/csv/test.csv', mode='a', index=False, header=False)

# print message
print("Data appended successfully.")
