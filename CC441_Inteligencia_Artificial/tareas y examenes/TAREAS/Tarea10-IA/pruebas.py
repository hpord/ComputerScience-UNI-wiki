import Dseparation


# +---+     +---+
# | X |     | Y |
# +---+     +---+
def bn_independiente():
    g = Dseparation.BayesNet()
    g.add_nodes_from(['X', 'Y'])
    return g


# +---+     +---+
# | X |---->| Y |
# +---+     +---+
def bn_dependiente():
    g = Dseparation.BayesNet()
    g.add_nodes_from(['X', 'Y'])
    g.add_edge('X', 'Y')
    return g


# +---+     +---+     +---+
# | X |---->| Y |---->| Z |
# +---+     +---+     +---+
def bn_cadena():
    g = Dseparation.BayesNet()
    g.add_nodes_from(['X', 'Y', 'Z'])
    g.add_edges_from([('X', 'Y'), ('Y', 'Z')])
    return g


# +---+     +---+     +---+
# | Y |<----| X |---->| Z |
# +---+     +---+     +---+
def bn_naive_bayes():
    g = Dseparation.BayesNet()
    g.add_nodes_from(['X', 'Y', 'Z'])
    g.add_edges_from([('X', 'Y'), ('X', 'Z')])
    return g


# +---+     +---+     +---+
# | X |---->| Z |<----| Y |
# +---+     +---+     +---+
def bn_v_estructura():
    g = Dseparation.BayesNet()
    g.add_nodes_from(['X', 'Y', 'Z'])
    g.add_edges_from([('X', 'Z'), ('Y', 'Z')])
    return g
