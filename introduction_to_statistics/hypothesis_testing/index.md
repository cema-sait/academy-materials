---
name: Hypothesis Testing
id: hypothesis_testing
dependsOn: [introduction_to_statistics.statistics_and_probability]
files: []
learningOutcomes:
  - Define hypothesis testing and explain its role in statistical inference.
  - Distinguish between null and alternative hypotheses, and between one-tailed and two-tailed tests.
  - Apply Z-tests and T-tests to compare means in appropriate contexts.
  - Perform F-tests and one-way ANOVA to compare variance and group means.
  - Use Chi-squared tests and Fisher's exact test to analyse categorical data.
  - Select the appropriate hypothesis test for a given research question and data type.
summary: |
  This module covers the principles and practice of hypothesis testing. 
---

# What is Hypothesis testing?

-   **Hypothesis testing** is a statistical procedure used to determine whether there is enough evidence from a sample to support a claim about a population.

-   Researchers usually want to evaluate the statistical significance of parameters and examine the variability of their point estimates (eg. mean, variance, standard deviation).

-   There are three approaches:

    1.  A **standard error (SE)** of the parameter can be computed to provide a measure of the precision of the point estimate (ie. how much uncertainty there is in an estimate)
    2.  A significance **(hypothesis)** test can be carried out to determine if the point estimate is significantly different from some value specified by the null hypothesis test $(H_0)$
    3.  A **confidence interval (CI)** for the estimate can be computed

-   The procedures presented here are based on a classical **('frequentist')** approach to statistics - which relies purely on the data collected in the current experiment.

-   **Bayesian** explicitly combines new data with prior knowledge or past experience (called a '**prior**') to calculate a final updated result (called a '**posterior**')

-   A ***null hypothesis*** is a statement that proposes that there is no association between the factor and the outcome $(H_0)$

    Examples:

    -   There is no association between smoking and lung cancer.
    -   Male and female students have the same mean examination score.

-   An ***alternative hypothesis*** is a statement that proposes an association, effect, or relationship exists between a factor and an outcome $(H_1)$ (the opposite of $(H_0)$)

-   ***Alternative hypothesis*** is stated and can be **one-tailed** or **2-tailed** in nature.

-   For example; if we have disease incidence rates in 2 groups (exposed and non-exposed), the usual *2-tailed hypothesis* is that $I$ in the exposed group is different than in the non-exposed group **(ie. it could be higher or lower).** We are trying to find out if there is statistical evidence to support a difference in rates *that **could be in either direction***

    -   A ***one-tailed hypothesis*** would be that $I$ is higher in the exposed group than in the non-exposed group (The alternative hypothesis would be that the rate is lower and we are not interested in the possibility of the rate being higher)

-   After stating the $H_0$ and $H_1$, the next step is to compute a **test statistic** (the values of a statistic; eg. a t-statistic, a Z-statistic or $\chi^2$ statistic)

-   **Significance Level** ($\alpha$) - is the probability of rejecting the null hypothesis when it is actually true (probability of Type I error). Most commonly, $\alpha = 0.05$

-   From the expected distribution of this test-statistic, a ***P-value*** is determined.

-   **P-value** is the probability that the test-statistic would be as large or larger (in absolute value) than the computed test statistic, if the null hypothesis were true.

-   A small **P-value** indicates that, if the null hypothesis were true, it is unlikely (low probability) that you would obtain a test statistic as large or larger that the one you have obtained. In this case we reject the null hypothesis in favor of the alternative hypothesis.

-   Decision rule:

    -   If $p<0.05$: **Reject** $H_0$

    -   If $p≥0.05$: Fail to reject/ **accept** $H_0$

-   **P-value** do not carry the full picture and are majorly dichotomised into "**significant**" and "non-significant" about the parameter of interest

-   **Critical region** - range of values of the test statistic for which we reject $H_0$

-   A **critical region** is determined by:

    -   the significance level ($\alpha$)
    -   whether a test is one-sided or two-sided
    -   the probability distribution of the test statistic
    -   eg. if $\alpha = 0.05$ then we allow only a $5%$ chance of Type I error
    -   For $\alpha = 0.05$, the critical values are $-1.96$ and $1.96$, the critical region is $Z<-1.96$ and $Z>1.96$

