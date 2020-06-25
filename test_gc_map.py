import gc_map

def test_gc_map_short_sequences():
    """Performs unit test on gc_map for short sequences."""
    assert gc_map.gc_map('ATGACTACGT', 4, 0.4) == 'atgaCTAC'
    assert gc_map.gc_map('ATGACTACGT', 4, 0.5) == 'atgaCTAC' # Must be greater than or equal to the threshold