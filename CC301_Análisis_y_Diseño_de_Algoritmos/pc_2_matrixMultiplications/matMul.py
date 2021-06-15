import numpy as np 
import time
import argparse
import matplotlib.pyplot as plt
  
def split(matrix): 
    """ 
    Splits a given matrix into quarters. 
    Input: nxn matrix 
    Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d 
    """
    row, col = matrix.shape 
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:] 
  
def strassen(x, y): 
    """ 
    Computes matrix product by divide and conquer approach, recursively. 
    Input: nxn matrices x and y 
    Output: nxn matrix, product of x and y 
    """
  
    # Base case when size of matrices is 1x1 
    if len(x) == 1: 
        return x * y 
  
    # Splitting the matrices into quadrants. This will be done recursively 
    # untill the base case is reached. 
    a, b, c, d = split(x) 
    e, f, g, h = split(y) 
  
    # Computing the 7 products, recursively (p1, p2...p7) 
    p1 = strassen(a, f - h)   
    p2 = strassen(a + b, h)         
    p3 = strassen(c + d, e)         
    p4 = strassen(d, g - e)         
    p5 = strassen(a + d, e + h)         
    p6 = strassen(b - d, g + h)   
    p7 = strassen(a - c, e + f)   
  
    # Computing the values of the 4 quadrants of the final matrix c 
    c11 = p5 + p4 - p2 + p6   
    c12 = p1 + p2            
    c21 = p3 + p4             
    c22 = p1 + p5 - p3 - p7   
  
    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically. 
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))  
  
    return c 


if __name__ == '__main__':


    parser = argparse.ArgumentParser(description="number of iterations")
    parser.add_argument('--iterations', type=int, default=None, required=False,
                        help='plot graphic')

    args = parser.parse_args()

    print("--------------------------------------------")
    print("\nWelcome to Matrix Multiplication Methods\n")
    print("--------------------------------------------\n")
    
    if args.iterations is None:
        flag = True
        while flag:
            number_matrixs = int(input("Type the number of the square matrices (dim 32): "))
            if number_matrixs > 0:
                matrix_test_1 = np.random.randint(low = 100, size = (number_matrixs, 32, 32))
                matrix_test_2 = np.random.randint(low = 100, size = (number_matrixs, 32, 32))

                # using numpy methods
                start1 = time.time()
                result_with_numpy_methods = np.dot(matrix_test_1, matrix_test_2)
                done1 = time.time()
                elapsed1 = done1 - start1

                # using Strassen method
                start2 = time.time()
                for i in range(number_matrixs):
                    #print("{} {}".format(matrix_test_1[i].shape, matrix_test_2[i].shape))
                    result_with_Stresseny_method = strassen(matrix_test_1[i], matrix_test_2[i])
                done2 = time.time()
                elapsed2 = done2 - start2

                # using naive method
                start3 = time.time()
                for i in range(number_matrixs):
                    result_naive_method = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*matrix_test_2[i])] 
                    for A_row in matrix_test_1[i]] 
                done3 = time.time()
                elapsed3 = done3 - start3
                

                print("--------------------------------------------")
                print("--------------------------------------------")
                print("\nThe times of each method:\n")
                print("  * Numpy methods: {}".format(round(elapsed1, 6)))
                print("  * Strasseny method: {}".format(round(elapsed2, 6)))
                print("  * Naive method: {}".format(round(elapsed3, 6)))
                print("--------------------------------------------")

                exit_option = input("\nDo you want to continue? type Y/N: ")
                if exit_option == 'N' or exit_option == 'n':
                    flag = False

            else:
                print("Size incorrect, type again!\n")
        print("\n--------------------------------------------")
        print("Happy codding!\nAuthor: Cristhian Wiki")
        print("--------------------------------------------\n")

    else:
        x_iteration = [0]
        y_time_np = [0.0]
        y_time_stny = [0.0]
        y_time_naive = [0.0]
        for i in range(args.iterations + 1):
            if i !=0  and i%10 == 0:
                print(i)
                x_iteration.append(i)
                matrix_test_1 = np.random.randint(low = 100, size = (i, 32, 32))
                matrix_test_2 = np.random.randint(low = 100, size = (i, 32, 32))

                # using numpy methods
                start1 = time.time()
                result_with_numpy_methods = np.dot(matrix_test_1, matrix_test_2)
                done1 = time.time()
                elapsed1 = done1 - start1
                y_time_np.append(elapsed1)

                # using Strassen method
                start2 = time.time()
                for j in range(i):
                    #print("{} {}".format(matrix_test_1[i].shape, matrix_test_2[i].shape))
                    result_with_Stresseny_method = strassen(matrix_test_1[j], matrix_test_2[j])
                done2 = time.time()
                elapsed2 = done2 - start2
                y_time_stny.append(elapsed2)

                # using naive method
                start3 = time.time()
                for j in range(i):
                    result_naive_method = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*matrix_test_2[j])] 
                    for A_row in matrix_test_1[j]] 
                done3 = time.time()
                elapsed3 = done3 - start3
                y_time_naive.append(elapsed3)
        
        plt.plot(x_iteration, y_time_np, color='k', linestyle='dashed', linewidth = 3, 
         marker='o', markersize=10, label = "Numpy methods")
        plt.plot(x_iteration, y_time_stny, color='g', linestyle='dashed', linewidth = 2, 
         marker='o', markersize=10,label = "Strassen method")
        plt.plot(x_iteration, y_time_naive, color='r', linestyle='dashed', linewidth = 2, 
         marker='o', markersize=10,label = "Naive method")

        # naming the x axis 
        plt.xlabel('iterations') 
        # naming the y axis 
        plt.ylabel('time (s)') 

        # giving a title to my graph 
        plt.title('time complexity of algorithms') 
        # show a legend on the plot 
        plt.legend() 
        plt.show()

    
