# This file is a TEMPLATE, meaning that the functions below are not
# complete. Enter code in this file _only_ where the comments below instruct you
# to do so. Should you need to import any additional modules other than 'math',
# do this at the top of the file.
#
# ENTER YOUR STUDENT NUMBER HERE: 670045174

import math 
class deck:
    def __init__(self,deck):
            self.deck=deck
    def __repr__(self):
        return str(self.deck)
    @classmethod
    def generate(cls,n):
        x=list(range(1,n+1))
        return cls(x)
    def reverse_deck(self,inplace=True,r=True):
        deck=self.deck[::-1] #reverse deck
        if inplace:
            self.deck=deck
        if r:
            return(deck)
    def weave_deck(self):
        #slicing deck in half
        l=len(self.deck)
        a = self.deck[:((l+1)//2)]
        b = self.deck[((l+1)//2):]
        
        self.deck[::2] = a #replacing odd numbers of deck with a
        self.deck[1::2] = b #replacing even numbers of deck with b
        return (self.deck)
    
    def shuffle_deck(self, order):
        n=str(1) #initialize multiplier
        
        prevdgt=False # boolean is true when the previous entry in the string is an integer
        for i in order: #for loop scans the command input
            
            #detect number of digits to multiply
            if str(i).isdigit():
                if prevdgt==True:
                    n+=str(i)
                else:
                    n=str(i)
                prevdgt=True
                #reverse and weaves the deck if command is detected
            elif i=='r':
                for x in range(int(n)):
                    self.reverse_deck()
                n=str(1)
                prevdgt=False
            elif i=='w':
                for x in range(int(n)):
                    self.weave_deck()
                n=str(1)
                prevdgt=False
        return (self.deck)
    def valid(self,str):
        allowed = set('0123456789()rw,')
        stack=0
        for s in str:
            if s=='(':
                stack+=1
            elif s==')':
                if stack==0:
                    return False
                else:
                    stack-=1
            elif s not in allowed:
                return False
        return stack==0
    def unravel(self,order):
            i=0
            n=''
            prev=0
            while '(' in order:
                if order[i]=='(':
                    x=1 if n=='' else int(n)
                    left=order[:i-prev]
                    mid=''
                    right=''
                    counter=0
                    for j,s in enumerate(order[i+1:]):
                        if s==')':
                            if counter==0:
                                right=order[i+j+2:]
                                break
                            else:
                                mid+=s
                                counter-=1
                        elif s=='(':
                            mid+=s
                            counter+=1
                        else:
                            mid+=s
                    mid*=x
                    order=left+mid+right
                    n=''
                    prev=0
                elif order[i].isdigit():
                    n+=order[i]
                    prev+=1
                    i+=1
                else:
                    n=''
                    i+=1
            return order#
    def unfold(self,order):
        i=0
        n=''
        prev=0
        while '(' in order:
            if order[i]=='(':
                x=1 if n=='' else int(n)
                left=order[:i-prev]
                mid=''
                right=''
                counter=0
                for j,s in enumerate(order[i+1:]):
                    if s==')':
                        if counter==0:
                            right=order[i+j+2:]
                            break
                        else:
                            mid+=s
                            counter-=1
                    elif s=='(':
                        mid+=s
                        counter+=1
                    else:
                        mid+=s
                mid=self.unfold(mid)*x
                order=left+mid+right
                n=''
                prev=0
            elif order[i].isdigit():
                n+=order[i]
                prev+=1
                i+=1
            else:
                n=''
                i+=1
        return order
        
    def shuffle_advanced(self, order):
        order=self.unfold(order)
        self.shuffle_deck(order)
        return self.deck
# Insert your code for the user interface (Q5) here.

if __name__ == '__main__':
    try:
        n=int(input('Enter a value for n: '))
        if n < 1:   #detecting errors in input n
            raise ValueError
        deck1=deck.generate(n=n)
        order=input('Enter shuffling operations: ')
        if not deck1.valid(order):         
            raise ValueError
        output=deck1.shuffle_advanced(order)
        print('Shuffled deck is:', output)
    except ValueError:
        print('Please enter positive integers for n as well as integers,brackets and w and r for operations, Make sure brackets are valid')
