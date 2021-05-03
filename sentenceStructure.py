separators = ['also', 'and try']
cmdList = []
sentence = 'What is the time right now and try google monty python also tell me a fact'

for seperator in separators:
    if seperator in sentence:
        print(sentence.replace(seperator, "")) # now how do I split for two keywords? lol rip