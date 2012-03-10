# Note on document/approach
# - I have tried to start at examples that could be suited for lecture slides
# - I then continue the examples along the same line. At some point these would
#   anyway be more for tasks (ovinger) for the students
# - I think these discretely- and sequence-oriented examples can be a nice
#   supplement to the current more mathematics-/formula-oriented examples..

# List of data:
# lactase_gene.txt
# lactase_exon_positions.tsv
# yeast_chr1.txt


# *************************************************
# EXAMPLES on list/sequence and looping
# (assumes that basic control (if) has been learned)

# Life is definitely digital. The genetic code of all living organisms are
# represented by a long sequence of simple molecules called nucleotides, or
# bases, which makes up the Deoxyribonucleic acid, or simply DNA. There are only
# four such nucleotides, and the entire genetic code of a human can be seen as a
# simple, though 3 billion long, string of the letters A,C,G,T.

# In this first example, we will simply detect a given letter in a sequence,
# using DNA to learn about strings, lists and looping.

# Could be used in chapter 2 to introduce lists and looping, or in chapter 4 to
# get input from command line.
# Note in relation to ch4: The existing examples on
# raw_input in ch4 starts straight off with numbers and formulas, meaning that
# conversion and eval is needed from the start. The example below would read in
# data (supposed to be some arbitrary DNA) as strings, allowing focusing on data
# input at first, and then later on conversion, eval and exec.

# -------------------------------------------------------------------------------
print '\n*****  Example: Finding positions with specific nucleotide *****\n'
# -------------------------------------------------------------------------------

dna = 'ACGGAGATT' #introduce string
# dna = raw_input()
# dna = open('src/lactaseGene.txt').readline()
i=0
while i<len(dna): #introduce while
    if dna[i] == 'A':
        print 'You got an A! (at position ', i, ')'
    i+=1


dna = 'ACGGAGATT'
for base in dna: #introduce for
    if base == 'A':
        print 'You got an A!'

dna = 'ACGGAGATT'
for i,base in enumerate(dna):
    if base == 'A':
        print 'You got an A! (at position ', i, ')'
       # print 'You got an A! (at position %i)' i

"""
count_v*: Return how many times base appears in the string dna.
"""

http://people.csail.mit.edu/pgbovine/python/tutor.html#mode=visualize

#Online Python Tutorial for the demo above?
Write first .do.txt, copy first part as 3.3, focus: mixing everything and
demonstrating how a problem can be solved in many different ways
other can be exercises (if text else exer...)

def count_v3(dna, base):
    """Return how many times base appears in the string dna."""
    return sum()

def count_v4(dna, base):
    """Return how many times base appears in the string dna."""
    # avoid making list, use sum directly on iterated values
    return sum(c == base for c in dna)


can gj;re timings...

pairs, triples?
Finn alla ATA sequences and their indices

# introduce set comprehension
dna = 'ACGGAGATT'
indicator = [base == 'A' for base in dna]
indicator = [dna[i] == 'A' for i in range(len(dna))]

indiceList = [i for i in range(len(dna)) if dna[i] == 'A']

aCount = len([i for i in range(len(dna)) if dna[i] == 'A'])
aCount = sum([base == 'A' for base in dna])
aCount = dna.count('A') # cheating.. - introduce standard library


# *************************************************
# Your genetic code is (essentially) the same from you are born until you die,
# and the same in your blood and your brain. What makes your cells different are
# which genes are turned on and off. This regulation of genes is orchestrated by
# an immensely complex mechanism, which we have only started to understand. A
# central part of this mechanism consists of molecules called transcription
# factors that float around in the cell and attach to DNA, and in doing so turn
# nearby genes on or off. These molecules bind preferentially to specific DNA
# sequences, and this binding preference pattern can be represented by a matrix
# of frequencies of given symbols at each position of the pattern.

# This example propose several alternative solutions. The basic solutions could
# fit well already into chapter 3, providing training on the use of looping,
# lists and indexing. Other variants make use of dicts, and could thus be used in
# chapter 6, there possibly referring back to the basic exercise in chapter 3, to
# show how dicts can simplify code.

# -------------------------------------------------------------------
print '\n*****  Example: Construct frequency matrix *****\n'
# -------------------------------------------------------------------

# import numpy as np

def construct_FreqMatrix_1(dnaList):
    frequencyMatrix = [[0 for v in dnaList[0]] for x in 'ATGC']

    for dna in dnaList:
      for index, value in enumerate(dna):
          if value == 'A':
              frequencyMatrix[0][index] +=1
          elif value == 'T':
              frequencyMatrix[1][index] +=1
          elif value == 'G':
              frequencyMatrix[2][index] +=1
          elif value == 'C':
              frequencyMatrix[3][index] +=1

    return frequencyMatrix

