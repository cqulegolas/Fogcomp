import contractInit


def handle_event(event):
    # receipt = contractInit.w3.eth.waitForTransactionReceipt(event['transactionHash'])
    # result = contractInit.contract.events.Confirmed.processReceipt(receipt)
    # print(result[2]['args'])
    print(event)

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        contractInit.time.sleep(poll_interval)

block_filter = contractInit.w3.eth.filter({'fromBlock':'latest', 'address':'0x2a0dCa2cCe68d40c2523b1A5e2928E47D6249FF3'}) #,'_from':'contractInit.wallet_address'
log_loop(block_filter, 2)

# 监听到的事件,topic格式:(0:对事件的字符做keccak散列运算, 1:address类型from参数补齐64位, 2:address类型to参数补齐64位),data: 没有indexed标记的value的值转化为16进制，并补齐64位
# AttributeDict({'address': '0x0aD55B06535Ed7668A3A572b574A89685b421C2c', 'blockHash': HexBytes('0x693b3efc11b805a0c14d4a89a75b50b0e3adb968c574e59625ca4a70f56a3eff'), 'blockNumber': 9767850, 'data': '0x000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000074465636f64653100000000000000000000000000000000000000000000000000', 'logIndex': 20, 'removed': False, 'topics': [HexBytes('0xd787e2fb8bd6a6d134d708f71d0a3238be9ba231d9147769151c7ea71ab201ed'), HexBytes('0x000000000000000000000000a6bc9ed754b9a78683c438256e51c6ee5f7e1b2a'), HexBytes('0x000000000000000000000000e41696e7c8118027fcac5a4b93fe98420893978b')], 'transactionHash': HexBytes('0xda6a2a6a69946c7b91e1bbffa9b5446a6c76b1bb7caae61bb9014b6f1e6be93e'), 'transactionIndex': 10})
