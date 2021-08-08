## **Competitive Analysis** 

### Based on Industry groups,Descriptions and Location of the Company 


- 4000 startups with their industry groups, description and location were collated to form a corpus.

- **Topic modelling**  using BERTopic was performed on the corpus. This resulted in a probabilty matrix of dimension =  (number of startups) * (number of topics) 

- To visualise how saturated a market space is, UMAP algorithm was used to reduce the matrix into 2 dimensional embeddings which preserves local as well as global distance thus giving meaning to the distance between each embedding.

- Visualization is done using a scatter plot where the user can visualize how saturated the market is with respect for to the startup they are investigating.

- The user has options to input metrics about the company they are interested in and select the states for which they want to analyse the competition. 

- The more clustered different points are, the saturated the domain is.

- Outliers indicate that the market is either untapped or is not viable for introducing new product.