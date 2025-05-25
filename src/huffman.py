import heapq
from collections import defaultdict
from typing import Dict, Tuple, Optional


class HuffmanNode:
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self):
        self.codes = {}
        self.reverse_codes = {}

    def build_frequency_table(self, text: str) -> Dict[str, int]:
        """Build frequency table for characters in the input text."""
        return defaultdict(int, {char: text.count(char) for char in set(text)})

    def build_huffman_tree(self, freq_table: Dict[str, int]) -> HuffmanNode:
        """Build Huffman tree from frequency table."""
        heap = []
        for char, freq in freq_table.items():
            heapq.heappush(heap, HuffmanNode(char, freq))

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            internal = HuffmanNode(None, left.freq + right.freq)
            internal.left = left
            internal.right = right
            heapq.heappush(heap, internal)

        return heap[0]

    def build_codes(self, root: HuffmanNode, current_code: str = "") -> None:
        """Generate Huffman codes for each character."""
        if root is None:
            return
        if root.char is not None:
            self.codes[root.char] = current_code or "0"
            self.reverse_codes[current_code] = root.char
            return
        self.build_codes(root.left, current_code + "0")
        self.build_codes(root.right, current_code + "1")

    def encode(self, text: str) -> Tuple[str, HuffmanNode]:
        """Encode the input text using Huffman coding."""
        if not text:
            return "", None
        freq_table = self.build_frequency_table(text)
        root = self.build_huffman_tree(freq_table)
        self.codes = {}
        self.build_codes(root)
        encoded = "".join(self.codes[char] for char in text)
        return encoded, root

    def decode(self, encoded: str, root: HuffmanNode) -> str:
        """Decode the encoded text using the Huffman tree."""
        if not encoded or not root:
            return ""
        decoded = []
        current = root
        for bit in encoded:
            current = current.left if bit == "0" else current.right
            if current.char is not None:
                decoded.append(current.char)
                current = root
        return "".join(decoded)