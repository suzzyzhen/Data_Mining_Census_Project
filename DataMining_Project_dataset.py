import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

    #add headers
feature_names = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','50k']

train_df_nan = pd.read_csv('census-income.data.csv', names = feature_names)
test_df_nan = pd.read_csv('census-income.test.csv', names = feature_names)

print('The total number of instances in train data is', len(train_df_nan), 'with features', len(train_df_nan.columns))
print('The total number of instances in test data is', len(test_df_nan), 'with features', len(test_df_nan.columns))



# replace '?' with nan values \n",
train_df_nan.replace(' ?', np.nan, inplace=True)
test_df_nan.replace(' ?', np.nan, inplace=True)

#replace the label column with '0' and '1', <=50k = 0; >50k = 1
train_df_nan['50k'] = pd.get_dummies(train_df_nan).iloc[:,-1]
test_df_nan['50k'] = pd.get_dummies(test_df_nan).iloc[:,-1]

counts_train = train_df_nan['50k'].value_counts()
counts_test = test_df_nan['50k'].value_counts()

print(counts_train)
print('***less than 50k',round(counts_train[0]/len(train_df_nan['50k']),3), '***More than 50k', round(counts_train[1]/len(train_df_nan['50k']),3))
print(counts_test)
print('***less than 50k',round(counts_test[0]/len(test_df_nan['50k']),3), '***More than 50k', round(counts_test[1]/len(test_df_nan['50k']),3))
#Test
#print(train_df_nan.head(50))
#print(test_df_nan.head(50))

#count instances with nan values
train_df = train_df_nan.dropna()
print(len(train_df_nan) - len(train_df), 'train instances contain missing values')
print(train_df_nan.isnull().sum())
test_df = test_df_nan.dropna()
print(len(test_df_nan) - len(test_df), 'test instances contain missing values')
print(test_df_nan.isnull().sum())

train_df_nan.head()

train_df_nan['occupation'].value_counts()

#use mode or KNN to fill missing values (pick two to three methods)
#fillna with mode
#print(train_df_nan['workclass'].value_counts(dropna=False).head())
#print(train_df_nan['occupation'].value_counts(dropna=False).head())
#print(train_df_nan['native_country'].value_counts(dropna=False).head())

train_df_nan['workclass'].fillna(train_df_nan['workclass'].mode()[0],inplace=True)
train_df_nan['occupation'].fillna(value ='Other-service', inplace=True)      #replace NaN occupation with other services
train_df_nan['native_country'].fillna(train_df_nan['native_country'].mode()[0],inplace=True)

#print('*'*100, train_df_nan.isnull().sum())

#print(test_df_nan['workclass'].value_counts(dropna=False).head())
#print(test_df_nan['occupation'].value_counts(dropna=False).head(10))
#print(test_df_nan['native_country'].value_counts(dropna=False).head())



test_df_nan['workclass'].fillna(test_df_nan['workclass'].mode()[0],inplace=True)
test_df_nan['occupation'].fillna(value ='Other-service', inplace=True)      #replace NaN occupation with other services
test_df_nan['native_country'].fillna(test_df_nan['native_country'].mode()[0],inplace=True)


#print('*'*100, test_df_nan.isnull().sum())


#normalization for continuous features


#transform categorical data into numeric data (encoder and one hot encoder)
from sklearn import preprocessing
import csv
feature_names = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','50k']
pd.set_option('display.max_row', 1000)
pd.set_option('display.max_columns', 50)
#dataset = pd.read_csv("census-income.data.csv",names = feature_names)

#######################################################################
file = open("dictionery.txt","w")
le = preprocessing.LabelEncoder()
########################################################################

#workclass
workclass = train_df_nan.workclass
#workclassUNI = dataset.workclass.unique()  #check the unique elements under this column
le.fit(workclass)
le_workclass_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
workclass_encoded = le.transform(workclass)
repr(le_workclass_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_workclass_mapping) + '\n' + "###########################" + '\n')

