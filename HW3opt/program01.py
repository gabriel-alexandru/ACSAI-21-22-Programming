def sortDict(dictionary, n):
    # Obtain the tuples by sorting the dictionary in crescent order.
    for tmp in dictionary:
        dictionary[tmp] = sorted(dictionary[tmp], key=str.lower)
    sortedTuples = sorted(dictionary.items(), key=lambda x: x[0], reverse=False)

    if len(sortedTuples) < n:
        return sortedTuples
    else:
        return sortedTuples[-n:]

def generateFrequenciesDictionary(text, min, max):
    tmp = {}
    text_len = len(text)
    for i in range(text_len - min + 1):
        for j in range(min, max + 1):
            if i+j == text_len + 1:
                break
            substr = text[i:i+j]
            if substr not in tmp:
                tmp[substr] = 1
            else:
                tmp[substr] += 1
    return tmp

def generateFrequenciesTuples(dict):
    frequencies = {}
    keys = dict.keys()
    for key in keys:
        if dict[key] in frequencies:
            frequencies[dict[key]].append(key)
        else:
            frequencies[dict[key]] = [key]
    return frequencies

def ex1(text_file, min_len, max_len, n):
    file = open(text_file, "r")
    text = file.read().replace("\n", "")
    freq_dict = generateFrequenciesDictionary(text, min_len, max_len)
    frequencies = generateFrequenciesTuples(freq_dict)
    return sortDict(frequencies, n)


if __name__ == '__main__':
    pass