
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json


echo "Timestamps:"
./jq-windows-amd64.exe -r '.[].receiptTime' aviation.json | head -n 6
echo ""


echo "Calculating average temperature..."
temps=$(./jq-windows-amd64.exe -r '.[].temp' aviation.json)
sum=0
count=0

for temp in $temps; do
    if [[ "$temp" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
        sum=$(awk -v s="$sum" -v t="$temp" 'BEGIN {print s + t}')
        ((count++))
    fi
done

if [[ $count -gt 0 ]]; then
    avg=$(awk -v s="$sum" -v c="$count" 'BEGIN {printf "%.1f", s / c}')
    echo "Average Temperature: $avg°C"
else
    echo "Average Temperature: N/A"
fi


echo "Checking cloud cover..."
clouds=$(./jq-windows-amd64.exe -r '.[].clouds' aviation.json)
cloudy_count=0
total=0

for cloud in $clouds; do
    ((total++))
    if [[ "$cloud" != "CLR" ]]; then
        ((cloudy_count++))
    fi
done

if [[ $cloudy_count -gt $((total / 2)) ]]; then
    echo "Mostly Cloudy: true"
else
    echo "Mostly Cloudy: false"
fi
