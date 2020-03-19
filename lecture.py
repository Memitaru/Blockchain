
'''
hash('key') --> integer

hash(' this is a very long string') --> bc129d1

JSON can store anything besides functions and can be stringified (serializing data)

"{\"key\": value}"

If you stringify it you can hash it

'''

hashlib.sha246({index, timestamp, transactions: [], proof})

chain = [
    {index, timestamp, transactions: [], proof},
    {index, timestamp, transactions: [], revHash, proof},
    {index, timestamp, transactions: [], revHash, proof},
]