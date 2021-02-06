import re 


def param_extract(response, level, black_list, placeholder):

    ''' 
    Function to extract URLs with parameters (ignoring the black list extention)
    regexp : r'.*?:\/\/.*\?.*\=[^$]'
    
    '''

    parsed = list(set(re.findall(r'.*?:\/\/.*\?.*\=[^$]' , response)))
    final_uris = []
        
    for i in parsed:
        delim = i.find('=')
        second_delim = i.find('=', i.find('=') + 1)
        if len(black_list) > 0:
            words_re = re.compile("|".join(black_list))
            if not words_re.search(i):
                final_uris.append((i[:delim+1] + placeholder))
                if level == 'high':
                    final_uris.append(i[:second_delim+1] + placeholder)
        else:
            final_uris.append((i[:delim+1] + placeholder))
            if level == 'high':
                final_uris.append(i[:second_delim+1] + placeholder)

    # for i in final_uris:
    #     k = [ele for ele in black_list if(ele in i)]
    
    return list(set(final_uris))
