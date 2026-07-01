---
name: Mutate and Case When
dependsOn: [introduction_to_R.introduction_to_r.05_select_and_rename]
tags: [r, dplyr, mutate, case_when]
learningOutcomes:
  - Create derived variables with mutate.
  - Apply conditional logic using case_when.
---

#  `mutate()`

- Raw data rarely arrives in the form your analysis needs.
- `mutate()` derives new columns from existing ones without altering a single original value. Think of it as adding new knowledge to your data, not replacing old knowledge.

## `mutate()` — Creating a New Column

- `mutate()` appends the new column to the right of the tibble. Every existing column is preserved exactly as it was.

```{webr-r}
#| label: mutate-basic
# here we decode the integer sex code into a human-readable label.
ideal |>
  mutate(sex_label = if_else(CalfSex == 1, "Male", "Female")) |>
  select(CalfID, CalfSex, sex_label, Weight, ReasonsLoss1) |>
  head(5)
```

## `mutate()` — Multiple Columns at Once

- A single `mutate()` call creates as many columns as you need. Later expressions in the same call can reference columns created earlier, so the order of your derivations matters and can build on itself.

```{webr-r}
#| label: mutate-multi
ideal |>
  mutate(
    sex_label = if_else(CalfSex == 1, "Male", "Female"),
    weight_lbs = round(Weight * 2.205, 1), # convert kg to pounds
    anaemic = ManualPCV < 24 # confirmatory test for anaemia
  ) |>
  select(CalfID, sex_label, Weight, weight_lbs, ManualPCV, anaemic) |>
  head(3)
```

## `mutate()` with `case_when()`

- `case_when()` is R's vectorised multi-condition classifier — the equivalent of Excel's nested `IFS`.
- Each condition is evaluated top-to-bottom; the first `TRUE` match determines the value assigned to that row.

```{webr-r}
#| label: case-when
ideal |>
  dplyr::mutate(
    anaemia_class = case_when(
      is.na(ManualPCV)  ~ "Unknown", # always test for NA first
      ManualPCV < 24 ~ "Severe anaemia",
      ManualPCV < 30 ~ "Mild anaemia",
      TRUE ~ "Normal" 
    )
  ) |>
  dplyr::select(CalfID, ManualPCV, anaemia_class)
```

## `case_when()` — The Mental Model

Each line is one rule: **"When** *this condition* **is true → assign** *this value*."

```{r}
#| label: case-when-structure
#| eval: false
mutate(
  new_column = case_when(
    condition_1 ~ "value when condition_1 is TRUE",
    condition_2 ~ "value when condition_2 is TRUE",
    condition_3 ~ "value when condition_3 is TRUE",
    TRUE ~ "value for everything else"
  )
)
```

Rules are tested in order. The moment a condition matches, R stops testing — so place the most specific conditions first, the broadest last.

