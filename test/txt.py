import csv
import re


def modify_text():
    with open('/Users/yueli/Desktop/linux_share/2.8.0_stable_perf/perf/com/health_check_case1_cpp_mix_com.txt',
              "r+", ) as f:
        read_data = f.read()
        read_data_no_special = re.sub('[{}[\]\'-]', '', read_data)
        f.seek(0)
        f.write(read_data_no_special.replace(':', ','))


modify_text()

if __name__ == '__main__':
    inputFile = '/Users/yueli/Desktop/linux_share/2.8.0_stable_perf/perf/com/health_check_case1_cpp_mix_com.txt'
    outputFile = '/Users/yueli/Desktop/linux_share/2.8.0_stable_perf/perf/com/health_check_case1_cpp_mix_com.csv'
    row = []

    csvFile = open(outputFile, 'w', newline='')
    writer = csv.writer(csvFile)
    writer.writerow(row)
    lines = open(inputFile, 'r', encoding='utf-8', ).readlines()
    for line in lines:
        csvFile.write(line)
    csvFile.close()
