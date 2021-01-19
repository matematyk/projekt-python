import pytest

import mwprojekt.distance as dist 


def test_velocity():
    x = dist.distance_on_geoid(
        lat1=52.271572, lon1=20.984068,
        lat2=52.2687, lon2=21.037813
    )
    print(x)

    #assert (x > 300)