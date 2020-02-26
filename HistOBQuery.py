import shrimpy
import plotly.graph_objects as go

public_key = '9cb130e5945be81cf9b87cdb7057368652cf0bd78f752becef5114e28cadf07d'
secret_key = '7d764377c8970b104e69e844912b28ed9c644d5b4d1a53118ae021f8c4729279b53c19ba9c51a7500237127eaa5d47f463580c35cb1133c8eb188e2ec4eba74b'
client = shrimpy.ShrimpyApiClient(public_key, secret_key)

historical_orderbooks = client.get_historical_orderbooks(
    'Bittrex',
    'BTC',
    'USD',
    '2019-05-19T00:00:00.000Z',
    '2019-05-20T00:00:00.000Z',
    10
)


