import contractInit


def nodeRegist1(rec):
    address = contractInit.wallet_address
    key = contractInit.wallet_private_key

    _nodeName = rec[3:11]
    _bandwidth = int(rec[26:30])
    _algorithm = rec[16:18]
    _protocol = rec[11]
    _commuCode = rec[12:16]
    _time = int(rec[18:22])
    _price = int(rec[22:26])
    print(_nodeName, _bandwidth , _algorithm , _protocol , _commuCode , _time , _price)
    
    nodes = contractInit.contract.functions.getNodeArr().call()
    names=[]   
    for node in nodes:
        names.append(node[0])

    
    # if _nodeName in names:
    #     ##创建一个交易,节点修改
    #     _nodeNum = names.index(_nodeName)
    #     nonce = contractInit.w3.eth.getTransactionCount(address)
    #     print(nonce)
    #     txn = contractInit.contract.functions.nodeModify(_nodeNum ,_nodeName, _bandwidth , _algorithm , _protocol , _commuCode , _time , _price).buildTransaction({
    #     'nonce':nonce,
    #     'gas': 3000000,
    #     'chainId': 3,
    #     'gasPrice': contractInit.w3.toWei('10', 'gwei'),
    #     })
    #     signed_txn = contractInit.w3.eth.account.signTransaction(txn, key)
    #     print(signed_txn.hash)
    #     print(signed_txn.rawTransaction)

    #     ##原始交易发送
    #     tmp = contractInit.w3.eth.sendRawTransaction(signed_txn.rawTransaction)  
    #     txhash = contractInit.w3.toHex(contractInit.w3.sha3(signed_txn.rawTransaction))
    #     print("https://ropsten.etherscan.io/tx/"+txhash)
    #     ##创建交易结束 


    # else :
    #     ##创建一个交易,节点注册
    #     nonce = contractInit.w3.eth.getTransactionCount(address)
    #     print(nonce)
    #     txn = contractInit.contract.functions.nodeRegist(_nodeName, _bandwidth , _algorithm , _protocol , _commuCode , _time , _price).buildTransaction({
    #     'nonce':nonce,
    #     'gas': 3000000,
    #     'chainId': 3,
    #     'gasPrice': contractInit.w3.toWei('10', 'gwei'),
    #     })
    #     signed_txn = contractInit.w3.eth.account.signTransaction(txn, key)
    #     print(signed_txn.hash)
    #     print(signed_txn.rawTransaction)

    #     ##原始交易发送
    #     tmp = contractInit.w3.eth.sendRawTransaction(signed_txn.rawTransaction)  
    #     txhash = contractInit.w3.toHex(contractInit.w3.sha3(signed_txn.rawTransaction))
    #     print("https://ropsten.etherscan.io/tx/"+txhash)
    #     ##创建交易结束


    # ##创建一个交易,节点移除
    # nonce = contractInit.w3.eth.getTransactionCount(address)
    # print(nonce)
    # txn = contractInit.contract.functions.nodeRemove(_nodeNum).buildTransaction({
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

