import os, filecmp

def search(put, box_file):
    for i in os.listdir(put):
        if os.path.isfile(f'{put}/{i}'):
            box_file.append(f'{put}/{i}')
        if os.path.isdir(f'{put}/{i}'):
            search(f'{put}/{i}', box_file)
    return box_file
box_file_put1 =  search('/home/gordey/Documents/python/search_file-sf-/back1', [])
box_file_put2 = search('/home/gordey/Documents/python/search_file-sf-/back2', [])
#print(f'{box_file_put1}\n{box_file_put2}')
def func(b1,b2):
    for i in range(len(b1)):
        for a in range(-1,len(b2)-1):

            if filecmp.cmp(b1[i], b2[a], shallow=True):
                print(b1.pop(i))
                print(b2.pop(a))


func(box_file_put1,box_file_put2)
print(box_file_put1, box_file_put2)
lis = [1,2,3,4,5]
for i in range(-1, len(lis)-1):
    print(lis[i])
