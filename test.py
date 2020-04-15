from LRU_cache import lru

x1 = lru(7)

assert x1.put(1,"Manjari") == "Entered"
assert x1.put(2,"Murala") == "Entered"
assert x1.put(3,"Madhu") == "Entered"
assert x1.get(1) == "Manjari"
assert x1.get(1) == "Manjari"
assert x1.get(3) == "Madhu"
assert x1.put(4,"Malathi") == "Entered"
assert x1.put(5,"Madhuri") == "Entered"
assert x1.put(6,"Teja") == "Entered"
assert x1.put(7,"V") == "Entered"
assert x1.get_cache() == {1: 'Manjari', 2: 'Murala', 3: 'Madhu', 4: 'Malathi', 5: 'Madhuri', 6: 'Teja', 7: 'V'}
print ("all test cases passed")