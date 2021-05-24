import os
import requests
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_BASE_URL = os.environ.get('ETHERSCAN_BASE_URL')
ETHERSCAN_API_KEY = os.environ.get('ETHERSCAN_API_KEY')


def get_contract_opcodes(contract_address: str):
    try:
        url = f"{ETHERSCAN_BASE_URL}?module=opcode&action=getopcode&address={contract_address}&apikey={ETHERSCAN_API_KEY}"
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        data = r.json()
        if data.get('status') == "1":
            return data.get('result')
        else:
            raise Exception(f"Something is wrong with the etherscan response: {data}")
    except Exception as e:
        raise Exception(e)

