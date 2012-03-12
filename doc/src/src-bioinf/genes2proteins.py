def simple_genetic_code_v1(filename):
    infile = open(filename, 'r')
    genetic_code = {}
    for line in infile:
        columns = line.split()
        print columns
        genetic_code[columns[0]] = columns[1]
    return genetic_code

import urllib, os
urlbase = 'http://hplgit.github.com/bioinf-py/data/'
genetic_code_file = 'genetic_code.tsv'
if not os.path.isfile(genetic_code_file):
    url = urlbase + genetic_code_file
    urllib.urlretrieve(url, filename=genetic_code_file)

code = simple_genetic_code_v1('genetic_code.tsv')
print code['UUC'], code['UUG']

def simple_genetic_code_v2(filename):
    return dict([line.split()[0:2] for line in open(filename, 'r')])

code2 = simple_genetic_code_v2('genetic_code.tsv')
assert code == code2

def complex_genetic_code_v1(filename):
    genetic_code = {}
    for line in open(filename, 'r'):
        columns = line.split()
        genetic_code[columns[0]] = {}
        genetic_code[columns[0]]['1-letter']   = columns[1]
        genetic_code[columns[0]]['3-letter']   = columns[2]
        genetic_code[columns[0]]['amino acid'] = columns[3]
    return genetic_code

def complex_genetic_code_v2(filename):
    genetic_code = {}
    for line in open(filename, 'r'):
        c = line.split()
        genetic_code[c[0]] = {
            '1-letter': c[1], '3-letter': c[2], 'amino acid': c[3]}
    return genetic_code

code = complex_genetic_code_v1('genetic_code.tsv')
print code['UUC']
print code['UUG']

code2 = complex_genetic_code_v2('genetic_code.tsv')
assert code == code2

name = 'UUC'
print '%s translates into the amino acid "%s" with "%s" '\
      'as 3-letter code.' % \
      (name, code[name]['amino acid'], code[name]['3-letter'])

def read_dnafile_v1(filename):
    lines = open(filename, 'r').readlines()
    # Remove newlines in each line and join
    dna = ''.join([line.strip() for line in lines])
    return dna

lactase_gene_file = 'lactase_gene.txt'
if not os.path.isfile(lactase_gene_file):
    url = urlbase + lactase_gene_file
    urllib.urlretrieve(url, filename=lactase_gene_file)

lactase_gene = read_dnafile_v1(lactase_gene_file)
print '10 first bases of the lactase gene: ', lactase_gene[:10]

lactase_exon_file = 'lactase_exon.tsv'
if not os.path.isfile(lactase_exon_file):
    url = urlbase + lactase_exon_file
    urllib.urlretrieve(url, filename=lactase_exon_file)

def read_exon_positions_v1(filename):
    positions = []
    infile = open(filename, 'r')
    for line in infile:
        start, end = line.split()
        start, end = int(start), int(end)
        positions.append((start, end))
    infile.close()
    return positions

def read_exon_positions_v2(filename):
    return [tuple(int(x) for x in line.split())
            for line in open(filename, 'r')]

lactase_exon_positions = read_exon_positions_v2(lactase_exon_file)
lactase_exon_positions1 = read_exon_positions_v1(lactase_exon_file)
assert lactase_exon_positions == lactase_exon_positions1
