// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ThreatLog {

    struct Threat {
        string org;
        string message;
        uint timestamp;
    }

    Threat[] public threats;

    function addThreat(string memory _org, string memory _msg) public {
        threats.push(Threat(_org, _msg, block.timestamp));
    }

    function getThreats() public view returns (Threat[] memory) {
        return threats;
    }
}