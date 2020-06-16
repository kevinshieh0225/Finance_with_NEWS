from bert_serving.client import BertClient
bc = BertClient()
hi = bc.encode(['[CLS]你好我要吃水果[SEP]'])
print(hi)
print(hi.shape)
print(type(hi))