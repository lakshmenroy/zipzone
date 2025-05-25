import unittest
from src.huffman import HuffmanCoding

class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.huffman = HuffmanCoding()

    def test_encode_decode(self):
        text = "hello world"
        encoded, tree = self.huffman.encode(text)
        decoded = self.huffman.decode(encoded, tree)
        self.assertEqual(text, decoded)

    def test_empty_string(self):
        text = ""
        encoded, tree = self.huffman.encode(text)
        self.assertEqual(encoded, "")
        self.assertIsNone(tree)
        decoded = self.huffman.decode(encoded, tree)
        self.assertEqual(decoded, "")

    def test_single_character(self):
        text = "a"
        encoded, tree = self.huffman.encode(text)
        self.assertEqual(encoded, "0")
        decoded = self.huffman.decode(encoded, tree)
        self.assertEqual(decoded, text)

if __name__ == '__main__':
    unittest.main()