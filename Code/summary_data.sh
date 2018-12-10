#!/bin/bash
for i in {1..30}
do
    python3 main.py WesternSahara s 1000GenStag\ Tour\(2\)\ SCX5SqrtToPMX\(1.0\)\ Inversion\(0.6\).csv
done

osascript -e 'tell app "System Events" to display dialog "Done"'

echo "done"