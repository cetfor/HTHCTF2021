echo "[Web challenges]"
ps -fp $(pgrep -u web1) | awk 'FNR == 2 {print}'

echo ""
echo "[Crypto challenges]"
ps -fp $(pgrep -u crypto1) | awk 'FNR == 2 {print}'
ps -fp $(pgrep -u crypto2) | awk 'FNR == 2 {print}'
ps -fp $(pgrep -u crypto3) | awk 'FNR == 2 {print}'
ps -fp $(pgrep -u crypto4) | awk 'FNR == 2 {print}'
ps -fp $(pgrep -u crypto5) | awk 'FNR == 2 {print}'

echo ""
echo "[RE challenges]"
ps -fp $(pgrep -u re1) | awk 'FNR == 2 {print}'
ps -fp $(pgrep -u re2) | awk 'FNR == 2 {print}'
ps -fp $(pgrep -u re3) | awk 'FNR == 2 {print}'
ps -fp $(pgrep -u re4) | awk 'FNR == 2 {print}'
ps -fp $(pgrep -u re5) | awk 'FNR == 2 {print}'

echo ""
echo "[Pwn challenges]"
ps -fp $(pgrep -u pwn1) | awk 'FNR == 2 {print}'
ps -fp $(pgrep -u pwn2) | awk 'FNR == 2 {print}'
ps -fp $(pgrep -u pwn3) | awk 'FNR == 2 {print}'
