import pytest

from src.velocity import velocity_on_geoid


def test_velocity():

    x = velocity_on_geoid(
    lat1=52.271572, lon1=20.984068,
    lat2=52.2687, lon2=21.037813, 
    date1='2020-11-27 16:00:19', 
    date2='2020-11-27 16:21:19')

