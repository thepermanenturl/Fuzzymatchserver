from fuzzywuzzy import process

def Fuzzfun(d):
    true=True
    false=False
    val = []
    header = []
    desc = []
    sugg = []
    for i in d['train_fields']:
        val.append(i['example_values'])
        header.append(i['header'])
        desc.append(i['description'])
        sugg.append(i['fuzzy_suggestions'])

    chead = []
    cval = []
    for i in d['test_fields']:
        cval.append(i['sample values'])
        chead.append(i['header'])

    m1str = []
    for i in range(len(val)):
        label = ""
        for j in val[i]:
            label = label + " " + j
        label = label + " " + header[i] + " " + desc[i]
        for j in sugg[i]:
            label += " " + j
        m1str.append(label.lower())

    m2str = []
    for i in range(len(chead)):
        cand = chead[i]
        for j in cval[i]:
            cand += " " + j
        m2str.append(cand.lower())

    match = []
    for i in range(len(m1str)):
        # for j in range(len(m2str)):
        match.append([d['train_fields'][i]['header'], process.extractOne(m1str[i], m2str)])

    dback = {}
    for i in range(len(chead)):
        if i < len(match):
            dback[chead[i]] = {"nearest_match": match[i][0], "score": float(match[i][1][1]) / 100}
        else:
            dback[chead[i]] = {"nearest_match": "", "score": 0}

    return dback