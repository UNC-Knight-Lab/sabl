from sabl.sabl import BarcodeSplitter
import numpy as np
import pandas as pd

# define sequences preceding the barcodes
backbones = ['CGTCCTGA', 'ACGTGTTC', 'TCTCGTCC', 'CACACGAG']
ref_barcodes = pd.read_excel("sample_data/reference_barcodes.xlsx")

# read in sequences and initialize barcode arrays
barcode = BarcodeSplitter(backbones, ref_barcodes)
barcode.read_sequences("sample_data/R1.txt")

# extract barcodes for each sequence and backbone
barcode.split_count()
barcode.export_results("sample_data/outputs")