insta_post = (10842, "tech_creator", 1250, ["#python", "#coding", "#dev"], True)

print("Instagram Post Tuple:", insta_post)
print("\nElement Data Types:")

for element in insta_post:
    print(f"{element!r} -> {type(element).__name__}")