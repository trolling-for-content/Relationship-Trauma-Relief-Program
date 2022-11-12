import time
import pyttsx3
engine = pyttsx3.init() #初始化语音引擎
engine.setProperty('rate', 200)   #设置语速
engine.setProperty('volume',1)  #设置音量
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)   #设置第一个语音合成器

ch = ""

def customParam():
  print("欢迎使用此程序，如果需要停止运行，请按Ctrl+C，（可能要多按几次）")
  ch = input("请输入你要发泄的恋爱对象名字\n")
  engine.setProperty('age',input("请输入对方年龄,(语音合成参数)\n"))
  sentence = input("请输入你要发泄的话\n")
  engine.setProperty('gender',input("请输入tts语音合成性别,参数共有三种：male,female,neutral\n"))

customParam()
while True:
  print("对不起，我错了")
  engine.say("对不起，我错了")
  engine.runAndWait()
  #engine.stop()
  time.sleep(0.25)