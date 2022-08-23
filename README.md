## Telco Churn Classification Project

## Reduce Customer Churn
<hr style="border-top: 50px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Goals
> - The main goal of this project is identify drivers of customer churn.
> - Build machine learning model that can predict and identify customers that are like to churn.
> - Deliver a report on recommendations for reducing customer churn.

#### Project Description
> - Telco is a leading communications company offering great services to its customers.
> - Customers are churning at a high rate affecting the company's performance.
> - We will therefore identify drivers of customer churn and look at features with highest and low churn rate.
> - We will use machine learning prediction models and demographics and offer recommendations for customer retention.

#### Initial Questions
> - What is the churn rate Telco?
> - What are the features with the highest churn rate?
> - What are the features with the lowest churn rate?
> - What demographic has the highest churn rate?
#### Audience
> - Codeup Data Science students

#### Project Deliverables
> - A final report notebook 
> - A final report notebook presentation
> - All necessary modules to make my project reproducible

#### Project Context
> - The Telco dataset from the Codeup database.



#### Data Dictionary


        Column                                 Description                                                    Data type  
---     ------                                 --------------                                                 -----  
> - 0   payment_type_id                        Unique payment type id for customer                            Int  
> - 1   internet_service_type_id               Unique internet service type id for customer                   int  
> - 2   contract_type_id                       Unique contract type id for customer                           int  
> - 3   senior_citizen                         1 if customer is senior citizen                                int  
> - 4   tenure                                 Months of tenure as a customer                                 int  
> - 5   monthly_charges                        Customer's monthly bill charges                                float
> - 6   total_charges                          Customer's total bills                                         float
> - 7   gender_encoded                         Yes for 1 if customer is female                                int  
> - 8   partner_encoded                        Yes for 1 if customer is partner                               int  
> - 9   dependents_encoded                     Yes for 1 if customer has dependents                           int  
> - 10  phone_service_encoded                  Yes for 1 if customer has phone service                        int  
> - 11  paperless_billing_encoded              Yes for 1 if customer has paperless billing                    int  
> - 12  multiple_lines_No phone service        Yes for 1 if customer has multiple_lines but no phone service  int  
> - 13  multiple_lines_Yes                     Yes for 1 if customer has multiple_lines                       int 
> - 14  online_security_No internet service    1 if customer has internet but no online security              int  
> - 15  online_security_Yes                    1 if customer has online security                              int  
> - 16  online_backup_No internet service      1 if customer has online_backup but no internet service        int  
> - 17  online_backup_Yes                      1 if customer has online_backup                                int  
> - 18  device_protection_No internet service  1 if customer has internet but no device protection            int  
> - 19  device_protection_Yes                  1 if customer has device protection                            int  
> - 20  tech_support_No internet service       1 if customer has tech_support but no internet service         int  
> - 21  tech_support_Yes                       1 if customer has tech_support                                 int  
> - 22  streaming_tv_No internet service       1 if customer is streaming_tv but no internet service          int  
> - 23  streaming_tv_Yes                       1 if customer is streaming_tv                                  int  
> - 24  streaming_movies_No internet service   1 if customer is streaming_movies but no internet service      int  
> - 25  streaming_movies_Yes                   1 if customer is streaming_movies                              int  
> - 26  contract_type_One year                 1 if customer has contract_type_One year                       int  
> - 27  contract_type_Two year                 1 if customer has contract_type_Two year                       int  
> - 28  internet_service_type_Fiber optic      1 if customer has internet_service_type_Fiber optic            int  
> - 29  internet_service_type_None             1 if customer has No internet_service_type                     int  
> - 30  payment_type_Credit card (automatic)   1 if customer has automatic payment_type_Credit card           int  
> - 31  payment_type_Electronic check          1 if customer has Electronic check payment_type                int  
> - 32  payment_type_Mailed check              1 if customer has Mailed check payment_type                    int  


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>


### Initial Hypothesis
> - alpha = 0.05
> - HO: There is no relation between collumn features and churn rate
> - (collumn features and churn rate are independent)
> - (We fail to reject the H0 that collumn feature and churn rate are dependent)
> - H⍺: There is a relation between collumn features and churn rate
> - (collumn features and churn are dependent)
> - (We reject the H0 that collumn feature and churn rate are independent)

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Conclusions & Next Steps
### Executive Summary 
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - With Telco churn rate being at 27%. We identified the main drivers of churn. As per our analysis the main issues were customers with short term contracts, device protection with no internet service, customers with payment type electronic checks.
> - I chose DecisionTree model as my best model1 with a 73% accuracy rate for predicting my target value, churn. When we run the test data, the accuracy for the Decision tree model1 train is maintained at 73%. Therefore, the model has no data overfit compared to other models.

### Recommendations
> - Come up with incentives and promotions to have customers sign up for long term contracts.
> - Provide customers with technical support.
> - Set customer accounts to automatic payments to prevent missed payments.

### Next steps
> - Investigate why customers with Fibre optic churn.
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### Plan
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x]  Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train three different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with the measurement id, the probability of the target values, and the model's prediction for each observation in my test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

##### Plan -> Acquire
> - Store functions that are needed to acquire data from the measures and species tables from the iris database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> Prepare
> - Store functions needed to prepare the iris data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
___

##### Plan -> Acquire -> Prepare -> Explore
> - Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, species. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to species (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver
> - Introduce myself and my project goals at the very beginning of my notebook walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary. (Don't throw everything out that I learned from Storytelling) .
> - Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook
