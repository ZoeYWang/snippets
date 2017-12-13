# this script is to extract interested reads from fastq file

import sys
import gzip

def get_reads(file1,string1,file2):
    new_file = open(file2, "r+")
    with gzip.open(file1, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if line.startswith(string1):
                new_file.write(lines[i-1])
                new_file.write(lines[i])
                new_file.write(lines[i+1])
                new_file.write(lines[i+2])



if __name__ == '__main__':
    file1 = sys.argv[1] # read in fastq file
    string1 = sys.argv[2] # start with string, usually primer
    file2 = sys.argv[3] # write to fastq file
    get_reads(file1, string1, file2)
