#!/bin/bash
for i in {1..1}
do
    python3 main.py Canada r Canada\ Optimal\ Run $i\ Canada\ Optimal\ Run.csv
done
    
osascript -e 'tell app "System Events" to display dialog "Done"'

echo "done"