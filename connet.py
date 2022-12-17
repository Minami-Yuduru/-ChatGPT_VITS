# 这是一个python文件
# 开发时间：2022/12/14 14:19
# 编写时请注意备注
import sys
sys.path.append('')

import chatgpt_main
import use_main

if __name__ == '__main__':
  all_text = input('最初の設定を入力してください:')
  audio_converse_class = use_main.single_speaker_model()
  while 1 == 1:
    resualt,all_text,audio_text = chatgpt_main.friend_chat(all_text)
    # print(all_text)
    audio_converse_class.generate(audio_text)

    if resualt == 'quit':
      break
