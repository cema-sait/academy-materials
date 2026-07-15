---
name: Introduction to Statistics and Probability
dependsOn: []
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

```{r}
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

```{r}
summary(health_data)  # Get min, max, mean, and median values
mean(health_data$Age)  # Mean age of participants
table(health_data$Disease)  # Count of people with and without the disease
```

This is called *descriptive statistics*

We could also check if *weight loss* differs between *Treatment A and B* by conducting a hypotheis testing

```{r}
t.test(Weight_Loss ~ Treatment, data=health_data)
```

We can model weight loss as a function of age and treatment using linear regression:

```{r}
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

a.) Histogram for Age Distribution

```{r}
set.seed(123)  # Ensures reproducibility

ages <- rnorm(100, mean=40, sd=10) #create a datset following normal distribution 

hist(ages, main="Age Distribution", xlab="Age", col="lightblue", breaks = 10)
```

b.) Boxplot of Weight Loss by Treatment Group

```{r}
boxplot(Weight_Loss ~ Treatment, data=health_data, 
        main="Weight Loss by Treatment",
        xlab="Treatment", ylab="Weight Loss (kg)",
        col=c("grey", "lightblue"))

```

## Types of Statistics

**Descriptive statistics**

- Summarizes data both numerically and graphically, facilitating the user's understanding of fundamental characteristics and enabling the identification of underlying patterns.

- These numerical summaries include measures that describe the central tendency of the data, indicating where the majority of the data points are concentrated (mean, median, mode, minimum, maximum), as well as measures of variability or dispersion, which illustrate the extent to which the data are spread out (variance, standard deviation). 

- Additional indices can reveal the degree of symmetry in the data distribution (skewness) and whether the tails of the distribution exhibit heavier or lighter characteristics than what is theoretically anticipated (kurtosis). 

- Graphical techniques include line and bar charts, histograms, pie charts, box plots.

**Inferential statistics**

- Utilizes sample data to derive predictions about larger populations through hypothesis testing and parameter estimation.

- Enables the researcher to ascertain the probability that any observed differences between or among groups are genuine rather than attributable to random variation.

- Specifically, if two samples were randomly drawn from the population and no modifications were made to either group, the scores on a particular variable would differ solely due to sampling variability.

- Therefore, if an intervention were implemented in one group, such as the administration of an experimental drug, inferential statistics would facilitate the determination of the likelihood that the observed differences were a result of the intervention rather than random chance.



## Types of Data

### Qualitative data
They are called categorical variables and are further divided into 2 classes namely nominal and ordinal variables:

1. Nominal variables: Variables whose categories are just names with no natural ordering. eg. gender
marital status, race,  district of birth etc.

2. Ordinal variables: Variables whose categories have a natural ordering. Eg education level,
performance category, degree classifications etc.

```{r}
# Create a vector for Gender
gender <- c("Male", "Female", "Male", "Male", "Male", "Female")

#convert to a categorical variable for analysis
gender <- factor(gender)

#count each category
table(gender)
```

### Quantitative data
They are numerical variables and are divided into two;

1. *Discrete variables*: can only assume certain values and there are gaps between them (whole numbers) eg. number of individuals positive of schistosomiasis.

```{r}
# Number of individuals positive for Schistosomiasis in different villages
schisto_cases <- c(12, 18, 25, 10, 30, 22, 15, 28, 19, 14)

# Print the dataset
print(schisto_cases)

```

2. *Continuous variables*: can assume any value in a specified range. eg. the weight or height of children in Nyatike sub-county

```{r}
set.seed(123)  # Ensures reproducibility

# Generating continuous data for 10 children
weight <- round(rnorm(10, mean=30, sd=5), 1)  # Weight in kg
height <- round(rnorm(10, mean=120, sd=10), 1)  # Height in cm

# Create a data frame
children_data <- data.frame(Child_ID = 1:10,
                            Weight_kg = weight,
                            Height_cm = height)

# Print dataset
print(children_data)

```

## Assignment

### Section 1: Conceptual Questions

1. What are the four main components of statistics? Briefly describe each.

2. Explain the difference between descriptive and inferential statistics. Provide an example of each in a public health context.

3. Define the following types of data and provide an example for each:
a) Nominal data
b) Ordinal data
c) Discrete data
d) Continuous data

4. Why is data visualization important in statistical analysis? Name two types of plots that are useful for visualizing numerical data.

5. A clinician wants to determine whether a new treatment is more effective than an existing one. Which statistical approach (descriptive or inferential) would they use and why?

### Section 2: Data Analysis in R

