# mini-cluster with distributed storage fabric 

A toy model of a **self-healing replicated key-value store** built with the goal of understanding Nutanix AOS paradigms.

Modeling the hyperconverged core architecture, storage nodes are equipped with a replication factor, which maintains a data fault tolerance governed by rf - 1. When a node fails the cluster coordinator automatically restores the node back to the specified replication factor with no human intervention.

## Quick start

'''bash
python demo.py # walk through of the self-healing component
python -m pytest -v # run invariant tests (200-step chaos test) for QE purposes
'''

## What it does
- Store each key on RF number of nodes
- Ensure redundancy by detecting under-replicated keys after node failures
- Self-heal by re-replicating at-risk data onto healthy nodes to restore RF

## Why I chose to build this
|This project | Nutanix concept |
|---|---|
|'Node'| A cluster node's storage |
| 'Coordinator' | The distributed storage fabric |
| Replication factor | Same for both |
| heal() | Self-healing and data re-protection |
| Hash-offset placement | Sharding |

## What it is lacking 
- Asynchronous healing (heartbeat protocols)
- Hashring to minimize resuffling after a new node is added
- Node failure is on/off, no partial fails or split brain procedures
