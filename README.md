# Solution
Simple repo.

- ## Section 1: Data Structures
Solve any two problems out of these three
——————————————————————————————————————————
- #### Problem 1: https://www.interviewbit.com/problems/3-sum/
Solution Code : https://github.com/MohitKumarMandhre/Solution/blob/master/ProblemStatements.txt
- ![alt text](https://github.com/MohitKumarMandhre/Solution/blob/master/prob1.PNG)

- #### Problem 2: https://www.interviewbit.com/problems/redundant-braces/ 
Solution Code : https://github.com/MohitKumarMandhre/Solution/blob/master/ProblemStatements.txt
- ![alt text](https://github.com/MohitKumarMandhre/Solution/blob/master/prob2.PNG)


- ## Second 2: Linux - Solve this basic problem
- Refer :- https://goo.gl/EPpifR

## To setup all the libraries use :-

- #### S-1) Create json file cointaining dependencies
- ![alt text](https://github.com/MohitKumarMandhre/Solution/blob/master/reqJson.PNG)

- #### S-2) cd to the directory where req.json is located.

- #### S-3) Create & activate your virtualenv.

- #### S-4) Define scripts ( .py file )
https://github.com/MohitKumarMandhre/Solution/blob/master/f1.py


- #### S-5) Run python file in your shell. ( $ python f1.py) 
- ![alt text](https://github.com/MohitKumarMandhre/Solution/blob/master/beforeD.PNG)
- ![alt text](https://github.com/MohitKumarMandhre/Solution/blob/master/after.PNG)

# SOLUTION 2 


- Defined scripts ( .py file ) https://github.com/MohitKumarMandhre/Solution/blob/master/f1.py


- ### Q. make sure that the code des'nt  crash anywhere
- Sol. => * surround code in a try catch block and print the error
-         * case 1: wrong file, throws exception ( No such file or directory: 'req1111.json' )
-         * case 2: the file is empty throws exception ( Expecting value: line 1 column 1 (char 0) )
-         * case 3: the file's data is not in json format throws exception (Expecting property name enclosed in double quotes: line 1 column 1 (char 0) )
- ![alt text](https://github.com/MohitKumarMandhre/Solution/blob/master/case1.png)
- ![alt text](https://github.com/MohitKumarMandhre/Solution/blob/master/case2-1.png)
- ![alt text](https://github.com/MohitKumarMandhre/Solution/blob/master/case2-2.png)

- ### Q. file can be huge ....limit memory usage  ``     => iterate one by one
- Sol. => * using an iterator as it is faster and has better memory efficiency
-         * allows a user to process every element of a json obj. individually

- ### --------------> parallel exe.
- Sol. => * idea is to create 2-threads that will process the same file simultaneously
-         * thread1 handles first half of packages by calling install method
-         * thread2 handles other half of packages by calling install method
- ![alt text](https://github.com/MohitKumarMandhre/Solution/blob/master/case%203.PNG)


