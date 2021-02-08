import requests

import src.mwprojekt.collect as col 

class MockResponse:

    @staticmethod
    def json():
        return {"result":{"0":{"Lines":"15","Lon":20.980501,"VehicleNumber":"1165+1164","Time":"2020-12-23 23:07:33","Lat":52.27523,"Brigade":"4"},"1":{"Lines":"22","Lon":20.943531,"VehicleNumber":"1229+1230","Time":"2020-12-23 23:00:23","Lat":52.272167,"Brigade":"12"},"2":{"Lines":"35","Lon":21.023636,"VehicleNumber":"1255+1256","Time":"2020-12-23 23:07:35","Lat":52.18334,"Brigade":"12"},"3":{"Lines":"6","Lon":21.084118,"VehicleNumber":"1268","Time":"2020-12-23 23:07:35","Lat":52.245308,"Brigade":"015"}}}


def test_get_json(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    resource_id, api_key, save, date = "xyz", "test", False, "2020-12-23 23:07:35"

    result = col.collect_from_api(resource_id, api_key, save, date)
    assert result == 0 