# Statistical Engine & Monte Carlo LLN Simulation

## Project Overview
This project builds a pure-Python statistical analysis engine from scratch and applies it to a probability simulation scenario.

- `StatEngine` (in `src/stat_engine.py`) processes raw 1D numerical data and computes:
  - Mean, median, and mode (including multimodal detection)
  - Sample and population variance
  - Sample and population standard deviation
  - Outliers using a standard-deviation threshold
- `simulate_crashes(days)` (in `src/simulation.py`) performs a Monte Carlo simulation of a startup server with daily crash probability `0.045`, illustrating the Law of Large Numbers (LLN).

Only Python standard library modules are used.

## Mathematical Logic

### Variance Formula
Given data points `x1, x2, ..., xn` and mean `x̄`:

- Population variance:
  `sigma^2 = (sum((xi - x̄)^2)) / n`
- Sample variance (Bessel's correction):
  `s^2 = (sum((xi - x̄)^2)) / (n - 1)`

The implementation supports both through `get_variance(is_sample=True)`.

### Median (Even vs Odd)
The data is sorted first:

- If `n` is odd, median is the middle element at index `n // 2`.
- If `n` is even, median is the average of the two middle elements:
  `(sorted_data[n//2 - 1] + sorted_data[n//2]) / 2`.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Statistical-Engine
   ```
2. Run the LLN simulation:
   ```bash
   python main.py
   ```

No external dependencies are required.

## Testing
Run all tests with:

```bash
python -m unittest discover -s tests -v
```

## Acceptance Criteria Checklist
- [x] Implements `StatEngine` as a class for raw 1D numeric data.
- [x] Mean is computed correctly from scratch.
- [x] Median handles both odd and even dataset lengths correctly.
- [x] Mode supports multimodal distributions (returns all modes as a list).
- [x] Mode returns a specific message when all values are unique.
- [x] Variance supports both sample (`n-1`) and population (`n`) formulas.
- [x] Standard deviation is derived from variance.
- [x] Outlier detection returns values beyond `threshold` standard deviations from mean.
- [x] Empty data input is handled gracefully (descriptive error, no divide-by-zero failure).
- [x] Mixed/non-numeric data is handled robustly (descriptive `TypeError` or cleaning mode).
- [x] Monte Carlo simulation uses `random` and computes simulated crash probability as `crashes / days`.
- [x] Simulation demonstrates LLN behavior with increasing trial counts.