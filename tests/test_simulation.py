import random
import unittest

from src.simulation import simulate_crashes


class TestSimulation(unittest.TestCase):
    def test_simulate_crashes_output_range(self):
        random.seed(1)
        crashes, rate = simulate_crashes(1000)
        self.assertTrue(0 <= crashes <= 1000)
        self.assertTrue(0.0 <= rate <= 1.0)

    def test_invalid_days_raises(self):
        with self.assertRaises(ValueError):
            simulate_crashes(0)

    def test_invalid_probability_raises(self):
        with self.assertRaises(ValueError):
            simulate_crashes(100, crash_probability=1.5)


if __name__ == "__main__":
    unittest.main()
