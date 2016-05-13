import fileinput

# Getting input from the file 'inp.txt'
f = fileinput.input("inp.txt")

# Reading the first input line i.e. total # of test cases
T = int(f.readline())

# Will put the output of 'print' statement directly into 'out.txt'
sys.stdout = open("out.txt", "w")

# Running total test cases
for t in range(T):

  # Striping any extra space from the sides of input and adding an extra happy side '+'
  s = f.readline().strip() + '+'
  print('Case #%d: %d' % (t + 1, s.count('-+') + s.count('+-')))
