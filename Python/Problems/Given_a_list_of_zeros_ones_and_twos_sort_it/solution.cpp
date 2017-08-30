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


void sortList(Node *head)
{Node *ptr = head;
 int count[3] = {0, 0, 0};
 while (ptr != NULL)
    {
        count[ptr->data] += 1;
        ptr = ptr->next;
    }
 int i = 0;
 ptr = head;
 while (ptr != NULL)
 { if (count[i] == 0)
      i += 1;
   else
    {ptr->data = i;
     ptr = ptr-> next;
     count[i] -= 1;
    }
 }
}












