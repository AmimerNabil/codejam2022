import csv


def getTables(csvreader):
    tables = []
    table = []
    for rows in csvreader:
        tableFound = False
        if len(rows) != 0:
            for cells in rows:
                if 'table' in cells.lower():
                    tableFound = True
                    tables.append(table)
                    table = []

            if not tableFound:
                table.append(rows)

    tables.append(table)
    return tables[1:]

# print(getTables(csvreader)[1])


# triggerwords
triggerWords = ['oral', 'presentation', 'component', 'deliverable', 'exam', 'assignment', 'portfolio', 'paper', 'test',
                'final', 'midterm', 'essay',
                'report', 'lab', 'workshop', 'webwork', 'topic', 'quiz', 'presentation']

# date
months = [
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
]

monthsAbbr = [
    'jan',
    'feb',
    'mar',
    'apr',
    'may',
    'jun',
    'jul',
    'aug',
    'sep',
    'oct',
    'nov',
    'dec'
]


def getDates(filename):
    file = open(filename + '.csv')
    csvreader = csv.reader(file)

    dates = {}
    for table in getTables(csvreader):
        if len(table) != 0:
            header = table[0]
            trigger = False
            triggerType = ""
            for cidx, cells in enumerate(header):
                words = cells.split()
                for word in words:
                    if word.lower() in triggerWords:
                        trigger = True
                        triggerType = cells

            if trigger:
                d = []
                for idx, row in enumerate(table[1:]):
                    for cells in row:
                        words = cells.split()
                        for word in words:
                            if (word.lower() in months) or (word.lower() in monthsAbbr):
                                d.append(cells)

                    if len(d) != 0:
                        key = triggerType + str(idx + 1)
                        dates[key] = d[-1]

    file.close()
    return dates
