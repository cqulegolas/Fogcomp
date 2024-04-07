import contractInit
nodes = contractInit.contract.functions.getNodeArr().call()
print(nodes)

def findNode1(_taskName,Tweight,Pweight,rec):
    global targetCode

    search=[rec[5:7],rec[4]]
    nodes = contractInit.contract.functions.getNodeArr().call()
    algs=[]
    ocps=[]
    coms=[]
    result0=[]
    result1=[]
    result2=[]
    scores=[]

    #检查算法
    for node in nodes:
        algs.append(node[3])
    print('算法列表: ',algs)

    #检查占用
    for node in nodes:
        ocps.append(node[2])
    print('占用情况: ',ocps)

    #检查通信
    for node in nodes:
        coms.append(node[4])
    print('通信协议: ',coms)

    k=0
    for ocp in ocps:
        if ocp == False:
            result0.append(k)
        k+=1

    i=0       
    for alg in algs:
        if alg == search[0]:
            result1.append(i)
        i+=1

    m=0       
    for com in coms:
        if com == search[1]:
            result2.append(m)
        m+=1

    avls = set(result1) & set(result0) & set(result2)
    avls = list(avls)
    print(result0,result1,result2)
    print('具备',search[0],search[1],'且空闲的设备:',avls)


    # 根据time与price权衡最佳设备
    for avl in avls:
        scores.append(Tweight*contractInit.contract.functions.nodeArr(avl).call()[6]+Pweight*contractInit.contract.functions.nodeArr(avl).call()[7])
        print(contractInit.contract.functions.nodeArr(avl).call()[6],contractInit.contract.functions.nodeArr(avl).call()[7])
    print('综合得分: ' , scores)

    if scores!=[]:   
        targetNum = avls[scores.index(min(scores))]
        targetCode = contractInit.contract.functions.nodeArr(targetNum).call()[5]
        print('建议请求第', targetNum ,'号设备','通信码为：', targetCode)


        #推送任务
        _toNodeNum = int(targetNum)
        _reqBandwidth = int(rec[7:11])
        to_addr = contractInit.contract.functions.nodeArr(targetNum).call()[8]
        _algorithm = search[0]
        print(_taskName, _toNodeNum, _reqBandwidth,to_addr,_algorithm)

        # #开始创建一个交易
        # address = contractInit.wallet_address
        # key = contractInit.wallet_private_key
        # nonce = contractInit.w3.eth.getTransactionCount(address)
        # print(nonce)
        # txn = contractInit.contract.functions.sendRequest(_taskName, _toNodeNum, _reqBandwidth,to_addr,_algorithm).buildTransaction({
        # 'nonce':nonce,
        # 'gas': 3000000,
        # 'chainId': 3,
        # 'gasPrice': contractInit.w3.toWei('10', 'gwei'),
        # })
        # signed_txn = contractInit.w3.eth.account.signTransaction(txn, key)
        # print(signed_txn.hash)
        # print(signed_txn.rawTransaction)

        # ##原始交易发送
        # tmp = contractInit.w3.eth.sendRawTransaction(signed_txn.rawTransaction)  
        # txhash = contractInit.w3.toHex(contractInit.w3.sha3(signed_txn.rawTransaction))
        # print("https://ropsten.etherscan.io/tx/"+txhash)
        # ##创建交易结束

    else:
        targetCode = '0'
        print("no ECN found")

