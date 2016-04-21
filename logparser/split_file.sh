#!/bin/bash

# Configuration stuff

fspec=$1
num_files=$2

# Work out lines per file.

total_lines=$(wc -l <${fspec})
((lines_per_file = (total_lines + num_files - 1) / num_files))

# Split the actual file, maintaining lines.

split --lines=${lines_per_file} --numeric-suffixes=1 ${fspec} ${fspec}.

for FILE in `ls ${fspec}.*`; do mv $FILE `echo $FILE | sed -e 's:\.0:\.:'`; done
# Debug information

#echo "Total lines     = ${total_lines}"
#echo "Lines  per file = ${lines_per_file}"    
#wc -l ${fspec}.*
echo "${lines_per_file}"