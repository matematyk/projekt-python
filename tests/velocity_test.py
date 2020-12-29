import pytest

from src.velocity import velocity_on_geoid


def test_velocity():
    lon1 = 20.981478
    lat1 = 52.27493
    date1 = "2020-12-23 23:11:43"
    lon2 = 20.983717
    lat2 = 52.27217
    date2 = "2020-12-23 23:12:15"
    y = velocity_on_geoid(lat1, lon1, lat2, lon2, date1, date2)
    print(y)

    x = velocity_on_geoid(
        lat1=52.271572, lon1=20.984068,
        lat2=52.2687, lon2=21.037813, 
        date1='2020-11-27 16:00:19', 
        date2='2020-11-27 16:21:19'
    )

