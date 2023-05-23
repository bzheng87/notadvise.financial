from web3 import Web3
contractAddress = "0x19AEf98360E3b960E91c3B641B1C13FF209a0C97";

# Your private key here
privateKey = "---";
# Deployer (owner) of the contract
ownerAddress = "0x86f41Fb061A3706F834665F2003caE43BA491996";
receiptAddress = "0x35C6B73748272329cBf4ca0762F8765b70343914";
strData = Web3.toBytes(hexstr=Web3.toHex(text=open('Epochtest.txt').read()))
sendTokenId = 4;
f = open("ROP_ABI.json", "r")
contractABI = f.read();
w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/b7affc0b71274946bc59749acb2adcc1'))
contract = w3.eth.contract(address=contractAddress,abi=contractABI);

estimateGas = contract.functions.safeTransferFrom(ownerAddress, receiptAddress, sendTokenId, strData).estimateGas();
transaction = contract.functions.safeTransferFrom(ownerAddress, receiptAddress, sendTokenId, strData).buildTransaction()
transaction.update({ 'gas' : estimateGas })
transaction.update({ 'nonce' : w3.eth.get_transaction_count(ownerAddress) })
signed_tx = w3.eth.account.sign_transaction(transaction, privateKey)
txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print("txnHash: " + txn_hash.hex())