def construct_FreqMatrix_2(dnaList):

    frequencyMatrix = [[0 for v in dnaList[0]] for x in 'ATGC']
    BpToMatrix = dict([(value, index) for index, value in enumerate('ATGC')])

    for dna in dnaList:
      for index, value in enumerate(dna):
          frequencyMatrix[BpToMatrix[value]][index] +=1

    return frequencyMatrix

def construct_FreqMatrix_3(dnaList):
    dnaLength = max([len(dna) for dna in dnaList])
    frequencyMatrix = dict([(bp, dict([(index,0) for index in range(dnaLength)])) for bp in 'ATGC'])
    BpToMatrix = dict([(value, index) for index, value in enumerate('ATGC')])

    for dna in dnaList:
        for index, value in enumerate(dna):
            frequencyMatrix[value][index] +=1

    return frequencyMatrix

def construct_FreqMatrix_4(dnaList):

    frequencyMatrix = np.zeros((len('ATGC'), len(dnaList[0])))
    BpToMatrix = dict([(value, index) for index, value in enumerate('ATGC')])

    for dna in dnaList:
      for index, value in enumerate(dna):
          frequencyMatrix[BpToMatrix[value]][index] +=1

    return frequencyMatrix


dnaList = ['TAATGC', 'GGATTC', 'GCAAGC', 'AGTTGA', 'CCGGCC']
frequencyMatrix_1=construct_FreqMatrix_1(dnaList)
frequencyMatrix_2=construct_FreqMatrix_2(dnaList)
frequencyMatrix_3=construct_FreqMatrix_3(dnaList)
# frequencyMatrix_4=construct_FreqMatrix_4(dnaList) #  this function needs to be checked


print 'solution1:\n'
for row in frequencyMatrix_1:
    print row
print

print 'solution2:\n'
for row in frequencyMatrix_2:
    print row
print

print 'solution3:\n'
print frequencyMatrix_3

# -------------------------------------------------------------------------------
print '\n*****  Example: Finding consensus from frequency matrix *****\n'
# -------------------------------------------------------------------------------

#  matrix is stored as a list
def find_consensus_1(frequencyMatrix):

    consensus = ''
    for column in range(len(frequencyMatrix[0])):
       maxBp =-1
       maxBpValue = None

       for rowIndex, value in enumerate('ATGC'):
             if frequencyMatrix[rowIndex][column] > maxBp:
                 maxBp = frequencyMatrix[rowIndex][column]
                 maxBpValue = value
             elif frequencyMatrix[rowIndex][column] == maxBp:
                 maxBpValue = '-'

       consensus+= maxBpValue

    return consensus

# matrix is stored as a dict of dicts
def find_consensus_2(frequencyMatrix):

    consensus = ''
    for column in range(len(frequencyMatrix['A'])):
       maxBp =-1
       maxBpValue = None

       for rowIndex, value in enumerate('ATGC'):
             if frequencyMatrix[value][column] > maxBp:
                 maxBp = frequencyMatrix[value][column]
                 maxBpValue = value
             elif frequencyMatrix[value][column] == maxBp:
                 maxBpValue = '-'

       consensus+= maxBpValue


    return  consensus


consensus_1=find_consensus_1(frequencyMatrix_2)
consensus_2=find_consensus_2(frequencyMatrix_3)

print'solution 1:\n'
print consensus_1
print '\nsolution 2:\n'
print consensus_2


# -------------------------------------------------------------------------------
print '\n*****  Example: Scanning matrix *****\n'
# -------------------------------------------------------------------------------

DNA='ATCTGATCAA'
probabilityMatrix={'A': {0: 0.2, 1: 0.2, 2: 0.6, 3: 0.2, 4: 0.2},
                  'C': {0: 0.2, 1: 0.4, 2: 0.0, 3: 0.0, 4: 0.8},
                  'T': {0: 0.2, 1: 0.0, 2: 0.2, 3: 0.6, 4: 0.0},
                  'G': {0: 0.4, 1: 0.4, 2: 0.2, 3: 0.2, 4: 0.0}}

len_window=len(probabilityMatrix['A'])

probabilitiesList=[]
for num in range(len(DNA)-len_window+1):
    substring=DNA[num:num+len_window]

    prob_value=1
    for index, value in enumerate(substring):
       prob_value *=probabilityMatrix[value][index]

    probabilitiesList.append(prob_value)

print probabilitiesList


# *************************************************
# This example could fit into chapter 5. Example of making dot-plot from two
# strings, printing it out as a table.

