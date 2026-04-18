import random
def get_random(num=3):
    try:
        array=[]
        i=0
        while (i<num):
            x=random.randint(1,100)
            array.append(x)
            if  array.count(x)>1:
                array.pop()
                break
            i+=1
                
        return array
    except Exception as e:
        print("Error",e)
print(get_random(7))

            