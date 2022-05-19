# Brute Force 0/1 knapsack
def get_strings(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def brute_force(p,w,m):
    assert len(p) == len(w), "no of items do not match for p and w" 
    n=len(p)
    solution=[]
    bit_strings=get_strings(n)
    best_profit=0
    for s in bit_strings:
        profit= sum([int(s[x])*p[x] for x in range(n)])
        weight= sum([int(s[x])*w[x] for x in range(n)])
        if(weight<=m and profit>best_profit):
            best_profit=profit
            solution=s
    return solution,best_profit

# Fractional Knapsack problem with Brute force  
def brute_force_fractional(p, w, m):
    assert len(p) == len(w), "Profit and weight do not have the same number of elements!"

    n = len(p)
    bit_strings = get_strings(n)

    max_profit = 0
    solution = ''

    for s in bit_strings:
        profit, weight = 0, 0
        s1 = ''
        for i in range(n):
            if weight < m and int(s[i]) == 1:
                if w[i] <= (m - weight):
                    profit += p[i]
                    weight += w[i]
                else:# fractional part
                    s1 = s[0:i] + 'f'
                    # f is the ratio of weight taken
                    f ='f = (' + str(m - weight) + '/' + str(w[i]) + ')'
                    unit = round(p[i]/w[i], 3) #round to 3 digits
                    profit += (m - weight)*unit
                    weight += m - weight
                   
        if profit > max_profit:
            max_profit = profit
            if s1 != '':
                # fractional item completes the max weight, so rest of the item are not considered
                solution = s1.ljust(4, '0')
            else:
                solution = s
       
    return(solution, f, max_profit)

# Fractional Knapsack problem with Greedy
def greedy(array, maxWeight):
    # array tuple = profit, weight, key
    for item in array:
        item.append(round(item[0]/item[1], 3))# tuple = profit, weight, key, unit profit

    array.sort(key = lambda x:x[3], reverse = True)# sorting array on the basis of unit profit
    profit = 0
    selected = []

    for item in array:
        if item[1] <= maxWeight:
            selected.append(item[0:3])
            maxWeight -= item[1]
            profit += item[0]
            if maxWeight == 0:
                break
        else:# fractional part
            selected.append([maxWeight * item[3], maxWeight, item[2]])
            profit += maxWeight * item[3]
            maxWeight = 0
            break

    return selected, profit

# 0/1 Knapsack problem with Dynamic: bottom up approach
def dynamic(p, w, m):
    assert len(p) == len(w), "Profit and weight do not have the same number of elements!"

    n = len(p)
    V = [[0 for j in range(m + 1)] for i in range(n + 1)] 
              
    # bottom up approach
    for i in range(n + 1): 
        for j in range(m + 1): 
            if i == 0 or j == 0: 
                V[i][j] = 0
            elif w[i - 1] <= j: 
                V[i][j] = max(V[i - 1][j], V[i - 1][j - w[i - 1]] + p[i - 1]) 
            else: 
                V[i][j] = V[i - 1][j] 

    # finding the solution
    rm, rp = m, V[n][m]
    solution = ''
    for i in range(n, 0, -1): 
        if rp <= 0: 
            break
        if rp != V[i - 1][rm]:  
            # included item
            solution = '1' + solution
 
            rp -= p[i - 1] 
            rm -= w[i - 1]
        else:
            solution = '0' + solution
    
    solution = solution.rjust(4, '0')
    return solution, V[n][m]

if __name__=='__main__':
    p=[100,200,300,400]
    w=[10, 20 , 30, 40]
    m=40
    solution,f, profit= brute_force_fractional(p,w,m)
    print(solution,f,profit)



    
