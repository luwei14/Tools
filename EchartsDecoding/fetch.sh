echo "Fetch Data from Echarts..."
wget -q -i jsonurls -P json/
echo "Decoding data..."
node bddecode.js
echo "Complete."
