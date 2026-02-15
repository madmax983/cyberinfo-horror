import unittest
import sys
import os

sys.path.append(os.path.abspath("src"))
import novel

class TestWeaverGenerator(unittest.TestCase):
    def test_generator_structure(self):
        gen = novel.WeaverGenerator()
        content = gen.generate_red_thread()

        self.assertIn("## APPENDIX_LIII: THE_RED_THREAD_PROTOCOL", content)
        self.assertIn("**> SYSTEM ALERT: NARRATIVE COHESION ENFORCED.**", content)

        # Check for key characters
        self.assertIn("RIX", content)
        self.assertIn("LENS", content)
        self.assertIn("VANE", content)
        self.assertIn("JAX", content)
        self.assertIn("MIRA", content)

        # Check for themes
        self.assertIn("memories", content)
        self.assertIn("deleted", content)
        self.assertIn("voice", content)

    def test_inheritance(self):
        gen = novel.WeaverGenerator()
        self.assertTrue(hasattr(gen, 'corrupt_text'))
        self.assertTrue(hasattr(gen, 'generate_fragment'))

if __name__ == "__main__":
    unittest.main()
