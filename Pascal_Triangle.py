class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #using DP(Dynamic Programming)Approach
        #T(C(N)=O(N**2)) and S(C(N)=O(N)) as it requires contigous space alloc depth and level wise  iteratively
        out=[[1]]#output initilize

        for r in range(2,numRows+1):#Triangular 2 Rows Iteration 
            t=[1]#cell's adder intialize
            for c in range(1,r-1):#Triangular columns Iteration 
                t.append(out[-1][c]+out[-1][c-1])#inserting cells val from both left and right sub part
            t.append(1)#incremeting adder by 1
            out.append(t)#inserting cell's added val to output

        return out#printing output
