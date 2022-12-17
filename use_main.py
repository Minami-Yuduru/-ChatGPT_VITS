
#使用VITS生成语音存储到地址

import matplotlib.pyplot as plt
import IPython.display as ipd

import os
import json
import math
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader

import commons
import utils
from data_utils import TextAudioLoader, TextAudioCollate, TextAudioSpeakerLoader, TextAudioSpeakerCollate
from models import SynthesizerTrn
from text.symbols import symbols
from text import text_to_sequence

from scipy.io.wavfile import write


def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm

#todo
class single_speaker_model():
    def __init__(self,path_of_pth = "./模型及配置/kotori/第四次/G_127000.pth",path_of_json = "./模型及配置/kotori/kotory.json"):#需要传入模型路径和配置文件路径
        self.hps = utils.get_hparams_from_file(path_of_json)
        self.net_g = SynthesizerTrn(
            len(symbols),
            self.hps.data.filter_length // 2 + 1,
            self.hps.train.segment_size // self.hps.data.hop_length,
            **self.hps.model).cpu()
        self._ = self.net_g.eval()

        self._ = utils.load_checkpoint(path_of_pth, self.net_g, None)

    def generate(self,text = 'おはようございます。'):
        stn_tst = get_text(text, self.hps)
        with torch.no_grad():
            x_tst = stn_tst.unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)])
            audio = self.net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=1)[0][
                0, 0].data.cpu().float().numpy()
        #ipd.display(ipd.Audio(audio, rate=self.hps.data.sampling_rate, normalize=False))
        print(ipd.Audio(audio, rate=self.hps.data.sampling_rate, normalize=False))
        audio = ipd.Audio(audio, rate=self.hps.data.sampling_rate, normalize=False)
        # 首先，需要获取音频数据的二进制数据
        audio_data = audio.data

        # 然后，使用open和write函数将音频数据写入文件
        with open('./audio/audio.wav', 'wb') as f:
            f.write(audio_data)

class multy_speaker_model():
    def __init__(self,path_of_pth = "./模型及配置/9人/G_833000.pth" , path_of_json = "./模型及配置/9人/config.json"):
        self.hps = utils.get_hparams_from_file(path_of_json)

        self.net_g = SynthesizerTrn(
            len(symbols),
            self.hps.data.filter_length // 2 + 1,
            self.hps.train.segment_size // self.hps.data.hop_length,
            n_speakers=self.hps.data.n_speakers,
            **self.hps.model).cuda()
        self._ = self.net_g.eval()

        self._ = utils.load_checkpoint(path_of_pth, self.net_g, None)

    def generate(self,text,speaker_index = int(1)): #speaker_index需要int类型
        stn_tst = get_text(text, self.hps)
        with torch.no_grad():
            x_tst = stn_tst.cuda().unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cuda()
            sid = torch.LongTensor([speaker_index]).cuda()  # 说话人,LoveLive的模型时0-8
            audio = self.net_g.infer(x_tst, x_tst_lengths, sid=sid, noise_scale=.667, noise_scale_w=0.8, length_scale=1)[0][
                0, 0].data.cpu().float().numpy()
        print(ipd.Audio(audio, rate=self.hps.data.sampling_rate, normalize=False))
        audio = ipd.Audio(audio, rate=self.hps.data.sampling_rate, normalize=False)
        # 首先，需要获取音频数据的二进制数据
        audio_data = audio.data

        # 然后，使用open和write函数将音频数据写入文件
        with open('./audio/audio.wav', 'wb') as f:
            f.write(audio_data)

if __name__ == '__main__':
    a = single_speaker_model()
    a.generate("ゆう君、あたしの処女をもらってください")