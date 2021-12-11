# Web challenges
#sudo su - web1 -c "cd /home/web1/ && flask run --host=0.0.0.0 --port=7801"
sudo su - web1 -c "nohup gunicorn --bind 0.0.0.0:7801 --chdir /home/web1/ run:app </dev/null >/dev/null 2>&1 &"

# Crypto challenges
sudo su - crypto1 -c "nohup socat TCP4-LISTEN:7806,tcpwrap=script,reuseaddr,fork EXEC:'python3 -u /home/crypto1/crypto1.py' </dev/null >/dev/null 2>&1 &"
sudo su - crypto2 -c "nohup socat TCP4-LISTEN:7807,tcpwrap=script,reuseaddr,fork EXEC:'python3 -u /home/crypto2/crypto2.py' </dev/null >/dev/null 2>&1 &"
sudo su - crypto3 -c "nohup socat TCP4-LISTEN:7808,tcpwrap=script,reuseaddr,fork EXEC:'python3 -u /home/crypto3/crypto3.py' </dev/null >/dev/null 2>&1 &"
sudo su - crypto4 -c "nohup socat TCP4-LISTEN:7809,tcpwrap=script,reuseaddr,fork EXEC:'python3 -u /home/crypto4/crypto4.py' </dev/null >/dev/null 2>&1 &"
sudo su - crypto5 -c "nohup socat TCP4-LISTEN:7810,tcpwrap=script,reuseaddr,fork EXEC:'python3 -u /home/crypto5/crypto5.py' </dev/null >/dev/null 2>&1 &"

# Reverse engineering challenges
sudo su - re1 -c "nohup socat TCP4-LISTEN:7811,tcpwrap=script,reuseaddr,fork EXEC:'/home/re1/re1',pty,ctty </dev/null >/dev/null 2>&1 &"
sudo su - re2 -c "nohup socat TCP4-LISTEN:7812,tcpwrap=script,reuseaddr,fork EXEC:'/home/re2/re2',pty,ctty </dev/null >/dev/null 2>&1 &"
sudo su - re3 -c "nohup socat TCP4-LISTEN:7813,tcpwrap=script,reuseaddr,fork EXEC:'/home/re3/re3',pty,ctty </dev/null >/dev/null 2>&1 &"
sudo su - re4 -c "nohup socat TCP4-LISTEN:7814,tcpwrap=script,reuseaddr,fork EXEC:'python3 -u /home/re4/re4.py' </dev/null >/dev/null 2>&1 &"
sudo su - re5 -c "nohup socat TCP4-LISTEN:7815,tcpwrap=script,reuseaddr,fork EXEC:'/home/re5/re5',pty,ctty </dev/null >/dev/null 2>&1 &"

# Pwnable challenges
sudo su - pwn1 -c "nohup socat TCP4-LISTEN:7821,tcpwrap=script,reuseaddr,fork EXEC:'/home/pwn1/pwn1',pty,ctty </dev/null >/dev/null 2>&1 &"
sudo su - pwn2 -c "nohup socat TCP4-LISTEN:7822,tcpwrap=script,reuseaddr,fork EXEC:'/home/pwn2/pwn2',pty,ctty </dev/null >/dev/null 2>&1 &"
sudo su - pwn3 -c "nohup socat TCP4-LISTEN:7823,tcpwrap=script,reuseaddr,fork EXEC:'/home/pwn3/pwn3',pty,ctty </dev/null >/dev/null 2>&1 &"
