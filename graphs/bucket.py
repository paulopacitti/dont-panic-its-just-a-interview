def strokesRequired(picture):
    print(picture)
    strokes = 0
    visited = [[] for i in range(len(picture))]
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            visited[i].append(False)
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if not visited[i][j]:
                dfs(i, j, picture[i][j], picture, visited)
                strokes += 1
    return strokes
    
def dfs(i, j, color, picture, visited): 
    visited[i][j] = True
    if not invalid_position(i+1, j, picture) and not visited[i+1][j] and picture[i+1][j] == color:
        dfs(i+1, j, color, picture, visited)
    if not invalid_position(i, j+1, picture) and not visited[i][j+1] and picture[i][j+1] == color:
        dfs(i, j+1, color, picture, visited)
    if not invalid_position(i-1, j, picture) and not visited[i-1][j] and picture[i-1][j] == color:
        dfs(i-1, j, color, picture, visited)
    if not invalid_position(i, j-1, picture) and not visited[i][j-1] and picture[i][j-1] == color:
        dfs(i, j-1, color, picture, visited)
    else:
        return
    
def invalid_position(i, j, picture):
    if i < 0 or j < 0 or i >= len(picture) or j >= len(picture[0]):
        return True
    else:
        return False

a = ['bbbbabbbbaababbbbbbbbbba', 'aacabbaabbbbabbbabbbabba', 'bbcbaaabbbbbbabbbbbbbaba', 'bbbababbcbbcbbaacbbbbbab',
 'abbabbbaabbbbbbbbbabbbbb', 'bbbbabbbbbaabbacbbabbaba', 'aababbbbbbbbaabbbbbbabba', 'abbbaabbabbbbbbbcbbbbbbb',
'bbbaabbbbbabbbbbbbbababb', 'bbbbbbbbbacabbbbbbbbbabb', 'bbbbbbbabbbaabbabbbbbbbb', 'bcbcbabbbababbbbbbbaabab',
'bbbbabbbabbabababbbbbcbb', 'bbbbabbbbbbbbbbbbbbababb', 'aabbbbbabbaababbbbbbbbab', 'abbbbbaaabbbbbbbabcababb',
'bbbbbbbabbbbabbbbbabbabb', 'babbacbaabbbbbbabbabbbab', 'bbbbbbababbbbbbabababbbb', 'bbabacbbabbcbbbbaabbbabb',
'abbbbcbbbbabbbbababbaaba', 'aabaaabbbbbbcbaabbabbaba', 'baaaabbbbababbbbbbbabbab', 'bbaabcbabbbaababbbbbabbb',
'baababbbbbababbabbabbbbb', 'baabbbbbbbababbbabbaabbc', 'baabbbabbbbbbbababbbaabb', 'baaaaabaabbbbbbbbbbbbcab',
'bbbbabaabbbbbabbbbbbcbbb', 'bbbbbbabaaabbbbbbbbbaabb', 'bbbabbcbabbbbbabbbbbbbba', 'abbbaabbbbbbbbabbaaaabbb',
'abbbabbbbcbbababbbabbbab', 'bbabbbbbabbbbbbaabbabccb', 'bbbbaaabbbbbbbabbcaaaaaa', 'aabacbabbbbbbabbbaaaabab',
'bbbbaabcbbababbbcabbcbaa', 'ababbabbbbbbaababbabaabb', 'bbbabbbbbbababbbbbbbbabb', 'aaabbbbaabbaaaababbbbbaa',
'bbbbabbabbbbbbabbbbbcbaa', 'bbbbaabbbbbababbabbabbba', 'bbbbbaaacabbabbbaacbbbab', 'abcbabbbababbbbbbbbbbbbb',
'abbbaabbbbaabbbbbbbbbbba', 'abbabbbbbbbabbabbbbbbaba', 'bababbbabbababbbabbbbbbc', 'bbbbbbbbaabababbbbabbbaa',
'bbbabbbabbacbbbabbbbbbba', 'bbbaaabbbbbabbaababaaaab', 'bcbbcbabcababababbbbbbab', 'bbbbbbbababbbbabbbbbbbbb',
'bbbbabbbababbbbaabbbbabb', 'bbbbababbbbbbabbbbbabbbb', 'bbbbbbbabbabababbbcabaaa', 'ababbababababbabbbabbbab',
'bbaabaaaabaabaabababbbbb', 'abbabaabbbabbbbcbbbbabab', 'abbbbababbcbcbbbbaabbaba', 'bbbbbbaabbabacbbbabababa',
'bbbbcbbbbbaabbbbbaccbbba', 'bbbbbabbbababbabbbababbb', 'babbbbbabbabaaabbbaabbbb', 'bbbbbbbbbbbababbbbacabba',
'babbbbaababbaabbbaabbbab', 'bbbaabbbbababbbbbbbaabbb', 'bbbababbbbbbbabbbbbabbba', 'bbabbababbbbbbbbbbbbbabb',
'aaaaabbaaabacbbbabbabaab', 'baaaaabbbbbabbbabbbbbaba', 'bbbabbbbbbabbbbbbbbaaabb', 'babbacabbbbaabbbbcbbabab',
'bbcbbabbbbbbbbaabbbbbbab', 'babbbbbbbbbaaabbcbbbabba', 'bbbbbbbbcbabbbbbbbbbbbca', 'bbbaabaabbbabbbaababcabb',
'bbbbabaabaabababbbbbbabb', 'bbbbcaabbbbbbbbbabbbaabb', 'bbbbbbbbcbababbaabcbbbbb', 'abbabbabbabcbbbaabbabbbb',
'cababbbabaaacabbbabbbbbb', 'bbabbbbcbbbabbacbacbbbab', 'ababbbababaabbbbabbbcabb', 'bbbbababbbbbabaabbbbbbbb',
'ababbbbbbbbbbabbbbabbbbb', 'bababbbaaaaaababbbbabbab', 'bbbbbcabbbbbbbbabbbaabbb', 'bbbbbbabbaababbaabbbbbca',
'bbaabbbbbbbbbaabcbbabbbb', 'aaabcbabbbacbbbabbbccbbb', 'bbbaabbbbbababbabbbbbbbb', 'bbbbaaabbbbababbaabbbabb',
'bbaabbabbbbbbaabbbabbaba', 'baabaaaabbbbbbbcbaababab', 'bbabbaabbbbbabbbbbbbbbab', 'bbbaaaaabbbbacbababbbaba',
'abbbbbbbabbababbbbbbbaab', 'bbbbcbabbbbbabbbbabbbabb', 'abbbbbaaababbbacbbbbabbb', 'bbabbabababaabbabbbbbbab',
'babbbbbbbbbabbbbaababbcb', 'abbbbbbaabbabbabbbbbaaab', 'bbbbabababbaaabbbbbbbabb', 'abbbbabbbabaaaaaabababbb',
'bbbbaaaabbbbbbaabbbbbaba', 'bbabbbbbbabababbbbbbbaaa', 'bbbbabbbaaabbbbabbbbbbba', 'babbabbabbbbababbbbbabba',
'abbbbbbbbbbbbbaabbabbbab', 'bbbbbbabbbbbabbabbbbbbab', 'aabbabbbcbbaabbbbbabbbbc', 'bbbbbbbabbabbbbbbabbbabb',
'aabbaabbbbbaabbbbbbababb', 'bbbbbabaababbbbabcababcb', 'abbabbbbbbbbbababbbbbbba', 'bababbbabbbabbaaabaabbba',
'bbbabbbbbaabaabbbbbbbaaa', 'bbbabcbbbbbbbabbbbabbabb', 'bbbbabcbbbbaabbbbaababba', 'bbbbbabbbbbbbbbabbbbbabb',
'abbaabbbbabbbabbbabbbbaa', 'abbbbaabbbbbabbbbaabbaaa', 'bbbbababbabbbbaabbabbbba', 'bbbabaabaabaabbaabababba', 'bbbabaabbbbbbbbbbcbbbbaa', 'babbbbbbbacabbbbbbbbabcb', 'bbbbabbabbbbbabbabbbbaab', 'bbbbbbabbabbbbbbbbabbbba', 'baabbbbabaaaabbbbbaabbba', 'aaaaabaabbabbbabbbabbbbb', 'bbbabababbbbbbbbaaabbbbb', 'bbaaabbabbbbaaabbbbbbbbb', 'babbbbbbabbabbbabbbbbabb', 'abcbbbbbbbbbbbabbababbab', 'babbbbaacbaababbbbbbabbb', 'bbbaaababbbbbbbbbababbab', 'acabbbbbbabbbbbbbbacbbbb', 'cbbbbbbbabbbbbbbbabbbbbb', 'bababababbbbbaabbbbabbaa', 'abbbbbbbbbbabbbabbcbabbb', 'abbaaaabbcbbbbbaababbbab', 'abbaabababbabbbbbbbbbbbb', 'abbabcbabbabbbbabbbaaabb', 'ababbabbbbbbabbbbbbabbcb', 'abbbbbbbabbabaabbabbabbb', 'aabbaabbbbbabbbbaababbbb', 'bbbbabbabbaabbbbbbbbbbba', 'baabbbabbabacbbbabbabbbb', 'bbbbbabbbbabbabbbbbabbaa', 'abbcbbbaabbbbbbbacbabbbb', 'bbbbbbabbbbababbbbababbb', 'bbabbabbbbbabbbbaaacabbb', 'bbbabbabbbbbbbabbaabbabb', 'aababbbbcbabbabacababbba', 'bababbbabbababacbbbabbba', 'acbabcbbabbbbcbbaababbbb', 'bbbbabcbbbcbbbbbbbbbbcbb', 'bbbbabaabaaabababaabaabb', 'bbbbababbbbbbbabbaabcbbb', 'bbbbabbbbbbbbababaabbbbb', 'cbbbbbbbabbbbbabbbbabbbb', 'bbbbaabbabbbbabbbbabbaba', 'abbbbbbbbbbababbbabbbaaa', 'bbbbbbcbbbbaaabbbabaaabb', 'bbabbbabbbbcbabbbbbaaabb', 'abcbbbbbbaaaabaaaaaabaab', 'bbbbaaaababbbbbbabbbbaab', 'cababbbbbaabbbbbababbbbb', 'abbbaaabbbbbbbabbbbbabba', 'bbaaabbbbaabbbbbbbbababb', 'aaababbabbbbbbbbbbbbaabb', 'bbbabbacbababbbbbbbcbbbb', 'bbbabbcbbbabbbbbabbbbbbb', 'bbbcbbabbbbabbaabbbbbbbb', 'bbbbbaabbbbabbbbcabbbabb', 'bbabbabbbcbbbbbaabbabbab', 'bbababbbbbbababbabbbbbbb', 'abbaabbabbbbcabbabcbbabb', 'bbbbccbbbaabbbacbbabbbbb', 'bbababbbbbbababbbabbbbab', 'aabaabbababbbbaabbbbabab', 'bbababbbbbbbbbbbbaaabbba', 'bbaabbbbcaabbbbabcbbabba', 'aaababbbaabbbbbabbabaaab', 'abbabbbbbbbbbbbbbabbcbab', 'ababbbbbbbbaaababbaabaab', 'babaaabbbbbbbbbbbabaaaab', 'abbbbbbaababaaabaaabbbaa', 'bcababbabbababbaabbababb', 'bbaabbbbabbabababababbbb', 'bbacbbbbbaaabbbbbabcbbbb', 'bbbbbabbbbcabbabbabbbbbb', 'babbbbbababbababbbababbb', 'bbcbcbbabbbabbbbbabbabbb', 'babbbbbbaabbbabbbbbabbbb', 'bbabbabbbaababbbbbbbbabb', 'bbbbbbbbbabbbbbbbbbbaaba', 'bbabbcaaabaabababababbba', 'abbbabbbbbbbabbabbaabbab', 'bbbaabbbbbbbbbaabbbbbbab', 'bbaabbababaabbababbbbbab', 'bbababcbbaaabcbbbbbbaaab', 'aabbbbabaaacbbbbabababaa', 'aabbbacbbbbbbbbaabbbabbc', 'baabbbabaabababbabbbbaab', 'bbabbcbabbbcbaabbbababbb', 'bbcbaabbbaababbabbabbbba', 'bbabbbbbababbbbbabbbbaab', 'bbbababababbbbabaabbbbbb', 'aabcbbabacaabcbbbbbbbabb', 'bbbaabbbaabaabbbabaabbcb', 'babbabbbbbbbbaabbaaaaaba', 'abbaaabbbbbbbbabaabbabbb', 'bbbbbababaaaabbabbabbabb', 'bbbabbbbbabbbabbababbaba', 'babbabbabbbbbbbbbbaabbbb', 'bababbbbbbbaabbbbbabbbbb', 'abbbbbbababbbbbaabbaabbb', 'bbbbbabaabbabababbaababb', 'babbaabbbaabbbabababbbbb', 'babaabaaaababbbaaaacbcba', 'bbbbbbbbaabbbbbababbbbba', 'bbbbbbaabbbbbaabbbbbbbbb', 'bbbbbabababbbabcbbbbbbbb', 'bbaaabbbcbbbbabbbbbbbaab', 'abbbbbbbbbbbbbababababbb', 'aabababbbbaababaabbaabbb', 'bbcbcbbbbababbbaaabbbbbb', 'bbbbbbbbabaabbbbbbbbbbab', 'aaabbbabaabbbbabaababbab', 'bbbbbbbaabbbaababbbabbbb', 'bbbbbbacbaabbabbbbbbabba', 'bbbaababbbaabbbbbabbbbbb', 'bbabababbbbabbcbbbbbabbb', 'caabbbabbbbbabbbabbaabbb', 'bbbbbbbbbabaabbbbaabbabb', 'abbcababbbbababbbbbbabab', 'bbbbbbbcababbbbbacbbcabc', 'babbaabbbbbbbabbabbabbbb', 'babaabbbaabbbbbabbbbbcbb', 'bbbbbbabbbaabbabaabbbaab', 'abbbbbbbbbaaaabbbbaaabba', 'aaababbabbbcbbabbabbbbbb', 'bbababbaabbbbabbbbbbbbba', 'aaababbabbbbbbbbbbabbabb', 'bbbbbbbaabbbbcabbabcbbaa', 'babbaababbabbbbbbbabbbab', 'bbbcbbbbbbbbbbbabbbbbabb', 'bbbbbabbbbbaabbbbbbabbba', 'bbbbabbabbabcbabbabbbabb', 'babbababababbbbbaababbba', 'abbbbaabbbabbabaaabbbabb', 'bbabbbbbaabbaaaaaaababbb', 'aabbbabbbbabbabbbaabbbbb', 'bbbaabbbbbbbbbbbababaabb', 'bbbababbabababbbabbbbbbb', 'cbbbaabbababababbabaabab', 'bbbbaaabbcbbbbababbbbbbb', 'bbabbbbbbaabababbabaabbb', 'bbabbbbbabaabaabbabaabab', 'bbbbbbbbbabbbabbbbbaabbb', 'bbbababbbabbabbaabbbbbba', 'bbbabbbbabbbabbcbbabbbab', 'bbbbbaaabbbbaabbbabbbbbb', 'bbbabbbabbabbababbabbaaa', 'bbbababbbbbbbabbbbbbbbbb', 'aaababbbcabbabbbabbbabaa', 'abbbbbbbbbbababbabbbbbbb', 'babbbbabaaabbabbababbbbb', 'bbbbbaabbabbabbbaacbcaba', 'bcbbcacaabbbbaabbbbaabba', 'bbbbbaabbbabbaabbaaabbbb', 'bbbbbabbbbbbbbbbbbbacbbb', 'bbbbbbbbbbbbabaaaaaababb', 'babbbbbabbbaaaaabbbbbbaa', 'bbaaabaababbabbbabbaabbb', 'abbbaabbbbbbabbabaabbbbb', 'bbbbbbbbabbbaaacbbababba', 'bbbbbbbbbaabaabbabbbabbb', 'abbbbbbbbbababbbbbcbaaba', 'abbbbbabbaaabbabbbbababa', 'bcbbbbbbbbbbabaaabbbbbbb', 'bbbbbbbbbabbaaabbabbbbaa', 'bbbaaabbbababbbbaabbbaba', 'aabbbbbacabbbbbbbbbbbbbb', 'bbababcbbabbbabbbbbbbbba', 'abaabbbbbbabbbbbbbbbbbba', 'baabbbbbaabaabbbbaaabbbb', 'bbbbbababaaaabaaabbabbba', 'abcaaaabbabbbbbbbbbbbaba', 'abbaabbbbbcbbababbbabaab', 'abbbabbbbbbacababaaaabbb', 'aaacbbaabbbababbabbbabbb', 'babaabbaaabababbbbababbb', 'bbbbbabbbaabbbbbacbbbbbb', 'babbbbaaabbbabbbabbbaaaa', 'babbabcbbaabababbabbabbb', 'bbabbbabbbabbbbbabbbbbab', 'aabbaabcbbbaabbbbbbbbbab', 'abbbbababbbaaabbabbbabbb', 'abbababcbbbbbbacbbbbbbbb', 'bbababbbbbbcbbbbbbabaaab', 'babbbabbbbbabababbbabbbb', 'bbaaabbbbbabbacbbaabbbbb', 'aaaabcbbabbacbbabbbabbba', 'bbbbbbbabcbbbababbabbbbb', 'babbbabababbbbabbbabbaba', 'cabababbabaaababbbababba', 'abbbbbbabbbbabbbbbbbbbaa', 'bbbbbbbbbabbbbbbbaabbbbb', 'bbbcbbbaabbbabbaabbbbabb', 'aabbaababbbbcbbabbabbbbb', 'abbbbbbbabbbaabbbabbabbc', 'aabbabbaabcbbbbbabbabbaa', 'bbbbababbbbaaabbbbbaaaac', 'aacbababaabbbbbaaabbabbb', 'abbbbbabbabbbbabbbbbcbba', 'bbbbcbbbbbbbcbabbbbbbaab', 'bcbbbbbbbcbabbbbaaabbbbc', 'aabaabbbbbaabaaabcabbbcb', 'aabbaacbbbbbbbbabbabbbbb', 'bbbabababbbbbbbabbbbbbba', 'abbbaabbabbbbbbbabaababa', 'bbaababbbbbabbbbbbabaabb', 'cbbbbabbbbbbbabbbbabbbab', 'baaabbbbbbbabbabbbbaabbb', 'abaabababbbbbbbabbbbbbbb', 'cbcbbbbbbababaaaabbbbabb', 'abbabbbbbbbbabaabbbababb', 'babbbbaababababbcbbbbbbb', 'bbbbabcaaababbbabbaaaaab', 'bbabaaabaabbbaabbbbcbacb', 'abbbbbbbabaaaababbabbcbb', 'bbaabbbaabbaaabbbbbbabbb', 'bacbbbbbaabbbbbbbbabcbaa', 'abbbabbbabaabaabbabbbbba', 'bbbaaaabbbbcbaaabbbbbbba', 'bbbababbbabbabaabbbbaaaa', 'babababbbbabbbbababbabba', 'abbbbbbbabbababbbcbbabbb', 'bbbbbbbbbabacbbbaabbbbbb', 'bbbbaaabbbbabbaabbbaaaba', 'bbbbbbbbbbbbbbababbbbabb', 'abaaabbbbabbabbabbabbcbb', 'bbbbbbbaaaaaabbbbbbbaaaa', 'bbbaaabbbbbbbbbbbababbba', 'aabbbbbbbbabbcababbbbbba', 'bbabaaaaabbcbbbbaaababbb', 'abbbabbabaabbbbbbbabbbbb', 'bbaabbaaabaabbbbbabbabab', 'bbbabbaabaaaabababbbabab', 'abbababbacabbbbbbbabbbbc', 'bbbbbbbabbbabbaabaababab', 'babbabbababcabbbababbbbb', 'bbbbaaabbbbcbabbbbbbbbac', 'bbbabbbbbabbababbbabbabb', 'bbbabbbabbababbbbabbbbaa', 'bbbbcbabbbbbbbbb', 'bbbbbbbbbabbabbabbbabbbb', 'abbbabbbbcbaabbabbabbbab', 'bbbababbbbbaaabbbaaabbbc', 'ababbbbbbabbabbbabbcbcbb', 'bbbbbababbbbbbabbababaab', 'bbacbcbaabaabbabbcbcabaa', 'babbabbbbbacbaabbaababbb', 'bbbbbabbbbaabbbbaa']

result = strokesRequired(a)
print(a)
