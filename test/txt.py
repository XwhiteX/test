import csv
import re


def modify_text():
    with open('/Users/kkk/Desktop/health_check_case1_cpp_single_live.txt',
              "r+", ) as f:
        read_data = f.read()
        read_data_no_special = re.sub('[{}[\]\'-]', '', read_data)
        f.seek(0)
        f.write(read_data_no_special.replace(':', ','))


modify_text()



if __name__ == '__main__':
    inputFile = '/Users/kkk/Desktop/health_check_case1_cpp_single_live.txt'
    outputFile = '/Users/kkk/Desktop/health_check_case1_cpp_single_live.csv'
    row = []

    csvFile = open(outputFile, 'w', newline='')
    writer = csv.writer(csvFile)
    writer.writerow(row)
    lines = open(inputFile, 'r', encoding='utf-8', ).readlines()
    for line in lines:
        csvFile.write(line)
    csvFile.close()

    with open(outputFile) as f:
        # load_15m = []
        fileList = f.read().split()
        # fileList = f.read()
        for line in fileList['min15']:
            print(line)
            # load_15 = line.split('min15')
            # print(load_15)
        # reader = csv.DictReader(fileList)
        # min15 = [row['min15'] for row in reader]
        # for line in fileList:
        #     print(line)
    f.close()




