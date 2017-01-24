# -*- coding: utf-8 -*-
import sys
from lxml import etree
from datetime import datetime
import unicodedata
task_a = etree.XML("<Task Type=\"TYPE_TASK_CHOICE_SINGLE\" Score=\"1\"><Title/><QuestionText><PlainText></PlainText><FormattedText>=</FormattedText></QuestionText><Options><IsAllowRandom>true</IsAllowRandom><IsCompulsory>false</IsCompulsory><IsOnlyForEduMode>false</IsOnlyForEduMode><IsDenyPartially>false</IsDenyPartially></Options><Variants><VariantText CorrectAnswer=\"False\"><PlainText></PlainText><FormattedText></FormattedText></VariantText><VariantText CorrectAnswer=\"False\"><PlainText></PlainText><FormattedText></FormattedText></VariantText><VariantText CorrectAnswer=\"False\"><PlainText></PlainText><FormattedText></FormattedText></VariantText><VariantText CorrectAnswer=\"False\"><PlainText></PlainText><FormattedText></FormattedText></VariantText></Variants></Task>")

task_b = etree.XML("<Task Type=\"TYPE_TASK_ENTER_NUM\" Score=\"1\"><Title/><QuestionText><PlainText></PlainText><FormattedText>=</FormattedText></QuestionText><Options><IsAllowRandom>true</IsAllowRandom><IsCompulsory>false</IsCompulsory><IsOnlyForEduMode>false</IsOnlyForEduMode><IsDenyPartially>false</IsDenyPartially></Options><InputNum><Value></Value></InputNum></Task>")

def remove_control_characters(s):
  return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

def get_pattern(filename):
  pattern_file = open(filename, 'rU')
  pattern_text = ""
  for line in pattern_file:
    pattern_text += line
  pattern = etree.XML(pattern_text)
  return pattern

def generate_xml(input_filename, output_filename, pattern_filename):
  pattern = get_pattern(pattern_filename)
  input_file = iter(open(input_filename, 'rU'))
  output_file = open(output_filename, 'w')
  try:
    while True:
      line = input_file.next()
      print "start loop"
      if "<<<TASK_A>>>" in line:
        print "task_a"
        task = task_a
        line = line.replace('<<<TASK_A>>>','')
        task[1][0].text = remove_control_characters(line.decode('utf-8'))
        for i in range(4):
          ans = input_file.next()
          ans = ans.replace('<<<ANS>>>','')
          task[3][i][0].text = remove_control_characters(ans.decode('utf-8'))
        pattern[3][0][1].append(etree.XML(etree.tostring(task, pretty_print=True)))
      if "<<<TASK_B>>>" in line:
        print "task_b"
        task = task_b
        line = line.replace('<<<TASK_B>>>','')
        task[1][0].text = remove_control_characters(line.decode('utf-8'))
        ans = input_file.next()
        ans = ans.replace('<<<ANS>>>','')
        task[3][0].text = remove_control_characters(ans.decode('utf-8'))
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
  output_filename = sys.argv[1].replace('.', '_') + "_out.xml"
  f = open(output_filename, 'w')
  f.close()
  generate_xml(input_filename, output_filename, pattern_filename)
  pass

if __name__ == '__main__':
  main()