// Declare this file as a StarkNet contract.
%lang starknet

from starkware.starknet.common.syscalls import get_caller_address
from starkware.cairo.common.cairo_builtins import HashBuiltin

// Define a storage variable.
@storage_var
func _roles( address: felt, role: felt ) -> (has_role: felt) {
}

@constructor
func constructor{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr,
}(roles_manager_address: felt) {
    _roles.write(roles_manager_address, 'roles_manager', 1);
    return ();
}

// Increases the balance by the given amount.
@external
func add_role{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr,
}(address: felt, role: felt) {
    let (caller) = get_caller_address();
    let (has_role) = _roles.read(caller, 'roles_manager');
    with_attr error_message("Caller does not have roles_manager role.") {
        assert 1 = has_role;
    }
    _roles.write(address, role, 1);
    return ();
}

// Returns the current balance.
@view
func has_role{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr,
}(address: felt, role: felt) -> (has_role: felt) {
    let (has_role) = _roles.read(address, role);
    return (has_role=has_role);
}
