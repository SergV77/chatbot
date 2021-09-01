import spacy

nlp = spacy.load("ru_core_news_lg")

#1 doc = nlp('Я собираюсь в Ленинград. Сейчас я лечу в Москву.')
#2 doc = nlp('Я хочу зеленое яблоко.')
#3 doc = nlp('Сильный шторм обрушился на пляж пошел. Начался дождь.')
doc = nlp('Кусок существительного - это фраза, в которой существительное является его заголовком.')


########### 4 ###############стр 66

for token in doc:
    if token.pos_ == 'NOUN':
        chunk = ''
        for w in token.children:
            if w.pos_ == 'DET' or w.pos_ == 'ADJ':
                chunk = chunk + w.text + ' '
        chunk = chunk + token.text
        print(chunk)


########### 3 ###############
# count = 0
# for sent in doc.sents:
#     if sent[len(sent)-2].pos_ == 'VERB':
#         count += 1
# print(count)


# for sent in doc.sents:
#     print([sent[i] for i in range(len(sent))])
# print([doc[i] for i in range(len(doc))])
#
# for i, sent in enumerate(doc.sents):
#     if i == 1 and sent[0].pos_ == 'PRON':
#         print('Следующее предложение начинается с местоимения.')


########### 2 ###############
# print([w for w in doc[3].children])


########### 1 ###############
# for token in doc:
#     # print(token.text, token.pos_, token.dep_)
#     print(token.head.text, token.dep_, token.text)

# for sent in doc.sents:
#     print([w.text for w in sent if w.dep_ == 'ROOT' or w.dep_ == 'obl'])

# for token in doc:
#     if token.ent_type != 0:
#         print(token.text, token.ent_type_)

# print([doc[i] for i in range(len(doc))])



