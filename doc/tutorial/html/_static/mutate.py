import random

def mutate(dna):
    dna_list = list(dna)
    mutation_site = random.randint(0, len(dna_list) - 1)
    dna_list[mutation_site] = random.choice(list('ATCG'))
    return ''.join(dna_list)

def get_base_frequencies_v2(dna):
        return {base: dna.count(base)/float(len(dna))
                for base in 'ATGC'}

def format_frequencies(frequencies):
    return ', '.join(['%s: %.2f' % (base, frequencies[base])
                      for base in frequencies])

dna = 'ACGGAGATTTCGGTATGCAT'
print 'Starting DNA:', dna
print format_frequencies(get_base_frequencies_v2(dna))

nmutations = 10000
for i in range(nmutations):
    dna = mutate(dna)

print 'DNA after %d mutations:' % nmutations, dna
print format_frequencies(get_base_frequencies_v2(dna))

def create_markov_chain():
    markov_chain = {}
    for from_base in 'ATGC':
        # Generate random transition probabilities by dividing
        # [0,1] into four intervals of random length
       slice_points = sorted(
           [0] + [random.random()for i in range(3)] + [1])
       transition_probabilities = \
           [slice_points[i+1] - slice_points[i] for i in range(4)]
       markov_chain[from_base] = {base: p for base, p
                         in zip('ATGC', transition_probabilities)}
    return markov_chain

mc = create_markov_chain()
print mc
print mc['A']['T'] # probability of transition from A to T

def check_transition_probabilities(markov_chain):
    for from_base in 'ATGC':
        s = sum(markov_chain[from_base][to_base]
                for to_base in 'ATGC')
        if abs(s - 1) > 1E-15:
            raise ValueError('Wrong sum: %s for "%s"' % \
                             (s, from_base))

check_transition_probabilities(mc)

def transition(transition_probabilities):
    interval_limits = []
    current_limit = 0
    for to_base in transition_probabilities:
        current_limit += transition_probabilities[to_base]
        interval_limits.append((current_limit, to_base))
    r = random.random()
    for limit, to_base in interval_limits:
        if r <= limit:
            return to_base
    # Should never reach this point
    raise ValueError('Wrong computation of random interval')

for i in range(4):
    print 'A to', transition(mc['A'])

def mutate_via_markov_chain(dna, markov_chain):
    dna_list = list(dna)
    mutation_site = random.randint(0, len(dna_list) - 1)
    from_base = dna[mutation_site]
    to_base = transition(markov_chain[from_base])
    dna_list[mutation_site] = to_base
    return ''.join(dna_list)

random.seed(10)  # ensure the same random numbers every time
dna = 'TTACGGAGATTTCGGTATGCAT'
print 'Starting DNA:', dna
print format_frequencies(get_base_frequencies_v2(dna))

mc = create_markov_chain()
import pprint
print 'Transition probabilities:\n', pprint.pformat(mc)
nmutations = 10000
for i in range(nmutations):
    dna = mutate_via_markov_chain(dna, mc)

print 'DNA after %d mutations (Markov chain):' % nmutations, dna
print format_frequencies(get_base_frequencies_v2(dna))

def transition_into_bases(markov_chain):
    return {to_base: sum(markov_chain[from_base][to_base]
                         for from_base in 'ATGC')/4.0
            for to_base in 'ATGC'}

print transition_into_bases(mc)



