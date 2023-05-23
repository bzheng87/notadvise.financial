from web3 import Web3

#input contract address
contractAddress = "";

# Your private key here
privateKey = "---";
# Deployer (owner) of the contract
ownerAddress = "";
receiptAddress = "";
strData = Web3.toBytes(hexstr=Web3.toHex(text=open('Epochtest.txt').read()))
sendTokenId = 4;
f = open("ROP_ABI.json", "r")
contractABI = f.read();

##enter infura key here
w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/'))
contract = w3.eth.contract(address=contractAddress,abi=contractABI);

estimateGas = contract.functions.safeTransferFrom(ownerAddress, receiptAddress, sendTokenId, strData).estimateGas();
transaction = contract.functions.safeTransferFrom(ownerAddress, receiptAddress, sendTokenId, strData).buildTransaction()
transaction.update({ 'gas' : estimateGas })
transaction.update({ 'nonce' : w3.eth.get_transaction_count(ownerAddress) })
signed_tx = w3.eth.account.sign_transaction(transaction, privateKey)
txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print("txnHash: " + txn_hash.hex())
