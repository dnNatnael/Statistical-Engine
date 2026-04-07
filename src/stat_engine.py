"""Pure-Python statistical engine for 1D numerical data."""

from __future__ import annotations

import math
from typing import Iterable, List


class StatEngine:
    """Compute descriptive statistics from raw 1D numerical data."""

    def __init__(self, data: Iterable[float], *, clean_data: bool = False) -> None:
        self.data = self._prepare_data(data, clean_data=clean_data)

    @staticmethod
    def _prepare_data(data: Iterable[float], *, clean_data: bool) -> List[float]:
        if data is None:
            raise TypeError("Input data cannot be None.")

        if not isinstance(data, (list, tuple)):
            raise TypeError("Input data must be a list or tuple of numeric values.")

        prepared: List[float] = []

        for index, value in enumerate(data):
            if isinstance(value, bool):
                if clean_data:
                    continue
                raise TypeError(
                    f"Invalid value at index {index}: bool is not allowed in numeric data."
                )

            if isinstance(value, (int, float)):
                prepared.append(float(value))
                continue

            if clean_data:
                continue

            raise TypeError(
                "Mixed or non-numeric data detected. "
                f"Invalid value at index {index}: {value!r} ({type(value).__name__})."
            )

        if not prepared:
            raise ValueError(
                "Input data is empty after validation/cleaning; at least one numeric value is required."
            )

        return prepared

    def get_mean(self) -> float:
        total = 0.0
        for value in self.data:
            total += value
        return total / len(self.data)

    def get_median(self) -> float:
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        midpoint = n // 2

        if n % 2 == 1:
            return sorted_data[midpoint]

        return (sorted_data[midpoint - 1] + sorted_data[midpoint]) / 2.0

    def get_mode(self):
        frequencies = {}
        for value in self.data:
            frequencies[value] = frequencies.get(value, 0) + 1

        highest_frequency = 0
        for count in frequencies.values():
            if count > highest_frequency:
                highest_frequency = count

        if highest_frequency == 1:
            return "No mode found: all values are unique."

        modes = []
        for value, count in frequencies.items():
            if count == highest_frequency:
                modes.append(value)

        return sorted(modes)

    def get_variance(self, is_sample: bool = True) -> float:
        n = len(self.data)
        if is_sample and n < 2:
            raise ValueError("Sample variance requires at least 2 data points.")

        mean_value = self.get_mean()
        squared_diff_sum = 0.0

        for value in self.data:
            diff = value - mean_value
            squared_diff_sum += diff * diff

        denominator = n - 1 if is_sample else n
        return squared_diff_sum / denominator

    def get_standard_deviation(self, is_sample: bool = True) -> float:
        variance = self.get_variance(is_sample=is_sample)
        return math.sqrt(variance)

    def get_outliers(self, threshold: float = 2):
        if threshold < 0:
            raise ValueError("Threshold must be non-negative.")

        mean_value = self.get_mean()
        std_dev = self.get_standard_deviation(is_sample=True)

        if std_dev == 0:
            return []

        outliers = []
        for value in self.data:
            z_score = abs((value - mean_value) / std_dev)
            if z_score > threshold:
                outliers.append(value)

        return outliers
