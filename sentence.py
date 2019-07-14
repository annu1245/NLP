paragraph = "The words nowadays you probably heard of everywhere is Machine Learning, AI, Deep Learning, Blockchain. So, this blog is about what is exactly machine learning, how it has affected people lives in past decade."

sentence = paragraph.split('. ')
sent = []
for sen in sentence:
    sent.append(sen.split('. '))
print(sent)