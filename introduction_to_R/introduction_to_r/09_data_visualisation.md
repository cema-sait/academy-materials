---
name: Data Visualisation
dependsOn: [introduction_to_R.introduction_to_r.08_joins]
tags: [r, ggplot2, charts, visualisation]
learningOutcomes:
  - Build bar and column charts with ggplot2.
  - Prepare summarised inputs for visual analysis.
  - Improve chart readability with ordering and coordinate transforms.
---

#  Data Visualisation in R

`ggplot2` translates data frames into graphics through three composable layers that stack with `+`: **data**, **aesthetics** (`aes()`), and **geometry** (`geom_*()`). Everything else (themes, labels, scales) is optional to polish on top.

## `geom_bar()` — Counting Outcomes {.code-only}

```{webr-r}
#| label: bar-plot
ggplot(data = ideal,
       mapping = aes(x = ReasonsLoss1)) +
  geom_bar(fill = "#185FA5") +
  theme_classic() +
  labs(title = "Survival of calves in the first year of life",
       x = "",
       y = "Number of visits")
```


## `geom_bar()` — Result

:::: {.columns}
::: {.column width="60%"}
```{r}
#| label: bar-plot-static
#| echo: false
#| fig-width: 5
#| fig-height: 3.5
#| out-width: "100%"
ggplot(data = ideal,
       mapping = aes(x = ReasonsLoss1)) +
  geom_bar(fill = "#185FA5") +
  theme_classic() +
  labs(title = "Survival of calves in the first year of life",
       x = "",
       y = "Number of visits")
```
:::
::: {.column width="40%"}
`geom_bar()` counts rows for you — supply only `x` and it derives bar heights automatically.

**What to notice**

- Two categories: `died`, `survived`
- `survived` is the largest group by a clear margin
- y-axis counts **visits**, not unique calves — one calf appears at every visit

> **Try it:** go back and change `fill = "#185FA5"` to `fill = "#639922"`, re-run, then advance again to see the updated chart.
:::
::::

## Preparing the Data — `calves_per_sub`

Before using `geom_col()`, summarise to one row per sub-location. 

```{webr-r}
#| label: col-data-prep
calves_per_sub <- ideal |>
  group_by(sublocation) |>
  summarise(n_calves = n_distinct(CalfID)) |>  # unique calves
  ungroup()

calves_per_sub
```

> `n_distinct(CalfID)` counts unique calves per sub-location.

## `geom_col()` — Pre-summarised Data {.code-only}

```{webr-r}
#| label: col-basic
ggplot(data = calves_per_sub,
       mapping = aes(x = sublocation, y = n_calves)) +
  geom_col(fill = "#185FA5") +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(x = "", y = "Number of calves",
       title = "Calves recruited per sub-location")
```


## `geom_col()` — Result

:::: {.columns}
::: {.column width="60%"}
```{r}
#| label: col-basic-static
#| echo: false
#| fig-width: 5.5
#| fig-height: 4.5
#| out-width: "100%"
calves_per_sub <- ideal |>
  group_by(sublocation) |>
  summarise(n_calves = n_distinct(CalfID)) |>
  ungroup()

ggplot(calves_per_sub,
       aes(x = sublocation, y = n_calves)) +
  geom_col(fill = "#185FA5") +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(x = "", y = "Number of calves",
       title = "Calves recruited per sub-location")
```
:::
::: {.column width="40%"}
`geom_col()` requires both `x` and `y`, you supply the heights you already computed.

| | `geom_bar()` | `geom_col()` |
|--|--|--|
| You supply | `x` only | `x` and `y` |
| R computes | counts | nothing |
| Use when | raw data | summarised data |

Notice the overlapping x-axis labels, a common problem with many categories. The next slide shows the fix.

> **Try it:** go back and add `fill = sublocation` inside `aes()` to colour each bar differently, then advance again.
:::
::::

## `coord_flip()` and `reorder()` {.code-only}

```{webr-r}
#| label: col-flipped
ggplot(data = calves_per_sub,
       mapping = aes(x = reorder(sublocation, n_calves),
                     y = n_calves)) +
  geom_col(fill = "#185FA5") +
  coord_flip() +
  theme_classic() +
  labs(x = "",
       y = "Number of calves",
       title = "Calves recruited per sub-location")
```


