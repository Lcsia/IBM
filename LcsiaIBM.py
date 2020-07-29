##LABORATORIO DE COMPORTAMIENTO SOCIAL E INTELIGENCIA ARTIFICIAL
#Laurent Avila Chauvet / Julio 2020
#Reto IBM @Talent-Home

import json 
from os.path import join, dirname 
from ibm_watson import SpeechToTextV1 
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pyaudio
import wave

#IBM Cloud
authenticator = IAMAuthenticator('s7xZD365fGwZ61S2zmSi3wZNdSBRd4eFNY-FnKxFWZD5')  
service = SpeechToTextV1(authenticator = authenticator) 
service.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/2ec64923-4dec-411d-9241-ccf860dbcc26') 


def TxtCom(Str1,Str2):
    Str1 = Str1.upper()
    Str2 = Str2.upper()
    Str2 = Str2.split()
    TempC = 0
    for i in range(len(Str2)):
        if Str1.find(Str2[i]) > 0:
            TempC += 1  
    return TempC/(len(Str1.split())-1)

def Sp2Txt(File):
    with open(join(dirname('__file__'), File+'.mp3'),  
          'rb') as audio_file: 
      
        dic = json.loads( 
                json.dumps( 
                    service.recognize( 
                        audio=audio_file, 
#                        content_type='audio/flac',    
                        model='es-MX_NarrowbandModel', 
                    continuous=True).get_result(), indent=2)) 
    Mp3Out = "" 
    while bool(dic.get('results')): 
        Mp3Out = dic.get('results').pop().get('alternatives').pop().get('transcript')+Mp3Out[:] 
    return Mp3Out

def RecSp(Time,Name):
    chunk = 1024 
    sample_format = pyaudio.paInt16  
    channels = 2
    fs = 44100  
    seconds = Time
    filename = Name+'.mp3'
    p = pyaudio.PyAudio() 
    print('Recording')
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []  
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        print(data)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    print('Finished recording')
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    

    
def ReadTxt(File):
    File = open(File+'.txt', encoding="utf8")
    return File.read()
    File.close()