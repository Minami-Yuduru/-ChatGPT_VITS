import os

import openai
openai.api_key = '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'

def QA():


    '''使用环境变量加API
    openai.api_key = os.getenv("OPENAI_API_KEY")'''
    #直接加api

    start_sequence = "\nA:"
    restart_sequence = "\n\nQ: "
    prompt = input(restart_sequence)
    if prompt == 'quit':
        return prompt
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt= prompt,
  temperature=0,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  #stop=["\n"]  已它为截止输入的标记
    )

    print(start_sequence + response['choices'][0]['text'].strip())
    return prompt

def chat():


  start_sequence = "\nAI:"
  restart_sequence = "\nHuman: "
  prompt = input(restart_sequence)
  if prompt == 'quit':
    return prompt
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.1,
    max_tokens=1500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  print(start_sequence + response['choices'][0]['text'].strip())
  return prompt

#用这个
def friend_chat(all_text,prompt0,call_name = '南ことり'):
  start_sequence = '\n'+str(call_name)+':'
  restart_sequence = "\nYou: "
  all_text = all_text + restart_sequence
  if prompt0 == '':
     prompt0 = input(restart_sequence) #当期prompt
  if prompt0 == 'quit':
     return prompt0
  prompt = all_text + prompt0 + start_sequence


  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["\nYou:"]
  )
  audio_text = response['choices'][0]['text'].strip()
  print(start_sequence + response['choices'][0]['text'].strip())
  all_text = prompt + response['choices'][0]['text'].strip()
  return prompt0,all_text,audio_text

if __name__ == '__main__':
  #设置API不执行
  all_text = input('输入初始设定文本:')
  while 1 == 1:
    resualt,all_text,audio_text = friend_chat(all_text,'')
    # print(all_text)
    if resualt == 'quit':
      break