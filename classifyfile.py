import os

def get_file(filepath):
    files_path = os.listdir(filepath)
    sql_type =['sql']
    xml_type = ['xml']
    for fi in files_path:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            get_file(fi_d)
        else:
            filename = os.path.join(fi_d)
            suffixname = filename.split('.')[-1]
            if suffixname in sql_type:
                sql_files.append(filename)
            if suffixname in xml_type:
                xml_files.append(filename)
    return sql_files, xml_files


if __name__ == "__main__":
	sql_files, xml_files=[], []
	sql_files, xml_files = get_file(filepath=search_dir)
	print(sql_files)
	print(xml_files)
