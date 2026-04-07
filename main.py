"""Entry point for LLN server crash simulation."""

import random

from src.simulation import run_crash_scenarios


def main() -> None:
    # Seeded for reproducible classroom/demo output.
    random.seed(42)

    day_counts = [100, 1000, 10000]
    results = run_crash_scenarios(day_counts)

    print("Startup Server Crash Simulation (theoretical p = 0.045)")
    for result in results:
        days = int(result["days"])
        crashes = int(result["crashes"])
        probability = result["simulated_probability"]
        print(f"Days={days:5d} | Crashes={crashes:4d} | Simulated p={probability:.4f}")

    print("\nInterpretation (Law of Large Numbers):")
    print(
        "As the number of simulated days increases, the observed crash rate tends to get "
        "closer to the true probability (0.045)."
    )
    print(
        "Using a very small dataset to plan yearly maintenance is risky because random "
        "short-term fluctuation can significantly overestimate or underestimate true crash risk."
    )


if __name__ == "__main__":
    main()