-   Degrees of freedom ($df$) is the number of independent pieces of information in a data set that are free to vary when estimating a parameter of testing a hypothesis. It is calculated as the sample size ($n$) minus the number of constraints estimated ($p$) and expressed as; $df = n-p$

## Errors in Hypothesis Testing

| **Reality**    | **Decision**                | **Result**                           |
|:------------------|:-------------------|:--------------------------------|
| $H_0$ is true  | Reject $H_0$                | **Type I Error (**$\alpha$)          |
| $H_0$ is true  | Do not reject/accept $H_0$  | Correct decision                     |
| $H_0$ is false | Reject $H_0$                | Correct decision (Power = $1-\beta$) |
| $H_0$ is false | Do not reject/ accept $H_0$ | **Type II Error (**$\beta$)          |

-   Therefore, the general process is:

    -   State the hypotheses.
    -   Choose the significance level (α).
    -   Select an appropriate statistical test.
    -   Calculate the test statistic.
    -   Obtain the p-value or compare with the critical value.
    -   Make a decision.
    -   Draw a conclusion in the context of the research question.

# Test Statistic

-   There are four common test statistics for evaluating the associations between exposure and disease: Pearson $\chi^2$, exact test statistics, Wald tests and likelihood ratio tests.

## t- Test and Z-Test

Both are used for comparing means (or a mean to a hypothesized value), but they differ in what's assumed known and the sample size regime in which they're valid.

### Z-test

It is used when the population standard deviation ($\sigma$) is **known**, or the sample size is large ($𝑛≥30$)

#### One-sample Z-test

-   Used when comparing **a sample mean** to a hypothesized population mean $\mu_0$

$$
Z = \frac{\bar{x}-\mu_0}{\frac{\sigma}{\sqrt{n}}}
$$

#### Two-sample Z-test

-   Used when comparing a **two independent sample means** with known variances

$$
Z = \frac{(\bar{x}_1-\bar{x}_2)-(\mu_1-\mu_2)}
{\sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}}
$$

where

-   $(\bar{x}_1)$ = sample mean of group 1

-   $(\bar{x}_2)$ = sample mean of group 2

-   $(\mu_1-\mu_2)$ = hypothesized difference between the population means (usually 0)

-   $(\sigma_1)$ = population standard deviation of group 1

-   $(\sigma_2)$ = population standard deviation of group 2

-   $(n_1)$ = sample size of group 1

-   $(n_2)$ = sample size of group 2

-   Z follows the standard normal distribution under $H_0$

-   Compare the computed Z to critical values of 1.96 for a two-tailed test at significance level of 0.05

**Hypotheses (Two-Sided)**

$$
H_0:\mu_1=\mu_2
$$

or equivalently,

$$
H_0:\mu_1-\mu_2=0
$$

versus

$$
H_A:\mu_1\neq\mu_2
$$

**Decision Rule**

At a significance level of $\alpha=0.05$,

-   Reject $H_0$ if

$$
|Z|>1.96
$$

or equivalently,

-   Reject $H_0$ if the p-value is less than 0.05.

#### Example 1: One-Sample Z-Test

A national survey reports that the mean birth weight of newborns is **3.3 kg**. The population standard deviation is known to be **0.5 kg**.

A sample of **49** newborns from a hospital has a mean birth weight of **3.15 kg**.

Test at the **5% significance level** whether the hospital's mean birth weight differs from the national average.

**Step 1: State the Hypotheses**

$$
H_0:\mu=3.3
$$

$$
H_A:\mu\neq3.3
$$

**Step 2: Compute the Test Statistic**

The test statistic is

$$
Z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}
$$

Substitute the values:

$$
Z=\frac{3.15-3.30}{0.5/\sqrt{49}}
$$

Calculate the denominator:

$$
\frac{0.5}{\sqrt{49}}
=\frac{0.5}{7}
=0.0714
$$

Then

$$
Z=\frac{-0.15}{0.0714}
=-2.10
$$

**Step 3: Decision**

At

$$
\alpha=0.05,
$$

the ***critical values*** are

