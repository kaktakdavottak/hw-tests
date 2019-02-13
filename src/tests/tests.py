import unittest
from src.helpers.config import Config, WINDOWS


class MyTest(unittest.TestCase):
    def test1_get_verbosity_level(self):
        self.assertRaises(TypeError, Config.get_verbosity_level(), (None, False))

    def test2_get_verbosity_level(self):
        self.assertEqual(Config.get_verbosity_level(),
                         'critical, error, warning, info, debug')
        self.assertEqual(Config.get_verbosity_level(level='critical',
                                                    text=False), 50)
        self.assertEqual(Config.get_verbosity_level(level='error',
                                                    text=False), 40)
        self.assertEqual(Config.get_verbosity_level(level='warning',
                                                    text=False), 30)
        self.assertEqual(Config.get_verbosity_level(level='info',
                                                    text=False), 20)
        self.assertEqual(Config.get_verbosity_level(level='debug',
                                                    text=False), 10)

    def test3_get_verbosity_level(self):
        self.assertIsInstance(Config.get_verbosity_level(), str)
        self.assertIsInstance(Config.get_verbosity_level(level=not None), int)

    def test4_get_windows_system_disk(self):
        if not WINDOWS:
            self.assertRaises(EnvironmentError)
        else:
            self.assertEqual(Config.get_windows_system_disk(), 'C:')


if __name__ == '__main__':
    unittest.main()
