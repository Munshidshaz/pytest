from main import get_weather


def test_get_weather():
    assert get_weather(21) == "hot"
    assert get_weather(-1) == "cold"
    assert get_weather(22.2) == "hot"
    assert get_weather(-5.1) == "cold"
    assert get_weather(10) == "cold"
