# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    #check that ACTG is properly transcribed to => ACUG
    assert transcribe("ACTG")=="ACUG"


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    #check that ACTG is properly transcribed and then reversed to => GUCA
    assert reverse_transcribe("ACTG")=="GUCA"
