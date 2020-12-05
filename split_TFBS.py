import sys
import math
import io
from platform import python_version
from pathlib import Path


def check_script_environment():
    ver = python_version()
    if ver[0:3] != '3.7':
        print('please check your python version, it should be 3.7.x')
    
    # create result folder
    Path("out").mkdir(parents=True, exist_ok=True)

def command_parser(argv):
    if len(argv) != 4:
        print('usage:')
        print('\tsplit_TFBS.py /path/to/source_file ${prefix} ${titleline_number}')
        exit(1)
    else:
        source_file = argv[1]
        prefix = argv[2]
        titleline_number = int(argv[3])
    return source_file, prefix, titleline_number

def read_source_file_content(source_file):
    TFBS_list = []
    with open(source_file, 'r') as f:
        # suppose source file can be load into memory entirely
        file_content = f.read()

        # split_result's first element is ''
        # split() will remove '>'
        TFBS_list = file_content.split('>')[1:]
        TFBS_list = ['>' + element for element in TFBS_list]
    return TFBS_list

def get_titleline_name(TFBS_list):
    titleline_list = []
    for TFBS in TFBS_list:
        buf = io.StringIO(TFBS)
        titleline = buf.readline()
        titleline_list.append(titleline)
    return titleline_list

def calc_outfile_name(TFBS_idx):
    resultfile_postfix = int(TFBS_idx/titleline_number)+1
    format_str = '{:0'+s_resultfile_postfix_length+'d}'
    s_formatted_resultfile_postfix = format_str.format(resultfile_postfix)
    s_resultfile_name = './out/'+prefix+'_'+s_formatted_resultfile_postfix+'.txt'
    return s_resultfile_name


if __name__ == '__main__':

    check_script_environment()
    source_file, prefix, titleline_number = command_parser(sys.argv)

    TFBS_list = read_source_file_content(source_file)

    titleline_list = get_titleline_name(TFBS_list)
    with open(prefix+'_name.txt', 'w+') as f:
        for titleline in titleline_list:
            f.write(titleline)

    resultfile_total_number = int(len(TFBS_list)/titleline_number)+1
    # 10^3=1000 but len('1000')=4, so int(log10(n))+1
    s_resultfile_postfix_length = str(int(math.log10(resultfile_total_number))+1)
    for TFBS_idx in range(len(TFBS_list)):
        s_resultfile_name = calc_outfile_name(TFBS_idx)
        with open(s_resultfile_name, 'a+') as f:
            f.write(TFBS_list[TFBS_idx])