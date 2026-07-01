---
name: Inspecting Your Data
dependsOn: [introduction_to_R.introduction_to_r.02_dataset_overview]
learningOutcomes:
  - Inspect structure and dimensions with head, dim, names, and glimpse.
  - Generate summary statistics and identify missing values.
---

Never analyse data you have not looked at. These three functions are your first line of due diligence, run them immediately after every `read_*()` call.

## Preview

- `head()` shows the first 5 rows.
- `dim()` confirms the number of rows and columns.
- `names()` lists every column

```r
head(ideal, 5)
```
```r
dim(ideal)
names(ideal)
```
## `glimpse()` — The Structural View

- `glimpse()` transposes your data: each column becomes a row, showing its type and first few values side by side.
- In a single screen, you learn the shape, the types, and the range of values.

```r
glimpse(ideal)
```

> Notice: `CalfSex` is an integer, not a label. Columns like `Theileria.spp.` contain dots in their names. `ReasonsLoss1` records the outcome. These are exactly the things we will fix with `rename()` and `mutate()`.

## `summary()` — The Statistical View

- `summary()` applies summary statistics to every numeric column. Missing values appear as a named count.
- One call brings out outliers, impossible values, and data completeness issues that would otherwise stay hidden until analysis.

```r
summary(ideal[, c("Weight", "ManualPCV", "Theileria.spp.", "ADWG")])
```