# Dot-plots are commonly used to visualize the similarity between two protein or
# nucleic acid sequences. They compare two sequences by organizing one sequence
# on the x-axis, and another on the y-axis, of a plot. When both sequences match
# at the same location on the plot, a dot is drawn at the corresponding position,
# In our example a dot is represented by 1. No presence at given location is
# represented by 0. A dot-plot can be manually read to find common patterns
# between two sequences that has undergone several insertions and deletions, and
# it servers as a conceptual basis algorithms that align two sequences in order
# to find evolutionary origin or shared functional parts. Such alignment of
# biological sequences is a particular variant of finding the edit distance
# between strings, which is a general technique, also used for e.g. spell
# correction in search engines.

# -------------------------------------------------------------------------------
print '\n*****  Example: Dot plots from pair of DNA sequences *****\n'
# -------------------------------------------------------------------------------

# Python list version of dotplot-matrix
dnaX = 'TAATGCCTGAAT'
dnaY = 'CTCTATGCC'

dotPlotMatrix = [ ['0' for v in dnaX] for x in dnaY]
for xIndex, xValue in enumerate(dnaX):
   for yIndex, yValue in enumerate(dnaY):
       if xValue == yValue:
           dotPlotMatrix[yIndex][xIndex] = '1'

print '\n'.join([''.join(row) for row in dotPlotMatrix])


# Numpy version of dotplot-matrix
import numpy as np
dnaX = 'TAATGCCTGAAT'
dnaY = 'CTCTATGCC'


dotPlotMatrix = np.zeros((len(dnaY), len(dnaX)))
for xIndex, xValue in enumerate(dnaX):
   for yIndex, yValue in enumerate(dnaY):
       if xValue == yValue:
           dotPlotMatrix[yIndex][xIndex] = 1


print dotPlotMatrix


# *************************************************
# DNA consists of four molecules called nucleotides, or bases, and can be
# represented as a string of the letters A,C,G,T. But this does not mean that all
# four nucleotides need to be similarly frequent. Are some nucleotides more
# frequent than others, say in yeast, as represented by the first chromosome of
# yeast? Also, DNA is really not a single thread, but two threads wound together.
# This wounding is based on a A from one thread binding to a T of the other
# thread, and C binding to G (that is, A will only bind with T, not with C or G).
# Could this fact force groups of the four symbol frequencies to be equal?
# (answer: the A-T and G-C binding does not in principle force certain
# frequencies to be equal, but in practice they usually become so because of
# evolutionary factors related to this pairing).
# The example could be used in connection with chapter 6 to mainly get
# acquainted with dictionaries, but also to read strings, from files.

# -------------------------------------------------------------------------------
print '\n*****  Example: Finding base frequencies *****\n'
# -------------------------------------------------------------------------------

def get_base_counts(dna):
    counts = {'A':0, 'C':0, 'G':0, 'T':0}
    for base in dna:
        counts[base] += 1
    return counts

def get_base_frequencies(dna):
    counts = get_base_counts(dna)
    return dict([(base, count*1.0/len(dna)) for base, count in counts.items()])

frequencies = get_base_frequencies('ACCAGAGT')
print "Base frequencies of sequence 'ACCAGAGT': ", frequencies

yeastChr1 = ''.join(line.strip() for line in open('input/yeast_chr1.txt'))
yeastFrequencies = get_base_frequencies(yeastChr1)
print "Base frequencies of chromosome 1 of yeast: ", yeastFrequencies


# The above might easily crash, because of unforeseen letters that do not
# initially exist as keys in dict. This can be solved by putting the following
# code lines at the start of the for loop:
#
#     if not symbol in frequencies:
#         frequencies[symbol]=0
#
# Or by exchanging the initialization to standard dict in the first line, with a
# special dict from Python standard library where non-existing keys will
# correspond to default values (in this case it defaults to zero due to int being
# sent in):
#     frequencies = defaultdict(int)


# *************************************************
# An important usage of DNA is for cells to store information on their arsenal of
# proteins. These proteins are what makes up the possible functional properties
# of a cell. Proteins are made based on the recipe found in genes. Genes are, in
# essence, only regions of the DNA. These are divided into exons, which are the
# coding regions of the gene, and introns, the regions inbetween. In order for a
# protein to be created, the exon regions are copied out of the DNA, joined
# together and then transcribed into mRNA. mRNA is messenger RNA, which is a
# small DNA-like sequence that is sent to the protein-creating machinery in the
# ribosomes, containing the recipe for a protein. One difference between the
# mRNA and the original DNA is that all T-bases (Thymine) are exchanged with
# U-bases (Uridine). In the ribosome, the mRNA is translated into proteins.
# Here, a genetic code is used to translate triplet of bases, or codons, into
# an amino acid. A protein is made up of a series of amino acids. Interestingly,
# the genetic code, which is the same for most forms of life, contains
# redundancy, i.e. that several codons code for the same aminoacids, as the 64
# possible codons are used to code for only 20 amino acids.

