import unittest
from pathlib import Path


class TestIndex(unittest.TestCase):
    def test_index_links_all_tools(self):
        readme = Path(__file__).parents[1].joinpath('README.md').read_text(encoding='utf-8')
        expected = {
            'http-security-headers-checker', 'tls-certificate-inspector', 'dns-security-checker',
            'password-strength-checker', 'jwt-decoder', 'phishing-url-analyzer', 'secret-scanner',
            'file-integrity-checker', 'auth-log-analyzer', 'osv-dependency-scanner',
            'cors-policy-checker', 'subnet-calculator', 'security-txt-checker'
        }
        for slug in expected:
            self.assertIn(f'/{slug})', readme)


if __name__ == '__main__':
    unittest.main()
