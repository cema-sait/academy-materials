---
name: Introduction to Probability
dependsOn: [introduction_to_statistics.statistics_and_probability]
learningOutcomes:
  - Define probability as a long-run relative frequency and apply the classical formula for equally likely outcomes.
  - Identify the sample space and classify events as simple or compound.
  - Apply set operations (union, intersection, difference, complement) and the addition rule to combine events.
  - Distinguish mutually exclusive events from non-exclusive events and apply the simplified addition rule.
  - Calculate and interpret conditional probability, including its role in defining risk ratios in epidemiology.
  - Apply Bayes' theorem to compute positive and negative predictive values in diagnostic testing.
  - Define random variables and calculate expected value and variance for discrete distributions.
---

## From Data to Decisions

You have already summarised data and fit models. **Probability** is the connective tissue underneath: it is how we quantify *uncertainty* and move from a sample to a statement about a population.

In public health it is behind:

- **Prevalence and risk** — a probability is a population proportion.
- **Diagnostic testing** — sensitivity, specificity, and predictive value are all conditional probabilities.
- **Inference** — P-values, confidence intervals, and every model you will fit rest on a probability model for the data.

## Defining Probability

Intuitively, the **probability** of an outcome is the proportion of times it would occur if the experiment were repeated indefinitely. It is a *long-run relative frequency*.

When a finite set of outcomes is **equally likely**,

$$P(A)=\frac{\text{number of outcomes in } A}{\text{total number of outcomes}}.$$

A fair die has **six equally likely** faces:

- $P(\text{roll a } 1) = 1/6$ — one favourable outcome out of six.
- $P(1 \text{ or } 2) = 2/6 = 1/3$ — two favourable outcomes.
- $P(1,2,3,4,5, \text{ or } 6) = 6/6 = 1$ — a **certain** event.
- $P(\text{not a } 2) = 1 - \tfrac{1}{6} = 5/6$ — **the complement.**

The **frequentist** definition in action: as we keep rolling, the observed proportion of 1s settles at $1/6$.

```r
die <- 1:6

# The four introductory examples (theoretical probabilities)
cat("P(roll a 1) =", round(1/6, 4), "\n") # 0.1667
cat("P(1 or 2) =", round(2/6, 4), "\n") # 0.3333
cat("P(any of 1-6) =", 6/6, "\n") # 1  (a certain event)
cat("P(not a 2) =", round(5/6, 4), "\n") # 0.8333

# Frequentist view: simulate rolls and watch P(1) converge to 1/6
set.seed(1)
rolls <- sample(die, 6000, replace = TRUE)
running <- cumsum(rolls == 1) / seq_along(rolls)

plot(running, type = "l", col = "#F58220", lwd = 2, ylim = c(0, 0.4),
     xlab = "Number of rolls", ylab = "Proportion of 1s",
     main = "Long-run frequency approaches 1/6")
abline(h = 1/6, lty = 2, col = "#2DA7E0", lwd = 2)
```

## Our Working Example

Throughout, we use a **simulated cohort** of 500 people with a smoking exposure and a disease outcome. Run this block first — it builds the `cohort` data used in all examples that follow. `iris` (built into R) serves as a practice dataset.

```r
set.seed(2024)
n <- 500
smoke <- rbinom(n, 1, 0.40) # 40% are smokers
dis <- rbinom(n, 1, ifelse(smoke == 1, 0.30, 0.10)) # smokers: higher risk
cohort <- data.frame(
  age = round(rnorm(n, 45, 12)),
  smoker = factor(ifelse(smoke == 1, "yes", "no"),  levels = c("no", "yes")),
  outcome = factor(ifelse(dis == 1, "case", "control"), levels = c("control", "case"))
)
head(cohort, 5)
```

## Probability Terminology

### Sample Space and Events

The **sample space** $S$ is the set of all possible outcomes of an experiment. An **event** is any subset of $S$. If all $|S|$ outcomes are equally likely, each has probability $1/|S|$.

- A **simple event** is a single outcome (e.g. a randomly chosen person is a *case*).
- A **compound event** combines several outcomes (e.g. *case* **and** *smoker*).

We will use the `iris` dataset as a practice example. The experiment **"Pick a random flower and note its species"** has sample space {setosa, versicolor, virginica}.

If species are equally likely:

$$P(\text{setosa}) = 1/3$$

### Events as Probabilities in R

An event is a logical condition. Its probability is the **mean of that logical vector** (the proportion of `TRUE`s).

```r
# Practice: P(Sepal.Length > 5) — a simple event on iris dataset
mean(iris$Sepal.Length > 5)

# Epidemiology Example: P(case) is the disease PREVALENCE in the cohort
mean(cohort$outcome == "case") # a probability IS a proportion

# P(smoker) — the exposure prevalence
mean(cohort$smoker == "yes")
```

`mean(outcome == "case")` returns **0.172**, which is the prevalence. In epidemiology a probability and a population proportion are similar.

## Definition of Probability

Classically, for equally likely outcomes,
$$P(A) = \frac{\text{number of outcomes in } A}{\text{total number of outcomes in } S}.$$

