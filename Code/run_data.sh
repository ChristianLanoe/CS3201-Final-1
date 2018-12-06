#!/bin/bash
for i in {1..30}
do
    python3 main.py WesternSahara r $i SCX100-PMX\(0.9\)\ Inversion\(0.2\).csv
done

osascript -e 'tell app "System Events" to display dialog "Done"'

echo "done"