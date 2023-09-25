
first_multiple_input = input().rstrip().split()
Rows= int(first_multiple_input[0])
Columns = int(first_multiple_input[1])
# Rows = int(input("Give the number of rows:"))
# Columns = int(input("Give the number of columns:"))

example_matrix = []
print("Please give the entries row-wise:")


for _ in range(Rows):
    r = []
    for __ in range(Columns):
        r.append((input()))
    example_matrix.append(r)
#T s i h % x i_# s M_$ a_# t % i r !

for _ in range(Rows):
    for __ in range(Columns):
        print(example_matrix[_][__], end=" ")
    print()
# res = ''.join(ele for sub in example_matrix for ele in sub)
res1=[]
for k in range(0,Columns):

    res1 += [sub[k] for sub in example_matrix]
print(res1)

x=""
for i in res1:
    x+=i
print(x)

string = x
string_copy = string
symbols = "!,@,#,$,%,&"
for char in symbols:
    string_copy = string_copy.replace(char, " ")
print(string_copy)