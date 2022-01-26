import requests
import time
import json

from config import ALCHEMY, API_ETHERSCAN


class API():
    def __init__(self):
        self.etherscan_key = API_ETHERSCAN
        self.alchemy_url = ALCHEMY
    #
    def get(self, url, attempts=0):
        print("_"*100)
        print(url)
        response = requests.get(url)
        resp = response.json()
        print(resp)
        if not bool(resp['status']) or resp['status'] == "0":
            if attempts > 4:
                return None
            print("\tStatus:\t{}".format(resp['status']))
            print("\tMessage:\t{}".format(resp['message']))
            print("\tResult:\t{}".format(resp['result']))
            if resp['result'] == "Max rate limit reached":
                print("Pausing 5 secs. Rate limit. Attempt: {}".format(attempts))
                time.sleep(5.5)
                return self.get(url, attempts + 1)
            elif resp['result'] == "Contract source code not verified":
                print("\nNot Verified: Proceed")
                return False
            else:
                print("Pausing 60 secs. Attempt: {}".format(attempts))
                time.sleep(61)
                return self.get(url, attempts + 1)
        return resp['result']
    #
    def post(self, url, my_obj):
        print("_"*100)
        print(url)
        response = requests.post(url, data = json.dumps(my_obj))
        resp = response.json()
        # print(resp)
        return resp

    def post_retry(self, url, my_obj, attempts=0):
        print("_"*100)
        print(url)
        response = requests.post(url, data = json.dumps(my_obj))
        resp = response.json()
        print(resp)
        if not bool(resp['status']) or resp['status'] == "0" or resp['']:
            if attempts > 4:
                return None
            print("\tStatus:\t{}".format(resp['status']))
            print("\tMessage:\t{}".format(resp['message']))
            print("\tResult:\t{}".format(resp['result']))

            if resp['result'] == "Max rate limit reached":
                print("Pausing 5 secs. Rate limit. Attempt: {}".format(attempts))
                time.sleep(5.5)
                return self.post(url, my_obj, attempts + 1)
            elif resp['result'] == "Contract source code not verified":
                print("\nNot Verified: Proceed")
                return False
            else:
                print("Pausing 60 secs. Attempt: {}".format(attempts))
                time.sleep(61)
                return self.post(url, my_obj, attempts + 1)
        return resp['result']

api = API()

def get_transfers_from(address, contracts):
    body = {
      "jsonrpc": "2.0",
      "id": 0,
      "method": "alchemy_getAssetTransfers",
      "params": [
        {
          "fromBlock": "0xA97AB8",
          "fromAddress": address,
          "excludeZeroValue": True,

        }
      ]
    }

    return api.post(api.alchemy_url, body)

def get_transfers_to(address, contracts):
    body = {
      "jsonrpc": "2.0",
      "id": 0,
      "method": "alchemy_getAssetTransfers",
      "params": [
        {
          "fromBlock": "0xA97AB8",
          "toAddress": address,
          "excludeZeroValue": True,

        }
      ]
    }

    return api.post(api.alchemy_url, body)
# def coingecko(api, ):
#     url_start = "http://api.etherscan.io/api?module=account&action=tokentx&address="
#     url_end = "&startblock=0&endblock=999999999&sort=asc&apikey="
#     url = url_start + address + url_end + self.api_etherscan
#     return self.get(url)

def etherscan_internal_transactions(address):
    url_start = "https://api.etherscan.io/api?module=account&action=txlistinternal&address="
    url_end = "&startblock=0&endblock=999999999&sort=asc&apikey="
    url = url_start + address + url_end + api.etherscan_key
    return api.get(url)

def etherscan_transactions(address):
    url_start = "https://api.etherscan.io/api?module=account&action=txlist&address="
    url_end = "&startblock=0&endblock=999999999&sort=asc&apikey="
    url = url_start + address + url_end + api.etherscan_key
    return api.get(url)

def etherscan_general(address, action):
    action = "action="+ action + "&address="
    url_start = "https://api.etherscan.io/api?module=account&"+action
    url_end = "&startblock=0&endblock=999999999&sort=asc&apikey="
    url = url_start + address + url_end + api.etherscan_key
    return api.get(url)

def etherscan_abi(address):
    url_start = "https://api.etherscan.io//api?module=contract&action=getabi&address="
    url_end = "&apikey="
    url = url_start + address + url_end + api.etherscan_key
    return api.get(url)