# Here is an example of using the genetic code to create the amino acid sequence
# of the Lactase protein (LPH) using the DNA sequence of the Lactase gene (LCT)
# as template. An important functional property of LPH is as an restriction
# enzyme to cleave the disaccaaride Lactose into two monsaccarides. Lactose is
# most notably found in milk. Organisms lacking the functionality of LPH will
# get digestive problems including elevated osmotic pressure in the intestine
# leading to diarea and referred to as lactose intolerance. Most mammals and
# humans lose their expression of LCT and therefore their ability to digest milk
# when they stop recieving breast milk.


# -------------------------------------------------------------------------------
print '\n*****  Example: Translating genes into proteins *****\n'
# -------------------------------------------------------------------------------

simple_genetic_code = {}
for line in open('input/genetic_code.tsv', 'r'):
    cols = line.split()
    simple_genetic_code[cols[0]] = cols[1]

simple_genetic_code2 = dict( [x.split()[0:2] for x in open('input/genetic_code.tsv', 'r')] )

assert simple_genetic_code == simple_genetic_code2

print "'ACG' translates into the amino acid with '%s' as 1-letter code." % simple_genetic_code['ACG']


complex_genetic_code = {}
for line in open('input/genetic_code.tsv', 'r'):
    cols = line.split()
    complex_genetic_code[cols[0]] = {}
    complex_genetic_code[cols[0]]['1-letter'] = cols[1]
    complex_genetic_code[cols[0]]['3-letter'] = cols[2]
    complex_genetic_code[cols[0]]['amino acid'] = cols[3]

complex_genetic_code2 = {}
for line in open('input/genetic_code.tsv', 'r'):
    cols = line.split()
    complex_genetic_code2[cols[0]] = {'1-letter': cols[1], '3-letter': cols[2], 'amino acid': cols[3]}

assert complex_genetic_code == complex_genetic_code2

print "ACG translates into the amino acid '%s' with '%s' as 3-letter code." % \
    (complex_genetic_code['ACG']['amino acid'], complex_genetic_code['ACG']['3-letter'])


lactase_gene = ''
for line in open('input/lactase_gene.txt'):
    lactase_gene += line.strip()

lactase_gene2 = ''.join([line.strip() for line in open('input/lactase_gene.txt') ])

assert lactase_gene == lactase_gene2

print '10 first bases of the lactase gene: ', lactase_gene[:10]

lactase_exon_positions = []
for line in open('input/lactase_exon_positions.tsv'):
    start, end = line.split()
    start, end = int(start), int(end)
    lactase_exon_positions.append( (start, end) )

lactase_exon_positions2 = [ tuple(int(x) for x in line.split()) for line in open('input/lactase_exon_positions.tsv', 'r') ]

assert lactase_exon_positions == lactase_exon_positions2

print 'Start and end position of the second exon of the lactase gene: ', lactase_exon_positions[1]

# for simplicity's sake, we will consider mRNA as the concatenation of exons,
# allthough in reality, additional base pairs are added to each end.

def write_with_line_sep(filename, output, chars_per_line):
    output_file = open(filename, 'w')
    for i in xrange(len(output)/chars_per_line):
        start = i * chars_per_line
        end = (i+1) * chars_per_line
        output_file.write(output[start:end] + '\n')
        # Alternative: print >>output_file, output[start:end]
    output_file.close()

def create_mRNA(lactase_gene):
    mrna = ''
    for start,end in lactase_exon_positions:
        mrna += lactase_gene[start:end].replace('T','U')
    return mrna

mrna = create_mRNA(lactase_gene)
write_with_line_sep('output/lactase_mrna.txt', mrna, 70)

print '10 first bases of the (coding sequence of the) mRNA for the lactase gene: ', mrna[:10]

def create_protein(mrna, simple_genetic_code):
    protein = ''
    for i in xrange(len(mrna)/3):
        start = i * 3
        end = start + 3
        protein += simple_genetic_code[mrna[start:end]]
    return protein

protein = create_protein(mrna, simple_genetic_code)
write_with_line_sep('output/lactase_protein.txt', protein, 70)

print '10 last amino acids of the erroneous lactase protein: ', protein[-10:]
print 'Lenght of the erroneous protein: ', len(protein)

# This first try to simulate the translation process is incorrect. The problem
# is that the translation always begins with the amino acid Methionine, code
# 'AUG', and ends when one of the stop codons is met. We must thus check for the
# correct start and stop criterias.

