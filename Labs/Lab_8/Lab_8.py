import numpy as np

def print_matrix(M_lol):
    print(np.array(M_lol))

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    
    return len(row)

def get_row_to_swap(M, start_i):
    scores = []

    for i in range(start_i, len(M)):
        scores.append(get_lead_ind(M[i]))
    
    return scores.index(min(scores)) + start_i

def add_rows_coefs(r1, c1, r2, c2):
    return [r1[i]*c1 + r2[i]*c2 for i in range(len(r1))]

def reduce_row(M, r):
  index = get_lead_ind(M[r])
  c = M[r][index]
  M[r] = [M[r][i]/c for i in range(len(M[r]))]

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub+1, len(M)):
        if get_lead_ind(M[i]) == best_lead_ind:  
          M[i] = add_rows_coefs(M[i], 1, M[row_to_sub], -1 * M[i][best_lead_ind] / M[row_to_sub][best_lead_ind])

def eliminate_backward(M, row_to_sub):
  for i in range(row_to_sub-1, -1, -1):
    M[i] = add_rows_coefs(M[i], 1, M[row_to_sub], -1 * M[i][row_to_sub] / M[row_to_sub][row_to_sub])

def swap_rows(M, a, b):
    M[a], M[b] = M[b], M[a]

def forward_step(M):
  print_matrix(M)
  for i in range(len(M)):
    print("===========================================================")
    print(f"Now looking at row {i}")
    swap = get_row_to_swap(M, i)
    print(f"Swapping rows {i} and {swap} so that entry 0 in the current row is non-zero")
    swap_rows(M, i, swap)
    print("The matrix is currently")
    print_matrix(M)
    print(f"Adding row {i} to rows below it to eliminate coefficients in column {get_lead_ind(M[i])}")
    eliminate(M, i, get_lead_ind(M[i]))
    print_matrix(M)

def backward_step(M):
  print("Now applying backward step:")
  print_matrix(M)
  for i in range( min(len(M), len(M[0]))-1, -1, -1):
    print(f"Adding row {i} to rows above it to eliminate coefficients in column {i}")
    eliminate_backward(M,i)
    reduce_row(M,i)
    print_matrix(M)
  
def solve(M, b):
  for i in range(len(M)):
    M[i].append(b[i])
  forward_step(M)
  backward_step(M)
  return [M[i][-1] for i in range(len(M))]

if __name__ == "__main__":
  M = np.array([[9,-25,39],[36,102,17],[12,53,37]])
  x = np.array([756,102,-181])
  b = np.matmul(M,x)
  res = solve(M.tolist(),b.tolist())
  print_matrix(res)
