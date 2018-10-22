filename=$1
cat $filename | grep p1p2.332 | awk '{print $6"\t"$7}' > sar.log
