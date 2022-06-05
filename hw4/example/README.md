## Assignment 4



[TOC]



#### Data Analysis Task

##### About Dataset

The dataset used by the project is Black Friday. The columns of the data are listed as follows:

* User_ID
* Product_ID
* Gender
* Age
* Occupation
* City_Category
* Stay_In_Current_City_Years
* Marital_Status
* Product_Category_1
* Product_Category_2
* Product_Category_3
* Purchase

These data together describe the quantity and consumption amount of various types of goods purchased by a user on Black Friday, as well as the user's user profile, such as age group, gender, marital status, occupation, residence city categories and residence time in the city.

##### Analysis Tasks

1. Age-Based Analysis
   1. Analyze the age distribution of consumers by gender.
   2. Analyze the occupational distribution of consumers in different age groups.
   3. Analyze the effects of gender, marital status and city category on purchasing power.
2. Purchase-Power Based Analysis
   1. Analyze the distribution of people with different occupations in different cities.
   2. Analyze the impact of occupation and city category on purchasing power.

#### Layout Design

The layout shown below is used:

![image-20220522120637501](https://tva1.sinaimg.cn/large/e6c9d24egy1h2h81r9h8oj20di08ugln.jpg)

The page layout looks like this:

![image-20220522121327382](https://tva1.sinaimg.cn/large/e6c9d24egy1h2h81rv3g9j21ge0u0q5y.jpg)

![image-20220522121437666](https://tva1.sinaimg.cn/large/e6c9d24egy1h2h81u3zr3j21gz0u0n0n.jpg)

The critical section contains the description of dataset to be analyzed, as well as viewing tabs for user selection, including Age-Based Analysis and Purchase-Power Based Analysis. Let users know where to choose what they want to see right from the start.

In the middle section, it contains the analysis graph of the dataset. When the user selects Age-Based Analysis, three related graphs can be seen. It is worth mentioning that the chart on the far left is an **interactive chart**. When the user hovers the mouse over the corresponding rectangle, the two charts on the right will display the analysis charts for the corresponding age group. When the user selects Purchase-Power Based Analysis, two related charts can be seen. Details about the chart are described later.

#### Detail of Figures

Bar, Pie, SunBurst, line and Polar charts were used to analyze dataset characteristics.

##### Age-Based Analysis

![image-20220522124302877](https://tva1.sinaimg.cn/large/e6c9d24egy1h2h81wje2nj21f80u041z.jpg)

The graph on the far left shows the distribution of different genders among consumers by age group. The graph shows that women and men have the largest numbers in the 26-35 age group, while women outnumber men in all age groups. The age distribution of both genders is consistent, indicating that women prefer to participate in Black Friday.

At the same time, the two graphs on the right change as the mouse hovers over the graph on the left to change the age group. Change is shown below. Different distributions for different age groups are shown.

![image-20220522125320289](https://tva1.sinaimg.cn/large/e6c9d24egy1h2h81yvd6tj21ev0u0dj2.jpg)



Take the above picture as an example, the upper right picture shows the occupational distribution of the 0-17 age group. Occupation 10 occupies 70%, presumably this occupation is student. At the same time, the lower right corner shows the distribution of purchase volume by gender, marital status and city type in this age group. Among them, the purchase volume of women is larger than that of men. In this age group, women and men are not married yet, and the purchase volume of city C is the largest. Note that it is normal to be unmarried at this age.

##### Purchase-Power Based Analysis

![image-20220522131735891](https://tva1.sinaimg.cn/large/e6c9d24egy1h2h8208sdjj221k0ly0x7.jpg)

The figure on the left depicts the distribution of different occupations in different cities, where the distribution of different occupations in each city is consistent. City B has the largest number of occupations in almost all occupations. The largest number of occupations in City A and City B is occupation 4, and the largest number of occupations in City C is 7.

The graph to the right shows the purchasing power of different occupations in each city, where purchasing power is the average purchasing volume among people in that occupation in that city. Overall, city C has the largest purchasing power, while city A and B are similar. Occupation 8 in city A  has the largest purchasing power among the three cities. It can be seen that although the number of occupations in City C is small, the income is high. The income of occupation 8 in City A is also very high.

#### How To Run

```sh
$conda env create -f environment.yml
$cd example
$conda activate hci4
$python app.py
```







