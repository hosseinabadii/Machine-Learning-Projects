# Apriori algorithm

Apriori algorithm is a popular algorithm for extracting **frequent itemsets** with applications in **association rule learning**. The apriori algorithm has been designed to operate on databases containing transactions, such as purchases by customers of a store. An itemset is considered as "frequent" if it meets a user-specified support threshold. For instance, if the support threshold is set to 0.5 (50%), a frequent itemset is defined as a set of items that occur together in at least 50% of all transactions in the database.

## Drawbacks

The two primary drawbacks of the Apriori Algorithm are: 

- At each step, candidate sets have to be built.
- To build the candidate sets, the algorithm has to repeatedly scan the database.
