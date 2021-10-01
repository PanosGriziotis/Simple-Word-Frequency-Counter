from pathlib import Path
import re


# 1 create a class and an initializer
class FrequenciesGenerator:
    def __init__(self, source_folder):
        self.source_folder = source_folder  # given folder path
        self.file_frequencies = {}  # initialised dictionary of a file's token frequencies
        self.total_frequencies = {}  # initialised dictionary of all files' token frequencies

    # 2 create a function that splits a text into a list of tokens

    def tokenize(self, text):
        return re.split(r'[\s.?,\-!)(:«»’"]+', text)

    # 3 create a function that saves the frequency of each token from a list in a dictionary

    def generate_frequencies(self, word_list):
        word_frequencies = {}
        for i in word_list:
            if i in word_frequencies:
                word_frequencies[i] += 1
            else:
                word_frequencies[i] = 1
        return word_frequencies

    # 4 create a function that a) reads each txt file from the folder directory and b) creates total and file frequency dictionaries of tokens

    def read_folder(self):
        files = Path(self.source_folder)
        for file in files.iterdir():

            if file.name.endswith('.txt'):
                with open(file, 'r', encoding="utf8") as reader:
                    read_file = reader.read()
                    tokenized_text = self.tokenize(read_file)

                    #  create nested dictionaries (file_frequencies) of each file
                    self.file_frequencies[file.name] = self.generate_frequencies(tokenized_text)
        self.total_frequencies = self.adding_dictionaries()
        return self.total_frequencies  # merged dictionary of all files' token-frequencies dictionaries

    # 4a function that merges nested dictionaries into one dictionary

    def adding_dictionaries(self):

        value_list = self.file_frequencies.values()  # list of all nested dictionaries

        for dictionary in value_list:
            for key, value in dictionary.items():
                if key in self.total_frequencies:
                    self.total_frequencies[key] += value
                else:
                    self.total_frequencies[key] = value
        return self.total_frequencies

    # 5 create a function that outputs a) the frequency of a given token (required argument) in total and b) in a given file (default argument)

    def get_frequency(self, token, file_name='default'):

        if 'default' != file_name:
            if file_name in self.file_frequencies:
                file_words = self.file_frequencies.get(file_name)
                if token in file_words:
                    return f' the word {token} appears {file_words[token]} times in {file_name}'
                else:
                    return f' word {token} not found in {file_name}'
            else:
                return f'{file_name} was not found'
        else:
            if token in self.total_frequencies:
                return f'the word {token} appears {self.total_frequencies[token]} times in total'
            else:
                return f'the word {token} appears 0 times in total'

    # 6 create a function that calculates a) the common tokens of two files and b) the similarity ratio of two given files

    def calculate_similarity(self, file_a, file_b):

        common_tokens = set()

        try:
            file_a_dict = self.file_frequencies.get(file_a)
            file_b_dict = self.file_frequencies.get(file_b)
            file_a_tokens = file_a_dict.keys()
            file_b_tokens = file_b_dict.keys()

            for token in file_a_tokens:
                if token in file_b_tokens:
                    common_tokens.add(token)
            file_similarity = len(common_tokens) / (len(file_a_tokens) + len(file_b_tokens))
        except AttributeError:
            return 'non valid file names'
        return f' {file_a} and {file_b} are {file_similarity * 100} % the same'
