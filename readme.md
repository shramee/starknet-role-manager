# starknet-role-mananger

A central contract to manage roles for wallets across all your contracts.

## Usage

1. Deploy the contract with `roles_manager` wallet address as input.
2. Call the contract with the same wallet address to add more wallets to `roles_manager` or other roles.
3. Call the contract from your other contract with caller address and roles to verify if they belong to the role.

Only the wallets with `roles_manager` role can add/remove roles.

## Functions

- ``

## Scripts

Scripts to test/deploy contract,

#### test

- `RUN_SCRIPT=test docker-compose up`
- Runs test in `src/contract_test.py` with `pytest`.
- Tests can really save you lots of time writing Starknet contracts.
- With tests you can catch bugs and also fix them, all this while your neighbour is still waiting for his contract to be accepted on L2.
- Read more about writing tests for Starknet contract,  
  https://www.cairo-lang.org/docs/hello_starknet/unit_tests.html

#### deploy

- `RUN_SCRIPT=deploy docker-compose up`
- Compiles the contract in `src/contract.cairo` to `build/contract.json`.
- Declares the contract class and deploys it from `build/contract.json`.
