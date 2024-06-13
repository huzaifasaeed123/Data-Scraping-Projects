import csv
pmc = []
board = []
with open("collective.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        board.append(row)


with open("pmcpassed.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        pmc.append(row)

print(len(pmc))
print(len(board))


for r in pmc:
    for i in board:
        if r[0].lower().replace(' ','') == i[1].lower().replace(' ','') and r[1].lower().replace(' ','') == i[2].lower().replace(' ',''):

            row = [r,i]

            with open('compared_data_1.csv','a',newline='') as new:
                res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                res_writer.writerow(row)
