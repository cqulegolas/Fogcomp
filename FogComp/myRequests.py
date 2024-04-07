import contractInit
# 当前用户设备下的请求
requests = contractInit.contract.functions.getMyRequests().call({'from':contractInit.wallet_address}) 
for request in requests:
    print(request[0],'：用户',request[5],'请求第',request[1],'号设备，','占用带宽',request[2],'，确认状态',request[3])

# 要处理的任务号
_taskNum = 0

# ##创建一个交易,任务接受
# address = contractInit.wallet_address
# key = contractInit.wallet_private_key
# nonce = contractInit.w3.eth.getTransactionCount(address)
# print(nonce)
# txn = contractInit.contract.functions.taskConfirm(_taskNum).buildTransaction({
#    'nonce':nonce,
#    'gas': 3000000,
#    'chainId': 3,
#    'gasPrice': contractInit.w3.toWei('10', 'gwei'),
#    })
# signed_txn = contractInit.w3.eth.account.signTransaction(txn, key)
# print(signed_txn.hash)
# print(signed_txn.rawTransaction)

# ##原始交易发送
# tmp = contractInit.w3.eth.sendRawTransaction(signed_txn.rawTransaction)  
# txhash = contractInit.w3.toHex(contractInit.w3.sha3(signed_txn.rawTransaction))
# print("https://ropsten.etherscan.io/tx/"+txhash)
# ##创建交易结束


# ##创建一个交易,任务完成
# address = contractInit.wallet_address
# key = contractInit.wallet_private_key
# nonce = contractInit.w3.eth.getTransactionCount(address)
# print(nonce)
# txn = contractInit.contract.functions.taskFinish(_taskNum).buildTransaction({
#    'nonce':nonce,
#    'gas': 3000000,
#    'chainId': 3,
#    'gasPrice': contractInit.w3.toWei('10', 'gwei'),
#    })
# signed_txn = contractInit.w3.eth.account.signTransaction(txn, key)
# print(signed_txn.hash)
# print(signed_txn.rawTransaction)

# ##原始交易发送
# tmp = contractInit.w3.eth.sendRawTransaction(signed_txn.rawTransaction)  
# txhash = contractInit.w3.toHex(contractInit.w3.sha3(signed_txn.rawTransaction))
# print("https://ropsten.etherscan.io/tx/"+txhash)
# ##创建交易结束


# ##创建一个交易,任务拒绝
# address = contractInit.wallet_address
# key = contractInit.wallet_private_key
# nonce = contractInit.w3.eth.getTransactionCount(address)
# print(nonce)
# txn = contractInit.contract.functions.taskDecline(_taskNum).buildTransaction({
#    'nonce':nonce,
#    'gas': 3000000,
#    'chainId': 3,
#    'gasPrice': contractInit.w3.toWei('10', 'gwei'),
#    })
# signed_txn = contractInit.w3.eth.account.signTransaction(txn, key)
# print(signed_txn.hash)
# print(signed_txn.rawTransaction)

# ##原始交易发送
# tmp = contractInit.w3.eth.sendRawTransaction(signed_txn.rawTransaction)  
# txhash = contractInit.w3.toHex(contractInit.w3.sha3(signed_txn.rawTransaction))
# print("https://ropsten.etherscan.io/tx/"+txhash)
# ##创建交易结束