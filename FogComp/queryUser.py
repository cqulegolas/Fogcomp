import contractInit
# 根据地址查询用户名和拥有的设备号
print(contractInit.contract.functions.queryUser(contractInit.wallet_address).call({'from':contractInit.wallet_address}))