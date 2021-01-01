from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    assert encrypt("hello world",2)=='jgnnq yqtnf'
    assert encrypt('hello what is your name we are',4)=='lipps alex mw csyv reqi ai evi'

def test_decrypt():
    assert decrypt("jgnnq yqtnf",2)=='hello world'
    assert decrypt("lipps alex mw csyv reqi ai evi",4)=='hello what is your name we are'
def test_hack():
    assert hack("jgnnq yqtnf")=='hello world'
    assert hack("lipps alex mw csyv reqi ai evi")=='hello what is your name we are'

