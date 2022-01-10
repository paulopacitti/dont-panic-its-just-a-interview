# description: https://massivealgorithms.blogspot.com/2019/09/leetcode-1152-analyze-user-website.html
def analysis(username, timestamp, websites):
    visits = {}
    logs_map = {}
    
    for i in range(len(username)):
        if username[i] in logs_map:
            logs_map[username[i]].append(websites[i])
        else:
            logs_map[username[i]] = [websites[i]]

    for values in logs_map.values():
        sequences = build_sequences(values)
        for s in sequences:
            if s in visits:
                visits[s] += 1
            else:
                visits[s] = 1
    
    max_occurences = -1
    max_sequence = None
    for k in visits.keys():
        if visits[k] > max_occurences:
            max_occurences = visits[k]
            max_sequence = k
    
    return list(max_sequence)

def build_sequences(array):
    sequences = []
    for i in range(0, len(array)-2):
        for j in range(i+1, len(array)-1):
            for k in range(j+1, len(array)):
                sequences.append((array[i],array[j],array[k]))

    return sequences

username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
print(analysis(username, timestamp, website))

# Time complexity: O(n³)
# Space complexity: O(len(usernames)*max(items_per_user) + n^3)