Every probability obeys three axioms:

- $0 \le P(A) \le 1$
- $P(S)=1$
- For disjoint events, probabilities add.

The **frequentist** reading is a long-run proportion over many repetitions, which is why `mean(condition)` estimates a probability, and **why larger samples give more stable estimates.**

```r
# Estimate P(case) from samples of increasing size
for (m in c(20, 100, 500)) {
  s <- sample(cohort$outcome, m, replace = TRUE)
  cat("n =", m, "  estimated prevalence =", round(mean(s == "case"), 3), "\n")
}
```

## Set Operations on Events

### Combining Events

| Operation | Notation | Meaning | Rule |
|---|---|---|---|
| Union | $A \cup B$ | $A$ **or** $B$ (or both) | $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ |
| Intersection | $A \cap B$ | $A$ **and** $B$ | $P(A\cap B)=P(A)\,P(B\mid A)$ |
| Difference | $A - B$ | $A$ but not $B$ | $P(A-B)=P(A)-P(A\cap B)$ |
| Complement | $A'$ | not $A$ | $P(A')=1-P(A)$ |

The union rule subtracts $P(A\cap B)$ so the overlap is not counted twice. The empty event $\varnothing$ has $P(\varnothing)=0$.

### Set Operations in R

```r
S <- cohort$smoker  == "yes" # event: smoker
D <- cohort$outcome == "case" # event: diseased (case)

c(P_smoker = mean(S),
  P_case = mean(D),
  P_union = mean(S | D), # smoker OR case
  P_intersect = mean(S & D), # smoker AND case
  P_smoker_only = mean(S & !D), # smoker but not a case
  P_not_case = mean(!D)) # complement of case
```

Check the union rule: $$P(S)+P(D)-P(S\cap D) = 0.436 + 0.172 - 0.126 = 0.482$$ which equals `mean(S | D)`.

## Mutually Exclusive Events

Two events are **mutually exclusive** (disjoint) when they cannot happen together: $A \cap B = \varnothing$, so $P(A\cap B)=0$ and the addition rule simplifies to
$$P(A\cup B)=P(A)+P(B).$$

A person's disease status is *case* or *control*, never both — those categories are mutually exclusive. Exposure and disease, however, are **not** disjoint (a person can be both a smoker and a case), which is exactly why they can be *associated*.

```r
# Mutually exclusive: no one is both a case AND a control
mean(cohort$outcome == "case" & cohort$outcome == "control")   

# NOT mutually exclusive: smoker and case co-occur
mean(cohort$smoker == "yes" & cohort$outcome == "case") 
```

## Conditional Probability

The probability of $A$ **given** that $B$ occurred restricts attention to the world where $B$ is true:
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0.$$

Rearranging gives the **general multiplication rule** $P(A\cap B)=P(B)\,P(A\mid B)$. Conditioning is necessary in epidemiology:

- **risk** *in the exposed*,
- **survival** *given* treatment,
- **disease** *given* a positive test.

### Contingency Tables: Marginal, Joint, Conditional

A 2×2 table holds all three probability types at once:

- **marginal** (row/column totals),
- **joint** (a single cell), and
- **conditional** (a cell relative to its row or column).

```r
tab <- table(cohort$smoker, cohort$outcome)
tab
prop.table(tab) # JOINT probabilities (cells sum to 1)
prop.table(tab, margin = 1) # CONDITIONAL on smoker: P(outcome | smoker)
```

The bottom row of the last output is $P(\text{case}\mid\text{smoker})$.

### Conditional Probability is Risk

Comparing a conditional probability across exposure groups gives the **risk ratio** — the measure of association in epidemiology.

```r
p_exposed   <- mean(cohort$outcome[cohort$smoker == "yes"] == "case")
p_unexposed <- mean(cohort$outcome[cohort$smoker == "no"]  == "case")

cat("Risk | smoker =", round(p_exposed,   3), "\n")
cat("Risk | non-smoker =", round(p_unexposed, 3), "\n")
cat("Risk ratio =", round(p_exposed / p_unexposed, 2), "\n")
```

Smokers are **3.5 times** as likely to be cases. That single number — a ratio of two conditional probabilities — is a fundamental measure in epidemiological analysis.

### Independence and the Gambler's Fallacy

$A$ and $B$ are **independent** when conditioning changes nothing:
$$P(A\mid B)=P(A) \quad\Longleftrightarrow\quad P(A\cap B)=P(A)\,P(B).$$

If exposure and disease were independent, the risk ratio would be 1 — no association. Independence also has a famous trap: past independent outcomes carry **no** information about the next one (***The gambler's fallacy***).

Each new patient, coin flip, or test is a fresh draw.

## Bayes' Theorem and Diagnostic Testing

### Inverting a Conditional Probability

A test tells us $P(\text{positive}\mid\text{disease})$, but a clinician needs the **inverse**, $P(\text{disease}\mid\text{positive})$.

**Bayes' theorem** flips it:

$$P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B\mid A)P(A)+P(B\mid A')P(A')}.$$

In screening language:

