from SLinkedList import SLinkedList

class Number(SLinkedList):
    
    def __add__(self,ll):
        n1=self.head    
        n2=ll.head
    
        res=Number()
        carry=0
        while n1 or n2:
            v1 = n1.data if n1 else 0
            v2 = n2.data if n2 else 0
	
            s=v1+v2+carry
      
            if s<9:
                carry=0
                res.add_last(s)
            else:
                carry=1
                res.add_last(s%10)
	
            if n1:
                n1=n1.next
            if n2:
                n2=n2.next
	
        return res
	
if __name__ == '__main__':
    a=Number()
    a.add_last(6) # Units
    a.add_last(1) # Tens
    a.add_last(4) # Hundreds
      
    b=Number()
    b.add_last(7) # Units
    b.add_last(5) # Tens
    b.add_last(0) # Hundreds
    b.add_last(1) # Thousands
      
    c=a+b
    c.print_l_r()
    
