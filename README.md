# Preface
The analyses presented in this repository are based on a hypothetical dataset provided by Viettel. The primary goal is to practice problem-solving skills through data analysis. The techniques were employed in this analysis include Exploratory Data Analysis (EDA), Cohort analysis, and the Apriori algorithm.
# Executive summary
The company is grappling with a low Customer Lifetime Value (CLV) compared to the E-commerce industry average, primarily due to a limited product catalog, restricted cross-selling capabilities, and subpar product quality in previous transactions. To address these underlying issues, conducting a market basket analysis to identify itemsets with high co-purchasing probabilities is the most effective solution, enabling the company to enhance the quality of its product recommendation features.
# Problem analysis and Hypothesis development
## Problem analysis
### EDA
Conduct Exploratory Data Analysis on all fields of the dataset, followed by Univariate Analysis and Multivariate Analysis
<br> ![image](https://github.com/user-attachments/assets/7a95bee2-cd98-4a17-8407-7ef12989d926)
<br> _Frequency distribution of event_type by sequence_number_
<br> ![image](https://github.com/user-attachments/assets/65828805-9a8a-4f8e-8ff5-3b65a2025a0b)
<br> _Distribution of retail_price_
<br><br> **Overall business insights from EDA results**
<br> ![image](https://github.com/user-attachments/assets/3e06cdae-ea4e-4237-a894-da826456d548)
<br> _Read the detailed report [here](https://drive.google.com/file/d/1pB2ZxP1XIyKBl5ogo8yVzLG2tB1yb41N/view)_
### Dive deeper into problem
#### 1. Revenue analyis
![image](https://github.com/user-attachments/assets/fa16583e-d561-43b6-82cb-3ea73783c2f2)
<br> _The number of items sold by category_
- Actual revenue shows a high discrepancy among product types. A potential reason for this issue could be that customers only purchase certain types of products because they only view certain types of products.
- To determine if the potential causes are driving the revenue discrepancy, we need to examine customer behavior on the website.
#### 2. Customer analysis
![image](https://github.com/user-attachments/assets/d5a5fd3e-ecff-4bac-a5f5-fb8f7f0055c5)
<br> Currently, customers are making relatively small purchases, with an average of 1.45 items per order. Unfortunately, the return rate is high and is increasing at a faster rate than completed orders. Notably, customer purchases are primarily driven by two channels: Adwords and Email.
- **Customer Lifetime Value (CLV) - the "golden metric"**

Customer Lifetime Value (CLV) is lower than the average of Ecommerce industry, which is $90.9 compared to $218 (source: Metrilo).
<br> CLV is calculating by multiplying the average customer lifetime and the average value created during their lifetime. 
<br> <br> Note: with the average customer lifetime of company defined as 13 months, customers who started purchasing in the last 13 months of the dataset are excluded as conducting analysis to avoid skewing the results, because their full customer lifecycle has not yet been realized. 
<br> <br> **Core problem:** Low Customer Lifetime Value (CLV) compared to the E-commerce industry average
## Hypothesis development
Employing Issue tree framework to determine potential root causes of the core problem, which helps us to develop hypothesis (or assumption) that need validating in the next phase.
<br> ![image](https://github.com/user-attachments/assets/8e4469aa-2d2c-4eee-bd6c-f738e07dc301)
<br> Hypothesis (or assumption) developed that low CLV is the result of the below root causes:

- Restricted cross-selling capabilities
- A limited product catalog
- Subpar product quality in previous transactions
- Long shipping waiting time
# Hypothesis validation and Solution development
## Hypothesis validation
### H1: Restricted cross-selling capabilities lead to poor CLV
**Apriori algorithm** is used to evaluate cross-selling capabilities of company
- **Logic of execution:** Build Apriori model to find itemsets which have high probility to buy together, then check if the dataset contains any sessions that include the potential itemsets discovered by the Apriori model.
  + If dataset includes less than 35% of potential product baskets, H1 is accepted
  + Else, H1 is rejected

**The results of Apriori algorithm is shown below:**
![image](https://github.com/user-attachments/assets/8e8f740d-d92e-4043-b293-3acb398caf68)
<br><br> With the thresholds encompassing min_support = 0.01, min_confidence = 0.24, min_lift = 1.4, there are 6 product baskets that are potentially bought together
<br><br> There is 0% of session that corresponds product basket discoverd above by Apriori algorithm
<br><br> => H1 is accepted
### H2: A limited product catalog leads to poor CLV
![image](https://github.com/user-attachments/assets/14b62a6e-15b8-4395-ac60-a8f65728328b)
<br> _Views by category_
<br> ![image](https://github.com/user-attachments/assets/c25bb3fe-9dfb-4320-9f40-141d9ca683da)
<br> _Revenue by category_
<br> <br> The most viewed product type is also the type that sells the most. This suggests that visibility can impact sales. However, additional data fields are needed to accurately assess the relationship between these two variables.
<br><br> => At present, it is still not possible to conclude this hypothesis
### H3: Long shipping waiting time leads to poor CLV
![image](https://github.com/user-attachments/assets/564346c2-a54a-4834-aa80-1fdebc12e34d)
<br> _Overall distribution of delivery time_
<br> ![image](https://github.com/user-attachments/assets/2b7645ac-68bc-40e0-b8a8-27dd20356807)
<br> _Distribution of delivery time of the final order (the last order before churning)_
<br><br> => Orders placed before customers stopped purchasing from the business had delivery times similar to those of customers who continued to make repeat purchases, all within the range of 0-7 days. This concludes that delivery time does not affect customer retention
<br><br> => H3 is rejected
### H4: Subpar product quality in previous transactions leads to poor CLV
Conduct Cohort analysis to evaluate retention rate of customer, then perform analysis on return behavior of customer to determine whether surpar product quality is the reason that make customer churn.

- **Cohort analysis**

The result of Cohort analysis indicates that company has a low customer retention rate (1% - 4%) compared to the average of Ecommerce industry
<br>![image](https://github.com/user-attachments/assets/a5df2efe-9626-4baa-bfb3-5197dfecbd68)

- **Analysis on return behavior of customer**

![image](https://github.com/user-attachments/assets/70d6edff-a346-44d5-8023-00ae9e9c07bf)
<br> _Product returned rate by quarter_
<br><br> Product returned rate of company is lower than the average of Ecommerce industry, but 99% of customer will never return to the company after they returned their order. With the fact that H3 is rejected, s product quality in previous transactions leads to decrease in retention rate, which negatively impacts the CLV.
<br><br> => H4 is accepted
## Solution development
- **Insights compilation:**
  + **Product basket:** A few product categories are likely to be purchased together. Some shopping carts contain products that are highly likely to be purchased together. However, the website currently does not recommend products within the same cart
  + **A limited product catalog** leads to poor CLV may lead to poor CLV
  + **Product quality** has influence on customer retention rate

- **Solution suggested:** Focusing on boosting the cross-sell opportunities by improving product suggestion feature on website is the most actionable solution that company can use to quickly increase their CLV
