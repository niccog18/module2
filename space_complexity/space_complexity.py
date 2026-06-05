# Part 1
# For each function, identify its space complexity and explain in one sentence:
# Function A: O(n) — creates a new reversed copy of the string.
# Function B: O(n) — stores (n)character counts in a dictionary.
# Function C: O(n²) — stores an entire n × n matrix.
# Function D: O(1) — uses a single variable (total) regardless of how many numbers are in the input

# Part 2
# You have a function that processes a large CSV file (5 million rows). You need to find all duplicate email addresses. Write two approaches: one that loads all emails into a set (fast, more memory), and one that sorts the file and scans for adjacent duplicates (slower, less memory).

# Generate sample data for testing
import csv
import time
# PYTHONIC: Added imports for argparse, logging, and pathlib
import argparse
import logging
from pathlib import Path
from typing import Set, Tuple

# PYTHONIC: Define constants instead of magic numbers
UNIQUE_EMAILS = 10_000
DEFAULT_SAMPLE_ROWS = 20_000
DEFAULT_LARGE_ROWS = 5_000_000

# PYTHONIC: Configure logging instead of using print()
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def generate_sample_csv(file_path: str | Path, num_rows: int, unique_emails: int = UNIQUE_EMAILS) -> None:
    # PYTHONIC: Added type hints and improved docstring
    """
    Generate a CSV file with sample email addresses for testing.
    
    Args:
        file_path: Path to output CSV file.
        num_rows: Number of email rows to generate.
        unique_emails: Number of unique emails before duplicates repeat.
    """
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(num_rows):
            # PYTHONIC: Use constant instead of magic number
            email = f"user{i % unique_emails}@example.com"
            writer.writerow([email])

# PYTHONIC: Moved generation to main() and if __name__ guard (see bottom)
logger.info("=== Space Complexity Examples ===")

# APPROACH 1: Set-based detection
# Time Complexity: O(n) — single pass through file
# Space Complexity: O(n) — stores all unique emails in the set
# PYTHONIC: Added type hints and improved docstring
def find_duplicates_set(file_path: str | Path) -> Set[str]:
    """
    Find duplicate emails in a file using a set.
    
    Space Complexity: O(n) — stores all seen emails in a set.
    Time Complexity: O(n) — single pass through file.
    
    Args:
        file_path: Path to CSV file with email addresses.
        
    Returns:
        Set of duplicate email addresses.
    """
    seen = set()
    duplicates = set()
    
    with open(file_path, 'r') as file:
        for line in file:
            email = line.strip()
            if email in seen:
                duplicates.add(email)
            else:
                seen.add(email)
    
    return duplicates

# APPROACH 2: Sort-based detection
# Time Complexity: O(n log n) — dominated by sorting step, then O(n) scan
# Space Complexity: O(n) — stores all emails in list for sorting
# PYTHONIC: Added type hints and improved docstring
def find_duplicates_sort(file_path: str | Path) -> Set[str]:
    """
    Find duplicate emails in a file using sorting.
    
    Space Complexity: O(n) — loads entire file into memory for sorting.
    Time Complexity: O(n log n) — sorting dominates, then O(n) scan for adjacent duplicates.
    
    Args:
        file_path: Path to CSV file with email addresses.
        
    Returns:
        Set of duplicate email addresses.
        
    Note:
        This approach loads the entire file into memory. For very large files,
        consider external sorting or streaming algorithms.
    """
    with open(file_path, 'r') as file:
        emails = [line.strip() for line in file]
    
    emails.sort()
    duplicates = set()
    
    # PYTHONIC: Use Pythonic iteration with enumerate or zip
    for i in range(1, len(emails)):
        if emails[i] == emails[i - 1]:
            duplicates.add(emails[i])
    
    return duplicates

# Benchmarking helper
# PYTHONIC: Added type hints and improved docstring
def benchmark_function(func, file_path: str | Path) -> Tuple[float, int]:
    """
    Benchmark a duplicate-finding function.
    
    Args:
        func: Callable that takes file_path and returns a set of duplicates.
        file_path: Path to test file.
        
    Returns:
        Tuple of (execution_time_seconds, number_of_duplicates_found).
        
    Note:
        Uses perf_counter() for accurate high-resolution timing.
    """
    # PYTHONIC: Use perf_counter for benchmarking (more accurate than time())
    start_time = time.perf_counter()
    result = func(file_path)
    end_time = time.perf_counter()
    return end_time - start_time, len(result)


# PYTHONIC: Moved execution into main() and added argparse for control
def main() -> None:
    """
    Main entry point: generate sample data and/or run benchmarks.
    """
    parser = argparse.ArgumentParser(
        description="Compare duplicate email detection approaches."
    )
    parser.add_argument(
        '--generate',
        action='store_true',
        help='Generate sample CSV file before benchmarking.'
    )
    parser.add_argument(
        '--rows',
        type=int,
        default=DEFAULT_SAMPLE_ROWS,
        help=f'Number of rows for generated sample (default: {DEFAULT_SAMPLE_ROWS:,}).'
    )
    parser.add_argument(
        '--unique-emails',
        type=int,
        default=UNIQUE_EMAILS,
        help=f'Number of unique emails before duplicates repeat (default: {UNIQUE_EMAILS:,}).'
    )
    parser.add_argument(
        '--large',
        action='store_true',
        help=f'Generate large file with {DEFAULT_LARGE_ROWS:,} rows (overrides --rows).'
    )
    parser.add_argument(
        '--file',
        default='emails.csv',
        help='Path to CSV file (default: emails.csv).'
    )
    parser.add_argument(
        '--benchmark',
        action='store_true',
        help='Run benchmarks on the file.'
    )
    
    args = parser.parse_args()
    file_path = Path(args.file)
    
    # PYTHONIC: Default behavior - generate if file missing or --generate flag set
    should_generate = args.generate or not file_path.exists()
    if should_generate:
        num_rows = DEFAULT_LARGE_ROWS if args.large else args.rows
        logger.info(f"Generating {num_rows:,} rows to {file_path}...")
        generate_sample_csv(file_path, num_rows, unique_emails=args.unique_emails)
        logger.info("Generation complete.")
    
    # PYTHONIC: Default behavior - benchmark if --benchmark flag set or no flags provided
    should_benchmark = args.benchmark or (not args.generate and not args.large)
    if should_benchmark:
        if not file_path.exists():
            logger.error(f"File {file_path} not found. Use --generate to create it.")
            return
        
        logger.info(f"Benchmarking on {file_path}...")
        logger.info("")
        logger.info("=" * 70)
        time_set, count_set = benchmark_function(find_duplicates_set, file_path)
        time_sort, count_sort = benchmark_function(find_duplicates_sort, file_path)
        
        logger.info("")
        logger.info("BENCHMARK RESULTS:")
        logger.info("-" * 70)
        logger.info(f"Set approach:  {time_set:.6f} seconds | {count_set:,} duplicates found")
        logger.info(f"Sort approach: {time_sort:.6f} seconds | {count_sort:,} duplicates found")
        logger.info(f"Winner: {'SET' if time_set < time_sort else 'SORT'} (faster by {abs(time_set - time_sort):.6f} seconds)")
        logger.info("=" * 70)
        logger.info("")


# PYTHONIC: Use if __name__ guard to prevent code running at import time
if __name__ == '__main__':
    main()

print("""
  Memory strategy:
    4 GB RAM  → Prefer sort-and-scan (avoids loading all emails into a set)
    64 GB RAM → Prefer set approach  (faster O(n) vs O(n log n), RAM isn't the constraint)
""")