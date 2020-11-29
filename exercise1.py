import numpy as np
import networkx as nx

def linear(n):
    # returns the matrix for linear polyene of length n, with alpha = 0 and beta = -1
    n_int = int(n)
    M = np.array([[-1 if i == j - 1 or i == j + 1 else 0 for i in range(n_int)] for j in range(n_int)])
    return M
    
def cyclic(n):
    # returns the matrix for linear polyene of length n, with alpha = 0 and beta = -1
    n_int = int(n)
    M = np.array([[-1 if i == j - 1 or i == j + 1 else 0 for i in range(n_int)] for j in range(n_int)])
    M[0,(n_int-1)] = -1
    M[(n_int-1),0] = -1
    return M
    
def platonic(n): # n must be 4, 6, 8, 12 or 20
    # returns the matrix for sp2 platonic solid, with alpha = 0 and beta = -1
    n_int = int(n)
    if n_int == 4:
        s = nx.tetrahedral_graph()
    elif n_int == 6:
        s = nx.cubical_graph()
    elif n_int == 8:
        s = nx.octahedral_graph()
    elif n_int == 12:
        s = nx.dodecahedral_graph()
    elif n_int == 20:
        s = nx.icosahedral_graph()
    else:
        print("n must be equal to 4, 6, 8, 12 or 20")
    
    M = - nx.adjacency_matrix(s)
    return M.todense()
    
def get_evals(Ma):
    # calculates the eigenvalues for a symmetric matrix
    evalss, evecs = np.linalg.eigh(Ma)
    return evalss
    
def degen(evals):
    # calculates the degeneracies of each eigenvalue
    test = 0
    count = 0
    result = []
    
    for e in evals:
        if abs(e - test) < 0.001: # threshold can be varied for accuracy
            count += 1
        else:
            if test != 0:
                result.append((round(test,3), count))
            test = e
            count = 1
            
    if count > 0:
        result.append((round(test,3), count))
        
    return result
    
def huckel():
    # this function gathers information from the user and executes the chosen tasks
    repeat = "yes"

    while repeat == "yes":
        print("")
        print("For the eigenvalues and degeneracies of a length n poly-ene, input p")
        print("For the eigenvalues and degeneracies of a length n cyclic poly-ene, input c")
        print("For the eigenvalues and degeneracies of a length n platonic solid, input s")
        print("")

        ans = input("Enter here:")

        if ans == "p":
            
            ans1 = input("Please specify n:")
            lin = linear(ans1)
            evals = sorted(get_evals(lin))
            print(degen(evals))

        elif ans == "c":
            print("Please specify n")
            ans1 = input("n:")
            cyc = cyclic(ans1)
            evals = sorted(get_evals(cyc))
            print(degen(evals))

        elif ans == "s":
            print("Please specify n where n = 4, 6, 8, 12 or 20")
            ans1 = input("n:")
            pla = platonic(ans1)
            evals = sorted(get_evals(pla))
            print(degen(evals))

        else:
            print("Make sure you have used lowercase to specify your category")

        print("")
        repeat = input("Do you want to repeat for another molecule?")
        
huckel()
