import json


# parse json in un dizionario
with open("/{PATH}/progetti_studio/python_backend_automation/littleJson.json") as g:
    data_dic = json.load(g)
    # print(data[0]['postId'])
    # cicla su tutto la lista e stampa il dizionario con il valore di una data chiave
    print(type(data_dic))
    # print(data_dic)
    #print('stampa markers:\n', data_dic['markers'])
    #print('stampa finders:\n', data_dic['finders'])
    print(data_dic)
    for i in data_dic['markers']:
        if i['name'] == 'Rixos The Palm Dubai':
            print(i['location'])
    for i in data_dic['finders']:
        if i['name'] != 'OpperMadeotel':
            print(i['location'])


# parse json in una lista
with open("/{PATH}/progetti_studio/python_backend_automation/exJson.json") as f:
    data = json.load(f)
    # print(data[0]['postId'])
    # cicla su tutto la lista e stampa il dizionario con il valore di una data chiave
    print(type(data))
    for i in data:
        if i['email'] == 'Dexter.Pacocha@lauren.biz':
            print(i)
            print(i['id'])  # 397
