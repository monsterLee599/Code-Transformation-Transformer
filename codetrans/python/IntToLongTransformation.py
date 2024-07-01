from Node import *
from AstToTree import *

# we will convert the integer to long, we should notice that the the method long() is not in python3.x, but in python2.x
# because the most data is python2.x and the tree-sitter can parser the python2.x and python3.x, so we can use this transformation
#we don't convert o and 1,because we want to convert 1/0 to true/false
#param: the root node of the tree generated from ast
#return: the code add long() convert
def IntToLong(tree_root_node):
    result=FindInt(tree_root_node)

    if len(result)==0:
        return 0
    else:
        for i in range(0,len(result)):
            ProcessIntToLong(result[i])

    code=TreeToTextPy(tree_root_node)
    return code

#if the code has integer(except for 0 and 1), it will return node.text, else, it will return false
#param: the node of the tree generated from ast
#return node.text or false
def IsInt(node):
    if node.type=='integer' and node.text!='0' and node.text!='1':
        return node.text

    if len(node.children)!=0:
        for child in node.children:
            result=IsInt(child)
            if result!=False:
                return result
            else:
                continue
        return False

    return False

#we will return the list of integers
#param: the node of the tree generated from ast
#return list of integers
def FindInt(node):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    int_list=[]
    if node.type=='integer' and node.text!='0' and node.text!='1' and 'L' not in node.text and 'j' not in node.text:
        is_num = True
        for i in range(0, len(node.text)):
            if node.text[i] not in number:
                is_num = False
                break
        if is_num:
            int_list.append(node)

    if len(node.children)!=0:
        for child in node.children:
            result=FindInt(child)
            if len(result)!=0:
                for i in range(0,len(result)):
                    int_list.append(result[i])

    else:
        pass

    return int_list

# we should know that in python3.x, threr is no long, so you can only use this transformation in python2.x
#param: the node that type is integer
#retrurn none
def ProcessIntToLong(node):
    integer=node.text
    integer=str(integer)
    integer=integer+'L'
    node.text=integer
    node.type='Long'


