## Opcode usage for the top 49 gas spending contracts on Ethereum mainnet

### Description

The top 49 contracts by gas expenditure are obtained from Etherscan (https://etherscan.io/gastracker - Gas Guzzlers).
For each contract we count the OPCODES by their appearance in the contract. We do the counting in two ways:
- not grouped - all opcodes are counted uniquely
- grouped - the stack management related OPCODES (PUSH, SWAP and DUP) that have multiple versions are grouped in the following way:
    * PUSH1...PUSH32 are represented as PUSH and PUSH contains the counts for every PUSH* OPCODE from PUSH1...PUSH32
    * SWAP1...SWAP16 are represented as SWAP and SWAP contains the counts for every SWAP* OPCODE from SWAP1...SWAP16
    * DUP1...DUP16 are represented as DUP and DUP contains the counts for every DUP* OPCODE from DUP1...DUP16
    
The results can be found in the `data/generated/` directory (`global_all.json`, `global_grouped.json`, `opcode_table_all.html`, `opcode_table_grouped.html`, `opcode_table_all.md` and `opcode_table_grouped.md`).


### Usage

1. `pip install -r requirements.txt`
2. `cp .env.sample .env`
3. Add your etherscan api key in `.env`
4. `python main.py`


### Results:

#### Not grouped:

| OPCODE      | Count |
| ----------- | ----------- |
| PUSH1 | 33493 |
| PUSH2 | 16525 |
| POP | 14834 |
| ADD | 12995 |
| JUMPDEST | 12330 |
| SWAP1 | 12215 |
| DUP1 | 12038 |
| DUP2 | 11172 |
| MSTORE | 8220 |
| JUMP | 7285 |
| DUP3 | 6842 |
| JUMPI | 6423 |
| MLOAD | 6274 |
| SWAP2 | 6116 |
| AND | 5336 |
| ISZERO | 5249 |
| DUP4 | 4551 |
| SUB | 4071 |
| REVERT | 3141 |
| DUP5 | 2599 |
| SWAP3 | 2541 |
| PUSH20 | 1927 |
| PUSH4 | 1881 |
| PUSH32 | 1863 |
| EQ | 1711 |
| CALLDATALOAD | 1631 |
| DUP6 | 1473 |
| SLOAD | 1461 |
| PUSH3 | 1353 |
| LT | 1336 |
| DUP7 | 1131 |
| MUL | 1113 |
| GT | 1063 |
| SWAP4 | 1032 |
| DUP8 | 903 |
| SHA3 | 873 |
| EXP | 810 |
| SWAP5 | 710 |
| CALLVALUE | 638 |
| DUP9 | 624 |
| CALLDATASIZE | 619 |
| NOT | 586 |
| CALLER | 544 |
| SSTORE | 544 |
| DIV | 541 |
| GAS | 504 |
| DUP10 | 451 |
| OR | 395 |
| SWAP6 | 381 |
| DUP11 | 368 |
| EXTCODESIZE | 339 |
| CALL | 281 |
| DUP12 | 280 |
| DUP13 | 277 |
| SLT | 264 |
| SWAP8 | 252 |
| SWAP7 | 244 |
| CALLDATACOPY | 243 |
| RETURN | 228 |
| PUSH5 | 218 |
| DUP14 | 199 |
| DUP15 | 183 |
| STOP | 178 |
| CODECOPY | 174 |
| PUSH8 | 152 |
| STATICCALL | 150 |
| ADDRESS | 143 |
| SWAP9 | 127 |
| CREATE2 | 124 |
| SWAP10 | 105 |
| PUSH16 | 99 |
| DUP16 | 96 |
| SWAP11 | 95 |
| LOG3 | 85 |
| DELEGATE_CALL | 65 |
| PUSH28 | 63 |
| PUSH14 | 60 |
| GASLIMIT | 56 |
| LOG1 | 55 |
| PUSH15 | 54 |
| MSTORE8 | 52 |
| TIMESTAMP | 51 |
| LOG2 | 51 |
| BYTE | 50 |
| NUMBER | 47 |
| PUSH21 | 47 |
| PUSH19 | 43 |
| SIGNEXTEND | 43 |
| SWAP12 | 42 |
| SGT | 42 |
| COINBASE | 37 |
| PUSH6 | 37 |
| LOG4 | 36 |
| GASPRICE | 34 |
| PUSH10 | 33 |
| PUSH12 | 32 |
| ORIGIN | 31 |
| BALANCE | 31 |
| PUSH29 | 27 |
| PUSH9 | 25 |
| SWAP14 | 23 |
| PUSH17 | 23 |
| PUSH7 | 22 |
| MOD | 20 |
| SWAP13 | 18 |
| DIFFICULTY | 17 |
| PUSH31 | 17 |
| PUSH11 | 17 |
| PUSH13 | 15 |
| PUSH24 | 13 |
| SDIV | 10 |
| PUSH25 | 9 |
| MSIZE | 7 |
| SMOD | 7 |
| PUSH18 | 7 |
| CODESIZE | 7 |
| PUSH27 | 6 |
| SWAP16 | 5 |
| SUICIDE | 5 |
| PUSH22 | 5 |
| PUSH26 | 5 |
| PC | 4 |
| SWAP15 | 3 |
| ADDMOD | 2 |
| MULMOD | 2 |
| XOR | 2 |
| LOG0 | 2 |
| CREATE | 2 |
| PUSH23 | 1 |
| CALLCODE | 1 |
| PUSH30 | 1 |
| BLOCKHASH | 1 |


#### Grouped:

| OPCODE      | Count |
| ----------- | ----------- |
| PUSH | 58073 |
| DUP | 43187 |
| SWAP | 23909 |
| POP | 14834 |
| ADD | 12995 |
| JUMPDEST | 12330 |
| MSTORE | 8220 |
| JUMP | 7285 |
| JUMPI | 6423 |
| MLOAD | 6274 |
| AND | 5336 |
| ISZERO | 5249 |
| SUB | 4071 |
| REVERT | 3141 |
| EQ | 1711 |
| CALLDATALOAD | 1631 |
| SLOAD | 1461 |
| LT | 1336 |
| MUL | 1113 |
| GT | 1063 |
| SHA3 | 873 |
| EXP | 810 |
| CALLVALUE | 638 |
| CALLDATASIZE | 619 |
| NOT | 586 |
| CALLER | 544 |
| SSTORE | 544 |
| DIV | 541 |
| GAS | 504 |
| OR | 395 |
| EXTCODESIZE | 339 |
| CALL | 281 |
| SLT | 264 |
| CALLDATACOPY | 243 |
| RETURN | 228 |
| STOP | 178 |
| CODECOPY | 174 |
| STATICCALL | 150 |
| ADDRESS | 143 |
| CREATE2 | 124 |
| LOG3 | 85 |
| DELEGATE_CALL | 65 |
| GASLIMIT | 56 |
| LOG1 | 55 |
| MSTORE8 | 52 |
| TIMESTAMP | 51 |
| LOG2 | 51 |
| BYTE | 50 |
| NUMBER | 47 |
| SIGNEXTEND | 43 |
| SGT | 42 |
| COINBASE | 37 |
| LOG4 | 36 |
| GASPRICE | 34 |
| ORIGIN | 31 |
| BALANCE | 31 |
| MOD | 20 |
| DIFFICULTY | 17 |
| SDIV | 10 |
| MSIZE | 7 |
| SMOD | 7 |
| CODESIZE | 7 |
| SUICIDE | 5 |
| PC | 4 |
| ADDMOD | 2 |
| MULMOD | 2 |
| XOR | 2 |
| LOG0 | 2 |
| CREATE | 2 |
| CALLCODE | 1 |
| BLOCKHASH | 1 |
