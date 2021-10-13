def pig_it(text):
    s1 = (text.split())
    ans = ' '

    for i in s1:
       if i in '!.%@&?':
           ans = ans + i
       else:
           ans1 = i[1:] + i[0] + 'ay'
           ans = ans + ans1 + ' '

    return ans.strip(' ')
print(pig_it('Pig latin is cool'))
    

