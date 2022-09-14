Thanks SalvaRC and his team for building the GNN network for ENSO forecasting, it helps a lot.
This GroupByRelations is Amendment PatchNorm Code for Graphino (https://github.com/salvaRC/Graphino/) Optimization.
GroupByRelationsV1.py is the first version of nodes grouping, which is full grouping without computing capability balancing: may need long computing time.
GroupByRelationsV2.py is the balanced code which allows the grouping stop when time hyperparameter is reached. It balances the forecast precision and GCU capability and keep the computing time limited.
*GroupByRelationsV3.py is in progressing to optimize the grouping algorithm with networkx package.
graph_conv_layer.py is from original author SalvaRC, and I modified the batchnorm procedure to normalize the dataset per relation groups.
For anything not clear please feel free to contact qinyuxuan@shphschool.com.
2022-9-14