## `coord_flip()` — Result

:::: {.columns}
::: {.column width="60%"}
```{r}
#| label: col-flipped-static
#| echo: false
#| fig-width: 5.5
#| fig-height: 4.5
#| out-width: "100%"
ggplot(calves_per_sub,
       aes(x = reorder(sublocation, n_calves), y = n_calves)) +
  geom_col(fill = "#185FA5") +
  coord_flip() +
  theme_classic() +
  labs(x = "",
       y = "Number of calves",
       title = "Calves recruited per sub-location")
```
:::
::: {.column width="40%"}
This transform the chart into a ranked, readable comparison.

- **`reorder(sublocation, n_calves)`** — sorts bars by value instead of alphabetically; the longest bar is always at top
- **`coord_flip()`** — rotates axes so long labels read horizontally without overlapping

> **Try it:** go back and change `reorder(sublocation, n_calves)` to `reorder(sublocation, -n_calves)` to reverse the sort order, then advance again.
:::
::::

## Preparing the Data — `calves_by_sex`

To split bars by gender, we need two grouping variables. Run this before the next slide.

```{webr-r}
#| label: sex-data-prep
calves_by_sex <- ideal |>
  mutate(sex_label = case_when(
    CalfSex == 1 ~ "Male",
    CalfSex == 2 ~ "Female",
    TRUE ~ "Unknown"
  )) |>
  group_by(sublocation, sex_label) |>
  summarise(n_calves = n_distinct(CalfID), .groups = "drop")

calves_by_sex
```

> The table now has **two rows per sub-location** — one for each sex. The next slide maps `CalfSex` to `fill` to split the bars.

## Grouped Bars — the `fill` Aesthetic {.code-only}

```{webr-r}
#| label: bar-grouped
top6_subs <- calves_by_sex |>
  group_by(sublocation) |>
  summarise(total = sum(n_calves)) |>
  slice_max(total, n = 5) |>
  pull(sublocation)

ggplot(filter(calves_by_sex, sublocation %in% top6_subs),
       aes(x = reorder(sublocation, n_calves),
           y = n_calves, fill = sex_label)) +
  geom_col(position = "dodge") +
  scale_fill_manual(values = c(Male = "#2196F3", Female = "#E91E63")) +
  coord_flip() + theme_classic() +
  labs(x = "", y = "Number of calves", fill = "Sex",
       title = "Calves per sub-location by sex (top 5)")
```


## Grouped Bars — Result

:::: {.columns}
::: {.column width="60%"}
```{r}
#| label: bar-grouped-static
#| echo: false
#| fig-width: 5.5
#| fig-height: 4
#| out-width: "100%"
calves_by_sex <- ideal |>
  mutate(sex_label = case_when(
    CalfSex == 1 ~ "Male",
    CalfSex == 2 ~ "Female",
    TRUE ~ "Unknown"
  )) |>
  group_by(sublocation, sex_label) |>
  summarise(n_calves = n_distinct(CalfID), .groups = "drop")

top6_subs <- calves_by_sex |>
  group_by(sublocation) |>
  summarise(total = sum(n_calves)) |>
  slice_max(total, n = 5) |>
  pull(sublocation)

ggplot(filter(calves_by_sex, sublocation %in% top6_subs),
       aes(x = reorder(sublocation, n_calves),
           y = n_calves, fill = sex_label)) +
  geom_col(position = "dodge") +
  scale_fill_manual(values = c(Male = "#2196F3", Female = "#E91E63")) +
  coord_flip() + theme_classic() +
  labs(x = "", y = "Number of calves", fill = "Sex",
       title = "Calves per sub-location by Gender  (top 5)")
```
:::
::: {.column width="40%"}
Mapping `fill = sex_label` tells ggplot2 to split each bar by sex and colour the groups automatically. `scale_fill_manual()` replaces the defaults with intentional colours.

**`position` options**

| Value | Effect |
|-------|--------|
| `"dodge"` | Side by side — compare values |
| `"stack"` | Stacked — compare totals |
| `"fill"` | Stacked to 100% — compare proportions |

> **Try it:** go back, remove the `top6_subs` filter and use `calves_by_sex` directly, switch `position` to `"stack"`, then advance again.
:::
::::

