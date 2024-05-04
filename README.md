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
1. Street Light - Whether streetlights are on, off or unavailable
2. Pedestrian - Whether pedestrians are involved
3. Speed Limit - The speed limit on the road
4. Vehicles involved - The type of vehicles involved
5. Traffic control - Whether it is presengt or not 
6. Light - Whether it is dark, bright, twilight or overcast
5. Holiday - The holiday celebrated at a specific day
6. Flat/Hill - Whether the road is flat or hilly
7. Obstacles hit - Number of obstacles on the road
weather - The weather conditions
8. Road character- 
9. Road surface - Whether the road is sealed or unsealed

## CONCLUSION AND RECOMMENDATION 
## Conclusion
Today, it is more important than ever for us to understand the factors that affect the causage of the road accidents. In the recent months, the road carnage in Kenya has increased and it'd be great that we understand the underlying factors to get to come up with the solutions. 
By the use of the  generated models we can leverage them to predict and monitor the serverity of the accidents.This would also allow the key stakeholders to come up with policies and strategies that will help with the reduction of the menance that is. 

From the analysis and modelling:
1. Based on the evaluation of various regression and classification models, it is evident that machine learning algorithms can effectively predict accident severity.

2. The Logistic Regression models achieved an of accuracy 98.73. KNN models achieved accuracies of approximately 93.61% and 95.56%, respectively. Both of these models provide essential quantitative insights into predicting road accidents and crash severity. They offer valuable information for improving road safety by accurately assessing accident likelihood and severity, helping stakeholders make informed decisions to prevent accidents and minimize their impact.

3. Through depth analysis, we successfully identified factors that significantly influence crash occurrences. These factors do include 'speedLimit ', 'flatHill', 'streetLight', 'vehiclesInvolved', play a pivotal role in understanding and predicting road accidents

4. Based on our crash severity analysis: Fatalities and Injuries: The more fatalities and serious injuries, the worse the crash. Context Matters: Holidays, poor lighting, and number of pedestrians involved make crashes more severe. Road Conditions: Speed limits, street lighting, and traffic control affect crash severity. Number of Vehicles: More vehicles usually mean a more severe crash..

5. Considering risk factors like hilly terrain, misty and foggy weather conditions, absence of streetlights, dark periods, and high-speed limits, which make accidents more severe. Understanding these risks helps us improve how we allocate resources.
## Recommendation 
Safety Campaigns: Implement targeted road safety campaigns focusing on the identified risk factors to raise awareness among road users and promote responsible driving practices in challenging terrain and low-light areas.

Continuous Model Refinement: More data from different countries all over the world need to do a more thorough documentation of road accidents occuring so as to have more sufficient data to build more accurate predictive models to assess severity of road accidents.

Enhanced Resource Allocation Directing additional resources towards addressing key factors, like hilly terrain, lack of streetlights, dark periods, and high-speed limits, which significantly influence the severity of fatal accidents. Prioritizing resource allocation to mitigate these specific risk factors can lead to more effective accident prevention and response strategies.

Enhancing Road Safety During Mist and Foggy Conditions

Most fatal accidents do occur when the weather is mist and foggy and hence we do recommend:

Improve visibility during mist or fog, including reflective road signs and vehicle lighting.

Use advanced weather forecasting to provide real-time alerts.

Educate drivers on safe practices during foggy conditions.

Upgrade roadside infrastructure to alert drivers of fog conditions


## Necessary Links 
* The dataset: [https://catalogue.data.govt.nz/dataset/crash-analysis-system-cas-data5](https://catalogue.data.govt.nz/dataset/crash-analysis-system-cas-data5)
* Dataset description: [https://opendata-nzta.opendata.arcgis.com/pages/cas-data-field-descriptions](https://opendata-nzta.opendata.arcgis.com/pages/cas-data-field-descriptions)

