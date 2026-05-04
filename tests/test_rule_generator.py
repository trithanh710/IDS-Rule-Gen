import unittest
from src.rule_generator import SuricataGenerator


class TestSuricataGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = SuricataGenerator(start_sid=1000001)

    def test_generate_rule_format(self):
        """
        Kiểm tra rule có đúng format Suricata hay không
        """
        ip = "1.2.3.4"
        description = "Cobalt Strike"
        sid = 1000001

        rule = self.generator.generate_rule(ip, description, sid)

        expected = (
            "alert ip $EXTERNAL_NET 1.2.3.4 -> $HOME_NET any "
            "(msg:'Blacklisted IP: Cobalt Strike'; sid:1000001; rev:1;)"
        )

        self.assertEqual(rule, expected)

    def test_sid_auto_increment(self):
        """
        Kiểm tra SID có tự động tăng khi generate nhiều rule
        """
        entries = [
            {"ip": "1.1.1.1", "description": "Test 1"},
            {"ip": "2.2.2.2", "description": "Test 2"},
        ]

        rules = self.generator.generate_rules(entries)

        # Kiểm tra số lượng rule
        self.assertEqual(len(rules), 2)

        # Kiểm tra SID trong từng rule
        self.assertIn("sid:1000001;", rules[0])
        self.assertIn("sid:1000002;", rules[1])


if __name__ == "__main__":
    unittest.main()
