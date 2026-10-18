import gzip
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAMERA = ROOT / 'firmware' / 'camera_recorder'
HAN = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')


class ArchiveTests(unittest.TestCase):
    def test_sketch_and_configuration(self):
        sketch = (CAMERA / 'camera_recorder.ino').read_text(encoding='utf-8')
        self.assertIn('#include "network_config.h"', sketch)
        self.assertIn('ssid = WIFI_SSID', sketch)
        self.assertIn('password = WIFI_PASSWORD', sketch)
        self.assertNotIn('const char* password = "', sketch)
        self.assertIn('YOUR_WIFI_PASSWORD', (CAMERA / 'network_config.example.h').read_text())
        self.assertFalse((CAMERA / 'network_config.h').exists())

    def test_embedded_web_interfaces(self):
        source = (CAMERA / 'camera_index.h').read_text(encoding='utf-8')
        arrays = re.findall(r'const uint8_t\s+(\w+)\[\]\s*=\s*\{(.*?)\};', source, re.S)
        self.assertTrue(arrays)
        for name, body in arrays:
            with self.subTest(name=name):
                raw = bytes(int(value, 16) for value in re.findall(r'0x([0-9a-fA-F]{2})', body))
                html = gzip.decompress(raw).decode('utf-8')
                self.assertIn('html', html.lower())
                self.assertIsNone(HAN.search(html))

    def test_cad_pair_structure(self):
        paths = list((ROOT / 'hardware' / 'cad').glob('*.dxf'))
        self.assertEqual(len(paths), 2)
        for path in paths:
            with self.subTest(path=path.name):
                lines = path.read_text(encoding='utf-8').splitlines()
                self.assertEqual(len(lines) % 2, 0)
                for line in lines[::2]:
                    int(line.strip())
                self.assertEqual(lines[-1].strip(), 'EOF')
                self.assertIn('fire-rescue-vehicle', lines)

    def test_public_text_and_artifacts(self):
        allowed = {'.md', '.h', '.cpp', '.ino', '.py', '.dxf'}
        for path in ROOT.rglob('*'):
            if '.git' in path.parts or '__pycache__' in path.parts:
                continue
            self.assertIsNone(HAN.search(path.relative_to(ROOT).as_posix()))
            if path.is_file() and path.suffix in allowed:
                self.assertIsNone(HAN.search(path.read_text(encoding='utf-8')))
        self.assertIn('not a verified complete', (ROOT / 'README.md').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
