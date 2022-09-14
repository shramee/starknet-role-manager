// Declare this file as a StarkNet contract.
%lang starknet

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
