import unittest
from uuid import UUID

from app.uuid_generator import UuidGenerator


def is_valid_uuid(string):
    try:
        UUID(string, version=4)
    except ValueError:
        return False

    return True


class TestUuidGenerator(unittest.TestCase):
    def test_generate(self):
        uuid = UuidGenerator.generate()

        self.assertTrue(is_valid_uuid(uuid))

if __name__ == '__main__':
    unittest.main()
