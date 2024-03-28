# Module 12 Report Template

## Overview of the Analysis

In this section, describe the analysis you completed for the machine learning models used in this Challenge. This might include:

* Explain the purpose of the analysis.
 - '''Credit Risk analysis is inherently imbalanced due to the larger proportion of creditworthy borrowers who get loans in the first-place. This analysis builds a credit risk model using an imbalanced dataset and then evaluates it's precision/accuracy and fit-for-purpose.'''
* Explain what financial information the data was on, and what you needed to predict.
 - '''This analysis using lending data that includes derogatory marks as well as final default or success status for the loan. It comes from P2P Lending companies and the history of loans they've made.'''
* Provide basic information about the variables you were trying to predict (e.g., `value_counts`).
 - '''The aim is for the model to predict the loan status (whether it defaults or is succesfully paid off) using variables such as loan size, interest rate, borrower income, debt to income, num of accounts, derogatory marks, total debt, loan status
* Describe the stages of the machine learning process you went through as part of this analysis.'''
 - '''we first create two sets from the original dataset. 1 has the target variable (loan status) the other has the features used to predict the target. Then the two sets are futher split into a test and train set (resulting in 2 sets of target dataframes and 2 sets of feature dataframes). We then use a Logistic Regression Model; fit the model using the training datasets; run the model predictions and compare those predictions against the test datasets for the target variable generating a confusion matrix and a classification report (accuracy, recall, f-1 score, support). Because the original dataset is inherently imabalanced, we then use a sampler library to resample the training datasets. This results in more training data for loan defaults that we would've originally seen in the lending data. We then fit the logistic regression model using the resampled datasets and re run the model to predict our target variables. When we do this we suffer a very slight drop in precison for predicting defaults, but realize a far higher recall. '''
* Briefly touch on any methods you used (e.g., `LogisticRegression`, or any resampling method).
 - '''We use logistic regression modelling, but given our dataset is imbalanced we use a Random Oversampler function to generate more datapoints we can use to produce a more robust logistic regression model.'''

## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:
  * Description of Model 1 Accuracy, Precision, and Recall scores.
   - '''Before Resampling
     - Accuracy = 95.205%
     - Precision for prediction 0 (i.e. succesfull loan paid off) = 100%
     - Precision for prediction 1 (i.e. default) = 85%
     - Recall for prediction 0 (i.e. succesfull loan paid off) = 99%
     - Recall for prediction 1 (i.e. default) = 91%'''



* Machine Learning Model 2:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
   - '''After Resampling
    - Accuracy = 99.368%
    - Precision for prediction 0 (i.e. succesfull loan paid off) = 100%
    - Precision for prediction 1 (i.e. default) = 84%
    - Recall for prediction 0 (i.e. succesfull loan paid off) = 99%
    - Recall for prediction 1 (i.e. default) = 99%'''

## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best?
 - '''The oversampled data is more accurate overall. It suffers a very slight dip in precision of predicting defaults compared to the original model, but it does a better job with recall and overall accuracy. The more balanced dataset results in better coverage of the models predictions.'''
* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? )
 - '''It depends on the nature of the credit lending agency. They might be fine with making riskier loans and collecting fees in which case there's less impact. However, if creditworthiness is of the greatest importance then it's important to more accurately and reliabely predict 1's (even if you over correct and falsely predict a 1) as opposed to falsely predicting a 0 when it should be a 1.'''

If you do not recommend any of the models, please justify your reasoning.
