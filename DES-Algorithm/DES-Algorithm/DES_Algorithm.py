class des():
    def __init__(self):
        self.text = list()
        self.password = list()

        self.IP = [58, 50, 42, 34, 26, 18, 10, 2,
                  60, 52, 44, 36, 28, 20, 12, 4,
                  62, 54, 46, 38, 30, 22, 14, 6,
                  64, 56, 48, 40, 32, 24, 16, 8,
                  57, 49, 41, 33, 25, 17, 9, 1,
                  59, 51, 43, 35, 27, 19, 11, 3,
                  61, 53, 45, 37, 29, 21, 13, 5,
                  63, 55, 47, 39, 31, 23, 15, 7]

        self.E =[32, 1, 2, 3, 4, 5, 
                 4, 5, 6, 7, 8, 9,
                 8, 9, 10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32, 1]

        self.S_BOX =[
                    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
                    ],

                    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
                    ],

                    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
                    ],

                    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
                    ],  

                    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
                    ], 

                    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
                    ], 

                    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
                    ],
   
                    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
                     ]
                    ]
        self.G = [57,  49,  41,  33,  25,  17,  9,
                1,  58,  50,  42,  34,  26,  18,
                10,  2,  59,  51,  43,  35,  27,
                19,  11,  3,  60,  52,  44,  36,
                63,  55,  47,  39,  31,  23,  15,
                7,  62,  54,  46,  38,  30,  22,
                14,  6,  61,  53,  45,  37,  29,
                21,  13,  5,  28,  20,  12,  4]

        self.P = [16, 7, 20, 21, 29, 12, 28, 17,
                 1, 15, 23, 26, 5, 18, 31, 10,
                 2, 8, 24, 14, 32, 27, 3, 9,
                 19, 13, 30, 6, 22, 11, 4, 25]

        self.SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

        self.H = [14, 17, 11, 24, 1, 5, 3, 28,
                15, 6, 21, 10, 23, 19, 12, 4,
                26, 8, 16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55, 30, 40,
                51, 45, 33, 48, 44, 49, 39, 56,
                34, 53, 46, 42, 50, 36, 29, 32]

        self.IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41, 9, 49, 17, 57, 25]

    #Permut the given block using the given table
    #Перемешивает блок в соотвествии с таблицей
    def permut(self, block, table):
        return [block[x-1] for x in table]

    """Converting a string into a list of bit"""
    #Преобразует строку в битовую последовательность
    def string_to_byte(self, text_original):
        string = [bin(symb)[2:] if isinstance (symb,int) else bin(ord(symb))[2:] for symb in text_original]
        bitList = list()
        for byte in string:
            byte = str(byte).zfill(8)
            if len(byte) < 9:
                for bit in byte:
                    if bit == 'b': 
                        bit = '0'
                    bitList.append(int(bit))
            else:
                for bit in byte:
                    if bit != 'b': 
                        bitList.append(int(bit))                    
        return bitList

    """Converting a list of bit into a string"""
    #Преобразует битовую последовательность в строку
    def byte_to_string(self,list_of_byte):
        text_encrypt = ''
        for i in range(0, len(list_of_byte), 8):
            lof = list_of_byte[i:i+8]
            text_encrypt += chr(int(''.join([str(lof[j]) for j in range(len(lof))]),2))
        return text_encrypt

    def encrypt(self,text,key):
        text_end = list()
        btlist = self.string_to_byte(text) #преобразует текст в битовую последовательность
        while len(btlist)%64 != 0: #расширяет битовую последовательность 0, если длина не кратна 64
            btlist.append(0)
        bit_block = []
        for btBlock in self.seperation_list(btlist, 64):#разбивает битовую последовательность на 64 битовые блоки
            bit_block.append(self.permut(btBlock, self.IP))
        self.password = self.string_to_byte(key[:64])#преобразует пароль в 56 битовую последовательность

        for block in bit_block:
            left_list, right_list = list(), list()
            left,right = self.seperation_list(block,32)
            left_list.append(left)
            right_list.append(right)
            for i in range(16):
                left_list.append(right_list[i])            
                right_list.append(self.xor(left_list[i], self.F_function(right_list[i], self.generate_key(self.password,i))))                
            text_end.extend(self.permut(self.combine_blocks([left_list[-1],right_list[-1]]), self.IP_1))
        return self.byte_to_string(text_end)

    def decrypt(self,cipher_text,key):
        text_end = list()
        btlist = self.string_to_byte(cipher_text) #преобразует текст в битовую последовательность
        while len(btlist)%64 != 0: #расширяет битовую последовательность 0, если длина не кратна 64
            btlist.append(0)
        bit_block = []
        for btBlock in self.seperation_list(btlist, 64):#разбивает битовую последовательность на 64 битовые блоки
            bit_block.append(self.permut(btBlock, self.IP))
        self.password = self.string_to_byte(key)[:64]#преобразует пароль в 64 битовую последовательность

        for block in bit_block:
            left_list, right_list = list(), list()
            left,right = self.seperation_list(block,32)
            left_list.append(left)
            right_list.append(right)
            for i in range(16):
                left_list.append(self.xor(right_list[i],self.F_function(left_list[i], self.generate_key(self.password,15 - i))))
                right_list.append(left_list[i])           
            text_end.extend(self.permut(self.combine_blocks([left_list[-1],right_list[-1]]), self.IP_1))
            left_list.clear()
            right_list.clear()
        return self.byte_to_string(text_end)

    #Разделяет лист на блок листов нужной длины
    def seperation_list(self,lst, step):
        return [lst[x:x+step] for x in range(0,len(lst),step)]

    #Объединяет блоки в листе
    def combine_blocks(self, block):
        cb = []
        for b in block:
            if len(b) > 1:
                for x in b:
                    cb.append(x)
            else:
                cb.append(x)
        return cb

    """возвращает лист [B[0]B[1]..B[8]]"""
    def F_function(self,bit,key):
        new_bit = self.permut(bit,self.E)
        new_key = key 
        B = self.seperation_list([new_bit[x] ^ new_key[x] for x in range(len(new_bit))],6)
        S = list()
        #""" операция хор между строкой и ключой и разбиение на список по 6 бит"""
        result = list()
        for i in range(len(B)):
            ############
            b = B[i]
            nb_row = int((lambda x,y: str(x) + str(y))(b[0],b[-1]),2)
            nb_column = int(''.join([str(s) for s in b[1:-1]]),2)
            s = self.S_BOX[i]
            s_nb_row = s[nb_row]
            S.append(self.int_to_bit(s_nb_row[nb_column],4))
        return self.permut(self.combine_blocks(S), self.P)
        
    def generate_key(self, key, iteration):
        new_key = self.permut(key,self.G)
        c,d = self.seperation_list(new_key,28)
        c,d = self.shift(c,d,self.SHIFT[iteration])
        return self.permut(c + d, self.H)

    #сдвиг листа на определенное значение
    def shift(self, c, d, n): 
        return c[n:] + c[:n], d[n:] + d[:n]

    def xor(self,list_one, list_two):
        s = []
        if len(list_one) == len(list_two):
            return [x ^ y for x,y in zip(list_one, list_two)]
        else :
            print("Error: ")

    def int_to_bit(self,number, length):
        string = bin(number)[2:]
        string = str(string).zfill(length)
        bitList = list()
        for byte in string:
            if byte == 'b': 
                byte = '0'
            bitList.append(int(byte))
        return bitList

class cbc(des):
    pass

if __name__ == '__main__':
    key = "secret_k"
    textD= "hello world"
    d = des()
    r = d.encrypt(textD,key)
    k = d.decrypt(r,key)
    print("Original text: ",textD)
    print("Cipher text: ",r)
    print("Decrypt text: ",k)
