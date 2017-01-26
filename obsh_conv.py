# -*- coding: utf-8 -*-
import sys
from datetime import datetime
import unicodedata
import re

def convert_txt(input_filename, output_filename):
  input_file = iter(open(input_filename, 'rU'))
  output_file = open(output_filename, 'w')
  true_ans_list = [1,3,2,1,4,3,4,1,4,2,3,4]
  print true_ans_list
  num_task = 0
  try:
    while True:
      line = input_file.next()
      match = re.search(r'\d?\d\.', line)
      if match:
        print match.group()
        num_task += 1
        if num_task > 5:
          num_task -= 5
          true_ans_list.pop(0)
        print num_task
        line = line.replace(match.group(), '<<<TASK_A>>>')
        line = line.strip()
        output_file.write(line+"\n")
        for i in range(1,5):
          line = input_file.next()
          line = line.strip()
          if i == true_ans_list[0]:
            line = line.replace(str(i)+")", '<<<ANS_T>>>')
          else:
            line = line.replace(str(i)+")", '<<<ANS_F>>>')
          output_file.write(line+"\n")
  except(StopIteration):
    input_file.close()
    output_file.close()

def main():
  if len(sys.argv) != 2:
    print 'usage: ./obsh_conv.py input_filename' 
    sys.exit(1)

  input_filename = sys.argv[1]
  output_filename = sys.argv[1].replace('.txt', '') + "_out.txt"
  f = open(output_filename, 'w')
  f.close()
  convert_txt(input_filename, output_filename)
  
if __name__ == '__main__':
  main()