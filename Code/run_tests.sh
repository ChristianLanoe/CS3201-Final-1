#!/bin/bash
for i in {1..30}
do
    python3 main.py WesternSahara s 1000\ SCX100-PMX\(0.9\)\ Inversion\(0.2\).csv
done
# python3 main.py Uruguay s SCX100-PMX\(0.9\)\ Inversion\(0.2\).csv

# python3 main.py WesternSahara r 0\ SCX100-\>\PMX\(0.9\)\ Inversion\(0.2\).csv

osascript -e 'tell app "System Events" to display dialog "Done"'

echo "done"