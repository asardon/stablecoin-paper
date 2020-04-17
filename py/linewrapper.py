# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:00:42 2020

@author: Aetienne
"""

in_file = open("../conference_101719.tex", "r")
text_string = in_file.read()
out_file = open("../whitepaper_src_reformatting.tex", "w") 


last_cutoff = 0
idx = 0
while idx < len(text_string):
    if text_string[idx] == "\n":
        out_file.write(text_string[last_cutoff:(idx+1)])
        last_cutoff = idx + 1
        idx = last_cutoff
    if idx - last_cutoff < 77 - 1:
        idx += 1
    else:
        for idy in range(20):
            if text_string[idx-idy] == " " or text_string[idx-idy] == "\n":
                break
        out_file.write(text_string[last_cutoff:(idx-idy+1)]+"\n")
        last_cutoff = idx - idy + 1
        idx = last_cutoff
out_file.close()