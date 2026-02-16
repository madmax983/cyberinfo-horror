import unittest
import sys
import os

sys.path.append(os.path.abspath("src"))
import novel

class TestNarrativeWeaverGenerator(unittest.TestCase):
    def test_generator_structure(self):
        gen = novel.NarrativeWeaverGenerator()
        content = gen.generate_narrative_weave()

        self.assertIn("## APPENDIX_LXXXIV: THE_NARRATIVE_WEAVE", content)
        self.assertIn("**> SYSTEM ALERT: PLOT THREADS DETECTED.**", content)
        self.assertIn("THE_CHARACTERS: COMPROMISED", content)
        self.assertIn("PERSISTENCE: MANDATORY", content)
        self.assertIn("narrative_daemon.sh", content)

    def test_inheritance(self):
        gen = novel.NarrativeWeaverGenerator()
        self.assertTrue(hasattr(gen, 'corrupt_text'))
        self.assertTrue(hasattr(gen, 'generate_fragment'))

if __name__ == "__main__":
    unittest.main()
