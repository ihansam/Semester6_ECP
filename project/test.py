import ast

with open("answer.txt", 'r') as af:
    documents = af.readline().rstrip()
    refined_docs = af.readline().rstrip()
    split_docs = af.readline().rstrip()
    word_index = af.readline().rstrip()
    word_freq = ast.literal_eval(af.readline().rstrip())

with open("test.txt", 'r') as rf:
    dic = ast.literal_eval(rf.read())

doc = str((dic['documents']))
refdoc = str(dic['refined_docs'])
spdoc = str(dic['split_docs'])
wdidx = str(dic['word_index'])
_100 = list(dic['word_freq']['100lines_short_adventuresOfHuckleberryFinn_MarkTwain'].values())
_10 = list(dic['word_freq']['10lines_emma_JaneAusten'].values())
_98 = list(dic['word_freq']['98lines_short_annaKarenina_LeoTolstoy'].values())
_99 = list(dic['word_freq']['99lines_short_aTaleOfTwoCities_CharlesDickens'].values())

print(documents == doc)
print(refined_docs == refdoc)
print(split_docs == spdoc)
print(word_index == wdidx)
print()
print(_100 == word_freq['100lines_short_adventuresOfHuckleberryFinn_MarkTwain'])
print(_10 == word_freq['10lines_emma_JaneAusten'])
print(_98 == word_freq['98lines_short_annaKarenina_LeoTolstoy'])
print(_99 == word_freq['99lines_short_aTaleOfTwoCities_CharlesDickens'])