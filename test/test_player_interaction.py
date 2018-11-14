from game2048.player_interaction import *
from pytest import *

def test_player_theme(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "0")
    assert player_setup_theme() == "0"
    monkeypatch.setattr('builtins.input', lambda x: "4")
    assert player_setup_theme() == None

def test_get_player_direction(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "d")
    assert get_player_direction() == 0
    monkeypatch.setattr('builtins.input', lambda x: "h")
    assert get_player_direction() == 2

def test_player_setup_size(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 4)
    assert player_setup_size() == 4
    monkeypatch.setattr('builtins.input', lambda x: 2)
    assert player_setup_size() == 2