- **sensitivity** $=P(+\mid \text{disease})$,
- **specificity** $=P(-\mid \text{no disease})$,
- **prevalence** $=P(\text{disease})$,

and the answer we want is the **positive predictive value** $P(\text{disease}\mid +)$.

### The Diagnostic 2×2 Table

Picture screening **100,000 people** with this test — 89% sensitivity, 93% specificity, for a disease with **0.35% prevalence**. Everyone lands in one of four cells:

|                   | Disease **present** | Disease **absent** | Total |
|-------------------|:---:|:---:|:---:|
| **Test positive** | 312 (TP) | 6,975 (FP) | **7,287** |
| **Test negative** | 38 (FN) | 92,675 (TN) | 92,713 |
| **Total**         | 350 | 99,650 | 100,000 |

- **Sensitivity** $=\frac{TP}{TP+FN}=\frac{312}{350}\approx 0.89$ — of the diseased, who tests positive.
- **Specificity** $=\frac{TN}{TN+FP}=\frac{92{,}675}{99{,}650}\approx 0.93$ — of the healthy, who tests negative.
- **PPV** $=\frac{TP}{TP+FP}=\frac{312}{7{,}287}\approx 0.043$ — of the test-positives, who is truly sick.

Of the **7,287** people who test positive, only **312** are actually ill — the other **6,975 are false positives**.

### Why a Positive Test Can Still Mean Low Risk

A good test applied to a **rare** disease produces mostly false positives. Try lowering `prevalence` and watch the predictive value change.

```r
sensitivity <- 0.89 # P(test + | disease)
specificity <- 0.93 # P(test - | no disease)
prevalence  <- 0.0035 # P(disease) -- try 0.01, 0.05, 0.20

ppv <- sensitivity * prevalence /
       (sensitivity * prevalence + (1 - specificity) * (1 - prevalence))

cat("Positive predictive value =", round(ppv, 4),
    " (", round(100 * ppv, 1), "% )\n", sep = "")
```

At 0.35% prevalence the PPV is just **4.3%** — 24 of every 25 positives are false alarms. This is why rare conditions are confirmed with a second, independent test.

### A Historical Epidemic: Smallpox, Boston 1721

Real data on 6,224 residents during a smallpox outbreak — did **inoculation** (a precursor to vaccination) reduce the risk of death?

```r
smallpox <- matrix(c(238, 5136,
                       6,  844),
                   nrow = 2, byrow = TRUE,
                   dimnames = list(result = c("lived", "died"),
                                   inoculated = c("yes", "no")))
smallpox
cat("P(died | inoculated) =", round(6   / 244,  4), "\n")  # 0.0246
cat("P(died | not inoculated) =", round(844 / 5980, 4), "\n")  # 0.1411
```

Death was about **1 in 40** for the inoculated versus **1 in 7** for those not inoculated — an early quantitative case for *immunisation*.

## Random Variables

### From Events to Numbers

A **random variable** $X$ attaches a number to each outcome — for example, days of hospital stay, number of new cases, cost of care.

Its **expected value** is the probability-weighted average, the long-run mean:
$$E(X)=\sum_i x_i\,P(X=x_i).$$

Expectation is how we turn a probability distribution into an **expected burden** — cases per week, bed-days per patient, cost per episode.

```r
x <- c(0, 1, 2, 3) # days of stay
p <- c(0.55, 0.25, 0.15, 0.05)  # probabilities (sum to 1)

Ex <- sum(x * p)
cat("E(X) = expected stay =", Ex, "days\n")
```

### Variability: Variance and Standard Deviation

The **variance** measures how much outcomes scatter around $E(X)$, weighting squared deviations by their probability:
$$\operatorname{Var}(X)=\sum_i (x_i-\mu)^2\,P(X=x_i), \qquad \sigma=\sqrt{\operatorname{Var}(X)}.$$

Two interventions can share the same expected outcome yet differ sharply in **risk** — the spread. Variance is how we quantify that uncertainty.

```r
x <- c(0, 1, 2, 3); p <- c(0.55, 0.25, 0.15, 0.05)
mu <- sum(x * p)
v <- sum((x - mu)^2 * p)
cat("E(X)  =", mu, " days\n")
cat("Var(X)=", v,  "\n")
cat("SD(X) =", sqrt(v), " days\n")

bp <- barplot(p, names.arg = x, col = "#2DA7E0", border = "white",
              xlab = "Days of stay", ylab = "Probability",
              main = sprintf("Length of stay (mean = %.1f days)", mu))
```

## Summary

- A **probability is a proportion** — in R, `mean(condition)`. Prevalence and risk are probabilities.
- **Set operations** (∪, ∩, −, complement) and the addition rule combine events; **mutually exclusive** events simply add.
- **Conditional probability** $P(A\mid B)$ is the engine of epidemiology; comparing it across groups gives the **risk ratio**.
- **Bayes' theorem** turns test accuracy (sensitivity, specificity) into **predictive value** — and warns us about false positives when disease is rare.
- **Random variables** summarise numeric outcomes through **expectation** (expected burden) and **variance** (uncertainty).
