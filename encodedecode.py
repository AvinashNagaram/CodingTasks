#python> this is the medium level of the problem
#["my","name","is","sai"] -> "2#my3#name2#is3#sai"  encode
#"2#my3#name2#is3#sai" -> ["my","name","is","sai"]  decode

class encodedecode:
    def encode(self,l):
        res = ""
        for i in l:
            res += str(len(i)) + "#" + i
        return res

    def decode(self,s):
        res = []
        i = 0 

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length =  int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j + length + 1
        return res


obj = encodedecode()
encoded = obj.encode(["my","name","is","sai"])
print(encoded)

decoded = obj.decode(encoded)
print(decoded)