def create_protein_fixed(mrna, simple_genetic_code):
    protein_fixed = ''
    trans_start_pos = mrna.find('AUG')
    for i in range(len(mrna[trans_start_pos:])/3):
        start = trans_start_pos + i*3
        end = start + 3
        amino = simple_genetic_code[mrna[start:end]]
        if amino == 'X':
            break
        protein_fixed += amino
    return protein_fixed

protein_fixed = create_protein_fixed(mrna, simple_genetic_code)
write_with_line_sep('output/lactase_protein_fixed.txt', protein_fixed, 70)

print '10 last amino acids of the correct lactase protein: ', protein_fixed[-10:]
print 'Lenght of the correct protein: ', len(protein_fixed)

# One type of lactose intolerance is called "Congenital lactase deficiency".
# This is a rare genetic disorder that causes lactose intolerance from birth,
# and is particularly common in Finland. The disease is caused by a mutation of
# the base in posision 30049 (0-based) of the lactase gene, a mutation from T to
# A. This exercise checks what happens to the protein if this base is mutated.

mutated_lactase_gene = lactase_gene[:30049] + 'A' + lactase_gene[30050:]
mutated_mrna = create_mRNA(mutated_lactase_gene)
write_with_line_sep('output/mutated_lactase_mrna.txt', mutated_mrna, 70)

mutated_protein = create_protein_fixed(mutated_mrna, simple_genetic_code)
write_with_line_sep('output/mutated_lactase_protein.txt', mutated_protein, 70)

print '10 last amino acids of the mutated lactase protein: ', mutated_protein[-10:]
print 'Lenght of the mutated lactase protein: ', len(mutated_protein)

# As we can see, the translation stops prematurely, creating a much smaller
# protein, which will not have the required characteristics of the lactase
# protein.

# A side note:
# A couple of mutations in a region for LCT located in front of LCT (actually in
# the introns of another gene) is the reason for the common lactose intolerance,
# i.e. the one that sets in for adults only. These mutations control the
# expression of the LCT gene, i.e. whether that the gene is turned on or off.
# Interestingly, different mutations have evolved in different regions of the
# world, e.g. Africa and Northern Europe. This is an example of convergent
# evolution, i.e. the acquisition of the same biological trait in unrelated
# lineages. The prevalence of lactose intolerance varies widely, from around 5%
# in northern Europe, to close to 100% in south-east Asia.

# *************************************************
# -------------------------------------------------------------------------------
print '\n*****  Example: Proportion of bases inside and outside exons *****\n'
# -------------------------------------------------------------------------------

# What is the proportion of letter 'A' inside and outside exons of the lactase gene?
#
lactase_exon_dna = ''.join([lactase_gene[start:end] for start, end in lactase_exon_positions])
lactase_exon_freqs = get_base_frequencies(lactase_exon_dna)
print 'Proportion of bases in exons: ', lactase_exon_freqs

lactase_intron_dna = ''
prev_end = 0
for start, end in lactase_exon_positions:
    lactase_intron_dna += lactase_gene[prev_end:start]
    prev_end = end
lactase_intron_dna += lactase_gene[prev_end:]
lactase_intron_freqs = get_base_frequencies(lactase_intron_dna)
print 'Proportion of bases in introns: ', lactase_intron_freqs


# *************************************************
# Could fit into chapter 8 as a random process. Function that takes a string as
# input, chooses a random position, and exchanges the symbol at that location to
# a random base. One may apply this function iteratively to a string, and see
# what one gets. The frequencies should appear completely random after a certain
# amount of iterations.

# -------------------------------------------------------------------------------
print '\n*****  Example: Single nucleotide mutations *****\n'
# -------------------------------------------------------------------------------

import random

def mutate(dna):
    dna_nmer_list = list(dna)
    mutation_site = random.randint(0, len(dna_nmer_list) - 1)
    dna_nmer_list[mutation_site] = random.choice(list('ATCG'))
    return ''.join(dna_nmer_list)

def print_freqs(dna):
    for base in 'AGCT':
       print 'Frequency of %s = %s' % (base, dna.count(base)*1.0/len(dna))

dna = 'ACGGAGATTTCGGTATGCAT'

print 'Starting DNA: ' + dna
print_freqs(dna)

for i in range(10000):
    dna = mutate(dna)

print 'Mutated DNA: ' + dna
print_freqs(dna)

# The observed rate at which mutations occur at a given position in the genome
# depends on the nucleotide at the position but maybe more importantly at the
# surrounding sequence context. There are a number of reasons why the observed
# mutation rates betwen different nucleotides vary. One is that there are
# different mechansism generating transitions from one base to another. Another
# is that the efficiency of the repair mechanism, which is an extensive process
# in living dividing cells, varies for different nucleotides. The surrounding
# context of the position determines to what degree there is a working selection
# pressure. If the position is in a region that excerts a function there will be a
# selective pressure.

