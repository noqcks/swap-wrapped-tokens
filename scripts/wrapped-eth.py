import requests
from brownie import Fixed, Wei, accounts, config, interface, network
from brownie.convert import to_string

weth = interface.WethInterface(config["networks"][network.show_active()]["weth"])
explorer = network.account.CONFIG.networks[network.show_active()]["explorer"]
acct = accounts.add(config["wallets"]["from_key"])

AMOUNT = 1

def account_balance(account):
    return {"WETH": weth_balance(account),"ETH": eth_balance(account)}

def eth_balance(account):
    return to_string(Wei(account.balance()).to("ether"))

def weth_balance(account):
    return to_string(Wei(weth.balanceOf(account)).to("ether"))

def get_eth():
    """
    Converts WETH to ETH
    """
    print(f"Account balance ({acct})")
    print(account_balance(acct), end="\n\n")

    print(f"Converting {AMOUNT} WETH to ETH")
    tx = weth.withdraw(f"{AMOUNT} ether", {"from": acct})
    print(f"Received {AMOUNT} ETH")
    print(f"Txn: {explorer}/tx/{tx.txid}", end="\n\n")

    print(f"Account balance ({acct})")
    print(account_balance(acct))

def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    print(f"Account balance ({acct})")
    print(account_balance(acct), end="\n\n")

    print(f"Converting {AMOUNT} ETH to WETH")
    tx = weth.deposit({"from": acct, "value": f"{AMOUNT} ether"})
    print(f"Received {AMOUNT} WETH")
    print(f"Txn: {explorer}/tx/{tx.txid}", end="\n\n")

    print(f"Account balance ({acct})")
    print(account_balance(acct))
