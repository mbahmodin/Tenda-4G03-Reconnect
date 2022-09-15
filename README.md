# Tenda-4G03-Reconnect
A shitty way to reconnect your 4G03 modem
# Dependency
```bash
sudo apt install chromium-chromedriver
pip install selenium
```
# How to use
`./connect.py --ip 192.168.11.1`
sometime it broke so add `timeout` command at the front so when it broke it wont lock you out. sorry.
example:
`timeout 2m ./connect.py --ip 192.168.11.1`
