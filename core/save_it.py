import os
import errno


def save_func(final_urls , outfile , domain):
    if outfile:
        if "/" in outfile:
            filename = f'{outfile}'
        else : 
            filename = f'output/{outfile}'
    else :
        filename = f"output/{domain}.txt"
    
    if os.path.exists(filename):
        os.remove(filename)

    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: 
            if exc.errno != errno.EEXIST:
                raise
    
    
    for i in final_urls:
        with open(filename, "a" , encoding="utf-8") as f:
            f.write(i+"\n")