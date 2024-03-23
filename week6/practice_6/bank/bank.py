import sys

answer = input("Greeting: ").strip() .lower()
if "hello" in answer:
    print("$0")
    sys.exit(0)

elif "h" in answer[0]:
    print("$20")
    sys.exit(0)

else:
    print("$100")
    sys.exit(0)
