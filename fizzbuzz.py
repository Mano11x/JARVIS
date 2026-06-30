# frout = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
# for frout in frout:
#     print(frout)

# for i in range(5):
#     print(i * 10)

# count = 1
# while count < 5:
#     print("count:", count)
#     count+=1

# for i in range(1, 10):
#     if i == 5:
#         continue
#     if i == 10:
#         break
#     print(i)
        
# number = int(input("Enter a number: "))

# if number % 2 ==0:
#     print("even")
# else:
#     print("odd")

for i in range(1, 10):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)