# Here, we only look at the nucleotide transitions, and not the surrounding context.
# The mutations of single nucleotides may be modelled as a Markov chain, that
# is, a random process that undergoes transitions between a set of states,
# according to a discrete distribution. More specifically, each transition from
# a specific nucleotide to another has a particular probability. The
# probabilities of the transitions going from a nucleotide (including the
# probability of no change, i.e. a transition to itself) must sum to 1. The
# markov chain can thus be specified by a set of 4x4=16 probabilities.

# In this exercise, one must create a random markov chain, and then mutate a
# sequence according to the markov chain. The set of four random probabilities
# summing to 1 for each nucleotide is created by dividing a interval from 0 to 1
# into four by finding 3 random split points.

def create_random_markov_chain():
    markov = {}
    for from_base in 'ACGT':
       slice_points = sorted([0] + [random.random() for i in range(3)] + [1])
       transition_probs = [slice_points[i+1] - slice_points[i] for i in range(4)]
       markov[from_base] = dict([ (to_base, prob) for to_base, prob in zip('ACGT', transition_probs) ])
    return markov

markov = create_random_markov_chain()
print markov
print markov['A']['T']

# The print_transition_probs function calculates the sum of the probabilities
# going into each particular nucleotide.

def print_transition_probs(markov):
    for to_base in 'ACGT':
       print 'Sum of probabilities for transition to %s = %s' % \
           (to_base, sum(markov[from_base][to_base] for from_base in 'ACGT')/4.0)

print_transition_probs(markov)

# The particular base to transition into is selected by finding a random number
# from 0 to 1 and choosing a transition if the probability of the transition is
# less than the number, iteratively subtracting the probabilities of every unchosen
# transition. The transition is thus correctly selected according to the
# probabilities. This works because the probabilities sum to 1.

def select_to_base(possible_base_transitions):
    rand_0_1 = random.random()
    for to_base, transition_prob in possible_base_transitions:
       if rand_0_1 < transition_prob:
           break
       rand_0_1 = rand_0_1 - transition_prob
    return to_base

def mutate_markov(dna, markov):
    dna_nmer_list = list(dna)
    mutation_site = random.randint(0, len(dna_nmer_list) - 1)
    from_base = dna[mutation_site]
    possible_base_transitions = markov[from_base].items()
    dna_nmer_list[mutation_site] = select_to_base( possible_base_transitions )
    return ''.join(dna_nmer_list)

markov = create_random_markov_chain()
print markov
print_transition_probs(markov)

dna = 'ACGGAGATTTCGGTATGCAT'
print 'Starting DNA: ' + dna
print_freqs(dna)

for j in range(1000):
    dna = mutate_markov(dna, markov)

print 'Mutated DNA: ' + dna
print_freqs(dna)

# One should see that the mutated DNA should contain more nucleotides of the
# ones where the sum of probabilities transitioning into the nucleotide, is
# largest (i.e. the output of the print_transition_probs function).


# *************************************************
# Example related to chapter 9, tying together various simple code snippets, as
# well as some code written for previous exercises. The classes are used to
# model the transcription and/or translation process, as explained previsouly.
# The __init__ function of Gene gets the DNA sequence of the gene, and the
# relative location of the exons within that gene. The Gene object creates and
# holds Exon objects, accordingly. There are different subclasses of genes:
# NoncodingGene, and ProteinCodingGene. A noncoding gene only makes RNA, but not
# proteins. The abstract method get_product() is overwritten for the different
# Gene subclasses. The method get_product_len() is inherited, and works on the
# results of the get_product(), the implementation of which changes with the
# class. This is thus an example of polymorphism.

# --------------------------------------------------------------------------------------------
print '\n*****  Example: Translating genes into proteins *****\n'
# --------------------------------------------------------------------------------------------

class Exon(object):
    def __init__(self, dna, start, end):
        self.exon_dna = dna[start:end]

    def get_dna(self):
        return self.exon_dna

class Gene(object):
    def __init__(self, dna, exon_positions):
        self.dna = dna
        self.exons = []
        for exon_start, exon_end in exon_positions:
            self.exons.append(Exon(dna, exon_start, exon_end))

    def get_dna(self):
        return self.dna

    def get_dna_len(self):
        return len(self.get_dna())

    def get_exon_dna(self):
        return ''.join([exon.get_dna() for exon in self.exons])

    def get_exon_dna_len(self):
        return len(self.get_exon_dna())

    def get_rna(self):
        return self.get_exon_dna().replace('T', 'U')

    def get_rna_len(self):
        return len(self.get_rna())

    def get_product(self):
        raise Exception('Gene superclass has no product.')

    def get_product_len(self):
        return len(self.get_product())

