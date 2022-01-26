
# To Start
1. Set up config
2. Set up db `curve_wars`
3. $ `flask db init`
4. $ `flask db migrate`
5. $ `python wsgi.py`

# Architecture
* **models** define sql data
* **routes** ...
* **templates** contain custom views
* **interface** defines structure for reading contracts

# App
* **basic**
  * Contains general purpose features, token, contract, address
  * Token inherits from Contract. Contract inherits from Address.
* **curve**
  * Contains interfaces which query the chain. May contain more details which allowz
* **data**
  * stores abis and basic curve info
* **deep**
  * Contains pages which query from outside of the chian such as transactions and transfers. These rely on information in basic section.
  * Separated from basic because it has more dependencies on sourcing beyond the chain


* **utility**
  * web3, local storage
    * .json for abi's
    * .py for initial curve contracts
    * api for external data sources

# Ramp up
* [x] Load CRV data contracts
* [x] Fetch abi
* [-] Get coins for each pools
* [ ] Get transfers for each coin to deposit contract
* [ ] Get `curve LPs`
* [ ] Get

# To Do

* [x] Get DB working
* [x] Get templates working for basic index support
  * [x] base
  * [x] deep
* [x] Get Curve Dashboard routes
* [x] Get Curve Dashboard dashboard template
  * trigger load
    * [x] address
    * [x] contracts
      * [x] abis
    * [x] tokens
## General
* [ ] Fetch ABI
* [ ] Construct Contracts
* [ ] Query balances
  * [ ] deposits in gauge
  * [ ] veCRV

## basic
  * address
    * forms
      * [ ] test
    * [ ] templates
    * [ ] complete routes
  * contract
    * [ ] templates
    * [ ] complete routes
  * token
    * [ ] templates
    * [ ] complete routes

## deep
  * transaction
    * [x] templates
    * [ ] complete routes
  * transfer
    * [x] templates
    * [ ] complete routes

## curve
  * adapter
    * [ ] interface
    * [ ] routes
    * [ ] templaes
  * boost
    * [ ] interface
    * [ ] routes
    * [ ] templates
  * deposit
    * [ ] interface
    * [ ] routes
    * [ ] templats
  * gauge
    * [ ] interface
    * [ ] routes
    * [ ] templates
  * staking
    * [ ] interface
    * [ ] routes  
    * [ ] templates
  * swap
    * [ ] interface
    * [ ] routes
    * [ ] templates

## scripts
  *


# Nav
  <a href="{{ url_for('transaction_bp.index') }}">Transactions</a>
  <a href="{{ url_for('transfer_bp.index') }}">Transfers</a>
