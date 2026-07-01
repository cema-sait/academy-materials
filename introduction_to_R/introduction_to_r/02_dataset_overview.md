---
name: Dataset Overview
dependsOn: [introduction_to_R.introduction_to_r.01_reading_data_into_r]
learningOutcomes:
  - Understand the IDEAL dataset context used throughout the course.
  - Load and reference a working dataset for analysis.
---

##  The Dataset We'll Use for Today's Session

The **IDEAL study** followed calves across 14 sublocations in Western Kenya, recording health indicators at roughly six-week intervals from birth to one year.

## Loading the IDEAL Dataset

Three lines take you from nothing to a live dataset. In practice, you run these once at the top of every script.

```r
# A tibble prints its dimensions and column types automatically
ideal
```

> Once a package is installed, you never need `install.packages()` again — only `library()`.

