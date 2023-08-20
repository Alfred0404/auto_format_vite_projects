import os, time, dotenv

dotenv.load_dotenv()

root_dir = os.getenv('ROOT_DIR')

dir_list = os.listdir(root_dir)

files_to_replace = ['index.html', 'style.css', 'main.js']
files_to_delete = ['counter.js', 'javascript.svg', 'public\\vite.svg' ]


def show_directory_list(list) :
    print('\nCurrent directory list :')
    for item in list:
        print(f'   - {item}')


def check_file(file_path) :

    if os.path.exists(file_path) :
        print(f'\nFile {file_path} exists')
        return True

    else :
        print(f'\nFile {file_path} does not exist')
        return False


def replace_file(file_path) :

    if check_file(file_path) :
        print(f'Replacing file {file_path} ...')
        os.remove(file_path)
        print(f'File {file_path} has been removed')

        new_file = open(file_path, 'w')


def format_file(file_path) :

    if check_file(file_path) :
        print(f'Formatting file {file_path} ...')

        _, extension = os.path.splitext(file_path)
        current_file = open(file_path, 'w')

        if extension == '.html' :
            current_file.write(
                               '<!DOCTYPE html>\n'
                               '<html lang="en">\n'
                               '<head>\n'
                               '    <meta charset="UTF-8">\n'
                               '    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n'
                               '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
                               '    <link rel="stylesheet" href="style.css">\n'
                               '    <title>Document</title>\n'
                               '</head>\n'
                               '<body>\n'
                               '    <script src="main.js"></script>\n'
                               '</body>\n'
                               '</html>\n'
                            )

        elif extension == '.css' :
            current_file.write(
                               '* {\n'
                               'padding: 0;\n'
                               'margin: 0;\n'
                               '}\n'
                            )


def delete_file(file_path) :

        if check_file(file_path) :

            print(f'Deleting file {file_path} ...')
            os.remove(file_path)
            print(f'File {file_path} has been deleted')


print(f'Root directory : {root_dir}')
show_directory_list(dir_list)


def format_vite_project() :
    while True:
        time.sleep(5)
        updated_dir_list = os.listdir(root_dir)

        if len(updated_dir_list) > len(dir_list) :
            print('\nNew directory detected')
            show_directory_list(updated_dir_list)

            directory_added = [item for item in updated_dir_list if item not in dir_list]

            dir_list.append(directory_added[0])

            new_directory_path = os.path.join(root_dir, directory_added[0])
            print(f'New directory path : {new_directory_path}')

            for file in files_to_replace :
                file_path = os.path.join(new_directory_path, file)
                replace_file(file_path)
                format_file(file_path)

            for file in files_to_delete :
                file_path = os.path.join(new_directory_path, file)
                delete_file(file_path)

if __name__ == '__main__' :
    format_vite_project()