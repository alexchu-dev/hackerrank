"""
    Consider a text file that contains a list of C, C++, and C# source code file namc es. The extensions for the file types are as follows:
    1. C → .c
    2. 2.C++ → .cpp
    3. C# → .cs

    Given a string, baseFilename, that denotes the name of a real text file, create the following three output files where baseFilename denotes the name of the file received as input and the base of the names for output files:
    1.    c_baseFilename, for storing C file names.
    2.    cpp_baseFilename, for storing C++ file names.
    3.    cs_baseFilename, for storing C# file names.

    Next, process the list of file names in baseFilename in order and, for each source code file name encountered, append its name to the appropriate output file.

    For example, the input baseFilename is file_00.txt and it contains the following data:
    first.c
    first. cpp
    first.cs
    second.c

    First, create the three files named c file_00.txt, cpp_file_00.txt and cs file_00.txt. Read in each source file name and write them out to their appropriate files. The results are:
    *   c_file_00.txt first.c second.c
    *   cpp_file_00.txt first.cpp
    *   cs_file_00.txt first.cs

    The file names must maintain the order in which they were listed in file_00.txt.

    Note: There may not be a file of every type included in the input. In that case, the output file for that type should still be created and it should be empty.

    Function Description
    Complete the code in the editor below. It must create three files and save the appropriate source file names to each one while maintaining order.

    The program has the following parameter(s):
    baseFilename: the name of a text file

    Constraints
    *   baseFilename has a maximum of 10^5 lines.

    Sample Case 0:
    Sample Input 0:
    names-List_00.txt
    Sample Output :
    Create the following three output files:
    *   c_names_list_00.txt: code1.c code3.c code4.c
    *   cpp_names_lIst_00.txt.m code1.cpp code5.cpp
    *  cs_names_ list_00.txt codel.cs code2.cs
"""
def organiseOutput(baseFilename):
    """
    Parameters:
    Returns:
    Exception:
    """
    c_names = []
    cpp_names = []
    cs_names = []

    with open(baseFilename, 'r') as my_file:
        for line in my_file:
            filename = line.strip()
            if filename.endswith(".c"):
                c_names.append(filename)
            elif filename.endswith(".cpp"):
                cpp_names.append(filename)
            elif filename.endswith(".cs"):
                cs_names.append(filename)
        print(c_names)
        print(cpp_names)
        print(cs_names)

baseFilename = 'test.txt'
organiseOutput(baseFilename)