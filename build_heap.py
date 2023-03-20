# python3


    
def heapify(i,data):
    parent = int((i/2)-1) 
    if i == 3:
        parent = 1
    
    if parent == -1:
        return
    # print("parent",parent, "i=",i)
    if data[i] < data[parent]:
        #swaping
        print(parent,i)
        data[i], data[parent] = data[parent], data[i]
        heapify(parent,data)

    else:
        return

def main():
    inp = input()
    if inp == "I":
        n = int(input())
        data = list(map(int, input().split()))
    elif inp == "F":
        print("F")
    

    # n = 5
    # data = [5,4,3,2,1]
    # data = [1,2,3,4,5]
    assert len(data) == n

    leaves = []
    num = n//2
    for i in range(num,n):
        leaves.append(i)
    
    print("leaves==",leaves)
    print("\n")

    for k in leaves[::-1]:
        heapify(k, data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print("asd")



if __name__ == "__main__":
    main()

