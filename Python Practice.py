# Sorting ALgorithms

            # Insertion Sort

""" The time complexity is O(n^2)"""

def InsertionSort(l):
    for i in range(1,len(l)):
        key=l[i]
        for j in range(i):
            if key<l[j]:
                l[i],l[j]=l[j],l[i]
                key=l[j]
    return l


        # The SelectionSort
        
""" The Time Complexity is O(n^2) """


ls=[1,2,6,3,4,1,7,3,5,2,7,3]
InsertionSort(ls)

def SelectionSort(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l

ls=[1,2,6,3,4,1,7,3,5,2,7,3]
SelectionSort(ls)


                """Merge Sort"""
                
class Mergesort():
    
    def __init__(self,L):
        self.List=L
        
        self.List=self.mergesort(self.List)
        print(self.List)
        
        
    def merge(self,l1,l2):
        self.ans=[]
        while (l1!=[] and l2!=[]):
            if l1[0]<=l2[0]:
                self.ans.append(l1[0])
                l1.pop(0)
            else:
                self.ans.append(l2[0])
                l2.pop(0)
        self.ans=self.ans+l1+l2
        return self.ans
    
    
    def mergesort(self,lst):
        
        if len(lst)<=1:
            return lst
        
        mid=len(lst)//2
        
        l=self.mergesort(lst[:mid])
        r=self.mergesort(lst[mid:])
        return (self.merge(l,r))
    
    
    
l=[9,7,6,5,4,3,1]

merge=Mergesort(l)



            """ QuickSort """
            
class QuickSort():
    
    def __init__(self,L):
        self.List=L
        self.N= len(self.List)
        
        self.qsort(0,self.N-1)
        
        print(self.List)
        
        
    def qsort(self,a,b):
        if a>b:
            return
        
        pivot=self.List[a]
        l=a+1
        
        for r in range(a+1,b+1):
            if self.List[r]<=pivot:
                self.List[r],self.List[l]=self.List[l],self.List[r]
                l+=1
        
        m=l-1 #Approriate position for pivot
        self.List[m],self.List[a]=self.List[a],self.List[m]
        
        self.qsort(a,m-1)
        self.qsort(m+1,b)
        
        
 
ls=[3,1,5,1,2,4,2,3,7,6,4,5]       
quick=QuickSort(ls)

quick.qsort(0,4)
                
                

            """ The Faster Sorting Algorithm"""
            
# The RootSort
            
    """ Insertion takes n*root(n) and n*root(n) for deleteMax
    Total time complexity is O(n*root(n)) """
            
class rootsort():
    
    """" self.L: length of the list
        self.ns: root of the self.L
        self.ls: list of the lists
        self.sorted: sorted list
        """
    
    
    def __init__(self,ls):
        self.L=len(ls)
        self.sorted=[]
        if (self.L **0.5)/int(self.L **0.5)>1.0:
            self.ns=int(self.L **0.5)+1
        else:
            self.ns=int(self.L **0.5)
        
        self.ls=[]
        for i in range(self.ns):
            self.ls.append([])#root(n) empty strings
            
        for e in ls:
            self.insert(e)
        for i in range(self.L):
            self.sorted.append(self.deleteMax())
            
    
        #Inserting an element in the list
    def insert(self,element):
        #Find the first list with empty space for insertion
        for i in range(self.ns):
             if len(self.ls[i])<self.ns:
                break
        else:
            print("It's Full'")
            # Finding Approriate position for j
        j=0
            
        while (j<len(self.ls[i])) and self.ls[i][j]<=element:
            j=j+1
        self.ls[i].insert(j,element)
            
        return self.ls
    
    # Deleting the Maximum
    def deleteMax(self):
        self.maximum=0
        self.count=0
        for i in range(self.ns):
            if len(self.ls[i])>0:
                if self.maximum<=self.ls[i][-1]:
                    self.maximum=self.ls[i][-1]
                    self.count=i
        self.ls[self.count].pop()
        return self.maximum        
            
        
    
    def __repr__(self):
        return ('rootsort')
    

ls=[1,4,2,1,5,4,2,5,1,2,7,6,4,3,2]
x=rootsort(ls)
    


        # Heaps and HeapSort
        
# Building A Heap from Scratch

class Heap():
    
    def __init__(self):
        self.ls=[]
        self.length=0
        
        
    #Inserting a key
    def insert(self,x):
        self.ls.append(x)
        self.length+=1
        curr=self.length-1
        
        while curr>0 and self.ls[curr]>self.ls[(curr-1)//2]:
            self.ls[curr],self.ls[(curr-1)//2]=self.ls[(curr-1)//2],self.ls[curr]
            curr=(curr-1)//2
            
    
    def max(self):
        return self.ls[0]
    
    def Heapify(self,index):
        largest=index
            
        if 2*index+1<self.length and self.ls[2*index+1]>self.ls[index]:
            largest=2*index+1
        
        if 2*index+2<self.length and self.ls[2*index+2]>self.ls[largest]:
            largest= 2*index+2
            
        if largest !=index:
            self.ls[index],self.ls[largest]=self.ls[largest],self.ls[index]
            if 2*largest+1<self.length:
                return self.Heapify(largest)
        
        return
    
    
    def extractmax(self):
        self.ls[0],self.ls[-1]=self.ls[-1],self.ls[0]
        self.ls.pop()
        self.length-=1
        self.Heapify(0)
        
        
    def increase_value(self,key,value):
        self.ls[key]=value
        curr=key
        while (curr>0) and (self.ls[curr]>self.ls[(curr-1)//2]):
            self.ls[curr],self.ls[(curr-1)//2]=self.ls[(curr-1)//2],self.ls[curr]
            curr=(curr-1)//2
        



l=[1,3,2,1,4,5,3,2,2]
heap=Heap()
for i in l:
    heap.insert(i)
    
heap.increase_value(4,10)
        


# Heap Sort algorithm based on Max Heap Property

class HeapSort():
   
    """ Heapsort Algorithm based on Max/Min Heaps Data Structures"""
    
    # Max Heaps Rules :
    """ The parent is bigger than its left and right child.
    The left child of the ith node is 2i+1 and the right one is 2i+2.
    The parent of the child i is (i-1)//2
    
    Parameters:
        self.L=length of the List
        self.height=Height of the Tree
        self.ls=The list we want to change
    """
        
        
    def __init__(self,List):
        import math
        self.ls=List
        self.L=len(self.ls)
        self.height=int(math.log(self.L,2))+1
        self.count=0
        
        for i in range(self.L-1,-1,-1):
            if 2*i+1<=self.L-1 or 2*i+2<=self.L-1:
                self.Heapify(i)
            else:
                self.count=i
    
    # Creating Heaps using Max Heapify. This Operation takes at most O(logn) for every nodes.
    # So, T(n)=O(n)
    def Heapify(self,index):
        # Checking if the left child exits and greater than parent
        largest=index
            
        if 2*index+1<self.L and self.ls[2*index+1]>self.ls[index]:
            largest=2*index+1
        
        if 2*index+2<self.L and self.ls[2*index+2]>self.ls[largest]:
            largest= 2*index+2
            
        if largest !=index:
            self.ls[index],self.ls[largest]=self.ls[largest],self.ls[index]
            if 2*largest+1<self.L:
                return self.Heapify(largest)
        
        return

        

    def __repr__(self):
        return("Heap Sort")

ls=[1,4,2,1,5,4,2,5,1,2,7,6,4,3,9]
x=HeapSort(ls)


             """ Priority Queue(Using Heap) """
             
class PriorityQ(Heap):
    def __init__(self):
        Heap.__init__(self)
    
    def insertelement(self,x):
        self.insert(x)
        
    def deletemax(self):
        return self.extractmax()
    
    def maximum(self):
        self.max()
    def increasevalue(self,key,value):
        self.increase_value(key,value)


pr=PriorityQ()
ls=[1,3,1,2,8,4,5,3,6,2,4]

for i in ls:
    pr.insertelement(i)
    
pr.deletemax()




                """ Binary Tree """
                
class BTree():
    
    def __init__(self,v,l=None,r=None):
        self.value=v
        self.left=l
        self.right=r
    
    def __str(self,v):
        
        if v:
            return (str(v))
        return ("E")
    
    def __str__(self):
        return ("({} {} {})".format(self.__str(self.value),self.__str(self.left),self.__str(self.right)))
    
    def preorder(self):
        """ Root Left Right"""
        ans=[self.value]
        
        if self.left:
            ans=ans+self.left.preorder()
        
        if self.right:
            ans=ans+self.right.preorder()
        
        return (ans)
               
    def postorder(self):
        """ Left Right Root"""
        
        ans=[]
        if self.left:
            ans=ans+self.left.postorder()
        
        if self.right:
            ans=ans+self.right.postorder()
        
        ans.append(self.value)
         
        return (ans)            
            
    def inorder(self):
        """ Left Root Right"""
        
        ans=[]
        
        if self.left:
            ans=ans+self.left.inorder()
        
        ans=ans+[self.value]
            
        if self.right:
            ans=ans+self.right.inorder()
            
        return(ans)




z=BTree(10,BTree(1),BTree(13,BTree(12),BTree(17)))

print(z)

print(z.inorder())
print(z.postorder())
print(z.preorder())


class BSTree(BTree):
    
    def search(self,v):
        
        if self.value == v:
            return True
        
        elif self.value > v and self.left:
            return self.left.search(v)
        elif self.value < v and self.right:
            return self.right.search(v)
        
        return False
    
    def insert(self,v):
        if self.value == v:
            return 
        
        elif self.value > v and self.left:
            self.left.insert(v)
            
        elif self.value > v:
            self.left=BSTree(v)
            
        elif self.value < v and self.right:
            self.right.insert(v)
            
        elif self.value < v:
            self.right= BSTree(v)
            
    def minimum(self):
        return self.inorder()[0]
    
    def maximum(self):
        return self.inorder()[-1]
    
    
    #def tree_successor(self,key):
        
            
            
            

x=BSTree(4)

x.insert(2)
x.insert(6)
x.insert(1)
x.insert(8)
x.insert(3)
x.insert(9)

x.minimum()
















print("ab\tgh")













    
    
    
