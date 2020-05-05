import os
import errno


def save_func(final_urls, outfile, filename):
    if outfile:
        if "/" in outfile:
            file_path = f'{outfile}'
        else:
            file_path = f'output/{outfile}'
    else:
        file_path = f"output/{filename}.txt"

    if os.path.exists(file_path):
        os.remove(file_path)

    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    for i in final_urls:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(i + "\n")
