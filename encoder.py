inptxt = input("Enter the text")
inptxt = inptxt.lower()
leng = len(inptxt)

encdict = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5",
    "f": "6",
    "g": "7",
    "h": "8",
    "i": "9",
    "j": "10",
    "k": "11",
    "l": "12",
    "m": "13",
    "n": "14",
    "o": "15",
    "p": "16",
    "q": "17",  
    "r": "18",
    "s": "19",
    "t": "20",
    "u": "21",
    "v": "22",
    "w": "23",
    "x": "24",
    "y": "25",
    "z": "26",
    " ": "|",
    ".":"/",
    ",": "*",
    "0": "S",
    "1": "T",
    "2": "J",
    "3": "O",
    "4": "P",
    "5": "G",
    "6": "V",
    "7": "M",
    "8": "L",
    "9": "B",
}
for i in range(0,leng):
    char = inptxt[i]
    print(encdict[char], end=" ")