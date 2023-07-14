# CMDLine-DDoSer
A DDoSer that can be ran from the CMDLine, by adding arguments. This DDoSer uses the UDP-Flood Method for DDoSing.

## Syntax
ddos.py --ddos ip_address \[--port port_num]

ddos.exe --ddos ip_address \[--port port_num]

## requirements
pip: `pip install argparse`

also uses: socket, random and 500-900MBpS (depends on your network speed)

but those are already built-in.

## EXE or PY?

They both give no printed output.

The EXE was created with --noconsole and --onefile. so for the exe you see no window, great for a no-access botnet.

The py is just a normal python script file.

The EXE can be used in malware, if you have a life-long specific ip target, you can add this exe in your script. make it download the exe from this github repository, then run it with --ddos ip and --port num if needed.
