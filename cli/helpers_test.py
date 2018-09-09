import unittest
import os.path as path
import os
import tempfile
from helpers import get_root

class HelperTests(unittest.TestCase):

	def test_getRoot(self):

		# Set up temporary directory context manager to test in
		with tempfile.TemporaryDirectory() as temp_dir:

			# Returns False when no config file exists
			self.assertEqual(get_root(temp_dir), False)

			# Create markdone config file
			with open(path.join(temp_dir,'.markdone'), 'w'):
				
				# Returns current directory if config is in it
				self.assertEqual(get_root(temp_dir), temp_dir)

				# Add child directory
				child_dir = path.join(temp_dir, 'child_dir')
				os.makedirs(child_dir)
				
				# Returns parent when called from empty child made above
				self.assertEqual(get_root(child_dir), temp_dir)
					
if __name__ == '__main__':
    unittest.main()