# Tenda-4G03-Reconnect
A shitty way to reconnect your 4G03 modem using python and selenium.
# Dependency

here's how to install the depenecy in raspberry pi os
```bash
sudo apt install chromium-chromedriver
pip install selenium
```
for other device install the chrome driver whatever you want just dont forget to change the chromedriver directory in the script. and install the selenium same way as the example for raspberry pi os.

# How to use
`./connect.py --ip 192.168.11.1`
sometime it broke so add `timeout` command at the front so when it broke it wont lock you out. sorry.
example:
`timeout 2m ./connect.py --ip 192.168.11.1`
