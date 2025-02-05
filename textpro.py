def sentence_maker(phrase):
    interrogatives = ('how', 'what', 'when', 'where', 'why', 'who')
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return '{}?'.format(capitalized)
    else:
        return '{}.'.format(capitalized)
    

results = []
while True:
    user_input = input('Say something: ')
    if user_input == '':
        break
    else:
        results.append(sentence_maker(user_input))

print(' '.join(results))
