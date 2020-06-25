import pytest
import seq_features

def test_number_negatives_for_single_AA():
    """Perform unit tests on number_negative for single AA"""
    assert seq_features.number_negatives('E') == 1
    assert seq_features.number_negatives('D') == 1


def test_number_negatives_for_empty():
    """Perform unit tests on number_negative for empty entry"""
    assert seq_features.number_negatives('') == 0


def test_number_negatives_for_short_sequence():
    """Perform unit tests on number_negative for short sequence"""
    assert seq_features.number_negatives('ACKLWTTAE') == 1
    assert seq_features.number_negatives('DDDDEEEE') == 8


def test_number_negatives_for_lowercase():
    """Perform unit tests on number_negative for lowercase"""
    assert seq_features.number_negatives('acklwttae') == 1
    
def test_number_negatives_for_invalid_amino_acid():
    with pytest.raises(RuntimeError) as excinfo:
        seq_features.number_negatives('B')
    excinfo.match("B is not a valid amino acid.") # This is what we want the interpreter to say in this case.