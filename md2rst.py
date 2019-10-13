# coding:utf-8
"""

# import commands  # python3 中已经deprecated

"""
import os
import subprocess
from os.path  import dirname
base_dir = dirname( __file__) 
blog_path = os.path.join(base_dir,'source')

# print(f"basedir :{base_dir}")
# print(f"blog_path:{blog_path}")

folder = blog_path

os.chdir(folder)
print('===== Processing folder {} ====='.format(folder))
all_file = os.listdir(folder)
all_md_file = [file for file in all_file if file.endswith('md')]
for file in all_md_file:
    (filename, extension) = os.path.splitext(file)
    convert_cmd = 'pandoc -V mainfont="SimSun" -f markdown -t rst {md_file} -o {rst_file}'.format(
        md_file=filename + '.md', rst_file=filename + '.rst'
    )

    print(f"convert_cmd: {convert_cmd}")
    ret_code = subprocess.call(convert_cmd, shell=True)

    if ret_code != 0:
        print(file + '处理失败')
    else:
        # ret_code == 0
        print(file + ' 处理完成')
