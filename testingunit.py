# Create a function that validates email addresses based on following set of rules:
# - Proper email format such as presence of “@”, no space in the address
# - Presence of valid email providers such as yahoo, gmail and outlook. Make sure there are no no disposable email providers such as yopmail.
# Write unit tests to validate different email addresses against the rules, including valid and invalid addresses (Use unittest module).
import re
import unittest

VALID_PROVIDERS = ['yahoo.com', 'gmail.com', 'outlook.com']
DISPOSABLE_PROVIDERS = ['yopmail.com']

def validate_email(email):
    """
    Validate email addresses based on specific rules.
    Parameters
    ----------
    email : str
        The email address to validate.

    Returns
    -------
    bool
        True if the email is valid, False otherwise.
    """
    if not isinstance(email, str) or ' ' in email:
        return False

    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        return False

    domain = email.split('@')[1]
    if domain in DISPOSABLE_PROVIDERS or domain not in VALID_PROVIDERS:
        return False

    return True


class TestValidateEmail(unittest.TestCase):

    def test_valid_emails(self):
        self.assertTrue(validate_email('test@yahoo.com'))
        self.assertTrue(validate_email('user@gmail.com'))
        self.assertTrue(validate_email('example@outlook.com'))

    def test_invalid_emails(self):
        self.assertFalse(validate_email('invalid@domain.com'))
        self.assertFalse(validate_email('user@yopmail.com'))
        self.assertFalse(validate_email('noatsign.com'))
        self.assertFalse(validate_email('invalid@domain.'))
        self.assertFalse(validate_email(' invalid@domain.com'))
        self.assertFalse(validate_email('invalid@domain.com '))

    def test_empty_email(self):
        self.assertFalse(validate_email(''))

    def test_space_in_email(self):
        self.assertFalse(validate_email('user @gmail.com'))
        self.assertFalse(validate_email('user@ gmail.com'))
        self.assertFalse(validate_email('user@ gmail .com'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            validate_email(5)
            validate_email(True)
    
if __name__ == '__main__':
    unittest.main()

# Design a function that takes a list of numerical data and performs calculations for mean,
# median and standard deviation. Write unit tests to verify the correctness of the statistical
# calculations for various inputs, including edge cases like an empty list or a list with one
# element (Use unittest module).

import numpy as np

def calculate_statistics(data):
    """
    Calculate mean, median, and standard deviation for a list of numerical data.

    Parameters
    ----------
    data : list of float
        The list of numerical data.

    Returns
    -------
    tuple of float
        A tuple containing mean, median, and standard deviation.
    """
    if not data:
        return (None, None, None)
    
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data, ddof=1)
    
    return (mean, median, std_dev)


class TestCalculateStatistics(unittest.TestCase):

    def test_statistics_with_multiple_elements(self):
        data = [1, 2, 3, 4, 5]
        mean, median, std_dev = calculate_statistics(data)
        self.assertAlmostEqual(mean, 3)
        self.assertAlmostEqual(median, 3)
        self.assertAlmostEqual(std_dev, 1.58, places=2)

    def test_statistics_with_one_element(self):
        data = [42]
        mean, median, std_dev = calculate_statistics(data)
        self.assertEqual(mean, 42)
        self.assertEqual(median, 42)
        self.assertIsNone(std_dev)

    def test_statistics_with_empty_list(self):
        data = []
        mean, median, std_dev = calculate_statistics(data)
        self.assertIsNone(mean)
        self.assertIsNone(median)
        self.assertIsNone(std_dev)

    def test_statistics_with_negative_numbers(self):
        data = [-1, -2, -3, -4, -5]
        mean, median, std_dev = calculate_statistics(data)
        self.assertAlmostEqual(mean, -3)
        self.assertAlmostEqual(median, -3)
        self.assertAlmostEqual(std_dev, 1.58, places=2)

    def test_statistics_with_mixed_numbers(self):
        data = [1, -1, 0, 2, -2]
        mean, median, std_dev = calculate_statistics(data)
        self.assertAlmostEqual(mean, 0)
        self.assertAlmostEqual(median, 0)
        self.assertAlmostEqual(std_dev, 1.58, places=2)
    
    def test_invlaid_input(self):
        with self.assertRaises(TypeError):
            data = ["1", "2", "3"]
            mean, median, std_dev = calculate_statistics(data)
            
if __name__ == '__main__':
    unittest.main()
