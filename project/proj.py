from os import listdir

PATH = './pracData/'                        # practice
STOPWORD = "./prcaStop/stopwords.txt"       # practice
file_names = listdir(PATH)
variables={
    'documents':{},
    'refined_docs':{},
    'split_docs':{},
    'word_index':{},
    'word_freq':{},
}

def load_data(PATH,file_names):
    document = {}
    for name in file_names:
        with open(PATH+name, 'r') as f:     
            document[name[:-4]] = f.read()  # 파일 이름에서 .txt 제거, file object read해 string value로 저장
    return document
print(load_data(PATH, file_names))          # test

def rm_exceptEng(dict_data):
    refinedoc = {}
    for filename, filedata in dict_data.items():
        new_content = ""
        for i in filedata:
            if i.isalpha() or i == " ":     # 알파벳과 공백은 통과
                new_content += i
            elif i == "\n":                 # 줄바꿈은 공백으로 치환
                new_content += " "          # (다른 문자는 제거)
        refinedoc[filename] = new_content
    return refinedoc
print(rm_exceptEng(load_data(PATH, file_names)))        # test

def get_splitDocs(dict_data):
    spldoc = {}
    for filename, filedata in dict_data.items():       # 소문자로 바꾸고 list로 split
        spldoc[filename] = filedata.lower().split()
    return spldoc
print(get_splitDocs(rm_exceptEng(load_data(PATH, file_names))))     # test

def get_wordIndex(dict_data):
    wordindex = {}
    index = 0
    with open(STOPWORD, 'r') as sfile:
        stoplist = sfile.read().split()     # make stop words list
    for wordlist in dict_data.values():
        for word in wordlist:               # 단어가 stop word list에 없고, word index dictionary key에도 없을 때
            if (word not in stoplist) and (word not in wordindex.keys()):
                wordindex[word] = index     # 그 단어를 key로, 현재 index를 value로 추가
                index += 1
    return wordindex
print(get_wordIndex(get_splitDocs(rm_exceptEng(load_data(PATH, file_names)))))      # test

def get_wordFreq(dict_wordIndex, dict_data):
    wdfreq = {}

    return wdfreq

def main():
    #step1
    variables['documents'] = load_data(PATH, file_names)
    variables['refined_docs'] = rm_exceptEng(variables['documents'])
    variables['split_docs'] = get_splitDocs(variables['refined_docs'])
    variables['word_index'] = get_wordIndex(variables['split_docs'])
    #step2
    variables['word_freq'] = get_wordFreq(variables['word_index'], variables['split_docs'])
    return variables
