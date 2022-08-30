import subprocess

result = subprocess.Popen('git log --oneline',
                          shell=True,
                          stdout=subprocess.PIPE)

lines = result.stdout.readlines()


for line in lines:
    print(line.decode('utf-8'))


print(len(lines))
