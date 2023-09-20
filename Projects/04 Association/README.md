# Association Rule Learning

Association rule learning is a type of unsupervised learning technique that checks for the dependency of one data item on another data item and maps accordingly so that it can be more profitable. It tries to find some interesting relations or associations among the variables of dataset. It is based on different rules to discover the interesting relations between variables in the database.

## Types of Association Rule Learning
Association rule learning can be divided into three algorithms:

1. **Apriori Algorithm:**  
This algorithm uses frequent datasets to generate association rules. It is designed to work on the databases that contain transactions. This algorithm uses a breadth-first search and Hash Tree to calculate the itemset efficiently. It is mainly used for market basket analysis and helps to understand the products that can be bought together. It can also be used in the healthcare field to find drug reactions for patients.

2. **FP Growth Algorithm**  
The FP growth algorithm stands for Frequent Pattern, and it is the improved version of the Apriori Algorithm. It represents the database in the form of a tree structure that is known as a frequent pattern or tree. The purpose of this frequent tree is to extract the most frequent patterns.

3. **Eclat Algorithm**  
Eclat algorithm stands for Equivalence Class Transformation. This algorithm uses a depth-first search technique to find frequent itemsets in a transaction database. It performs faster execution than Apriori Algorithm.




## FP Growth vs Apriori

| Algorithm | FP Growth | Apriori |
| --------- | --------- | ------- |
| Pattern Generation | FP growth generates pattern by constructing a FP tree | Apriori generates pattern by pairing the items into singletons, pairs and triplets.|
| Candidate Generation | There is no candidate generation | Apriori uses candidate generation |
| Memory Usage | A compact version of database is saved | The candidates combinations are saved in memory |
| Process | The process is faster as compared to Apriori. The runtime of process increases linearly with increase in number of itemsets. | The process is comparatively slower than FP Growth, the runtime increases exponentially with increase in number of itemsets |
