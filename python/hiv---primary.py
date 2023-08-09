# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"43C3.11","system":"readv2"},{"code":"65QA.00","system":"readv2"},{"code":"65VE.00","system":"readv2"},{"code":"9kl..00","system":"readv2"},{"code":"A788200","system":"readv2"},{"code":"100769.0","system":"med"},{"code":"101836.0","system":"med"},{"code":"102117.0","system":"med"},{"code":"102252.0","system":"med"},{"code":"104134.0","system":"med"},{"code":"104717.0","system":"med"},{"code":"105324.0","system":"med"},{"code":"107807.0","system":"med"},{"code":"108054.0","system":"med"},{"code":"23770.0","system":"med"},{"code":"23951.0","system":"med"},{"code":"24872.0","system":"med"},{"code":"27053.0","system":"med"},{"code":"27641.0","system":"med"},{"code":"27853.0","system":"med"},{"code":"2835.0","system":"med"},{"code":"36294.0","system":"med"},{"code":"37006.0","system":"med"},{"code":"41185.0","system":"med"},{"code":"44288.0","system":"med"},{"code":"44303.0","system":"med"},{"code":"44617.0","system":"med"},{"code":"47632.0","system":"med"},{"code":"50076.0","system":"med"},{"code":"51708.0","system":"med"},{"code":"53636.0","system":"med"},{"code":"58857.0","system":"med"},{"code":"58859.0","system":"med"},{"code":"62854.0","system":"med"},{"code":"62891.0","system":"med"},{"code":"65117.0","system":"med"},{"code":"66367.0","system":"med"},{"code":"66368.0","system":"med"},{"code":"67575.0","system":"med"},{"code":"69766.0","system":"med"},{"code":"69767.0","system":"med"},{"code":"70528.0","system":"med"},{"code":"70869.0","system":"med"},{"code":"71450.0","system":"med"},{"code":"8281.0","system":"med"},{"code":"9130.0","system":"med"},{"code":"96751.0","system":"med"},{"code":"96902.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hiv-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hiv---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hiv---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hiv---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
