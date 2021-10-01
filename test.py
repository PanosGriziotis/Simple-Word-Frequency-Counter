from frequency_counter import FrequenciesGenerator as FG

test = FG('test_data_Μ901_final_project')
test.read_folder()
print(test.get_frequency('αλλά', '35406.pdf.txt'))
print(test.calculate_similarity('35406.pdf.txt', 'Handout 01. Decibels.doc.txt'))
