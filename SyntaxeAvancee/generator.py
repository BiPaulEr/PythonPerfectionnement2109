def generator(limit):
    for i in range (0, limit):
        print(f"about to be done {i}")
        yield i
        print(f"done {i}")
        
gen = generator(3)

print(gen)
for i in gen:
    print(i)

def fonction(limit):
    print("je suis execute")
fun = fonction(3)