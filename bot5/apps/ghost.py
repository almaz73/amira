import random 
number = 0
randPic = ' 🐮 🐭 🐫 🐯 🦏 🦍 🦊 🦒 🐀 🐨 🦘 🐖 🦇 🦓 🐰 🦝 🦔 🦄 🐆 🐄 🐷 🦙 🐽 🦁 🐻 🐈 🐣 🐔 🐤 🦜 🐧 🦉 🦃 🦚 🐸 🐍 🦎 🐊 🦖 🐲 🐉 🐋 🦈 🐳 🐙 🦋 🦠 🦂 🕷 🐜 🌹 🌺 🌼 🌻 🌴 🌲 🌳 🍂 ☘ 🌈 🐕'

def isStarted():
  global number 
  return number


def end():
  global number
  number = 0


def start():
  global number
  number = random.randrange(1, 100)
  return '🌈 Я загадал число, от 1 до 100, попробуй угадай 🤔'


def ask(text):
  global number
  pic = random.randrange(1, 60, 2)
  if text > number: return f'{randPic[pic]}  меньше {randPic[pic+2]}'
  if text < number: return f'{randPic[pic]}  БОЛЬШЕ {randPic[pic+2]}'
  if text == number: 
    number = 0
    return f'❌❌❌ {randPic[pic]} Вы угадали. {randPic[pic+2]} Игра закончена! {randPic[pic+4]}'

