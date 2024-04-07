import time
import contract_abi
from web3 import Web3,HTTPProvider
from eth_account import Account
w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/27bc1e872f70454db541e0eb7103ab48'))

# 合约初始化，地址，ABI，登陆一个以太坊账户
contract = w3.eth.contract(address = '0x2a0dCa2cCe68d40c2523b1A5e2928E47D6249FF3', abi = contract_abi.abi)

# wallet_address       = '0x423ac5c763D89F0a626e041B66B9038f5B85642F'
# wallet_private_key   = '17B7E830CC67877DF2F1DFB41BD0ECCA4EFF6B5BE4315AB381FB2DE94964BEAD'

# wallet_address       = '0x98b79FBC1B6ADde5f93A16C98c2a90Da6033e196'
# wallet_private_key   = '969B84BFE1DC48AEAA34806C4F875253FD65561C1483F406406BAA1F5D9F81DB'

# wallet_address       = '0x86038592BC68C81190043a223b92420199BaA8a7'
# wallet_private_key   = '4E3ECC4FAD2CA1ED44AA77378CA16269A8F0483A24A774AC7499EA46DC91638C'



















# wallet_address       = '0xE41696E7C8118027fcaC5a4b93FE98420893978B'
# wallet_private_key   = 'EAD5375A3C5A7125BE4B9FADB9AA1D232415DB4F4A9B070FDBD425C90E503F83'

# wallet_address       = '0xA6bc9eD754b9a78683c438256E51c6EE5f7e1B2A'
# wallet_private_key   = '9734176879092BB40C28039637EF347B2622413A9101C51326271CFD2289E302'

# wallet_address       = '0x0A58cbdE5469E82dDa3Ec6Cf819f461475d22fd8'
# wallet_private_key   = '243C3B1E74ECA75080B2718C0BD66B6B1624857C9F236786964D04A68D8B9C27'

# wallet_address       = '0x1B59bF6c05dF40500faC64FDA248aB3F9d74DcA8'
# wallet_private_key   = '62F11FDDAF40C22B7517E30E069549A518BD642879AF64964FA3089E77ED0B2D'

# wallet_address       = '0xA7c62F8F2eafa03C8760f1Faa460330cc89879BB'
# wallet_private_key   = '01d7423885175efb5a4c88c916c1b102882ec512333c6ec95c8d0f0d7890ef5b'
    
# wallet_address       = '0x82ec0fc638516ABc3880856983008033E3fE0299'  
# wallet_private_key   = '2b472b160e484ded32112f0a4c932a4aebd93710abad076c3e9ca540eeef8a20'
