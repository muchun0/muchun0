from getResponse import writeDialogue
from getResponse import AutoReply
from getResponse import readDialogue

def main():
    while True:
        text = '对方：' + input("输入对方话语：\n")
        writeDialogue(text)
        ReplyText = '我：'+AutoReply(prompt= readDialogue())
        print(ReplyText)
        writeDialogue(ReplyText)

if __name__ == '__main__':
    main()