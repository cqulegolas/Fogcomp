//At: 0x2a0dCa2cCe68d40c2523b1A5e2928E47D6249FF3

pragma solidity ^0.6.6;
pragma experimental ABIEncoderV2;
contract FogComp {
    
    event toBeConfirmed (address indexed _from, address indexed _to ,uint _nodeNum);
    event Confirmed (address indexed _from, address indexed _to, string _taskName);
   
    struct user{
        string userName;
        bool registed;
    }
    
    struct node{
        string nodeName;
        uint bandwidth;
        bool occupied;
        string algorithm;
        string protocol;
        string commuCode;
        uint time;
        uint price;
        address belongTo;
    }
    
    struct request{
        string taskName;
        uint toNodeNum;
        uint reqBandwidth;
        bool confirmed;
        string algorithm;
        address fromAddress;
    }
    
    mapping(address=> request[]) requesteArr;
    mapping(address=> uint) private nodeCount;
    mapping(address => user) private userMap;
    node[] public nodeArr;
    
    function userRegist (string memory _userName) public returns (address) {
        require(userMap[msg.sender].registed != true);
        userMap[msg.sender].userName = _userName;
        userMap[msg.sender].registed = true;
        return msg.sender;   
    }
    
    function userRemove () public returns (address) {
        require(userMap[msg.sender].registed == true);
        delete userMap[msg.sender];
        for (uint i = 0; i < nodeArr.length; i++) {
            if (nodeArr[i].belongTo == msg.sender) {
                delete nodeArr[i];
            }
        }
        nodeCount[msg.sender] = 0;
        return msg.sender;
    }
    
    function nodeRegist (string memory _nodeName, uint _bandwidth ,string memory _algorithm ,string memory _protocol , string memory _commuCode ,uint _time ,uint _price) public returns (address) {
        require(userMap[msg.sender].registed == true);
        nodeArr.push(node(_nodeName , _bandwidth, false , _algorithm , _protocol ,  _commuCode, _time , _price, msg.sender));
        nodeCount[msg.sender]++;
        return msg.sender;
    }
    
    function nodeModify (uint _nodeNum , string memory _nodeName, uint _bandwidth ,string memory _algorithm ,string memory _protocol , string memory _commuCode ,uint _time ,uint _price) public returns (address) {
        require(msg.sender == nodeArr[_nodeNum].belongTo);
        nodeArr[_nodeNum].nodeName = _nodeName;
        nodeArr[_nodeNum].bandwidth = _bandwidth;
        nodeArr[_nodeNum].algorithm = _algorithm;
        nodeArr[_nodeNum].protocol = _protocol;
        nodeArr[_nodeNum].commuCode = _commuCode;
        nodeArr[_nodeNum].time = _time;
        nodeArr[_nodeNum].price = _price;
        return msg.sender;
    }
    
    function nodeRemove (uint _nodeNum) public returns (address) {
        require(msg.sender == nodeArr[_nodeNum].belongTo);
        delete nodeArr[_nodeNum];
        nodeCount[msg.sender]--;
        return msg.sender;
    }
    
    function nodeLength () public view returns (uint) {
        return nodeArr.length;
    }
    
    function queryUser(address user_addr) public view returns (string memory,uint[] memory) {
        uint[] memory result = new uint[](nodeCount[user_addr]);
        uint counter = 0;
        for (uint i = 0; i < nodeArr.length; i++) {
            if (nodeArr[i].belongTo == user_addr) {
                result[counter] = i;
                counter++;
            }
        }
        return (userMap[user_addr].userName,result);
    }
    
    function getNodeArr() public view returns (node[] memory) {
        return nodeArr;
    } 
    
    function sendRequest (string memory _taskName ,uint _toNodeNum , uint _reqBandwidth , address to_addr , string memory _algorithm ) public returns (address) {
        require(nodeArr[_toNodeNum].occupied == false && to_addr == nodeArr[_toNodeNum].belongTo && keccak256(abi.encodePacked(nodeArr[_toNodeNum].algorithm)) == keccak256(abi.encodePacked(_algorithm)));
        requesteArr[to_addr].push(request(_taskName, _toNodeNum, _reqBandwidth, false, _algorithm , msg.sender));
        emit toBeConfirmed(msg.sender , to_addr, _toNodeNum); 
        return msg.sender;
    }
    
    function getMyRequests() public view returns (request[] memory) {
        return requesteArr[msg.sender];
    }
    
    function taskConfirm (uint _taskNum) public returns (address) {
        require(msg.sender == nodeArr[requesteArr[msg.sender][_taskNum].toNodeNum].belongTo && nodeArr[requesteArr[msg.sender][_taskNum].toNodeNum].occupied == false);
        requesteArr[msg.sender][_taskNum].confirmed = true;
        nodeArr[requesteArr[msg.sender][_taskNum].toNodeNum].occupied = true;
        emit Confirmed(requesteArr[msg.sender][_taskNum].fromAddress ,msg.sender, requesteArr[msg.sender][_taskNum].taskName);
    }
    
    function taskDecline (uint _taskNum) public returns (address) {
        require(msg.sender == nodeArr[requesteArr[msg.sender][_taskNum].toNodeNum].belongTo && requesteArr[msg.sender][_taskNum].confirmed == false);
        delete requesteArr[msg.sender][_taskNum];
    }
    
    function taskFinish (uint _taskNum) public returns (address) {
        require(msg.sender == nodeArr[requesteArr[msg.sender][_taskNum].toNodeNum].belongTo && requesteArr[msg.sender][_taskNum].confirmed == true);
        nodeArr[requesteArr[msg.sender][_taskNum].toNodeNum].occupied = false;
        delete requesteArr[msg.sender][_taskNum];
    }
    
}