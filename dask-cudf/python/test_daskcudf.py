import pytest

def test_cluster():
    from dask_cuda import LocalCUDACluster
    from dask.distributed import Client

    cluster = LocalCUDACluster()
    client = Client(cluster)
    # this assumes running on a machine with more than one GPU
    assert len(client.scheduler_info()['workers']) > 1

def test_multicolumn_groupby():
    import cudf, dask_cudf

    tmp_df = cudf.DataFrame()
    tmp_df['id'] = [0, 0, 1, 2, 2, 2]
    tmp_df['val1'] = [0, 1, 0, 0, 1, 2]
    tmp_df['val2'] = [9, 9, 9, 9, 9, 9]

    ddf = dask_cudf.from_cudf(tmp_df, npartitions=2)
    cudfSeries = ddf.groupby(['id', 'val1']).count().compute()

    expectedValues = [1, 1, 1, 1, 1, 1]

    assert len(expectedValues) == len(cudfSeries)

    for (actual, expected) in zip(cudfSeries, expectedValues) :
        assert actual == pytest.approx(expected)