6. Write an R script to create a data frame for 10 individuals containing the following columns: ID, Age (randomly generated normally distributed values with mean 40 and SD 10), and Disease Status (1 = Has disease, 0 = No disease).

7. Consider the following dataset:

```{r}
data1 <- data.frame(
  Age = c(25, 34, 45, 50, 29, 60, 38, 40, 55, 48),
  Disease = c(1, 0, 1, 1, 0, 1, 0, 0, 1, 1),
  Treatment = c("A", "B", "A", "A", "B", "A", "B", "B", "A", "B"),
  Weight_Loss = c(5, 3, 6, 4, 2, 8, 3, 4, 7, 6)
)
```

a) Write an R command to compute the mean age of participants.

b) Write an R command to count the number of individuals with and without the disease.

8.Using the dataset above, write an R command to perform a t-test to check if weight loss differs between Treatment A and Treatment B.

9. Suppose you want to model weight loss as a function of age and treatment using a linear regression model in R. Write the R command for fitting and summarizing the model.

10. Interpret the following output from a t-test:

t = 2.45, df = 8, p-value = 0.038


What does this tell us about the difference in weight loss between the two treatment groups?

### Section 3: Application-Based Questions

11. A public health officer wants to analyze how access to healthcare services affects treatment outcomes. What kind of data should they collect, and how would they analyze it?

12. An epidemiologist is studying the spread of an infectious disease in different regions. What statistical techniques could they use to compare the prevalence across regions?

13. A researcher wants to determine whether exercise and weight loss reduce the risk of developing type 2 diabetes. How would they set up an analysis in R?

14. What are some potential biases in data collection that could affect the validity of a statistical analysis in a clinical trial?

15. In the following boxplot R command:

```{r}
boxplot(Weight_Loss ~ Treatment, data=data1,
        main="Weight Loss by Treatment",
        xlab="Treatment", ylab="Weight Loss (kg)",
        col=c("grey", "lightblue"))
```

What insights can be drawn from this type of visualization in a clinical study?

**Bonus Question:**
A public health officer wants to determine if exercise has a significant effect on reducing blood pressure. What type of statistical test should they use, and how can they implement it in R?




## Definitions of Common Terminologies used in Probability

1. A sample space (S) is a set of all possible outcomes of an experiment.  If all outcomes are equally likely that is have the same probability, then each has probability $1/|S|$.

```{r}
# considering data iris, conduct an experiment where we
#randomly select a species from the dataset, the sample space is; 
data(iris)
sample_space <- unique(iris$Species)
sample_space
#S={setosa,versicolor,virginica} is the sample space
```

Question 1: If the experiment was to randomly select a flower and consider all its attributes, what is the sample space?
 
 Question 2: If the experiment was to randomly select a species from the dataset, and assuming that all outcomes are equally likely, what is the probaility of selecting *setosa*?
 

2. An event is a subset of S. An event is simple if it consists of just a single outcome otherwise it is compound.

```{r}
# Count flowers where Sepal.Length > 5
count_large_sepal <- sum(iris$Sepal.Length > 5)

# Probability calculation
prob_large_sepal <- count_large_sepal / nrow(iris)
print(prob_large_sepal)  # Output: Probability value
```

- - The sum() function counts how many TRUE values exist, giving you the number of occurrences where iris$Sepal.Length > 5

- This is a simple event since it consists of a single outcome.

Question: What is the probability of Picking a Flower with Sepal.Length > 5, is this a simple or a compound event?

3. If A and B are events in S, then 

(i) $A∪B$ (read $A$ union $B$) consists of all the outcomes in A or in B (or both!)

$P(A∪B) = P(A)+P(B)−P(A∩B)$

-- We can obtain $P(Setosa ∪ Sepal.Length>5)$

```{r }
# Probability of Setosa OR Large Sepal
#event A is setosa and event B is Sepal.Length > 5
# Calculate probabilities
prob_A <- sum(iris$Species == "setosa") / nrow(iris)
prob_B <- sum(iris$Sepal.Length > 5) / nrow(iris)
prob_A_intersect_B <- sum(iris$Species == "setosa" & iris$Sepal.Length > 5) / nrow(iris)

# Apply the union formula
prob_union <- prob_A + prob_B - prob_A_intersect_B

# Print result
print(prob_union)
```

-nrow(iris) counts the number of flowers in iris

(ii) $A∩B$ (read $A$ intersection $B$) consists of all the outcomes in both A and B

$P(A∩B) = P(A)⋅P(B∣A)$

- We can obtain $P(Setosa ∩ Sepal.Length>5)$
```{r}
# Probability of Setosa AND Large Sepal
# Count flowers that are Setosa AND have Sepal.Length > 5
count_intersection <- sum(iris$Species == "setosa" & iris$Sepal.Length > 5)

# Probability calculation
prob_intersection <- count_intersection / nrow(iris)
prob_intersection
```

