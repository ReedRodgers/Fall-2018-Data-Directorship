import pandas as pd

data = pd.read_csv('EngSoc_Survey.csv')

# Lets clean this data up
# First, remove all responses that aren't finished or are a preview response
data = data[(data.Finished != 'False') & (data.Status != 'Survey Preview')]
# data = data[data.Status != 'Survey Preview']
# Remove the additional header rows Qualtrics gives us
data = data.drop([0,1])

# Convert columns to ints where applicable
data['Duration'] = data['Duration'].astype('int')

# Get rid of the outliers in terms of completion time
durationStd = data.Duration.std()
durationMed = data.Duration.median()
data = data[(data.Duration <= durationStd) | (data.Duration <= .2*durationMed)]

