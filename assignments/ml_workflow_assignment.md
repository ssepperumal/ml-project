Task 1
Label: repeat_purchase_flag
     This repeat_purchase_flag has to predict (whether customer will purchase again or not).
Data leakage column: discount_used_on_repeat_order
     This is leakage because it’s only known after the repeat purchase happens, so it gives away the answer.
     
     
Task 2
Exploratory Data Analysis (EDA)
	To understand the data (missing values, patterns, etc.) before building a model.
Train-Test Split
	To test the model on unseen data and check if it actually works properly.
