# import sys
import csv
from itertools import islice

# input_tsv = csv.reader(sys.stdin, dialect=csv.excel_tab)
# output_csv = csv.writer(sys.stdout, dialect=csv.excel)
#
# for row in input_tsv:
#     output_csv.writerow(row)


# with open('sample.tsv', 'r') as inp_tsv:
#     inp_reader = csv.reader(inp_tsv, dialect=csv.excel_tab)
#     inp_data = [line for line in inp_reader]
#     print(inp_data)
#
# with open('output.csv', 'w') as out_csv:
#     out_writer = csv.writer(out_csv, quotechar='', quoting=csv.QUOTE_NONE)
#     out_writer.writerows(inp_data)
input_tsv_file = 'C:\zData\Work\ESSP\gbif\GBIF-Master.csv'
output_csv_file = 'C:\zData\Work\ESSP\gbif\out.csv'
with open(output_csv_file, 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile, dialect=csv.excel)
    with open(input_tsv_file, encoding='utf8') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        # reader = csv.DictReader(tsvfile, dialect=csv.excel_tab)
        for row in reader:
            writer.writerow(row)
with open(output_csv_file, 'r', newline='') as csvfile:
    for line in islice(csvfile, 10):
        print(line)
