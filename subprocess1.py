import subprocess

result = subprocess.run(["python", "ranges.py"])
print("args: ", result.args)
print("returncode: ", result.returncode)
print("stderr: ", result.stderr)
print("stdout: ", result.stdout)

subprocess.run(["node",  "otherjs.js"])