###########################################################################

#education
education = train_df_nan.education
#educationUNI = dataset.education.unique()  #check the unique elements under this column
le.fit(education)
le_education_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
education_encoded = le.transform(education)
repr(le_education_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_education_mapping) + '\n' + "###########################" + '\n')

########################################################################

#marital_status
marital_status = train_df_nan.marital_status
#marital_statusUNI = dataset.marital_status.unique()  #check the unique elements under this column
le = preprocessing.LabelEncoder()
le.fit(marital_status)
le_marital_status_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
marital_status_encoded = le.transform(marital_status)
repr(le_marital_status_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_marital_status_mapping) + '\n' + "###########################" + '\n')

########################################################################

#occupation
occupation = train_df_nan.occupation
#occupationUNI = dataset.occupation.unique()  #check the unique elements under this column
le.fit(occupation)
le_occupation_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
occupation_encoded = le.transform(occupation)
repr(le_occupation_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_occupation_mapping) + '\n' + "###########################" + '\n')

########################################################################

#relationship
relationship = train_df_nan.relationship
#relationshipUNI = dataset.relationship.unique()  #check the unique elements under this column
le.fit(relationship)
le_relationship_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
relationship_encoded = le.transform(relationship)
repr(le_relationship_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_relationship_mapping) + '\n' + "###########################" + '\n')

########################################################################

#race
race = train_df_nan.race
#raceUNI = dataset.race.unique()  #check the unique elements under this column
le.fit(race)
le_race_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
race = le.transform(race)
repr(le_race_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_race_mapping) + '\n' + "###########################" + '\n')

########################################################################

#sex
sex = train_df_nan.sex
#sexUNI = dataset.sex.unique()  #check the unique elements under this column
le.fit(sex)
le_sex_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
sex_encoded = le.transform(sex)
repr(le_sex_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_sex_mapping) + '\n' + "###########################" + '\n')

########################################################################

#native_country
native_country = train_df_nan.native_country
#native_countryUNI = dataset.native_country.unique()  #check the unique elements under this column
le.fit(native_country)
le_native_country_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
native_country_encoded = le.transform(native_country)
repr(le_native_country_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_native_country_mapping) + '\n' + "###########################" + '\n')

########################################################################
file.close()
#####################################################################################'workclass','education','marital_status','occupation','relationship','race','sex','native_country'

column_list = [workclass_encoded, education_encoded, marital_status_encoded, occupation_encoded, relationship_encoded, race, sex_encoded, native_country_encoded]

census_list = []

for (workclass_1, education_1, marital_1, occupation_1, relationship_1, race_1, sex_1, native_1) in zip(workclass_encoded, education_encoded, marital_status_encoded, occupation_encoded, relationship_encoded, race, sex_encoded, native_country_encoded):
    census_list.append((workclass_1, education_1, marital_1, occupation_1, relationship_1, race_1, sex_1, native_1))

with open ('encoding.csv','w') as f:
    thewriter = csv.writer(f, delimiter =",")
    thewriter.writerow(('workclass', 'education', 'marital status', 'occupation', 'relationship', 'race', 'sex', 'native country'))
    for row in census_list:
        thewriter.writerow(row)



#handle unbalanced data (boosting and bagging)
#balancing the data
from sklearn.utils import resample

train_df_nan['50k'].value_counts()
rich=train_df_nan.loc[train_df_nan['50k']==1]
poor=train_df_nan.loc[train_df_nan['50k']==0]
train_df_nan['50k'].value_counts()
rich_upsample=resample(rich,replace=True,n_samples=len(poor),random_state=27)
balancetrain=pd.concat([rich_upsample,poor],ignore_index=True)
balancetrain['50k'].value_counts()

#algorithms: KNN/Naive Bayes/Random forest



#plt.scatter(test_df_nan[:,0], test_df_nan[:,1], s=10)