class NoncodingGene(Gene):
    def get_product(self):
        return self.get_rna()

class ProteinCodingGene(Gene):
    def __init__(self, dna, exon_positions, simple_genetic_code):
        Gene.__init__(self, dna, exon_positions)
        self.simple_genetic_code = simple_genetic_code

    def get_product(self):
        return create_protein_fixed(self.get_rna(), self.simple_genetic_code)


gene_dna = ''.join([line.strip() for line in open('input/lactase_gene.txt') ])
exon_positions = [[int(pos) for pos in line.split()] for line in open('input/lactase_exon_positions.tsv')]

print
gene = Gene(gene_dna, exon_positions)
print 'gene.get_dna()[0:10]: %s, len=%s: ' % (gene.get_dna()[0:10], gene.get_dna_len())
print 'gene.get_exon_dna()[0:10]: %s, len=%s: ' % (gene.get_exon_dna()[0:10], gene.get_exon_dna_len())
print 'gene.get_rna()[0:10]: %s, len=%s: ' % (gene.get_rna()[0:10], gene.get_rna_len())
print

noncoding_gene = NoncodingGene(gene_dna, exon_positions)
print 'noncoding_gene.get_dna()[0:10]: %s, len=%s: ' % \
    (noncoding_gene.get_dna()[0:10], noncoding_gene.get_dna_len())
print 'noncoding_gene.get_exon_dna()[0:10]: %s, len=%s: ' % \
    (noncoding_gene.get_exon_dna()[0:10], noncoding_gene.get_exon_dna_len())
print 'noncoding_gene.get_rna()[0:10]: %s, len=%s: ' % \
    (noncoding_gene.get_rna()[0:10], noncoding_gene.get_rna_len())
print 'noncoding_gene.get_product()[0:10]: %s, len=%s: ' % \
    (noncoding_gene.get_product()[0:10], noncoding_gene.get_product_len())
print

protein_coding_gene = ProteinCodingGene(gene_dna, exon_positions, simple_genetic_code)
print 'protein_coding_gene.get_dna()[0:10]: %s, len=%s: ' % \
    (protein_coding_gene.get_dna()[0:10], protein_coding_gene.get_dna_len())
print 'protein_coding_gene.get_exon_dna()[0:10]: %s, len=%s: ' % \
    (protein_coding_gene.get_exon_dna()[0:10], protein_coding_gene.get_exon_dna_len())
print 'protein_coding_gene.get_rna()[0:10]: %s, len=%s: ' % \
    (protein_coding_gene.get_rna()[0:10], protein_coding_gene.get_rna_len())
print 'protein_coding_gene.get_product()[0:10]: %s, len=%s: ' % \
    (protein_coding_gene.get_product()[0:10], protein_coding_gene.get_product_len())


# *************************************************
# When the human genome was sequenced, it turned out that a large part of the
# genome did not seem to serve any specific function. Only around 3% of the
# genome were directly coding for proteins, which is the primary purpose of DNA,
# and referred to as the central dogma of molecular biology. The remaining DNA
# were then often referred to as junk DNA. Although a much larger part of the
# genome has since been understood to perform important functions, a relatively
# large part of our DNA still have no known function. Some of this DNA has a
# very simple, repetitive structure, and is even not of human origin. This is
# referred to as repeating elements. Part of this is for instance the remains of
# viruses that integrated into the DNA of our early ancestors without causing
# any apparent damage. However, although these repeating element typically have
# a simple structure and a non-human origin, this does not necessarily mean they
# today do not serve any function. A basic question to ask, is how much these
# repeating elements fall inside genes. The example doesn't really fit into a
# specific chapter, but could be a small project as a summary example, putting
# different teqhniques together. It involves lists, numpy vectors, looping,
# compound looping, object-orientation, algorithmic thinking, and alternative
# paths to same goal. It also turns out to be a bit more tricky than it may
# appear at first sight. This is more thoroughly described (in norwegian) along
# with input data, hints, and suggested solutions here:
# http://invitro.titan.uio.no/wiki/hyperbrowser/doku.php/public:programming_day
#
# This project needs the following files:
# HumanRepeatsChr1.tsv
# HumanGenesChr1.tsv
# HumanRepeatsChr1Starts.memmap
# HumanRepeatsChr1Ends.memmap
# HumanGenesChr1Starts.memmap
# HumanGenesChr1Ends.memmap


# Get data:
# a) Read intervals (repeating elements and genes) from two tabular files and
#     calculate the total overlap of intervals.
# b) Read numpy-vectors

# Represent data:
# a) As 4 separate lists (start/end of track 1/2)
# b) Objects (list of class Segment, possibly as class SegmentCollection)

