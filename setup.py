from setuptools import setup, find_packages

setup(
    name="sabl",
    version="0.1.0",
    description="Sequence Assessment for Barcode Libraries (SABL) is a Python package designed to analyze DNA sequences and extract barcodes based on specified backbones. It provides functionality to read sequences, identify barcodes, count matches against reference barcodes, and export results in various formats.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Kevin Coghlan",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "numpy",
        "pandas"
    ],
)