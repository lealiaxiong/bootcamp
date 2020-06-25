import gc_blocks

def gc_map(seq, block_size, gc_thresh):
    """Divides a sequence into blocks and capitalizes blocks with GC content greater than or equal to the threshold."""
    
    blocks = gc_blocks.make_blocks(seq, block_size)
    
    block_gc_content = gc_blocks.gc_blocks(seq, block_size)
    
    # Initialize final sequence
    seq_analyzed = ''
    
    for i, val in enumerate(block_gc_content):
        if val >= gc_thresh:
            seq_analyzed += blocks[i].upper()
        else:
            seq_analyzed += blocks[i].lower()
            
    return seq_analyzed