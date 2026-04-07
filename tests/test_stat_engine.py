import unittest

from src.stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):
    def test_mean_odd_list(self):
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertEqual(engine.get_mean(), 3.0)

    def test_mean_even_list(self):
        engine = StatEngine([2, 4, 6, 8])
        self.assertEqual(engine.get_mean(), 5.0)

    def test_median_odd(self):
        engine = StatEngine([5, 1, 3])
        self.assertEqual(engine.get_median(), 3.0)

    def test_median_even(self):
        engine = StatEngine([1, 2, 4, 3])
        self.assertEqual(engine.get_median(), 2.5)

    def test_mode_single(self):
        engine = StatEngine([1, 2, 2, 3, 4])
        self.assertEqual(engine.get_mode(), [2.0])

    def test_mode_multi(self):
        engine = StatEngine([1, 1, 2, 2, 3])
        self.assertEqual(engine.get_mode(), [1.0, 2.0])

    def test_mode_all_unique(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_mode(), "No mode found: all values are unique.")

    def test_variance_sample_and_population(self):
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertAlmostEqual(engine.get_variance(is_sample=True), 2.5)
        self.assertAlmostEqual(engine.get_variance(is_sample=False), 2.0)

    def test_standard_deviation_known_outcome(self):
        # Known dataset where population standard deviation is exactly 2.
        engine = StatEngine([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertAlmostEqual(engine.get_standard_deviation(is_sample=False), 2.0)

    def test_outliers(self):
        engine = StatEngine([10, 11, 12, 12, 13, 14, 100])
        self.assertEqual(engine.get_outliers(threshold=2), [100.0])

    def test_empty_data_raises(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_mixed_type_raises(self):
        with self.assertRaises(TypeError):
            StatEngine([1, 2, "3", None, 5])

    def test_mixed_type_cleaning(self):
        engine = StatEngine([1, 2, "3", None, 5], clean_data=True)
        self.assertEqual(engine.data, [1.0, 2.0, 5.0])

    def test_sample_variance_requires_at_least_two(self):
        engine = StatEngine([42])
        with self.assertRaises(ValueError):
            engine.get_variance(is_sample=True)


if __name__ == "__main__":
    unittest.main()
