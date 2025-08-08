i =0
while i <= 100:
    
    record = {"id": f"{i}", 
        "name": f"record{i}",
        "score": f"{i}"
    }
    i +=1
    print(record)

    if 70<= record <= 100:
        print("your record is A")
    
