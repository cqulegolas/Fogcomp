import contractInit
with open('userRegist.txt') as f:   
    info = f.read()


# #开始创建一个交易
# address = contractInit.wallet_address
# key = contractInit.wallet_private_key
# nonce = contractInit.w3.eth.getTransactionCount(address)
# print(nonce)
# #选择要调用的函数，并从read传入函数输入值
# txn = contractInit.contract.functions.userRegist(info).buildTransaction({
#    'nonce':nonce,
#    'gas': 3000000,
#    'chainId': 3,
#    'gasPrice': contractInit.w3.toWei('10', 'gwei'),
#    })
# signed_txn = contractInit.w3.eth.account.signTransaction(txn, key)
# print(signed_txn.hash)
# print(signed_txn.rawTransaction)

# #原始交易发送
# tmp = contractInit.w3.eth.sendRawTransaction(signed_txn.rawTransaction)  
# txhash = contractInit.w3.toHex(contractInit.w3.sha3(signed_txn.rawTransaction))
# print("https://ropsten.etherscan.io/tx/"+txhash)
# #创建交易结束



# 0x47dd20450f4bebd9d1b84022deeca54f8196409fc6d98b866b1481a41d9552d6  Alice
# 0x9d0da95a9ffcbd6044e9973af056ca5eccca373042f33cd4b71a2fab0d2993bc  Bob
# 0xeb74a6a86dda90e1896c9ad200f0704589eee8d0edbff60d776e4cdb3a16a7a7  Cindy