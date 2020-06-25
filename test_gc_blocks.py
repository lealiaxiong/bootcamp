import pytest

import gc_blocks 

# Test check_blocks

def test_check_block_size_for_integer():
    """Perform unit tests on check_block_size for integer block size"""
    assert gc_blocks.check_block_size(6) == True
    assert gc_blocks.check_block_size(3) == True
    assert gc_blocks.check_block_size(0) == True
    
def test_check_block_size_for_float():
    """Perform unit tests on check_block_size for floats"""
    assert gc_blocks.check_block_size(4.6) == False
    
def test_check_block_size_for_negative():
    """Perform unit tests on check_block_size for negative numbers"""
    assert gc_blocks.check_block_size(-5) == False
    assert gc_blocks.check_block_size(-4.3) == False


# Test make_blocks

def test_make_blocks_for_empty_seq():
    """Perform unit tests on make_blocks for empty seq"""
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.make_blocks('', 1) == ()
    excinfo.match("Block size is longer than sequence.")
    
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.make_blocks('', 7) == ()
    excinfo.match("Block size is longer than sequence.")
    
def test_make_blocks_for_single_nucleotide():
    """Perform unit tests on make_blocks for empty seq"""
    assert gc_blocks.make_blocks('C', 1) == ('C',)
    assert gc_blocks.make_blocks('A', 1) == ('A',)
    
def test_make_blocks_for_noninteger_block_size():
    """Perform unit tests on make_blocks for noninteger block_size"""
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.make_blocks('ACTGCTAGA', 3.6)
    excinfo.match("block_size is not a positive integer.")
    
def test_make_blocks_for_negative_block_size():
    """Perform unit tests on make_blocks for noninteger block_size"""
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.make_blocks('ACTGCTAGA', -3.6)
    excinfo.match("block_size is not a positive integer.")
    
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.make_blocks('ACTGCTAGA', -5)
    excinfo.match("block_size is not a positive integer.")
    
def test_make_blocks_for_short_sequences():
    """Perform unit tests on make_blocks for short sequences"""
    assert gc_blocks.make_blocks('atgactacgt', 4) == ('ATGA', 'CTAC')
    
def test_make_blocks_for_long_block():
    """Perform unit tests on make_blocks for when the block size is longer than the sequence"""
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.make_blocks('ATGACTAGCTAGC', 20)
    excinfo.match("Block size is longer than sequence.")
    
# Test gc_content

def test_gc_content_single_nucleotide():
    """Perform unit tests on gc_content for single nucleotide"""
    assert gc_blocks.gc_content('C') == 1/1
    assert gc_blocks.gc_content('G') == 1/1
    assert gc_blocks.gc_content('A') == 0
    assert gc_blocks.gc_content('T') == 0
    
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.gc_content('Z')
    excinfo.match("Z is not a valid nucleotide.")
    
def test_gc_content_short_sequences():
    """Perform unit test on gc_content for short sequences"""
    assert gc_blocks.gc_content('CGACGGGA') == 6/8
    assert gc_blocks.gc_content('CGGGACGGA') == 7/9
    
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.gc_content('ACTTACZGGAC')
    excinfo.match("Z is not a valid nucleotide.")
    
# Test gc_blocks
    
def test_gc_blocks_single_nucleotide():
    """Perform unit tests on gc_blocks for single nucleotide"""
    assert gc_blocks.gc_blocks('C', 1) == (1/1,)
    assert gc_blocks.gc_blocks('G', 1) == (1/1,)
    assert gc_blocks.gc_blocks('A', 1) == (0,)
    assert gc_blocks.gc_blocks('T', 1) == (0,)
    
def test_gc_blocks_for_empty_seq():
    """Perform unit tests on gc_blocks for empty seq"""
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.gc_blocks('', 1) == ()
    excinfo.match("Block size is longer than sequence.")
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.gc_blocks('', 50) == ()
    excinfo.match("Block size is longer than sequence.")
    
def test_gc_blocks_short_sequences():
    """Perform unit tests on gc_blocks for short sequence"""
    assert gc_blocks.gc_blocks('ATGACTACGT', 4) == (0.25, 0.5)
    
def test_gc_blocks_for_long_block():
    """Perform unit tests on gc_blocks for when the block size is longer than the sequence"""
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.gc_blocks('ATGACTAGCTAGC', 20)
    excinfo.match("Block size is longer than sequence.")
    
def test_gc_blocks_lowercase():
    """Perform unit tests on number_negative for lowercase"""
    assert gc_blocks.gc_blocks('atgactacgt', 4) == (0.25, 0.5) # We want the function to be agnostic to case
    
def test_gc_blocks_invalid_amino_acid():
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.gc_blocks('B', 1)
    excinfo.match("B is not a valid nucleotide.")
    
    with pytest.raises(RuntimeError) as excinfo:
        gc_blocks.gc_blocks('ATGACTBCGT', 4)
    excinfo.match("B is not a valid nucleotide.")