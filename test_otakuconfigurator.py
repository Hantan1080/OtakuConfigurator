# test_otakuconfigurator.py
"""
Tests for OtakuConfigurator module.
"""

import unittest
from otakuconfigurator import OtakuConfigurator

class TestOtakuConfigurator(unittest.TestCase):
    """Test cases for OtakuConfigurator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OtakuConfigurator()
        self.assertIsInstance(instance, OtakuConfigurator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OtakuConfigurator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
