import pickle
import os
import zipfile
from typing import Tuple
from src.huffman import HuffmanCoding, HuffmanNode

class FileHandler:
    @staticmethod
    def read_file(file_path: str) -> str:
        """Read text from a file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise Exception(f"Error reading file {file_path}: {str(e)}")

    @staticmethod
    def write_file(file_path: str, content: str) -> None:
        """Write text to a file."""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            raise Exception(f"Error writing file {file_path}: {str(e)}")

    @staticmethod
    def save_compressed(file_path: str, encoded: str, tree: HuffmanNode) -> None:
        """Save compressed data and Huffman tree in a .zip file."""
        try:
            zip_path = os.path.splitext(file_path)[0] + ".zip"
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                # Save encoded data
                zf.writestr("encoded.bin", encoded.encode('utf-8'))
                # Save Huffman tree
                tree_data = pickle.dumps(tree)
                zf.writestr("tree.pkl", tree_data)
        except Exception as e:
            raise Exception(f"Error saving compressed file {zip_path}: {str(e)}")

    @staticmethod
    def load_compressed(file_path: str) -> Tuple[str, HuffmanNode]:
        """Load compressed data and Huffman tree from a .zip file."""
        try:
            with zipfile.ZipFile(file_path, 'r') as zf:
                encoded = zf.read("encoded.bin").decode('utf-8')
                tree_data = zf.read("tree.pkl")
                tree = pickle.loads(tree_data)
                return encoded, tree
        except Exception as e:
            raise Exception(f"Error loading compressed file {file_path}: {str(e)}")