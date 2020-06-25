import bootcamp_utils

def check_block_size(block_size):
    """Checks to make sure the block size is an integer >= 0."""
    
    if block_size >= 0 and type(block_size) == int:
        ret_val = True
    else:
        ret_val = False
    
    return ret_val

def make_blocks(seq, block_size):
    """Divides a sequence into blocks of size block_size."""
    
    # Convert sequence to upper case
    seq = seq.upper()
    
    # Check if block size is positive integer
    if not check_block_size(block_size):
        raise RuntimeError('block_size is not a positive integer.')
    
    # Check if block size is larger than sequence length
    if block_size > len(seq):
        raise RuntimeError('Block size is longer than sequence.')
    
    # Initialize list of blocks
    blocks = []
    
    # Initialize counter
    i = 0
    
    while i + block_size <= len(seq):
        blocks.append(seq[i:i+block_size])
        i += block_size

    return tuple(blocks)

def gc_content(block):
    """Gets the GC content of a block of bases."""
    
    # Check for valid sequence
    for b in block:
        if b not in ('A', 'T', 'C', 'G'):
            raise RuntimeError(b + ' is not a valid nucleotide.')
            
    # Calculate GC content
    return (block.count('G') + block.count('C'))/len(block)

def gc_blocks(seq, block_size):
    """Divides a sequence into blocks and computes the GC content for each block, returning a tuple."""
    
    # Make a tuple of blocks
    blocks = make_blocks(seq, block_size)
    
    # Initialize list of block GC contents
    block_gc = []
    
    # Get the GC content of each block
    for block in blocks:
        block_gc.append(gc_content(block))
        
    return tuple(block_gc)