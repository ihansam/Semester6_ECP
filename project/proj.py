from os import listdir

PATH = './data/'
STOPWORD = "./stopword/stopwords.txt"
file_names = listdir(PATH)
variables={
    'documents':{},
    'refined_docs':{},
    'split_docs':{},
    'word_index':{},
    'word_freq':{},
}

def load_data(PATH,file_names):
    pass

def rm_exceptEng(dict_data):
    pass

def get_splitDocs(dict_data):
    pass

def get_wordIndex(dict_data):
    pass

def get_wordFreq(dict_wordIndex, dict_data):
    pass


def main():
    #step1
    variables['documents'] = load_data(PATH, file_names)
    variables['refined_docs'] = rm_exceptEng(variables['documents'])
    variables['split_docs'] = get_splitDocs(variables['refined_docs'])
    variables['word_index'] = get_wordIndex(variables['split_docs'])
    #step2
    variables['word_freq'] = get_wordFreq(variables['word_index'], variables['split_docs'])
    
    return variables
