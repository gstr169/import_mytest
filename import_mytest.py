# -*- coding: utf-8 -*-
import sys
from datetime import datetime

def generate_xml(input_filename, output_filename):
  input_file = open(input_file, 'rU')
  output_file = open(output_file, 'w')
  output_file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
  output_file.write("<MyTestX>\n")
  output_file.write("    <Version>11.0.0.29</Version>\n")
  dt = datetime.now()
  output_file.write("    <SaveDate>" + dt.isoformat() + "</SaveDate>\n")
  output_file.write("    <TestOptions>\n")
  output_file.write("        <TestCreate>" + dt.isoformat() + "</TestCreate>\n")
  output_file.write("        <TestLastSave>" + dt.isoformat() + "</TestLastSave>\n")
  output_file.write("        <TestUID/>\n")  
  output_file.write("        <Title></Title>\n")
  output_file.write("        <Author/>\n")  
  output_file.write("        <AuthorEmail/>\n")  
  output_file.write("        <TestUID></>\n")  
  output_file.write("        <TestUID/>\n")  
  output_file.write("        <TestUID/>\n")  



  for line in input_file
    if line == ""
  input_file.close()
  output_file.close()
  pass

def main():
  if len(sys.argv) != 2:
    print 'usage: ./import_mytest.py input_filename' 
    sys.exit(1)

  import_file = sys.argv[1]
  output_file = sys.argv[1].replace('.', '_') + "_out.xml"
  f = open(output_file, 'w')
  f.close()
  generate_xml(input_file, output_file)
  pass

if __name__ == '__main__':
  main()