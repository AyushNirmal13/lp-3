// P13: Bank Account Smart Contract
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {

    // Stores the balance of each user's wallet address
    mapping(address => uint) public balance;

    // Deposit Ether into the user's account
    function deposit() public payable {
        require(msg.value > 0, "Amount must be greater than zero");

        balance[msg.sender] += msg.value;
    }

    // Withdraw Ether from the user's account
    function withdraw(uint amount) public {
        require(amount > 0, "Amount must be greater than zero");
        require(balance[msg.sender] >= amount, "Insufficient balance");

        // Update balance before sending Ether
        balance[msg.sender] -= amount;

        // Transfer Ether to the user's wallet
        (bool success, ) = payable(msg.sender).call{value: amount}("");

        require(success, "Transfer failed");
    }

    // Display the user's account balance
    function showBalance() public view returns (uint) {
        return balance[msg.sender];
    }
}

/*
HOW TO COMPILE AND RUN:

1. Open https://remix.ethereum.org
2. Open File Explorer and create a file named P13.sol.
3. Paste this complete program and save it (Ctrl + S).
4. Open Solidity Compiler from the left sidebar.
5. Select compiler version 0.8.20.
6. Click Compile P13.sol.
7. Open Deploy & Run Transactions.
8. Select Environment: Remix VM.
9. Select Contract: BankAccount.
10. Set Value = 0 wei and click Deploy.
11. Expand BankAccount under Deployed Contracts.

FUNCTION EXECUTION:

1. DEPOSIT:
   - Find the Value field at the bottom.
   - Enter 1 and select Ether as the unit.
   - Click Transact beside deposit().

2. CHECK BALANCE:
   - Click Call beside showBalance().
   - Expected Output: 1000000000000000000 Wei.

3. WITHDRAW:
   - Change the bottom Value field to 0 wei.
   - Enter 200000000000000000 in the amount field of withdraw().
   - Click Transact.

4. CHECK FINAL BALANCE:
   - Click Call beside showBalance().
   - Expected Output: 800000000000000000 Wei.

EXPECTED RESULTS:

Initial Deposit = 1 Ether
Withdrawal = 0.2 Ether
Remaining Balance = 0.8 Ether

IMPORTANT NOTES:
- Remix VM uses simulated Ether; no real money is involved.
- Use the same account for all operations.
- deposit() and withdraw() use Transact.
- showBalance() uses Call.
- No MetaMask or Sepolia connection is required for this practical.
*/
