from frequency_counter import FrequenciesGenerator as FG

# insert path of the folder with text files
test = FG('test_data')
test.read_folder()
print(test.get_frequency('αλλά', '35406.pdf.txt'))
print(test.calculate_similarity('35406.pdf.txt', 'Handout 01. Decibels.doc.txt'))