# Compute:
# assume: no overlap within each track
# a) all pairs (double for loop)
# each t1-seg vs each t2-seg: count overlap. O(k*l) = O(n^2), where n is number
#                             of segments across tracks
#
# b) at each bp iterate through segments
# each bp: overlapped by any t1-seg (loop through intervals) and overlap by any
#          t2-seg? O(N*n), where N is number of bps
#
# c) at each bp, check for coverage in vectors each bp: Covered by t1-seg and
# t2-seg (each track as binary vector)? O(N), i.e. could be more efficient (but
# large memory)
#
# d) state machine each segment event, that is starts/ends (traversed by
# position, order regardless of track): update state, if in state 4 (inside segs
# for both tracks) count bps until next event. O(n)
#
# e) numpy-based state computation Combine positional events with state info (by
# compound vector element or by bitwise manipulation), sort elements, perform
# aggregation, compute lengths as distance between events, filter out states of
# interest


# *************************************************
# The regulation of which genes are active at a given time and in a given cell, is a very sophisticated mechanisms
# that involves proteins called transcription factors (TFs) that bind to DNA in order to regulate the expression (use) of nearby genes.
# The locations where a given transcription factor binds, will usually show a certain sequence specificity.
# An important problem is then to try to exploit the sequence specificty of binding, and find common patterns in DNA that may correspond the the binding by such a TF.
# In the example below, the strength of a pattern corresponding to a suggested set of substrings, is compared against patterns from random selections of substrings
# The example could serve as a somewhat larger project, and could also be extended beyond the code below.
# A possible further extension could e.g. be to try to determine the best pattern from scratch (i.e. the variable positionsList).
# This can be done by just making multiple guesses and choosing the best one, or by methods such as Expectation Maximization or Markov Chain Monte Carlo.
# The example involves strings, lists, dicts, looping, functions and randomness

# ------------------------------------------------------------------------------------------
print '\n*****  Example: Hypothesis testing for motif discovery *****\n'
# ------------------------------------------------------------------------------------------
import math
import random
from collections import defaultdict
def construct_ProbMatrix(frequencyMatrix, lines_number):
    frequencyRowSize = len(frequencyMatrix['A'])
    probabilityMatrix = defaultdict(dict)

    for base in 'ATGC':
        for index in range(frequencyRowSize):
            probabilityMatrix[base][index]=1.0*frequencyMatrix[base][index]/lines_number

    return probabilityMatrix

#  should find multiplication of probabilities, but will find summation of
#  log(probabilities) to avoid overflow
def find_probability(motif_substrings, probabilityMatrix):
    total_probability=0
    for substring in motif_substrings:
        for index, base in enumerate(substring):
            total_probability+=math.log(probabilityMatrix[base][index])

    return total_probability

#  Task: check if the given alignment is the correct one
dnaList=['AGATACCGTC',
     	'TAATACCCTA',
     	'TTACCATGAT',
     	'TGTGTTGCCG',
     	'CTCATACAAA']

positionsList=[2,2,0,4,3]  #  can use different values.
motifLength=5
dnaLength = len(dnaList[0])
# 1. find motif substrings

motif_substrings=[]
for index, dna in enumerate(dnaList):
	stPosition=positionsList[index]
	motif_substrings.append(dna[stPosition:stPosition+motifLength])

# 2. find probability matrix for given positions(firstly need to find frequency
# matrix (already implement)).
frequencyMatrix=construct_FreqMatrix_3(motif_substrings)	# dict in dict
probabilityMatrix=construct_ProbMatrix(frequencyMatrix, len(dnaList))

# 3. find the probability to meet the consensus sequences based on probability matrix

probability_AllSequences=find_probability(motif_substrings, probabilityMatrix)

# 4. find the positions for random motif subsequences

random_positions=[]
for num in range(len(dnaList)):
    random_positions.append(random.randint(0,dnaLength-motifLength+1))

#  5. repeat steps 1-3 for random positions
motif_substrings_random=[]

for index, dna in enumerate(dnaList):
    stPosition=random_positions[index]
    motif_substrings_random.append(dna[stPosition:stPosition+motifLength])

frequencyMatrix_random=construct_FreqMatrix_3(motif_substrings_random)	# dict in dict
probabilityMatrix_random=construct_ProbMatrix(frequencyMatrix_random, len(dnaList))

probability_AllSequences_random=find_probability(motif_substrings_random, probabilityMatrix_random)

# 6. check if the alignment is correct: if probability_given_positins/probability_random_positions > 0.7.

if probability_AllSequences-probability_AllSequences_random>math.log(0.7):
	print 'correct alignment'
else:
	print 'incorrect alignment'