$$
\pm1.96.
$$

Since

$$
|-2.10|>1.96,
$$

we reject the null hypothesis.

**Step 4: Conclusion**

There is sufficient statistical evidence to conclude that the mean birth weight at the hospital is significantly different from the national average.

#### Example 2: Two-Sample Z-Test

A researcher wants to compare the mean systolic blood pressure of patients receiving a **new drug** and those receiving the **standard treatment**.

The population standard deviations are known.

| Group              | Sample Size | Mean | Population SD |
|:-------------------|------------:|-----:|--------------:|
| New Drug           |          50 |  128 |             8 |
| Standard Treatment |          60 |  135 |             9 |

Test whether the two population means differ at the 5% significance level.

**Step 1: State the Hypotheses**

$$
H_0:\mu_1=\mu_2
$$

or

$$
H_0:\mu_1-\mu_2=0
$$

versus

$$
H_A:\mu_1\neq\mu_2
$$

**Step 2: Compute the Test Statistic**

The test statistic is

$$
Z=
\frac{(\bar{x}_1-\bar{x}_2)}
{\sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}}
$$

Substitute the values:

$$
Z=
\frac{128-135}
{\sqrt{\frac{8^2}{50}+\frac{9^2}{60}}}
$$

Calculate the denominator:

$$
\frac{8^2}{50}
=\frac{64}{50}
=1.28
$$

$$
\frac{9^2}{60}
=\frac{81}{60}
=1.35
$$

Therefore,

$$
\sqrt{1.28+1.35}
=
\sqrt{2.63}
=
1.622
$$

Now compute the Z statistic:

$$
Z=
\frac{-7}{1.622}
=
-4.32
$$

**Step 3: Decision**

Critical values at

$$
\alpha=0.05
$$

are

$$
\pm1.96.
$$

Since

$$
|-4.32|>1.96,
$$

we reject the null hypothesis.

**Step 4: Conclusion**

There is sufficient statistical evidence that the mean systolic blood pressure differs between the two treatment groups.

**Try this in R**

```{r}
# Summary statistics
x1 <- 128
x2 <- 135

sigma1 <- 8
sigma2 <- 9

n1 <- 50
n2 <- 60

z <- (x1 - x2) /
     sqrt((sigma1^2/n1) + (sigma2^2/n2))

# Compute two-sided p-value
p.value <- 2 * pnorm(-abs(z))

z
p.value
```

## t-Test

### One-sample t-Test

-   This is used to determine whether the mean of a sample differs significantly from a known or hypothesized population mean **when the population standard deviation is unknown**.

-   Unlike the Z-test, the population standard deviation ($\sigma$) is replaced by the sample standard deviation ($s$).

The test statistic is

$$
t=\frac{\bar{x}-\mu_0}{\frac{s}{\sqrt{n}}}
$$

where

-   $\bar{x}$ = sample mean
-   $\mu_0$ = hypothesized population mean
-   $s$ = sample standard deviation
-   $n$ = sample size

The test statistic follows a **t-distribution** with $df=n-1$ degrees of freedom.

#### Example 1: One-Sample t-Test

Suppose the national mean birth weight is **3.3 kg**.

A sample of **25** newborns from a hospital has

-   Sample mean = **3.15 kg**
-   Sample standard deviation = **0.40 kg**

Test whether the hospital mean differs from the national mean at the 5% significance level.

**Step 1: State the Hypotheses**

$$
H_0:\mu=3.3
$$

$$
H_A:\mu\neq3.3
$$

**Step 2: Compute the Test Statistic**

The test statistic is

$$
t=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}
$$

Substitute the values:

$$
t=\frac{3.15-3.30}{0.40/\sqrt{25}}
$$

Compute the denominator:

$$
\frac{0.40}{5}=0.08
$$

Therefore,

$$
t=\frac{-0.15}{0.08}
=-1.875
$$

**Step 3: Degrees of Freedom**

$$
df=n-1=25-1=24
$$

**Step 4: Decision**

The critical value for

$$
\alpha=0.05
$$

(two-sided) with

$$
df=24
$$

is approximately

$$
\pm2.064.
$$

Since

