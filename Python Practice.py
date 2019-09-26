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
    


        # HeapSort
        

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
    
    
    
