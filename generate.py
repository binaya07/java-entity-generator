import re

# Takes class name and columns as input
class_name = input('Enter class name : ').strip().capitalize()
columns = input(
    'Enter columns as comma separated values (eg "column1", "column2") : ').split(',')

# Create Java file
file_name = class_name + '.java'
file = open(file_name, 'w+')

columnNameRegex = re.compile(r'"(.*)"')

# Create Java entity
java_entity = 'public class ' + class_name + ' {\n\n'
for column in columns:
    column = columnNameRegex.search(column).group(1).strip()
    if column != '':
        java_entity += '@Column(name="' + column + '")\n'
        variable_name = column.replace('_', '').replace(' ', '').lower()
        java_entity += 'private String ' + variable_name + ';\n\n'

java_entity += '}'

# Write to file
file.write(java_entity)
file.close()