$$
|-1.875|<2.064,
$$

we fail to reject the null hypothesis.

**Step 5: Conclusion**

There is insufficient statistical evidence that the hospital's mean birth weight differs from the national average.

```{r}
# Example data
weights <- c(
3.0,3.4,3.1,3.2,2.9,
3.3,3.0,3.2,3.1,3.4,
3.0,3.2,3.1,3.3,3.2,
3.0,3.4,3.1,3.2,3.3,
3.0,3.1,3.2,3.4,3.1
)

t.test(weights, mu = 3.3)
```

### Two-Sample t-Test

-   The two-sample t-test compares the means of two independent groups when the population standard deviations are unknown.

The test statistic is

$$
t=
\frac{\bar{x}_1-\bar{x}_2}
{s_p\sqrt{\frac1{n_1}+\frac1{n_2}}}
$$

where

$$
s_p=
\sqrt{
\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}
{n_1+n_2-2}
}
$$

is the pooled standard deviation.

-   The degrees of freedom are $df=n_1+n_2-2$

#### Example 2: Two-Sample t-Test

A researcher compares the mean systolic blood pressure between patients receiving a new drug and those receiving standard treatment.

| Group              | Sample Size | Mean |  SD |
|:-------------------|------------:|-----:|----:|
| New Drug           |          12 |  128 |   8 |
| Standard Treatment |          12 |  135 |   9 |

Assume equal variances.

**Step 1: State the Hypotheses**

$$
H_0:\mu_1=\mu_2
$$

$$
H_A:\mu_1\neq\mu_2
$$

**Step 2: Compute the Pooled Standard Deviation**

$$
s_p=
\sqrt{
\frac{(12-1)(8^2)+(12-1)(9^2)}
{12+12-2}
}
$$

$$
=
\sqrt{
\frac{704+891}{22}
}
$$

$$
=
\sqrt{72.5}
=8.51
$$

**Step 3: Compute the Test Statistic**

$$
t=
\frac{128-135}
{8.51\sqrt{\frac1{12}+\frac1{12}}}
$$

Compute

$$
\sqrt{\frac1{12}+\frac1{12}}
=
0.408
$$

Therefore,

$$
t=
\frac{-7}{8.51\times0.408}
=
\frac{-7}{3.47}
=
-2.02
$$

**Step 4: Degrees of Freedom**

$$
df=12+12-2=22
$$

**Step 5: Decision**

Critical value:

$$
t_{0.025,22}=2.074
$$

Since

$$
|-2.02|<2.074,
$$

we fail to reject the null hypothesis.

**Step 6: Conclusion**

There is insufficient statistical evidence that the two treatments differ in mean systolic blood pressure.

```{r}
new_drug <- c(
120,130,125,128,135,122,
129,131,126,128,130,132
)

standard <- c(
140,132,138,133,136,135,
129,137,140,133,138,131
)

t.test(new_drug,
       standard,
       var.equal = TRUE)
```

## $\chi^2$ Test

-   Is the commonly used for comparison of proportions. $$
    \chi^2 = \sum \frac{(observed-expected)^2}{expected}
    $$

where *Observed (O)*: Actual counts in the data *Expected (E)*: Counts expected under $H_0$

The expected frequency for each cell is: $$
E = \frac{(Row total) (Column total)}{Grand total}
$$

#### Example 1: Chi-square

A study investigates whether smoking is associated with lung disease.

**Step 1: Data**

|             | Lung Disease | No Disease |   Total |
|:------------|-------------:|-----------:|--------:|
| Smokers     |           40 |         20 |      60 |
| Non-smokers |           20 |         40 |      60 |
| **Total**   |       **60** |     **60** | **120** |

**Step 2: State the Hypotheses**

**Null hypothesis (**$H_0$)

$$
H_0:\ \text{Smoking and lung disease are independent.}
$$

**Alternative hypothesis (**$H_A$)

$$
H_A:\ \text{Smoking and lung disease are associated.}
$$

**Step 3: Compute the Expected Frequencies (If there were truly no association between smoking and lung disease (i.e., if** $H_0$ were true), how many people would we expect to see in each cell?)

The expected frequency for each cell is calculated as

