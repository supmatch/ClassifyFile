import os

def eachFile(filepath):
    files_path = os.listdir(filepath)
    sql_type =['sql']
    xml_type = ['xml']
    for fi in files_path:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            eachFile(fi_d)
        else:
            child = os.path.join(fi_d)
            arrs = child.split('.')[-1]
            if arrs in sql_type:
                sql_files.append(child)
            if arrs in xml_type:
                xml_files.append(child)
    return sql_files, xml_files


if __name__ == "__main__":
	sql_files, xml_files=[], []
	sql_files, xml_files = eachFile(filepath=search_dir)
	print(sql_files)
	print(xml_files)
