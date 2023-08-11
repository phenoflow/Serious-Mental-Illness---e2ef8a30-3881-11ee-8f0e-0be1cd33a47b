# Siobhan Reilly, Ivan Olier, Claire Planner, Tim Doran, David Reeves, Darren M Ashcroft, Linda Gask, Evangelos Kontopantelis, 2023.

import sys, csv, re

codes = [{"code":"E110.00","system":"readv2"},{"code":"E110000","system":"readv2"},{"code":"E110100","system":"readv2"},{"code":"E110200","system":"readv2"},{"code":"E110300","system":"readv2"},{"code":"E110400","system":"readv2"},{"code":"E110600","system":"readv2"},{"code":"E110z00","system":"readv2"},{"code":"E114.00","system":"readv2"},{"code":"E114.11","system":"readv2"},{"code":"E114000","system":"readv2"},{"code":"E114100","system":"readv2"},{"code":"E114200","system":"readv2"},{"code":"E114300","system":"readv2"},{"code":"E114500","system":"readv2"},{"code":"E114600","system":"readv2"},{"code":"E114z00","system":"readv2"},{"code":"E115.11","system":"readv2"},{"code":"E11y.00","system":"readv2"},{"code":"E11y000","system":"readv2"},{"code":"E11y100","system":"readv2"},{"code":"E11y300","system":"readv2"},{"code":"E11yz00","system":"readv2"},{"code":"Eu25000","system":"readv2"},{"code":"Eu25011","system":"readv2"},{"code":"Eu25012","system":"readv2"},{"code":"Eu30.00","system":"readv2"},{"code":"Eu30.11","system":"readv2"},{"code":"Eu30y00","system":"readv2"},{"code":"Eu30z00","system":"readv2"},{"code":"Eu31.11","system":"readv2"},{"code":"Eu31.12","system":"readv2"},{"code":"Eu31.13","system":"readv2"},{"code":"Eu33213","system":"readv2"},{"code":"Eu33312","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('serious-mental-illness-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["serious-mental-illness-smi-manicdepress---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["serious-mental-illness-smi-manicdepress---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["serious-mental-illness-smi-manicdepress---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
