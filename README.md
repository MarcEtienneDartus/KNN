# KNN : K-Nearest Neighbors Algorithm

KNN can be used for <b>classification</b> : the output is a class membership.
An object is classified by a majority vote of its neighbors, with the object being assigned to the class most common among its k nearest neighbors.

It can also be used for <b>regression</b> : output is the value for the object (predicts continuous values). This value is the average (or median) of the values of its k nearest neighbors.

## Data set

An exemple of data we can process:

![](./Readme_Content/iris.jpg?raw=true "Iris data set")

The project has two steps:

- We have a first dataset named "training.csv". It has exactly the same structure as the Iris dataset with 4 input variables and a qualitative output variable. the goal is to cut it into two sets: <b>training</b> and <b>testing</b> set. For this, parameters such as the number of lines in each data set and the K must varied.

- The second dataset is named "predict.csv". We must use the model to predict the class for each sample of the file. An output file will contain each prediction associated with its line.

## Run the code

Now we can run the code !

```cmd
python knn.py
```

It will show us the different k for our parameters:
- 80% training set
- 20% testing set


![](./Readme_Content/prediction.jpg?raw=true "Iris data set")

We found that K=7 has the best percentage of accuracy after running some test.

At the end we have an output file with our prediction called "Prediction.txt"