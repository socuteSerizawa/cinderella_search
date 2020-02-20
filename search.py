from write_csv import CinderellaWriteCsv

list_sample = []

list_sample.append({'a':10, 'b':20, 'c':30})
list_sample.append({'a':11, 'b':22, 'c':33})

cin_csv = CinderellaWriteCsv('./sample.csv', list_sample[0].keys())

cin_csv.add_columns(list_sample)