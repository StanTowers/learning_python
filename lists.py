
lucky_numbers = [4, 6, 2, 99, 17, 56, 9]
friends = ["Kai", "Seb", "Seb", "Marc"]
friends.extend(lucky_numbers)
friends.insert(1, "Bongo")
friends.remove("Marc")
friends.append("Creed")
friends.pop()
print(friends)
print(friends.count("Seb"))
print(friends.index("Seb"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)