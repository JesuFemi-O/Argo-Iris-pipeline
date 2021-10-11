import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib


# when we get to this step in the workflow, the template spec
# would have our data injected into the container from the previous task in our dag
# and so data would be available in whatever path we specify here -> /data/*.csv

# if I run this container without it being part of a workflow, it woud fail.
# this is because the image would not have data/*.csv in it. that data is passed into
# this container as an artifact by the workflow, during the workflow execution by argo

x_train = pd.read_csv('/tmp/x_train.csv')
x_test = pd.read_csv('/tmp/x_test.csv')
y_train = pd.read_csv('/tmp/y_train.csv')
y_test = pd.read_csv('/tmp/y_test.csv')

# in the long run I only want this step to build the model and output it as an artifact
# for now I would do everything in this step
model = DecisionTreeClassifier()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

score = accuracy_score(y_pred=y_pred, y_true=y_test)

# save model test performance
with open('/tmp/score.txt', 'w') as f:
    print('Model Score:', score, file=f)

# save the model to disk
filename = '/tmp/finalized_model.sav'
joblib.dump(model, filename)


# we can therefore get 2 artifacts from here:
# - the test score of our model
# - the the pickled model object


# when this flow works what we can do is build a tool that can take clean data
# allow you to pick an army of models
# choose a decison matrix
# return your best model back to you
# even better, provide a service endpoint with your model as an api so you can easily use in your business
