from movie_extract.movie_e import ice_breaking, gen_url, req, get_key, req2df, df2parquet

def test_ib():
    ice_breaking()

def test_req2df():
    req2df()

def test_df2parquet():
    df2parquet()
