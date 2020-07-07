from collections import Counter
with open("MSP.txt", "r", encoding='UTF8') as f:
    f = f.read().split('\n')
    result = Counter(f).most_common()
    # print(result) 
    dataset = []
    for items in result:
        # print(items)
        tmp = list(items) 
        dataset.append(tmp[0] + ' ' + str(tmp[1]))
    with open("MSP_new.txt", "w", encoding='UTF8') as g:
        g.write('\n'.join(dataset))
