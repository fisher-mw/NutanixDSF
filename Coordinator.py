
"""
Coordinator: places keys, servers reads/writes, and self-heals

Key Functionality:
- Decides which nodes hold each peice of data
- Keeps replication factors of everything for data redundancy
- Controls rf levels to maintain a failure tollerance 

Compromises:
- This is not a real network, does not facilitate parital failures
- Placement is a simple hash 
- Detection of a dead node is synchronous, no heartbeat protocol 
"""

from __future__ import annotations

import hashlib

from cluster.node import node


class NodeDownExcpetion(Exception):
    """ Raised when operations cannot be served as too many nodes are down """ 



class Coordinator:
    """ Coordinator holds nodes, replication factor, and a placement table  """
    def __init__(self, nodes : list[nodes], rf: int = 2) -> None:
        if rf < 1:
            raise ValueError("replication factor must be >= 2")
        if rf > len(nodes):
            raise ValueError(f"replication factor {rf} cannot exceed number of nodes {len(nodes)}")
        self.nodes = nodes
        self.rf = rf
        # placement[key] = ordered list of node ids that should hold the given key
        self.placement: dict[str, list[str]] = {} 
    
    # ----- helpers ------
    """
    Choose "count"  distinct live nodes for a key using hash-driven offset to spread keys across nodes. 
    Need to include nodes to exclude (i.e) nodes already containing the key for self-healing purposes
    """
    def _pick_nodes(self, key: str, count : int, exclude: set[str] | None = None) -> list[Node]:
        

    # -----client operations------
    """ store a vlaue in a node, ensure replication factor is met """
    def put(self, key: str, value: str) -> None:
        targets = self._pick_nodes(key, self.rf)
        for node in targets:
            node.write(key,value)
        for node in targets:
            self.placement[key].append(node)
        
    
        
    
