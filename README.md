# mini-cluster with distributed storage fabric 

A toy model of a **self-healing replicated key-value store** built with the goal of understanding Nutanix AOS paradigms.

Modeling the hyperconverged core architecture, storage nodes are equipped with a replication factor, which maintains a data fault tolerance governed by rf - 1. When a node fails the cluster coordinator automatically restores the node back to the specified replication factor with no human intervention.

## Quick start

'''bash
python demo.py # walk through of the self-healing component
python -m pytest -v # run invariant tests (200-step chaos test) for QE purposes
'''

## What it does

