import sys
import json
import base64
import subprocess
from ethermint.evm.v1.tx_pb2 import MsgEthereumTx
from ethermint.evm.v1.tx_pb2 import DynamicFeeTx
from cosmos.tx.v1beta1.tx_pb2 import Tx

def main():
    # Step 1: Read JSON data from standard input
    json_data = sys.stdin.read()
    print("Step 1: Received JSON data from stdin.")

    # Step 2: Parse the JSON data
    data = json.loads(json_data)
    print("Step 2: Parsed JSON data.")

    # Step 3: Get the transaction data from the "txs" field
    txs = data["result"]["txs"]
    print("Step 3: Extracted transaction data from 'txs' field.")

    # Step 4: Process all transactions
    for i, tx_data in enumerate(txs):
        print(f"\nProcessing transaction {i+1}:")
        
        # Step 4.1: Decode the transaction
        decoded_tx_data = base64.b64decode(tx_data)
        print("Step 4.1: Decoded transaction data.")

        # Step 4.2: Write the decoded data to a binary file
        with open(f'data_{i}.bin', 'wb') as f:
            f.write(decoded_tx_data)
        print("Step 4.2: Wrote decoded data to binary file.")

        # Step 4.3: Print the decoded data using protoc
        print("Step 4.3: Decoded transaction data:")
        subprocess.run(['protoc', '--decode_raw'], input=decoded_tx_data)

        # Step 4.4: Parse the decoded data using Tx
        tx = Tx()
        tx.ParseFromString(decoded_tx_data)
        print("Step 4.4: Parsed decoded data using Tx.")

        # Step 4.5: Get the value from the parsed Tx
        value = tx.body.messages[0].value
        print("Step 4.5: Extracted value from parsed Tx.")

        # Step 4.6: Parse the value using MsgEthereumTx
        msg_ethereum_tx = MsgEthereumTx()
        msg_ethereum_tx.ParseFromString(value)
        print("Step 4.6: Parsed value using MsgEthereumTx.")

        # Step 4.7: Get the data value from MsgEthereumTx
        data_value = msg_ethereum_tx.data.value
        print("Step 4.7: Extracted data value from MsgEthereumTx.")

        # Step 4.8: Parse the data value using DynamicFeeTx
        dynamic_fee_tx = DynamicFeeTx()
        dynamic_fee_tx.ParseFromString(data_value)
        print("Step 4.8: Parsed data value using DynamicFeeTx.")
        print("Dynamic Fee Tx:", dynamic_fee_tx)

    print("\nProcessing complete.")

if __name__ == "__main__":
    main()