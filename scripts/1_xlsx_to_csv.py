import pandas as pd

data_2009_2010 = pd.read_excel( io = 'raw_data/online_retail_II.xlsx', 
                                sheet_name = 0,
                                header = 0)

data_2010_2011 = pd.read_excel( io = 'raw_data/online_retail_II.xlsx',
                                sheet_name = 1,
                                header = 0)

# print(data_2009_2010.head)