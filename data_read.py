import csv
import pandas as pd

adult_train = pd.read_csv('Adult_train.tab', delimiter = '\t' )
adult_train.drop([0,1], inplace = True)
adult_train.reset_index()


def numeric(dataframe):
    for column in dataframe:
            dataframe[column] = pd.to_numeric(dataframe[column],downcast = 'integer', errors='ignore')


numeric(adult_train)


columns= ('workclass', 'education', 'marital-status', 'occupation',  'relationship', 'race', 'sex', 'y')
for column in columns:
    adult_train[column + '_cat'] = pd.Categorical(adult_train[column]).codes


adult_train['native-country_cat'] = pd.Categorical(adult_train['native-country'], categories = ('United-States', 'Not-United-States')).codes

adult_train_cat = adult_train[['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week', \
                               'workclass_cat', 'education_cat', 'marital-status_cat', 'occupation_cat', 'relationship_cat',\
                               'race_cat', 'sex_cat', 'native-country_cat','y_cat' ]]