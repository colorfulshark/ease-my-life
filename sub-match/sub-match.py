#! /usr/bin/env python3
#! coding = utf-8

import sys
import os
import re

class FileHelper:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.mov_ext = ('avi', 'flv', 'mkv', 'mov', 'mp4', 'webm', 'wmv')
        self.sub_ext = ('srt', 'ssa', 'ttml', 'sbv', 'dfxp', 'vtt', 'ass')

    def get_file_ext(self, file_path):
        (name, ext) = os.path.splitext(file_path)
        ext = ext[1:].lower()
        return (name, ext)

    def analyze_file(self):
        self.mov_files = []
        self.sub_files = []
        files = os.listdir(self.dir_path)
        for f in files:
            # ignore hidden files
            if (f.startswith('.')):
                continue
            (_, ext) = self.get_file_ext(f)
            if (ext in self.mov_ext):
                self.mov_files.append(f)
            elif (ext in self.sub_ext):
                self.sub_files.append(f)

    def get_mov_list(self):
        return self.mov_files

    def get_sub_list(self):
        return self.sub_files

    def get_file_path(self, filename):
        return '{}/{}'.format(self.dir_path, filename)

    def rename_sub(self, mov, sub):
        (mov_name, _) = self.get_file_ext(mov)
        (_, sub_fmt) = self.get_file_ext(sub)
        new_sub = '{}.{}'.format(mov_name, sub_fmt)
        os.rename(self.get_file_path(sub), self.get_file_path(new_sub))


class SubMatch:
    def __init__(self):
        self.parse_args()

    def show_help(self):
        print('usage: sub-match.py [movie path]')

    def parse_args(self):
        if (len(sys.argv) < 2):
            self.show_help()
            exit(1)
        arg1 = sys.argv[1]
        if (arg1 == '-h' or arg1 == '--help'):
            self.show_help()
            exit(0)
        self.dir_path = arg1

    def run(self):
        fh = FileHelper(self.dir_path)
        fh.analyze_file()
        mov_list = fh.get_mov_list()
        sub_list = fh.get_sub_list()

        # if there is only 1 film and 1 subtitle, they should match with each other
        if (len(mov_list) == 1 and len(sub_list) == 1):
            fh.rename_sub(mov_list[0], sub_list[0])
            return
        # use standard episode schema SxxExx
        for mov in mov_list:
            res = re.findall('s\d*e\d*', mov.lower())
            if (len(res) == 0):
                continue
            episode = res[0]
            for sub in sub_list:
                if (sub.lower().find(episode) == -1):
                    continue
                fh.rename_sub(mov, sub)
                break

def main():
    SubMatch().run()

main()
