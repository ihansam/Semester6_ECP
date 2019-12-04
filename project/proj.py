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
    document = {}
    for name in file_names:                 # name: 각 파일 이름
        with open(PATH+name, 'r') as f:     
            document[name[:-4]] = f.read()  # 파일 이름에서 확장자 제거
    return document

def rm_exceptEng(dict_data):
    refinedoc = {}
    for filename, filedata in dict_data.items():
        refined = ""
        for i in filedata:                  # file data의 모든 문자에 대해
            if i.isalpha() or i == " ":     # 알파벳과 공백은 통과하고
                refined += i
            elif i == "\n":                 # 줄바꿈은 공백으로 치환하며
                refined += " "              # 그 외 문자는 제거한다
        refinedoc[filename] = refined
    return refinedoc

def get_splitDocs(dict_data):
    spldoc = {}
    for filename, filedata in dict_data.items():       
        spldoc[filename] = filedata.lower().split()     # 소문자로 바꾸고 list로 split
    return spldoc

def get_wordIndex(dict_data):
    wordindex = {}
    index = 0
    with open(STOPWORD, 'r') as sfile:      # Make stop words list
        stoplist = sfile.read().lower().split()
    for wordlist in dict_data.values():     # 각 word list의 모든 word에 대해
        for word in wordlist:               # 그 단어가 wordindex의 key로 추가되지 않았고, stop word list에 없다면
            if (word not in wordindex.keys()) and (word not in stoplist):
                wordindex[word] = index     # 그 단어를 key로, 현재 index를 value로 wordindex dictionary에 추가
                index += 1                  # 추가할 때마다 index 증가
    return wordindex

def get_wordFreq(dict_wordIndex, dict_data):
    allwordlist = []                        # 순서가 없는 wordindex dictionary를 index 순서의 list로 변환: allwordlist 
    for i in range(len(dict_wordIndex)):
        for word, index in dict_wordIndex.items():
            if i == index:
                allwordlist.append(word)
                break
    allwdfreq = {}
    for filename, filewordlist in dict_data.items():    # 각 파일의 word list에 대해
        filewdfreq = {}                                 # allwordlist의 각 word를 key로, 개수를 value로 하는 dictionary: filewdfreq
        for word in allwordlist:                        
            filewdfreq[word] = filewordlist.count(word)
        allwdfreq[filename] = filewdfreq
    return allwdfreq

def main():
    #step1
    variables['documents'] = load_data(PATH, file_names)
    variables['refined_docs'] = rm_exceptEng(variables['documents'])
    variables['split_docs'] = get_splitDocs(variables['refined_docs'])
    variables['word_index'] = get_wordIndex(variables['split_docs'])
    #step2
    variables['word_freq'] = get_wordFreq(variables['word_index'], variables['split_docs'])
    return variables
print(main())