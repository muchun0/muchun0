# This Python file uses the following encoding: utf-8
import requests
import json

url = 'https://welm.weixin.qq.com/v1/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'cchi48mv9mc753cgt1lg'
}
stop=",，.。"

def AutoReply(prompt=None,model="xl",max_tokens=16,temperature=0.0,top_p=0.0,top_k=10,n=1,echo=False,stop=None):
    '''
    :param prompt: string 可选，默认值空字符串，给模型的提示
    :param model: string 必选，要使用的模型名称，当前支持的模型名称有medium、 large 和 xl
    :param max_tokens: max_tokens: integer 可选，最多生成的token个数，默认值 16
    :param temperature: number 可选 默认值 0.85，表示使用的sampling temperature，更高的temperature意味着模型具备更多的可能性。
        # 对于更有创造性的应用，可以尝试0.85以上，而对于有明确答案的应用，可以尝试0（argmax采样）。 建议改变这个值或top_p，但不要同时改变。
    :param top_p: number 可选 默认值 0.95，来源于nucleus sampling，采用的是累计概率的方式。
        # 即从累计概率超过某一个阈值p的词汇中进行采样，所以0.1意味着只考虑由前10%累计概率组成的词汇。 建议改变这个值或temperature，但不要同时改变。
    :param top_k: integer 可选 默认值50，从概率分布中依据概率最大选择k个单词，建议不要过小导致模型能选择的词汇少。
    :param n: integer 可选 默认值 1 返回的序列的个数
    :param echo: boolean 可选 默认值false，是否返回prompt
    :param stop: string 可选 默认值 null，停止符号
    :return: json type response
    ''''''
    '''
    body = {
        'prompt':prompt,
        'model':model,
        'max_tokens':max_tokens,
        'temperature':temperature,
        'top_p':top_p,
        'top_k':top_k,
        'n':n,
        'echo':echo,
        'stop':stop,
    }
    body = json.dumps(body)
    try:
        res = requests.post(url=url, headers=headers, json=body).json()['choices'][0]['text']
    except:
        res = "请求出错啦，要排查下"

    return res
#

def writeDialogue(text):
    with open('D:\python\WechatAutoReply\dialogueContent.txt','a',encoding='utf-8') as f:
        f.write(text+'\n')
def readDialogue():
    with open('D:\python\WechatAutoReply\dialogueContent.txt','r',encoding='utf-8') as f:
        return f.read()
if __name__ == '__main__':
    res = AutoReply('锦瑟无端五十弦')
    print(res)

