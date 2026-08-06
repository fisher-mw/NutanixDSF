"""
Single node in a cluster

One server in a Nutanix cluster. It has local storage, (in this case a plain dict) and can be healthy or down. 
In a real cluster the Controler Virtual Machine woudl serve I/O for the node's disks; here the Node plays both 
roles at once since there is no hypervisor to model
"""

from future import __annotations__

class Node:
    def __init__(self, node_id: str) -> None:
        self.node_id = node_id
        self._data = dict[str,str] = {}
        self.alive = True
        
#------Storage Operations-------
