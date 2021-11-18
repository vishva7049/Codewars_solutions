def find_admin(lst,lang):

    l1= []

    for ele in lst:
        if(ele['githubAdmin']== 'yes' and ele['language'] == lang):
            l1.append(ele)
    return l1