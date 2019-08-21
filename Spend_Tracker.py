import mintapi
import datetime
import pandas as pd
mint = mintapi.Mint('username', 'password')

## Get transactions
transaction=mint.get_transactions() # as pandas dataframe
transaction.describe()
transaction.head()

debit_transaction = transaction[transaction['transaction_type'] == 'debit']
debit_transaction['Date'] =pd.to_datetime(debit_transaction['date'])
debit_transaction['Month']=debit_transaction['Date'].dt.month
debit_transaction['Year'] =debit_transaction['Date'].dt.year

filter_list = ['bills & utilities','mobile phone','internet','utilities','television']
debit_transaction.loc[debit_transaction.category.isin(filter_list),'category']='Bills & utilities'
filter_list = ['coffee shops', 'fast food', 'food & dining','restaurants']
debit_transaction.loc[debit_transaction.category.isin(filter_list),'category']='Eating Out'
filter_list = ['charity','gifts & donations','kids activities' ]
debit_transaction.loc[debit_transaction.category.isin(filter_list),'category']='Charity'
filter_list = ['movies & dvds', 'hotel','air travel', 'travel', 'amusement', 'sports' , 'sporting goods','entertainment' ]
debit_transaction.loc[debit_transaction.category.isin(filter_list),'category']='Travel & Amusement'
filter_list = ['parking', 'rental car & taxi','auto & transport','public transportation','service & parts','auto insurance']
debit_transaction.loc[debit_transaction.category.isin(filter_list),'category']='Transport'
filter_list = ['groceries','shopping','books','clothing','gift','home improvement','newspapers & magazines','electronics & software','office supplies']
debit_transaction.loc[debit_transaction.category.isin(filter_list),'category']='Groceries & shopping'
filter_list = ['shipping','personal care','hair','home services','tuition']
debit_transaction.loc[debit_transaction.category.isin(filter_list),'category']='Business services'
filter_list = ['doctor','pharmacy']
debit_transaction.loc[debit_transaction.category.isin(filter_list),'category']='Health'

value_list = ["Zareen's Restaurant","Gulzaar Halaal","Vons"]
debit_transaction.loc[debit_transaction.description.isin(value_list),'category']='Eating Out'
value_list = ['Halal Meats']
debit_transaction.loc[debit_transaction.description.isin(value_list),'category']='groceries & shopping'
month=datetime.datetime.now().month
year=datetime.datetime.now().year

## Exporting to Excel
debit_transaction_current_month_year.to_excel('C:\\Users\\mmujtaba\\Downloads\\month%s_transaction.xlsx' %month,index = False)
The same can be done to get the data for the whole year:
debit_transaction_current_year = debit_transaction[(debit_transaction['Year']==year) & (debit_transaction['category']!='credit card payment') & (debit_transaction['category']!='check')  & (debit_transaction['account_name']!='PayPal Account') & (debit_transaction['account_name']!='Venmo')]

Total=debit_transaction_current_month_year['amount'].sum()
print("Monthly spending: %s" %(Total))
monthly_budget=***
## Monthly budget spent compared to month spent 
print("Monthly budget spent: %s" %((Total)/monthly_budget))
x=pd.to_datetime(debit_transaction_current_month_year['Date'])
print("Month spent: %s" %(max(x.dt.day)/30))
debit_transaction_current_month_year[['date','category','description','amount']]
