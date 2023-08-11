# Siobhan Reilly, Ivan Olier, Claire Planner, Tim Doran, David Reeves, Darren M Ashcroft, Linda Gask, Evangelos Kontopantelis, 2023.

import sys, csv, re

codes = [{"code":"E120.00","system":"readv2"},{"code":"E121.00","system":"readv2"},{"code":"E123.00","system":"readv2"},{"code":"E12y.00","system":"readv2"},{"code":"E12yz00","system":"readv2"},{"code":"E12z.00","system":"readv2"},{"code":"E133.00","system":"readv2"},{"code":"E134.00","system":"readv2"},{"code":"Eu22011","system":"readv2"},{"code":"Eu22012","system":"readv2"},{"code":"Eu22015","system":"readv2"},{"code":"Eu22300","system":"readv2"},{"code":"Eu22y12","system":"readv2"},{"code":"Eu23312","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('serious-mental-illness-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["serious-mental-illness-smi-paranoia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["serious-mental-illness-smi-paranoia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["serious-mental-illness-smi-paranoia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
