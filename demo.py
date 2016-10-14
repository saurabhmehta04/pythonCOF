import csv


def main():
    print("Parsing csv file")
    with open('demo.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            print(', '.join(row))

if __name__ == '__main__':
    main()
