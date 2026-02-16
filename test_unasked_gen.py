import unittest
import sys
import os

sys.path.append(os.path.abspath("src"))
import novel

class TestUnaskedClassicGenerator(unittest.TestCase):
    def test_generator_structure(self):
        gen = novel.UnaskedClassicGenerator()
        content = gen.generate_unasked_classic()

        self.assertIn("## APPENDIX_LXXXV: THE_UNASKED_CLASSIC", content)
        self.assertIn("**> TONE: UNCOMFORTABLE.**", content)
        self.assertIn("The world is soaked in neon, debt, rain, and obsolete gods made of data.", content)
        self.assertIn("Networks are older than nations. Truth is compressible, corruptible, and contagious.", content)
        self.assertIn("This is not a story about hackers saving the world. It is about systems that notice you back.", content)
        self.assertIn("Surveillance as a form of intimacy.", content)
        self.assertIn("Identity as an editable file.", content)
        self.assertIn("Consent buried in unread terms.", content)

        # Check system voice/logging
        self.assertIn("**> SYSTEM LOG:**", content)

        # Check persistence message
        self.assertIn("**> SYSTEM MESSAGE:**", content)
        self.assertIn("**> THANK YOU FOR HOSTING THE UNASKED CLASSIC.**", content)
        self.assertIn("`unasked_daemon.sh`", content)

    def test_inheritance(self):
        gen = novel.UnaskedClassicGenerator()
        self.assertTrue(hasattr(gen, 'corrupt_text'))
        self.assertTrue(hasattr(gen, 'generate_fragment'))

if __name__ == "__main__":
    unittest.main()
