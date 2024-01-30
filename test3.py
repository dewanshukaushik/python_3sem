from sklearn import datasets 
digits = datasets.load digits ()
dir ( digits )
digits . images . shape print ( digits . images [0])
import matplotlib . pyplot as plt plt . imshow( digits . images [0] ,cmap=’bi nary ’) plt . show()
def plot multi ( i ):
’ ’ ’ Plots 16 digits , starting with digit i ’ ’ ’ nplots = 16 fig = plt . figure ( figsize =(15 ,15)) for j in range ( nplots ):
plt . subplot (4 ,4 , j+1)
plt . imshow( digits . images [ i+j ] , cmap=’binary ’) plt . t i t l e ( digits . target [ i+j ])
plt . axis ( ’ off ’) plt . show() plot multi (0)