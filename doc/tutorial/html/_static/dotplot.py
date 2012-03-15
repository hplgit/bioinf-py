def dotplot_list_of_lists(dna_x, dna_y):
    dotplot_matrix = [['0' for x in dna_x] for y in dna_y]
    for x_index, x_value in enumerate(dna_x):
        for y_index, y_value in enumerate(dna_y):
            if x_value == y_value:
                dotplot_matrix[y_index][x_index] = '1'
    return dotplot_matrix

dna_x = 'TAATGCCTGAAT'
dna_y = 'CTCTATGCC'

M = dotplot_list_of_lists(dna_x, dna_x)
for row in M:
    for column in row:
        print column,
    print

def make_string(dotplot_matrix):
    return '\n'.join([' '.join(row) for row in dotplot_matrix])


def make_string_expanded(dotplot_matrix):
    rows = []
    for row in dotplot_matrix:
        row_string = ' '.join(row)
        rows.append(row_string)
    plot = '\n'.join(rows)
    return plot

M2 = [['1', '1', '0', '1'],
     ['1', '1', '1', '1'],
     ['0', '0', '1', '0'],
     ['0', '0', '0', '1']]

s = make_string_expanded(M2)

# end of testing join operations in detail
print '-------------'
M = dotplot_list_of_lists(dna_x, dna_x)
print make_string(M)
print repr(make_string(M))

import numpy as np

def dotplot_numpy(dna_x, dna_y):
    dotplot_matrix = np.zeros((len(dna_y), len(dna_x)), np.int)
    for x_index, x_value in enumerate(dna_x):
        for y_index, y_value in enumerate(dna_y):
            if x_value == y_value:
                dotplot_matrix[y_index,x_index] = 1
    return dotplot_matrix

print dotplot_numpy(dna_x, dna_y)

dna_x = 'ATTGCAGCTTAAGGAATCGTGCAGATTAAAGGCACCACGAATTAAGACCAGGGACATAA'
dna_y = 'ATTGCAGCGGAAGGAATACTGCAGGTTAAAGTCACCAGGAATTCAGACCAGTTTCATAA'
dna_y = 'ATTGCAGCCTAAGGAATCGTGCAGATTAAACTCACCACGAATTAAGACCAGGGACATAT'
p = dotplot_numpy(dna_x, dna_y)
#from matplotlib.pyplot import plot, show
#p = np.eye(60) # test
#x = [i for i in xrange(p.shape[1]) for j in xrange(p.shape[0]) if p[i,j] == 1]
#y = [j for i in xrange(p.shape[1]) for j in xrange(p.shape[0]) if p[i,j] == 1]
#plot(x, y, 'ro')
#show()

# Test
M = dotplot_list_of_lists(dna_x, dna_y)
for i in xrange(p.shape[0]):
    for j in xrange(p.shape[1]):
        assert p[i,j] == int(M[i][j]), '%s vs %s' % (p[i,j], int(M[i][j]))


