# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

firstly a big pro is that all boats will have about the same amount of Data, so that only one boat running out of space and creatings errors isn't likley. In contrast Random Partitioning makes quiring more complex and time intensive since all boats would need to be quired.

## Partitioning by Hour

Partitioning by Hour will lead to wasted space, at the time where, most likley the first boat, runs out of space there would be more space available on the second boat but sticking to the distribution of the Data, will not be used. From the researchers side it will be easier and quicker to query since the location of the data is clear.

## Partitioning by Hash Value

This approach is closer to distributing randomly and will ensure that the space across all three boats is evenly used. Using Hashes makes it easy to query for single entries but still makes it time consumning for batches since all boats need to be queried for it. 
