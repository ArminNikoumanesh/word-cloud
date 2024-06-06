stop_words = (
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'also', 'am', 'an', 'and', 'any', 'are', "aren't", 'as',
    'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', "can't", 'cannot',
    'com', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each',
    'else', 'ever', 'few', 'for', 'from', 'further', 'get', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'nor',
    'having', 'he', "he'd", "he'll", "he's", 'hence', 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself',
    'his', 'how', "how's", 'however', 'http', 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'r',
    'it', "it's", 'its', 'itself', 'just', 'k', "let's"'like', 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no',
    'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out',
    'over', 'own', 'same', 'shall',
    "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'since', 'so', 'some', 'such', 'than', 'that',
    "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'therefore', 'these', 'they',
    "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very',
    'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's",
    'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't",
    'www', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves')

punctuation = (
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
    ']',
    '^', '_', '`', '{', '|', '}', '~', '\\')

context = ".ph.d."

dic = {}


def remove_punctuations(word):
    if word[0] in punctuation:
        word = word.replace(word[0], '', 1)
    if word[-1] in punctuation:
        word_list = list(word)
        del word_list[-1]
        word = "".join(word_list)

    return word


words = context.split()
words = [x for x in words if x.lower() not in stop_words]

for i in range(len(words)):
    words[i] = remove_punctuations(words[i])

for each_word in words:
    word = each_word.lower()
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

print(dic)
