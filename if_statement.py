
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a not a male but are short")
else:
    print("You are not a male and not tall")