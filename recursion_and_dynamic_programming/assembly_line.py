# description: https://www.geeksforgeeks.org/assembly-line-scheduling-dp-34/

def assembly_line_dp(a, t, e, x):
    best_time_line_1 = [None for j in range(len(a[0]))]
    best_time_line_2 = [None for j in range(len(a[0]))]
    best_time_line_1[0] = e[0] + a[0][0]
    best_time_line_2[0] = e[1] + a[1][0]

    for j in range(1, len(a[0])):
        best_time_line_1[j] = min(best_time_line_1[j-1] + a[0][j], best_time_line_2[j-1] + t[1][j] + a[0][j])
        best_time_line_2[j] = min(best_time_line_2[j-1] + a[1][j], best_time_line_1[j-1] + t[0][j] + a[1][j])
   
    return min(best_time_line_1[-1] + x[0], best_time_line_2[-1] + x[1])

# Time Complexity: O(n), where n is the number of stations in each pipeline
# Space Complexity: O(n) 

def assembly_line(a, t, e, x):
    best_time_line_1 = e[0] + a[0][0]
    best_time_line_2 = e[1] + a[1][0]

    for j in range(1, len(a[0])):
        temp_1 = min(best_time_line_1 + a[0][j], best_time_line_2 + t[1][j] + a[0][j])
        temp_2 = min(best_time_line_2 + a[1][j], best_time_line_1 + t[0][j] + a[1][j])

        best_time_line_1, best_time_line_2 = temp_1, temp_2
   
    return min(best_time_line_1 + x[0], best_time_line_2 + x[1])

# Time Complexity: O(n), where n is the number of stations in each pipeline
# Space Complexity: O(1) 

a = [[4, 5, 3, 2],[2, 10, 1, 4]]
t = [[0, 7, 4, 5],[0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]
print(assembly_line(a, t, e, x))

