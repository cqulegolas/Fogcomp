# paste from Remix IDE
abi = """[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "_from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "_taskName",
				"type": "string"
			}
		],
		"name": "Confirmed",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "_from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_nodeNum",
				"type": "uint256"
			}
		],
		"name": "toBeConfirmed",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "getMyRequests",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "taskName",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "toNodeNum",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "reqBandwidth",
						"type": "uint256"
					},
					{
						"internalType": "bool",
						"name": "confirmed",
						"type": "bool"
					},
					{
						"internalType": "string",
						"name": "algorithm",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "fromAddress",
						"type": "address"
					}
				],
				"internalType": "struct FogComp.request[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getNodeArr",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "nodeName",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "bandwidth",
						"type": "uint256"
					},
					{
						"internalType": "bool",
						"name": "occupied",
						"type": "bool"
					},
					{
						"internalType": "string",
						"name": "algorithm",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "protocol",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "commuCode",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "time",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "address",
						"name": "belongTo",
						"type": "address"
					}
				],
				"internalType": "struct FogComp.node[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "nodeArr",
		"outputs": [
			{
				"internalType": "string",
				"name": "nodeName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "bandwidth",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "occupied",
				"type": "bool"
			},
			{
				"internalType": "string",
				"name": "algorithm",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "protocol",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "commuCode",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "belongTo",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "nodeLength",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_nodeNum",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_nodeName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_bandwidth",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_algorithm",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_protocol",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_commuCode",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_price",
				"type": "uint256"
			}
		],
		"name": "nodeModify",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_nodeName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_bandwidth",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_algorithm",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_protocol",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_commuCode",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_price",
				"type": "uint256"
			}
		],
		"name": "nodeRegist",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_nodeNum",
				"type": "uint256"
			}
		],
		"name": "nodeRemove",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "user_addr",
				"type": "address"
			}
		],
		"name": "queryUser",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_taskName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_toNodeNum",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_reqBandwidth",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "to_addr",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_algorithm",
				"type": "string"
			}
		],
		"name": "sendRequest",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_taskNum",
				"type": "uint256"
			}
		],
		"name": "taskConfirm",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_taskNum",
				"type": "uint256"
			}
		],
		"name": "taskDecline",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_taskNum",
				"type": "uint256"
			}
		],
		"name": "taskFinish",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_userName",
				"type": "string"
			}
		],
		"name": "userRegist",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "userRemove",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""
