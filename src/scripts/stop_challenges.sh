echo "Stopping web challenges"
sudo pkill -U web1

echo "Stopping crypto challenges"
sudo pkill -U crypto1
sudo pkill -U crypto2
sudo pkill -U crypto3
sudo pkill -U crypto4
sudo pkill -U crypto5

echo "Stopping re challenges"
sudo pkill -U re1
sudo pkill -U re2
sudo pkill -U re3
sudo pkill -U re4
sudo pkill -U re5

echo "Stopping pwn challenges"
sudo pkill -U pwn1
sudo pkill -U pwn2
sudo pkill -U pwn3
