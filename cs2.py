#!/usr/bin/python
import math

def hm_dist(f,g): # calculating the hamming distance
	n=len(f);
	cnt=0;
	cnt=int(cnt);
	for i in range(0,n):
		if(int(f[i])!=int(g[i])):
			cnt=cnt+1;
	return (cnt);


def fn(y,t,s,m):
	k=math.pow(2.0,m)/2;
	k=int(k);
	if(m<s):
		s=m;
	lv=[];
	l1=[];
	l2=[];
	if(s!=0):
		y1=[];
		
		for p in range(0,k):
			pk=int(p)+int(k);
			print "value of p is ";
			print p;			
			print "value of pk is ";
			print pk;
			if((int(y[p])==1)and(int(y[pk])==1)):
				y1.insert(p,0);
			else:			
				y1.insert(p,int(y[p])+int(y[pk]));
		
		lv.append(fn(y1,t,s-1,m-1)); #recursive call
		ltemp = len(y);
		ltemp = int(ltemp)/2;		
		y2=[];	
		ltemp2 = int(ltemp)*2;
		y3=[];
		for j in range(0,ltemp):
			y2.insert(j,y[j]);

		for j in range(ltemp,ltemp2):
			y3.insert(j,y[j]);

		l1.append(fn(y2,t/2,s,m-1));
		l2.append(fn(y3,t/2,s,m-1)); 
	
		print "value of s ";
		print s;
		for pqr in l1:
			print pqr;
		for pqr in l2:
			print l2;

		
	else:	#code for the base case follows
		q=len(y);
		q=int(q);
		ls1=[];
		ls2=[];
		for i in range(0,q):
			ls1.insert(i,0);
			ls2.insert(i,1);
		dist1 = hm_dist(y,ls1);
		dist2 = hm_dist(y,ls2);
		if(dist1<=t):
			lv.append(ls1);
		if(dist2<=t):
			lv.append(ls2);
	
		
	return(lv);



y=[];
t = raw_input("Enter value for t ?");
s = raw_input("Enter value for s ?");
m = raw_input("Enter value for m ?"); 
m=int(m);
s=int(s);
t=int(t);
m2 = math.pow(2.0,m);
m2 = int(m2);
for i in range(0,m2): # getting values into the truth table
	j=raw_input("Enter value to truth table");	
	y.append(j);

print "Printing the array";
for i in y:
	print i;

yt = fn(y,t,s,m); # function being called with the initial parameters

print "Printing Lv";	
for list in yt:
	print list;

