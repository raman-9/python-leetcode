def findMedianSortedArrays(self,num1,num2):
    merged=[]
    i=j=0 #pointer of num1 and num2 with complexity O(log(m+n))
    
    while i<len(num1) and i<len(num2): 
        if num1[i]<num2[j]:
            merged.append(num1[i])
            i+=1
        else:
            merged.append(num2[i])
            j+=1
            
        merged.extend(num1[i:])
        merged.extend(num2[i:])
        
        n = len(merged)
        if n%2 == 1:
            return merged[n//2]
        else:
            return (merged[n//2-1]+merged[n//2])/2
        