import urllib, os

# Task 1: read data for the lactase gene and its exon regions

urlbase = 'http://hplgit.github.com/bioinf-py/data/'

def download(urlbase, filename):
    if not os.path.isfile(filename):
        url = urlbase + filename
        urllib.urlretrieve(url, filename=filename)

def read_dnafile_v1(filename):
    lines = open(filename, 'r').readlines()
    # Remove newlines in each line and join
    dna = ''.join([line.strip() for line in lines])
    return dna

def read_exon_regions_v2(filename):
    return [tuple(int(x) for x in line.split())
            for line in open(filename, 'r')]

lactase_gene_file = 'lactase_gene.txt'
download(urlbase, lactase_gene_file)
lactase_gene = read_dnafile_v1(lactase_gene_file)
lactase_exon_file = 'lactase_exon.tsv'
download(urlbase, lactase_exon_file)
lactase_exon_regions = read_exon_regions_v2(lactase_exon_file)

# Task 2: extract the exon regions in one string and find
# the proportion of bases (letters)

def get_exons(dna, exon_regions):
    return ''.join([dna[start:end] for start, end in exon_regions])

lactase_exon_dna = get_exons(lactase_gene, lactase_exon_regions)

lactase_exon_A_freq = lactase_exon_dna.count('A')/\
                      float(len(lactase_exon_dna))
# or

def get_base_frequencies_v2(dna):
        return {base: dna.count(base)/float(len(dna))
                for base in 'ATGC'}

def print_frequencies(frequencies):
    return ', '.join(['%s: %.2f' % (base, frequencies[base])
                      for base in frequencies])

lactase_exon_freqs2 = get_base_frequencies_v2(lactase_exon_dna)
assert lactase_exon_freqs2['A'] == lactase_exon_A_freq
print 'Proportion of bases in exons:   ', print_frequencies(lactase_exon_freqs2)

# Task 3: extract the introns (regions between the exons) in one string
# and find the proportion of bases (letters)

def get_introns(dna, exon_regions):
    s = ''
    prev_end = 0
    for start, end in exon_regions:
        s += dna[prev_end:start]
        prev_end = end
    s += dna[end:]
    return s

lactase_intron_dna = get_introns(lactase_gene, lactase_exon_regions)
lactase_intron_freqs = get_base_frequencies_v2(lactase_intron_dna)
print 'Proportion of bases in introns: ', print_frequencies(lactase_intron_freqs)

