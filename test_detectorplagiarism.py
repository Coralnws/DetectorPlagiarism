# test_detectorplagiarism.py
"""
Tests for DetectorPlagiarism module.
"""

import unittest
from detectorplagiarism import DetectorPlagiarism

class TestDetectorPlagiarism(unittest.TestCase):
    """Test cases for DetectorPlagiarism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DetectorPlagiarism()
        self.assertIsInstance(instance, DetectorPlagiarism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DetectorPlagiarism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
