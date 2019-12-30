# f = open('file1.txt','r')
# print(f'cursor position-{f.tell()}')
# print(f.read())
# print(f'cursor position-{f.tell()}')
# f.seek(0)
# print("after seek method")
# print(f'cursor position-{f.tell()}')
# f.close()
# with open('file1.txt','w') as f:
#     f.write("hello!\n my name is zahera fatima.")
with open('file1.txt','r') as rf:
    with open('file2.txt','w') as wf:
        wf.write(rf.read())
    # f.write("\n i am in be of electronic engineering. ")