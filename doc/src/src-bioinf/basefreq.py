def get_base_counts(dna):
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in dna:
        counts[base] += 1
    return counts

def get_base_frequencies(dna):
    counts = get_base_counts(dna)
    return {base: count*1.0/len(dna)
            for base, count in counts.items()}

dna = 'ACCAGAGT'
frequencies = get_base_frequencies(dna)

def print_frequencies(frequencies):
    return ', '.join(['%s: %.2f' % (base, frequencies[base])
                      for base in frequencies])

print "Base frequencies of sequence '%s':\n%s" % \
      (dna, print_frequencies(frequencies))

# Real data
import urllib, os
yeast_file = 'yeast_chr1.txt'
if not os.path.isfile(yeast_file):
    url = 'http://hplgit.github.com/bioinf-py/doc/src/data/%s'\
          % yeast_file
    urllib.urlretrieve(url, filename=yeast_file)

def read_dnafile_v1(filename):
    lines = open(filename, 'r').readlines()
    # Remove newlines in each line and join
    dna = ''.join([line.strip() for line in lines])
    return dna

def read_dnafile_v2(filename):
    dna = ''
    for line in open(filename, 'r'):
        dna += line.strip()
    return dna

dna = read_dnafile_v2(yeast_file)
yeast_freq = get_base_frequencies(dna)
print "Base frequencies of yeast DNA (length %d):\n%s" % \
      (len(dna), print_frequencies(yeast_freq))

assert get_base_frequencies(read_dnafile_v1(yeast_file)) == \
       get_base_frequencies(read_dnafile_v2(yeast_file))
