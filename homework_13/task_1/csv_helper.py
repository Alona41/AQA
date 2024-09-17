import csv


file1 = 'C:/Users/cluba/Downloads/r-m-c.csv'
file2 = 'C:/Users/cluba/Downloads/random-michaels.csv'
result_file = 'result_your_second_name.csv'


def read_csv(file_path):

    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return list(reader)


def write_csv(file_path, data):

    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def remove_duplicates(file1, file2, result_file):

    data1 = read_csv(file1)
    data2 = read_csv(file2)


    combined_data = data1 + data2


    unique_data = []
    for row in combined_data:
        if row not in unique_data:
            unique_data.append(row)


    write_csv(result_file, unique_data)



remove_duplicates(file1, file2, result_file)

