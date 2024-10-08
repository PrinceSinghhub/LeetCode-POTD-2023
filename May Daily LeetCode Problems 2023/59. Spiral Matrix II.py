class Solution:
	def generateMatrix(self, n):
		mat=[[0 for _ in range(n)] for _ in range(n)]

		s=1
		r=n
		c=n
		k,l=0,0

		while k<r and l<c:
			for i in range(l,c):
				mat[k][i]=s
				s=s+1
			k=k+1

			for i in range(k,r):
				mat[i][c-1]=s
				s=s+1
			c=c-1

			if k<r:
				for i in range(c-1,l-1,-1):
					mat[r-1][i]=s
					s=s+1
				r=r-1

			if l<c:
				for i in range(r-1,k-1,-1):
					mat[i][l]=s
					s=s+1
				l=l+1

		return mat