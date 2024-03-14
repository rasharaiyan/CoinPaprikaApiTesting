import unittest

if __name__ == "__main__":
    # Define the directory containing the tests.
    test_dir = '.'
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir=test_dir, pattern="test_*.py")

    # Run the tests
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
