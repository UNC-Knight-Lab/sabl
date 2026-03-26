import pandas as pd
import numpy as np
import os

class BarcodeSplitter:

    def __init__(self, backbones, ref_barcodes):
        self.backbones = backbones
        self.ref_barcodes = ref_barcodes
        self.dna_sequences = []
        self.barcodes = []

    def _sequence_match(self, seq, backbone):
        j = 0
        # cut anything that is too small (ideal len = 150nt)
        if len(seq) < 160:
            return "0000"
        else:
            for i in range(50,100):
                # check match at each position
                if (seq[i] == backbone[j]):
                    if (seq[i + 1] == backbone[j + 1]):
                        if (seq[i + 2] == backbone[j + 2]):
                            if (seq[i + 3] == backbone[j + 3]):
                                if (seq[i + 4] == backbone[j + 4]):
                                    if (seq[i + 5] == backbone[j + 5]):
                                        if (seq[i + 6] == backbone[j + 6]):
                                            if (seq[i + 7] == backbone[j + 7]):
                                                # success returns barcode
                                                return (seq[i + 8]) + (seq[i + 9]) + (seq[i + 10]) + (seq[i + 11])
            return ('NNNN')
    
    # count sequence failures
    def _count_barcodes_with_N(self,barcodes):
        return sum('N' in bc for bc in barcodes)

    # count size failures
    def _count_barcodes_with_0(self,barcodes):
        return sum('0' in bc for bc in barcodes)
    
    def read_sequences(self, file_path):
        self.num_backbones = len(self.backbones)

        # read in input file and extract DNA sequences
        with open(file_path, 'r') as f:
            lines = f.readlines()

            # extract DNA sequences
            for i in range(1, len(lines), 4):
                sequence = lines[i].strip()
                self.dna_sequences.append(sequence)

        self.num_seq = len(self.dna_sequences)

        for i in range(self.num_backbones):
            self.barcodes.append(np.empty(self.num_seq, dtype="U4"))

        self.num_ref_barcodes = len(self.ref_barcodes)
    
    def split_count(self):

        for i in range(self.num_seq):
            for j in range(self.num_backbones):
                self.barcodes[j][i] = self._sequence_match(self.dna_sequences[i], self.backbones[j])
        
        # concatenate the four arrays for each sequence
        self.concatenated_barcodes = [
            ''.join(self.barcodes[j][i] for j in range(self.num_backbones))
            for i in range(self.num_seq)
        ]

        # store pulled barcode sequences in NumPy array
        self.match_count = np.zeros((self.num_ref_barcodes,), dtype=int)

        # count frequency of each barcode
        for i in range(len(self.concatenated_barcodes)):
            for j in range(len(self.ref_barcodes)):
                if self.concatenated_barcodes[i] == self.ref_barcodes.iloc[j,0]:
                    self.match_count[j] += 1
                    break
    
    def export_results(self, folder):
        size_fail_count = self._count_barcodes_with_0(self.concatenated_barcodes)
        size_fail_percentage = (size_fail_count / self.num_seq) * 100

        sequence_fail_count = self._count_barcodes_with_N(self.concatenated_barcodes)
        sequence_fail_percentage = (sequence_fail_count / self.num_seq) * 100

        fail_count = sequence_fail_count + size_fail_count
        fail_percentage = (fail_count / self.num_seq) * 100

        success_count = self.num_seq - fail_count
        success_percentage = (success_count / self.num_seq) * 100

        print(f"Total sequences: {self.num_seq}")
        print(f"Total success: {success_count} ({success_percentage}%)")
        print(f"Total fail: {fail_count} ({fail_percentage}%)")
        print(f"Size fail: {size_fail_count} ({size_fail_percentage}%)")
        print(f"Sequence match fail: {sequence_fail_count} ({sequence_fail_percentage}%)")

        # export the count values to a QC txt file
        qc_file_path = os.path.join(folder, f"QC.txt")
        with open(qc_file_path, 'w') as QC_file:
            QC_file.write(f"Total sequences: {self.num_seq}\n")
            QC_file.write(f"Total success: {success_count} ({success_percentage}%)\n")
            QC_file.write(f"Total fail: {fail_count} ({fail_percentage}%)\n")
            QC_file.write(f"Size fail: {size_fail_count} ({size_fail_percentage}%)\n")
            QC_file.write(f"Sequence match fail: {sequence_fail_count} ({sequence_fail_percentage}%)\n")

        print(f"Text file saved to: {qc_file_path}")

        df = pd.DataFrame({'Concatenated Barcodes': self.concatenated_barcodes})
        df.to_excel(os.path.join(folder, f"barcodes.xlsx"), index=False)
        print(f"Excel file saved to: {os.path.join(folder, f'barcodes.xlsx')}")

        # create a DataFrame with ref_barcodes and match_count as columns
        result_df = pd.DataFrame({'Ref Barcodes': self.ref_barcodes.iloc[:, 0], 'Match Count': self.match_count})
        excel_file_path = os.path.join(folder, f"frequency.xlsx")
        result_df.to_excel(excel_file_path, index=False)
        print(f"Excel file with match counts saved to: {excel_file_path}")