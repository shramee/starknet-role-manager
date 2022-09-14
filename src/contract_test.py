import os
import pytest

from starkware.starknet.testing.starknet import Starknet

def str_to_felt( str ):
	return int( str.encode('utf-8').hex(), 16 );

OWNER_ADDR = 0x70AEBF10E9735F92CA6EDC49A9D6F3774FFAFE92;
ADDR1 = 0x32429A3EB84A66A83A038E66540042F5864E51A0;
ADDR2 = 0x8421A0832429A64422F54A66A83A038E53EBE665;
# The path to the contract source code.
CONTRACT_FILE = os.path.join(os.path.dirname(__file__), "contract.cairo")

async def setupContract( constructor_calldata = [] ):
	# Create a new Starknet class that simulates the StarkNet
	# system.
	starknet = await Starknet.empty()

	# Deploy the contract.
	return await starknet.deploy(
		source=CONTRACT_FILE,
		constructor_calldata=constructor_calldata,
	)

@pytest.mark.asyncio
async def test_constructor_takes_one_param():
	await setupContract( [OWNER_ADDR] )

@pytest.mark.asyncio
async def test_owner_has_role_roles_manager():
	contract = await setupContract( [OWNER_ADDR] )
	exec = await contract.has_role( address=OWNER_ADDR, role=str_to_felt( 'roles_manager' ) ).call()
	assert exec.result == (1,)

@pytest.mark.asyncio
async def test_add_role_is_protected():
	contract = await setupContract( [OWNER_ADDR] )

	# add roles_manager role for addr1, should fail.
	await contract.add_role( address=ADDR1, role=str_to_felt( 'roles_manager' ) ).execute()

	# addr1 should not have roles_manager role
	exec = await contract.has_role( address=ADDR1, role=str_to_felt( 'roles_manager' ) ).call()
	assert exec.result == (0,)

# @pytest.mark.asyncio
# async def test_owner_can_add_addr():
# 	contract = await setupContract( [OWNER_ADDR] )

# 	# addr1 does not has roles_manager role
# 	exec = await contract.has_role( address=ADDR1, role=str_to_felt( 'roles_manager' ) ).call()
# 	assert exec.result == (0,)

# 	# add roles_manager role for addr1
# 	await contract.add_role( address=ADDR1, role=str_to_felt( 'roles_manager' ) ).execute()

# 	# addr1 now has roles_manager role
# 	exec = await contract.has_role( address=ADDR1, role=str_to_felt( 'roles_manager' ) ).call()
# 	assert exec.result == (1,)

