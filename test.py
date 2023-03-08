from lib import spotify
from lib import ip
from commands import network, cpu, misc, memory
from config import SPOTIFY_TOKEN

def test_spotify():
    spotty = spotify.Spotify(SPOTIFY_TOKEN)
    print(spotty.get_currently_playing())

def test_public_ip_lib():
    test = ip.Ip()
    print(test.get_public_ip_info())

def test_local_ip_lib():
    test = ip.Ip()
    print(test.get_local_ip())


def test_network():
    test = network.Network()
    test.public_ip("#fff68f", "#fff68f")
    test.local_ip("#fff68f", "#fff68f")

def test_cpu():
    test = cpu.Cpu()
    test.cpu_load("#100089", "#fff68f")

def test_time():
    test = misc.Misc()
    test.get_time("#100089", "#fff68f")

def test_memory():
    test = memory.Memory()
    test.get_available_amount("#fff68f", "#fff68f")
    test.get_pretty("#fff68f", "#fff68f")
    test.get_memory_load("#fff68f", "#fff68f")
    test.get_total_amount("#fff68f", "#fff68f")


test_spotify()
test_public_ip_lib()
test_local_ip_lib()
test_network()
test_cpu()
test_time()
test_memory()