$$
E=\frac{(\text{Row Total})(\text{Column Total})}{\text{Grand Total}}
$$

For **Smokers with Lung Disease**,

$$
E=\frac{60\times60}{120}=30
$$

the expected frequencies for all cells are:

|             | Lung Disease | No Disease |   Total |
|:------------|-------------:|-----------:|--------:|
| Smokers     |           30 |         30 |      60 |
| Non-smokers |           30 |         30 |      60 |
| **Total**   |       **60** |     **60** | **120** |

**Step 4: Compute the Chi-square Statistic**

The Pearson Chi-square statistic is

$$
\chi^2=\sum\frac{(O-E)^2}{E}
$$

**Cell 1 (Smokers, Lung Disease)**

$$
\frac{(40-30)^2}{30}
=
\frac{100}{30}
=
3.33
$$

**Cell 2 (Smokers, No Disease)**

$$
\frac{(20-30)^2}{30}
=
\frac{100}{30}
=
3.33
$$

**Cell 3 (Non-smokers, Lung Disease)**

$$
\frac{(20-30)^2}{30}
=
\frac{100}{30}
=
3.33
$$

**Cell 4 (Non-smokers, No Disease)**

$$
\frac{(40-30)^2}{30}
=
\frac{100}{30}
=
3.33
$$

**Step 5: Sum the Contributions**

$$
\chi^2
=
3.33+3.33+3.33+3.33
=
13.33
$$

**Step 6: Compute the Degrees of Freedom**

The degrees of freedom are calculated as

$$
df=(r-1)(c-1)
$$

where

-   $r=2$ (number of rows)
-   $c=2$ (number of columns)

Therefore,

$$
df=(2-1)(2-1)=1
$$

**Step 7: Make a Decision**

For a significance level of

$$
\alpha=0.05,
$$

the critical value is

$$
\chi^2_{0.05,1}=3.841.
$$

Since

$$
13.33>3.841,
$$

we **reject the null hypothesis**.

**Conclusion**

There is sufficient statistical evidence to conclude that **smoking is significantly associated with lung disease**.

**Create the contingency table**

```{r}
# Create the contingency table
smoking <- matrix(c(40,20,
                    20,40),
                  nrow = 2,
                  byrow = TRUE)

rownames(smoking) <- c("Smokers",
                       "Non-smokers")

colnames(smoking) <- c("Disease",
                       "No Disease")

smoking
#display the expected frequencies


```

**Perform the test**

```{r}
chisq.test(smoking)
chisq.test(smoking, correct = F)

result <- chisq.test(smoking)

result$expected

#extract individual components
result$statistic
result$parameter
result$p.value
```

**Interpretation of the Output**

-   Chi-square statistic ($\chi^2$) = 13.33: This measures how much the observed frequencies differ from the expected frequencies under the null hypothesis.

-   Degrees of freedom (df) = 1: Determined by the table dimensions, $(r−1)(c−1)$.

-   p-value = 0.00026: Since this is less than 0.05, there is strong evidence against the null hypothesis.

-   *Conclusion*: There is a statistically significant association between smoking and lung disease

### Choosing the Appropriate Hypothesis Test

| **Situation**                                                                                                                                | **Appropriate Test**                      |
|:-----------------------------------------------|:----------------------|
| Compare one sample mean to a known value, with **population standard deviation (**$\sigma$) known or **large sample size (**$n \geq 30$)     | One-sample **Z-test**                     |
| Compare one sample mean to a known value, with **population standard deviation (**$\sigma$) unknown                                          | One-sample **t-test**                     |
| Compare the means of **two independent groups**, with **population standard deviations known**                                               | Two-sample **Z-test**                     |
| Compare the means of **two independent groups**, with **population standard deviations unknown**                                             | Two-sample **t-test** (pooled or Welch's) |
| Compare **paired or matched observations** (e.g., before-and-after measurements, twins, matched subjects)                                    | Paired **t-test**                         |
| Compare the association between **two categorical variables** (e.g., exposure vs. disease, treatment vs. outcome, gender vs. smoking status) | **Pearson's Chi-square test**             |
|                                                                                                                                              |                                           |