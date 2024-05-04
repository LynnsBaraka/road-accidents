# Deciphering Road Accidents: Predictive Analytics for Road Accident Severity

<img src="car.jpg" alt="Car Image" width="800" height="400" />

## INTRODUCTION

Road accidents stand as a formidable global challenge, inflicting injuries and fatalities that reverberate through families and communities. In Kenya, these incidents persist as a significant public health issue, claiming thousands of lives annually. While our dataset transcends national borders, the grim reality remains: road traffic injuries rank among the top 10 leading causes of death worldwide, as per the World Health Organization (WHO). This underscores the critical need for effective prevention strategies.

By delving into the underlying causes of these accidents and uncovering hidden patterns and risk factors, we have the opportunity to revolutionize road safety. Through targeted interventions informed by our analysis, we can strive to mitigate the frequency and severity of accidents, ultimately saving lives and sparing communities from the devastating impact of road-related incidents.
## Stakeholders 
Key stakeholders who will benefit from this project include:

1. Government policymakers.

2. transportation experts.

3. Safety Agencies.

4. General Public

5. Consumers.

## Authors

- Esther Gakio
- Baraka Waswa 
- Anita Bosibori 
- Andrew Maina
- Chris Mukiri
  
## Project Overview 
The project aims to develop a model capable of accurately determining the severity of road accidents by unveiling hidden patterns and risk factors that extend beyond conventional understanding and delving into the complexities of accident data  

## Objectives 
1. **Identify Key Predictive Factors:** Analyze various factors including roadway conditions, environmental influences, and driver behavior to identify the most significant predictors of crash occurrences. This analysis will serve as the foundation for developing the predictive model.
2. **Build a Predictive Model for Crash Severity:** Construct and train a predictive model to accurately forecast the severity of road accidents, categorizing outcomes as non-injury, minor, serious, or fatal. This model will leverage identified key factors and apply machine learning techniques to predict outcomes based on real-time and historical data.
3. **Develop an Early Warning System:** Create a system that uses the predictive model to identify high-risk areas and times for potential accidents. This system will enable stakeholders, such as traffic management centers and law enforcement agencies, to implement proactive measures including enhanced surveillance and targeted road safety campaigns.
4. **Optimize Resource Allocation with Predictive Analytics:** Utilize the predictive model to improve the allocation of emergency response and medical resources. By forecasting the likelihood and severity of accidents in specific areas, this objective aims to ensure that resources are more strategically deployed, enhancing response times and operational efficiency.

## Data Exploration And Preprocessing 
The project kicks off with loading the dataset into a DataFrame and conducting a thorough examination of its structure and contents. This involves identifying available columns and potential groupings, followed by checks for missing values and inconsistencies.

After ensuring data integrity, we delve into exploring the distribution of the dataset's columns, focusing on understanding the importance and impact of each column.

Subsequently, we proceed to data preprocessing, where missing values, duplicates, and data inconsistencies are addressed. This step involves cleaning the data by adjusting data types and standardizing formats as necessary.

Additionally, visualizations are employed to gain deeper insights into the dataset, particularly in understanding different factors such as the factors influencing the fatality of accidents.

These comprehensive steps in data exploration and preprocessing are crucial for preparing the dataset for subsequent modeling and insights extraction, ensuring that the data is reliable and conducive to meaningful analysis.



## Modelling 
In our project, we employed linear Regression as the baseline model and an iteration thereafter with Decision Tree, KNN, Random Forest and XGboost. Our system was designed to discern the severity of the road accidents. Through our findings, we aim to provide insights into the factors affecting the severity of the road accidents and the predictive factors.






After modeling, here are the top features contributing to the models' performance.


## CONCLUSION AND RECOMMENDATION 
## Conclusion
Today, it is more important than ever for us to understand the factors that affect the causage of the road accidents. In the recent months, the road carnage in Kenya has increased and it'd be great that we understand the underlying factors to get to come up with the solutions. 
By the use of the  generated models we can leverage them to predict and monitor the serverity of the accidents.This would also allow the key stakeholders to come up with policies and strategies that will help with the reduction of the menance that is. 

Our ultimate model effectively and accurately predcited the severity of the accidents, enabling us to generate the following conclusions.

1. Logistic Regression achieved the highest validation and test accuracies, with validation accuracy of 0.9857 and test accuracy of 0.9871, respectively. This indicates that the Logistic Regression model generalized well to unseen data and performed consistently well across both validation and test datasets.
2. K-Nearest Neighbors (KNN) attained slightly lower validation and test accuracies compared to Logistic Regression. The validation accuracy was 0.9422, and the test accuracy was 0.9361. While KNN performed reasonably well, it showed a slightly lower accuracy compared to Logistic Regression, suggesting that it may not generalize as effectively to unseen data.
3. KNN with GridSearchCV exhibited improved performance compared to the standard KNN model. With a validation accuracy of 0.9603 and a test accuracy of 0.9556, the GridSearchCV optimized KNN model demonstrated enhanced generalization and achieved higher accuracies than the standard KNN model..
## Recommendations


## Necessary Links 
* The dataset: [https://catalogue.data.govt.nz/dataset/crash-analysis-system-cas-data5](https://catalogue.data.govt.nz/dataset/crash-analysis-system-cas-data5)
* Dataset description: [https://opendata-nzta.opendata.arcgis.com/pages/cas-data-field-descriptions](https://opendata-nzta.opendata.arcgis.com/pages/cas-data-field-descriptions)

