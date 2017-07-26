import unittest
from unittest.mock import patch

from app.uuid_generator import UuidGenerator


def generate_mocked_uuid():
    return 'mocked_uuid'


class TestUuidGenerator(unittest.TestCase):
    @patch('uuid.uuid4', generate_mocked_uuid)
    def test_generate(self):
        uuid = UuidGenerator.generate()

        self.assertEqual(uuid, 'mocked_uuid')

if __name__ == '__main__':
    unittest.main()
