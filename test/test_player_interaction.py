from game2048.player_interaction import *
from pytest import *

def test_player_setup(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "0")
    assert player_setup() == "0"
    monkeypatch.setattr('builtins.input', lambda x: "4")
    assert player_setup() == None

def test_get_player_direction(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "d")
    assert get_player_direction() == 0
    monkeypatch.setattr('builtins.input', lambda x: "h")
    assert get_player_direction() == 2
