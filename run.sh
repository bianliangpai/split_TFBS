echo "command:"
echo "                            /path/to/source_file   prefix  titleline_num"
echo "    python3.7 split_TFBS.py Zmays_TFBS_clover.txt  TF      100"

python3.7 split_TFBS.py Zmays_TFBS_clover.txt TF 100

echo ""
echo "output:"
echo "    ./TF_name.txt"
echo "    ./out/TF_*.txt"