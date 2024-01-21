# description: https://leetcode.com/problems/simplify-path/

def simplifyPath(path: str) -> str:
    dirs = path.split("/")
    current_path = []
    print(dirs)

    for i in range(len(dirs)):
        if dirs[i] == "" or dirs[i] == ".":
            continue
        if dirs[i] == "..":
            if current_path:
                current_path.pop()
        else:
            current_path.append(dirs[i])
    
    return "/" + "/".join(current_path)

# Time complexity: O(n), where n is the lenght of the characters to split
# Space complexity: O(d), where d is the number of directories