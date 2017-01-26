# -*- coding: utf-8 -*-
import sys
from lxml import etree
from datetime import datetime
import unicodedata

def remove_control_characters(s):
  return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

def get_pattern(filename):
  pattern_file = open(filename, 'rU')
  task_a_file = open ("task_a.xml", 'rU')
  task_b_file = open ("task_b.xml", 'rU')
  task_a_text = ""
  task_b_text = ""
  pattern_text = ""
  for line in pattern_file:
    pattern_text += line
  pattern_file.close()
  for line in task_a_file:
    task_a_text += line
  task_a_file.close()
  for line in task_b_file:
    task_b_text += line
  task_b_file.close() 
  pattern = etree.XML(pattern_text)
  task_a = etree.XML(task_a_text)
  task_b = etree.XML(task_b_text)
  return [pattern, task_a, task_b]

def generate_xml(input_filename, output_filename, pattern_filename):
  [pattern, task_a, task_b] = get_pattern(pattern_filename)
  input_file = iter(open(input_filename, 'rU'))
  output_file = open(output_filename, 'w')
  try:
    while True:
      line = input_file.next()
      if "<<<TASK_A>>>" in line:
        print "task_a"
        task = task_a
        line = line.replace('<<<TASK_A>>>','')
        line = line.strip()
        task[1][0].text = remove_control_characters(line.decode('utf-8'))
        for i in range(4):
          ans = input_file.next()
          ans = ans.strip()
          if '<<<ANS_T>>>' in ans:
            print "in true"
            ans = ans.replace('<<<ANS_T>>>','')
            task[2][i].set("CorrectAnswer", "True")
          if '<<<ANS_F>>>' in ans:
            print "in false"
            ans = ans.replace('<<<ANS_F>>>','')
            task[2][i].set("CorrectAnswer", "False")
          task[2][i][0].text = remove_control_characters(ans.decode('utf-8'))
        pattern[3][0][1].append(etree.XML(etree.tostring(task, pretty_print=True)))
      if "<<<TASK_B>>>" in line:
        print "task_b"
        task = task_b
        line = line.replace('<<<TASK_B>>>','')
        line = line.strip()
        task[1][0].text = remove_control_characters(line.decode('utf-8'))
        ans = input_file.next()
        ans = ans.replace('<<<ANS>>>','')
        task[2][0].text = remove_control_characters(ans.decode('utf-8'))
        pattern[3][1][1].append(etree.XML(etree.tostring(task, pretty_print=True)))
  except(StopIteration):
    output_file.write(etree.tostring(pattern, method='xml', pretty_print=True, encoding="utf-8", xml_declaration=True))
    input_file.close()
    output_file.close()

def main():
  if len(sys.argv) != 3:
    print 'usage: ./import_mytest.py input_filename pattern_filename' 
    sys.exit(1)

  input_filename = sys.argv[1]
  pattern_filename = sys.argv[2]
  output_filename = sys.argv[1].replace('.txt', '') + "_out.xml"
  f = open(output_filename, 'w')
  f.close()
  generate_xml(input_filename, output_filename, pattern_filename)
  pass

if __name__ == '__main__':
  main()