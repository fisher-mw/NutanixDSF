"""
Single storge node in a cluster

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

    """ store one of the RF copies that exists across the cluster """
    def write(self, key:str, value:str) -> None:
        self._data[key] = value
    """ drop this nodes replica of the key (we need this when rebalancing) """
    def delete(self, key:str) -> None:
        self._data.pop(key, None)
    
    def holds(self, key:str) -> bool:
        return key in self._data
    
    """ all keys this node currently stores """
    def keys(self) -> set[str]:
        return set(self._data.keys())

    def read(self, key:str) -> str:
        return self._data.get(key)


    # ----- add functions for failure simulation -----
    # need kill, revive, and repair 
    """ simulate node failure, data does not clear, simply unreachable """
    def kill(self) -> None:
        self.alive = False
    
    """ brings failed node back to life with data intact """
    def revive(self) -> None:
        self.alive = True

    def repair(self) -> str:
        if self.alive:
            status = "Up"
        else:
            status = "Down"
        return f"Node {self.node_id} currently {status} with {len(self._data.keys())} keys"