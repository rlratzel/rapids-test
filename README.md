# rapids-test

This repo is for integration tests for [nightly RAPIDS conda packages](https://anaconda.org/rapidsai-nightly).

Test scripts focus on confirming functioning interaction between cross-project APIs.

For example:

1. Loading CSV data with cuStrings columns into a cuDF
2. Finding DBSCAN clusters from a cuDF.
3. Creating a DMatrix and training an XGBoost model from a cuDF.
4. Creating a dask-cuda cluster and running a multi-column groupby over cuDF partitions.
