with open("D:\python\\connection.txt","r",encoding="utf-8") as f:
    data = f.read()
    with open("D:\python\\connection.txt", "w", encoding="utf-8") as file:
        file.write(data)