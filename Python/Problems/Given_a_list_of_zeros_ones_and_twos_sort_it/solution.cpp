/*
Please note that it's Function problem i.e.
you need to write your solution in the form Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.*/


/*
  Sort the list of 0's,1's and 2's
  The input list will have at least one element
  Node is defined as
  struct Node
  {
     int data;
     Node *next;
  }
*/
#include <vector>
#include<iostream>
void sortList(Node *head)
{Node *temp = head;
std::vector <Node> l0;
std::vector <Node> l1;
std::vector <Node> l2;
while (temp != NULL) 
{ if (temp->data == 2)                                                        
    {l2.push_back(*temp);  
    }
  else if (temp->data == 1)                                                   
    l1.push_back(*temp);                                                     
  else                                                                        
    l0.push_back(*temp);
  temp = temp->next;
}
int n0 = l0.size();
int n1 = l1.size();
int n2 = l2.size();
for(int i=0; i< n0-1; i++)
    l0[i].next = &l0[i+1];
for(int i =0; i< n1-1; i++)
    l1[i].next = &l1[i+1];
for(int i =0; i< n2-1; i++)
    l2[i].next = &l2[i+1];
if (n0 > 0)
head = &l0[0];
else if (n1 > 0)
head = &l1[0];
else
head = &l2[0];
if (n0>0)
{   if (n1>0) 
        l0[n0-1].next = &l1[0];
    else if (n2>0) 
        l0[n0-1].next = &l2[0];
    else
        l0[n0-1].next = NULL;
}
if (n1>0)
    {if (n2>0)
        l1[n1-1].next = &l2[0];
    else
        l1[n1-1].next = NULL;
    }
if(n2 > 0)
    l2[n2-1].next = NULL;
}






