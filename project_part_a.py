import pandas as pd
import numpy as np

# Feature Ranking

# Function for finding the entropy using input data
def calculate_entropy(input_data):
    # initialize entropy
    entropy = 0
    # eg. Label is either Yes or No in case of Response
    labels = input_data.unique()
    for label in labels:
        # calculate proportion based on number of occurance of example "Sunny" label in "Outlook" attribute
        proportion = len(input_data[input_data == label]) / len(input_data)
        # subtact with multiplier from entropy calculation
        entropy -= proportion * np.log2(proportion)   
    # now we have entropy for full attribute  
    return entropy

# IG = entropy(parent) - [average entropy(children)]
def calculate_information_gain(input_data, parent):

    # total samples and entropy(parent)
    #print("Total Samples:" , len(parent))
    #print("Starting Entropy of Parent:", calculate_entropy(parent))

    # Find unique class Yes or No
    labels = parent.unique()
    # for label in labels:
    #     proportion = len(parent[parent == label])
    #     print(label, ":", proportion)
    # print("\n")
    
    # empty array to store all the entropies
    feature_entropy = {}

    # Go through each feature
    for feature in input_data:
        #print("Running analysis on Feature:", feature)
        feature_entropy[feature] = 0
        # values of the feature target is now identified - "Humidity"'s values
        values = input_data[feature].unique()
        for value in values:
            subset = parent[input_data[feature] == value]   
            feature_entropy[feature] += len(subset) / len(parent) * calculate_entropy(subset)  

    # to store all the IG's
    information_gain = {}
    for feature in feature_entropy:
        information_gain[feature] = calculate_entropy(parent) - feature_entropy[feature]
    return information_gain

# Given the data from Lecture slides
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Class': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Using Pandas library to convert above dataset to DataFrame
df = pd.DataFrame(data)

# Separate features and target variable
predictors = df.drop(columns=['Class'])
response = df['Class']


# Call IG function
information_gain_ = calculate_information_gain(predictors, response)

# Rank features based on information gain
ranked_features = sorted(information_gain_, key=information_gain_.get, reverse=True)

# Display the ranked features and their information gain
print("\n\nRanking based of IG \n\n")
index = 0
for feature in ranked_features:
    index+=1
    print(f"Rank:{index} - {feature}, IG: {information_gain_[feature]}")

print("\n\nDecsion Tree using Recursion: \n\n")

# Part 2
# 
def recurisve_decision_tree(data, target, current_level=1):
    # calculate the info gain with respect to data and target
   # info_gains = calculate_information_gain(data, target)
    # max is the best splitting node
    best_feature_node = max(calculate_information_gain(data, target), key=calculate_information_gain(data, target).get)
    # print splitter node
    print(" - " * current_level, "Best Split using IG:", best_feature_node, ": ", calculate_information_gain(data, target)[best_feature_node])
    # recursive loop to build child nodes after splitting
    for value in data[best_feature_node].unique():
        # extracting the subset of data where the current feature equals the current value
        subset = data[data[best_feature_node] == value]
        # extracting the corresponding subset of target values
        subset_target = target[data[best_feature_node] == value]
        print(" - " * (current_level+1), "Value:", value)

        
        # making sure dp belongs to the same class
        if len(subset_target.unique()) == 1:
            # print the class
            print(" - " * (current_level+2), "Class:", subset_target.iloc[0])
        else:
            # if more classes prevail, split again to find child nodes
            childTree = subset.drop(columns=[best_feature_node])
            # !!! recursive call !!!
            recurisve_decision_tree(childTree, subset_target, current_level+2)

recurisve_decision_tree(predictors,response) 