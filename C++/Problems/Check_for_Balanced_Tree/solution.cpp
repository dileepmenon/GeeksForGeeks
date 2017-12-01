/*
Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.*/


/* A binary tree node structure
struct Node {
    int data;
    Node* left, * right;
}; */
// This function should return tree if passed  tree 
// is balanced, else false.  Time complexity should
//  be O(n) where n is number of nodes in tree


int checkBalanced(Node *root)
    {if (root == NULL)
        return 0;
    int l_h, r_h;
    l_h = checkBalanced(root->left);
    if (l_h == -1)
        return -1;
    r_h = checkBalanced(root->right);
    if (r_h == -1)
        return -1;
    if (abs(l_h - r_h) > 1)
        return -1;
    if (l_h > r_h)
        return 1 + l_h;
    else
        return 1 + r_h;
    }


bool isBalanced(Node *root)
{int chk = checkBalanced(root);
 if (chk == -1)
    return false;
 else
    return true;
}
