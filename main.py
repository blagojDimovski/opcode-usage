import json
from json2html import json2html
from etherscan import get_contract_opcodes
from typing import List, Dict
import matplotlib.pyplot as plt
import numpy as np
from time import sleep


def compute_opcode_stats(grouped: bool = False):
    contract_addresses = get_contract_addresses()

    global_opcode_counts = dict()

    g_keyword = 'all'
    if grouped:
        g_keyword = 'grouped'

    for contract_addr in contract_addresses:
        opcode_counts = compute_contract_opcode_stats(contract_addr, g_keyword, grouped)
        global_opcode_counts = update_global_counts(opcode_counts, global_opcode_counts)
        # sleep for a few seconds, not to get blocked by etherscan (rate limit)
        sleep(3)

    sorted_opcodes = dict(sorted(global_opcode_counts.items(), key=lambda item: item[1], reverse=True))


    save_to_file(f"global_{g_keyword}", sorted_opcodes)
    draw_chart(f"opcode_distribution_{g_keyword}", sorted_opcodes)
    create_html_table(f"opcode_table_{g_keyword}", sorted_opcodes)
    create_markdown_table(f"opcode_table_{g_keyword}", sorted_opcodes)


def get_contract_addresses() -> List[str]:

    with open("data/input/contract_addresses.json", "r") as f:
        contract_addresses = json.loads(f.read())
    return contract_addresses


def compute_contract_opcode_stats(contract_addr: str,  g_keyword: str = 'all', grouped: bool = False) -> Dict[str, int]:

    opcode_resp = get_contract_opcodes(contract_addr)
    if grouped:
        opcode_counts = count_opcodes_grouped_stack_ops(opcode_resp)
    else:
        opcode_counts = count_opcodes(opcode_resp)

    save_to_file(f"{contract_addr}_{g_keyword}", opcode_counts)
    return opcode_counts


def count_opcodes(opcode_resp: str) -> Dict[str, int]:
    """Parse the etherscan contract opcodes response from string to dict in the format OPCODE:NUM_APPEARANCES.
    NUM_APPEARANCES is the total number of times that the opcode appeared."""

    opcode_list = opcode_resp.split("<br>")[:-1]

    opcode_counts = dict()
    for opcode in opcode_list:
        # strip the opcode mnemonic from params
        if 'Unknown Opcode' in opcode:
            continue

        opcode = opcode.split()[0]

        if opcode in opcode_counts:
            opcode_counts[opcode] += 1
        else:
            opcode_counts[opcode] = 1

    return opcode_counts


def count_opcodes_grouped_stack_ops(opcode_resp: str) -> Dict[str, int]:
    """
    Parse the etherscan contract opcodes response from string to dict in the format OPCODE:NUM_APPEARANCES.
    NUM_APPEARANCES is the total number of times that the opcode appeared.
    The stack management related opcodes (PUSH*, DUP*, SWAP*) are grouped.
    The opcodes PUSH1...PUSH32 are represented as PUSH
    The opcodes DUP1...DUP16 are represented as DUP
    The opcodes SWAP1...SWAP16 are represented as SWAP
    """

    opcode_list = opcode_resp.split("<br>")[:-1]
    grouping_opcodes = ['PUSH', 'DUP', 'SWAP']
    opcode_counts = dict()
    for opcode in opcode_list:
        # strip the opcode mnemonic from params
        if 'Unknown Opcode' in opcode:
            continue

        opcode = opcode.split()[0]

        for gopc in grouping_opcodes:
            if gopc in opcode:
                opcode = gopc

        if opcode in opcode_counts:
            opcode_counts[opcode] += 1
        else:
            opcode_counts[opcode] = 1

    return opcode_counts


def update_global_counts(contract_opcode_counts: Dict[str, int], global_opcode_counts: Dict[str, int]) -> Dict[str, int]:
    """Update the global opcode stats with the opcode counts from specific contracts."""

    for opcode, counts in contract_opcode_counts.items():
        if opcode in global_opcode_counts:
            global_opcode_counts[opcode] += counts
        else:
            global_opcode_counts[opcode] = counts

    return global_opcode_counts


def save_to_file(title: str, data: dict):

    with open(f"data/generated/{title}.json", "w") as f:
        f.write(json.dumps(data))


def draw_chart(chart_name: str, opcode_counts: dict):
    opcodes = list(opcode_counts.keys())
    counts = list(opcode_counts.values())

    x = np.arange(len(opcodes))  # the label locations
    width = 0.8

    fig, ax = plt.subplots()
    ax.bar(x, counts, width, label='Opcodes')

    # Add some text for labels, title and custom x-axis tick labels, etc.

    ax.set_ylabel('Counts')
    ax.set_xlabel('Opcodes')
    ax.set_title('Opcode counts')
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.legend()

    plt.show()

    fig.savefig(f"charts/{chart_name}.png")


def create_html_table(table_name: str, opcode_counts: dict):
    table = json2html.convert(opcode_counts)
    with open(f"data/generated/{table_name}.html", "w") as f:
        f.write(table)


def create_markdown_table(table_name: str, opcode_counts: dict):

    table_rows = ["| OPCODE      | Count |", "| ----------- | ----------- |"]
    for key, value in opcode_counts.items():
        table_rows.append(f"| {key} | {value} |")

    table = "\n".join(table_rows)

    with open(f"data/generated/{table_name}.md", "w") as f:
        f.write(table)


if __name__ == '__main__':
    compute_opcode_stats()


