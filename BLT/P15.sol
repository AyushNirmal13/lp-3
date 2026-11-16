// P15: Student Data Smart Contract
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    // Structure to store student information
    struct Student {
        uint id;
        string name;
        uint marks;
    }

    // Array to store multiple students
    Student[] public students;

    // Add a new student
    function addStudent(uint id, string memory name, uint marks) public {
        students.push(Student(id, name, marks));
    }

    // Retrieve student details using array index
    function getStudent(uint index)
        public
        view
        returns (uint, string memory, uint)
    {
        require(index < students.length, "Invalid index");

        Student memory s = students[index];

        return (s.id, s.name, s.marks);
    }

    // Return total number of students
    function getCount() public view returns (uint) {
        return students.length;
    }

    // Fallback function
    fallback() external payable {
    }
}

/*
HOW TO COMPILE AND DEPLOY:
1. Open https://remix.ethereum.org
2. Open File Explorer and create a file named P15.sol.
3. Paste this complete program and save it (Ctrl + S).
4. Open Solidity Compiler from the left sidebar.
5. Select compiler version 0.8.20.
6. Click Compile P15.sol.
7. Open Deploy & Run Transactions.
8. Select Environment: Remix VM.
9. Select Contract: StudentData.
10. Set Value = 0 wei.
11. Click Deploy.
12. Expand StudentData under Deployed Contracts.

FUNCTION EXECUTION:

1. ADD FIRST STUDENT:
   - Find addStudent().
   - Enter id = 101.
   - Enter name = "Rahul".
   - Enter marks = 85.
   - Click Transact.

2. GET STUDENT DETAILS:
   - Find getStudent().
   - Enter index = 0.
   - Click Call.
   - Expected Output: 101, Rahul, 85.

3. GET TOTAL STUDENTS:
   - Click Call beside getCount().
   - Expected Output: 1.

4. ADD SECOND STUDENT:
   - Enter id = 102.
   - Enter name = "Priya".
   - Enter marks = 90.
   - Click Transact beside addStudent().

5. CHECK TOTAL STUDENTS AGAIN:
   - Click Call beside getCount().
   - Expected Output: 2.

6. GET SECOND STUDENT DETAILS:
   - Enter index = 1 in getStudent().
   - Click Call.
   - Expected Output: 102, Priya, 90.

FALLBACK FUNCTION TEST:

1. Find Low level interactions in the deployed
   contract panel.
2. Keep the calldata field empty.
3. Set Value = 0.01 and select Ether.
4. Send the transaction using the available
   Transact button.
5. The payable fallback function should execute
   successfully.

IMPORTANT:
- Use Remix VM for local testing.
- No MetaMask or real Ether is required.
- addStudent() changes contract data, so use Transact.
- getStudent() and getCount() are read-only,
  so use Call.
- Fallback is triggered when a call has unmatched
  function data and no receive() function is defined.
- Do not enter Ether in the Value field when
  calling addStudent().

EXPECTED RESULTS:

First Student: 101, Rahul, 85
Second Student: 102, Priya, 90
Total Students: 2
Fallback Transaction: Successful

IMPORTANT CONCEPTS:

1. STRUCT: Groups related student information.
2. ARRAY: Stores multiple student records.
3. PUSH(): Adds a student to the array.
4. MEMORY: Temporary data location.
5. REQUIRE(): Validates the student array index.
6. FALLBACK: Handles calls with unmatched function data.

GAS FEE OBSERVATION:

- addStudent() requires gas because it modifies data.
- getStudent() and getCount() are view functions.
- Normal Remix VM read calls do not require
  an on-chain transaction fee.
*/
