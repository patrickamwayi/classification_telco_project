# import standard libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import our own acquire module
import acquire

# import splitting functions
from sklearn.model_selection import train_test_split

def prep_iris(df):
    df = df.drop(columns=['species_id'])
    df = df.drop(columns=['measurement_id'])
    df = df.rename(columns = {'species_name': 'species'})

    dummy_df = pd.get_dummies(df[['species']], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    #df = df.drop(columns=['species'])

    return df

def prep_titanic(df):
    #df=df.drop(columns = ["embarked","class"])
    df=df.drop(columns = ["age","deck"])
    df.embark_town = df.embark_town.fillna(value = "Southampton")
    dummy_df =pd.get_dummies(df[['sex','embark_town']], drop_first = True)
    df = pd.concat([df,dummy_df], axis = 1)
    df = df.drop(columns = ["sex","embark_town"])

    return df



def prep_telco(df):
    #df = df.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id'])

    df['gender_encoded'] = df.gender.map({'Male': 1, 'Female': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type'
                            ]],
                              drop_first=True)
    df = pd.concat( [df, dummy_df], axis=1 )
    

    df= df.drop(columns = ['customer_id', 
                         'gender', 
                         'partner', 
                         'dependents', 
                         'phone_service', 
                         'tech_support', 
                         'streaming_tv',
                         'multiple_lines',
                         'online_security',
                         'online_backup',
                         'device_protection',
                         'paperless_billing',
                         'churn',
                         'contract_type',
                         'internet_service_type',
                         'payment_type',
                         'streaming_movies'])

    df.total_charges.replace({"":0," ":0},inplace=True)
    df.total_charges = df.total_charges.astype(float)

    return df

    # split
def my_train_test_split(df,target):

     train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[target])
     train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train[target])

     return train, validate, test 