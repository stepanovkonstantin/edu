# documents_input = open('documents.txt', 'r')
# documents = []
# for line in documents_input.readlines():
#     linenoends = line.replace('\n','')
#     doc_split = list(linenoends.split(','))
#     doc_dict = dict(type=doc_split[0], number=doc_split[1], name=doc_split[2])
#     documents.append(doc_dict)
# # print(documents)
# documents_input.close()
#
# directories_input = open('directories.txt', 'r')
# directories = {}
# for line in directories_input.readlines():
#     linenoends = line.replace('\n','')
#     dir_split = list(linenoends.split(','))
#     directories[dir_split[0]] = dir_split[1:]
# # print(directories)
# directories_input.close()

documents_list = [
    {"type": "passport", "number": "2207 876234", "name": "Vasya Pupkin"},
    {"type": "invoice", "number": "11-2", "name": "Gena Bukin"},
    {"type": "insurance", "number": "10006", "name": "Pavel Dudkin"},
    {"type": "passport", "number": "4521 123456", "name": "Konstantin Stepanov"}
]

directories_list = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': ['4521 123456']
}

doc_file = 'documents_tool/saved/documents.txt'
documents_input = open(doc_file, "w")
for document in documents_list:
    wline = document["type"] + "," + document["number"] + "," + document["name"] + "\n"
    print(wline)
    documents_input.write(wline)
documents_input.close()

dir_file = 'documents_tool/saved/directories.txt'
directories_input = open(dir_file, "w")
for dir_num, dir_values in directories_list.items():
    doc_str = ''
    for doc_num in dir_values:
        doc_str = doc_str + "," + doc_num
    wline = dir_num + doc_str + "\n"
    print(wline)
    directories_input.write(wline)
directories_input.close()
