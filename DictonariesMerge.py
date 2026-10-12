dict1={"a":1,"b":2};
dict2={"c":3,"d":4};
dict1["e"]=5;
dict2["f"]=6;
#1st method;
merged=dict1|dict2;
print(merged);
# Modern Python (3.9+) offers the most concise syntax.  The pipe operator (|) creates a new dictionary by combining key-value pairs, with values from the right-hand dictionary overwriting duplicates.  For in-place modification, the update operator (|=) merges the second dictionary into the first, similar to the traditional update() method but with cleaner syntax. 
#2 nd method
merged1={**dict1,**dict2};
print(merged1);
#3 rd method 
# it does not create a new dictonary it update dict followed by .update() by merging dict1 and dict2
merged2=dict1.update(dict2);
print(merged2);
print(dict1);
# For older versions (3.5–3.8) or specific use cases, other methods are available.  Dictionary unpacking ({**d1, **d2}) is the standard non-destructive method, creating a new dictionary while preserving the original types.  The update() method is the classic approach that modifies the first dictionary in place and returns None.  The dict() constructor can merge dictionaries using unpacking or keyword arguments, though keyword arguments require string keys.  Finally, itertools.chain() chains the items of multiple dictionaries into a single iterator, which can be passed to the dict() constructor to create a new merged dictionary, offering flexibility for merging more than two dictionaries in a single expression. 