or simply:

```{r}
# Intersection: Setosa AND Sepal.Length > 5
prob_A_intersect_B <- sum(iris$Species == "setosa" & iris$Sepal.Length > 5) / nrow(iris)
prob_A_intersect_B
```


(iii) $A-B$ (read $A$ minus $B$) consists of all the outcomes in A but not in B

$A−B = {x∈A∣x∈/B}$

$P(A−B) = P(A)−P(A∩B)$

```{r}
# P(A) = Probability of picking Setosa
prob_A <- mean(iris$Species == "setosa")

# P(A ∩ B) = Probability of picking Setosa and Sepal.Length > 5
prob_A_intersect_B <- mean(iris$Species == "setosa" & iris$Sepal.Length > 5)

# P(A - B) = P(A) - P(A ∩ B)
prob_A_minus_B <- prob_A - prob_A_intersect_B

# Print result
prob_A_minus_B

```


Q1. What is the probability of a Sepal.Length ≤ 4.5

Q2. What is the probability of a Virginica Flower with Petal.Width > 2


(iv) $A^{'}$ (read $A$ complement) consists of all outcomes not in A (that is, $S-A$)

$P(A′)=1−P(A)$

```{r}
# Probability of picking Setosa
prob_setosa <- mean(iris$Species == "setosa")

# Probability of NOT picking Setosa (complement of Setosa)
prob_not_setosa <- 1 - prob_setosa

prob_not_setosa
```


(v) $0/$ (read as empty set) for the event which doesn’t contain any outcomes

$P(∅)=0$

```{r}
# Probability of a species that doesn't exist in the dataset
prob_empty_event <- mean(iris$Species == "non_existent_species")

# This will print 0 because the event has no outcomes
prob_empty_event

```


Note: Event A occurs if the outcome of the random experiment is a member of the set A

## Definition of Probability
Probability simply means the possibility of the outcome of any random event.

The probability of an event A occuring is

\[
\begin{equation}
P(A) = \frac{\text{Number of elements in A}}{\text{Total number of elements in the sample space}}
\end{equation}
\]

**Example 1**
If a normal die is rolled, what is the probability that the number showing is less than 7?

**Example 2**
Find the probability of throwing an 8 on a normal die

**Example 3**
A marble is drawn at random from a bag containing 3 red, 2 blue, 5 green and 1 yellow
marble. What is the probability that it is not green?

## Mutually exclusive events
Two events are incompatible, disjoint or mutually exclusive when the occurence of one precludes the occurrence of the other, i.e. they can not occur at the same time.

If two events A and B are mutually exclusive, the probability of A or B happening,
denoted $P(A ∪ B)$, is

\[
\begin{equation}
P(A ∪ B) = P(A) + P(B)
\end{equation}
\]

**Example**

A number is selected at random from the integers 2 to 25. Find the probability that it is
(a) a perfect square;
(b) a prime number;
(c) a prime number or perfect square

```{r}
#example of a mutually exclusive event
# No flower can be both setosa and virginica at the same time
both_species <- sum(iris$Species == "setosa" & iris$Species == "virginica")

both_species
```

- The mutually exclusive events in this case are Setosa and Virginica since no flower can belong to both groups at the same time!

Question: What is the probability of picking Setosa OR Virginica

## Conditional Probability
Conditional probability can refer to the occurrence of event A subject to another event B. 

The conditional probability of A given B is defined by $P(A | B)$ = $P(A ∩ B)/P(B)$ , provided that $P(B)$ is not equal to 0.

```{r}
# probability of Sepal.Length > 5 given that the Flower is Setosa
#event B is Sepal.Length > 5 while event A is the Flower is Setosa
#meaning we first observe event A then observe event B given we have 
#observed event A already

count_setosa_large_sepal <- sum(iris$Species == "setosa" & iris$Sepal.Length > 5)

count_setosa <- sum(iris$Species == "setosa")

# Probability of Sepal.Length > 5 given Setosa
prob_large_sepal_given_setosa <- count_setosa_large_sepal / count_setosa

prob_large_sepal_given_setosa
```

- This gives the probability that a Setosa has Sepal.Length > 5

Q1. The probability that a randomly chosen flower has Sepal.Length > 6

Q2. The probability that a flower has Sepal.Length > 6 given that it is Virginica

Q3. The probability that a randomly selected flower has Petal.Width > 1.5 

Q4. The probability that a flower is Versicolor given that Petal.Width > 1.5

