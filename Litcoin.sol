pragma solidity ^0.4.0;

contract LitCoin {
    address public creator;
    mapping(address => uint) public balances;
    address public burnAddr;
    uint totalSupply;
    
    event CoinIssued(uint amount);
    event CoinsSupply(uint amount);
    
    function LitCoin(){
        creator = msg.sender;
        burnAddr = 0x0000000000000000000000000000000000000000;
    }
    function issue(address receiver, uint amount) {
        require(msg.sender == creator);
        balances[receiver] += amount;
        totalSupply += amount;
        CoinIssued(amount);
    }
    
    function transfer(address receiver, uint amount) {
        require(balances[msg.sender] >= amount);
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        
    }
    
    function burn(uint amount) {
        require(balances[msg.sender] >= amount);
        require(msg.sender == creator);
        balances[msg.sender] -= amount;
        balances[burnAddr] += amount;
        totalSupply -= amount;
        CoinsSupply(amount);
        
        
        
        
    }
}
