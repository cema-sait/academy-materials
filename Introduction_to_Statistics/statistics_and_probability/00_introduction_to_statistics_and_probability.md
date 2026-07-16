---
name: Introduction to Statistics and Probability
dependsOn: [Introduction_to_Statistics.statistics_and_probability]
learningOutcomes:
  - Define statistics and explain its key components; data collection, analysis, interpretation, and presentation.
  - Differentiate between descriptive and inferential statistics and apply them in public health contexts.
  - Classify data as qualitative or quantitative and distinguish nominal, ordinal, discrete, and continuous variables.
  - Apply fundamental probability concepts, including sample spaces, events, unions, intersections, complements, and conditional probability.
  - Use R to create, summarize, analyze, and visualize data using basic statistical methods.
---

## Definition of Statistics

**Statistics** is a discipline within the field of mathematics that encompasses the collection, analysis, interpretation, and presentation of data.

Examples:

- How many people in the country have a disease within a certain period of time

- Whether a treatment is safe and effective

- How many people were born and died. These are known as vital statistics

- How many people have access to and use health care

- Exercise and weight loss to lower the risk of getting type 2 diabetes


This definition points out 4 *components* of statistics:

**1. Data collection:**
Data can be collected from various sources such as surveys, databases, and experiments. In R, we can create a dataset manually or load data from a file (.xlsx or .csv)

```r
# Creating a dataset manually
health_data <- data.frame(
  ID = 1:10,  
  Age = c(25, 34, 45, 50, 29, 60, 38, 40, 55, 48),
  Disease = c(1, 0, 1, 1, 0, 1, 0, 0, 1, 1),  # 1 = Has disease, 0 = No disease
  Treatment = c("A", "B", "A", "A", "B", "A", "B", "B", "A", "B"), #treatment A or B
  Weight_Loss = c(5, 3, 6, 4, 2, 8, 3, 4, 7, 6)  # Weight loss in kg
)
# View the dataset
print(health_data)
```

**2. Data analysis:**
Analyzing data involves the systematic summarization and examination of underlying patterns. Let us conduct an analysis of the data we generated manually above.

```r
summary(health_data)  # Get min, max, mean, and median values
mean(health_data$Age)  # Mean age of participants
table(health_data$Disease)  # Count of people with and without the disease
```

This is called *descriptive statistics*

We could also check if *weight loss* differs between *Treatment A and B* by conducting a hypotheis testing

```r
t.test(Weight_Loss ~ Treatment, data=health_data)
```

We can model weight loss as a function of age and treatment using linear regression:

```r
model1 <- lm(Weight_Loss ~ Age + Treatment, data=health_data)
summary(model1)

```


 - This is called *inferential statistics*

Therefore, Statistics is divided into **two** broad categories; descriptive and inferential (we will see the details later).


 **Data Interpretation:**
From the t-test and linear regression model results we have obtained above, we can interpret them as follows;

- If p-value < 0.05, we conclude a significant difference in weight loss between the two treatments.

- If p-value > 0.05, we conclude no significant difference.

- The Estimate for Age *0.16210* tells us that weight loss increases with age - from *model1*.

**Data presentation:**
Visualizing data facilitates the effective communication of research findings. Here we will use a histogram and a box-plot.
