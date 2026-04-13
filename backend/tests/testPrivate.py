from private import classifyWeather

def test_classify_weather_cold():
    assert classifyWeather(-2) == "cold"

def test_classify_weather_hot():
    assert classifyWeather(20) == "hot"

def test_classify_weather_boundary():
    assert classifyWeather(-1) == "cold"

def test_classify_weather_warm():
    assert classifyWeather(10) == "warm"

def test_classify_weather_hot():
    assert classifyWeather(16) == "hot"
