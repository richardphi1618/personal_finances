# Personal Finances Data Cleaner

This is a project where I can inspect my transaction history from my Navy Federal accounts with a bi tool later. This python script cleans and categorizes all the transaction data before I upload to my bi tool of choice. 

What the data folder should look like:
```
./data
├── Wife <----------------------------------------------------account_owner
│   ├── CC <--------------------------------------------------account_type
│   │   ├── CC_20190813_20191009.CSV <------------------------transaction_data
│   │   ├── CC_202206_202208.CSV
│   │   ├── creditcard2.CSV
│   │   ├── creditcard3.CSV
│   │   ├── creditcard4.CSV
│   │   └── transactions_april_june_2022.CSV
│   ├── checking
│   │   └── checking.CSV
│   └── savings
│       └── savings.CSV
├── Joint
│   └── Savings
│       └── shared_savings.CSV
├── Me
│   ├── CC
│   │   └── CC_201907_20220809.CSV
│   ├── checking
│   │   └── checking.CSV
│   └── savings
│       └── savings.CSV
├── master_processed.csv
└── master_raw.csv
```
> 💡note: the name of the file doesn't matter. must be a csv