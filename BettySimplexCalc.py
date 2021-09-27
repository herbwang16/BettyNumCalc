import numpy as np



def add_row(matrix, row1, row2):
	matrix[row1, :]= (matrix[row1, :] + matrix[row2, :]) %2

def swap_row(matrix, row1, row2):
	matrix[[row1, row2]] = matrix[[row2, row1]]

def add_col(matrix, col1, col2):
	matrix[:, col1]= (matrix[:, col1] + matrix[:, col2]) %2

def swap_col(matrix, col1, col2):
	matrix[:, [col1, col2]] = matrix[:, [col2, col1]]

def smith_normal(matrix):
	n = len(matrix)
	m = len(matrix[0])
	ret = matrix
	i = 0
	result = np.where(ret[i:,i:] == 1)
	while len(result[0]) > 0 and i <= m and i <= n:
		j=0
		while j<len(result[0]):
			if result[0][j]==0 and result[1][j]!=0:
				swap_col(ret,result[1][j]+i, i)
				print(result)
				print("j is "+str(j))
				print("return is ")
				print(ret)
				break
			j+=1

		result = np.where(ret[i:,i:] == 1)
		print(result)

		for row in range(n-i):
			if ret[i+row,i]!=0 and row!=0:
				add_row(ret, row+i, i)

		print("return2 is ")
		print(ret)

		for col in range(m-i):
			if ret[i,i+col]!=0 and col!=0:
				print(col)
				add_col(ret, col+i, i)
		print("return3 is ")
		print(ret)

		
		# if j == (len(result)-1):
		# 	result = np.where(ret[i+1:,i:] == 1)
		# 	continue

		i = i+1
		result = np.where(ret[i:,i:] == 1)
	print(len(result))
	
	return ret

def calcB1(mat1, mat2):
	return len(np.where(mat2==1))-len(np.where(mat1==1))

def calcB2(mat2):
	return 

def main():
	mat1 = np.array([[0,0,0,1,1,0,0,0],
               [1,0,1,1,0,1,0,0],
               [0,1,1,0,1,0,0,1],
               [1,1,0,0,0,0,1,0],
               [0,0,0,0,0,1,1,1]])
	mat2 = np.array([[1,0,0,1],
	                [0,0,1,1],
	                [0,1,0,1],
	                [0,0,0,0],
	                [0,0,0,0],
	                [1,1,0,0],
	                [1,0,1,0],
	                [0,1,1,0]])
	smn1=smith_normal(mat1)
	smn2=smith_normal(mat2)
	print("b1 is")
	print(calcB1(smn1,smn2))
	

if __name__ == "__main__":
    main()