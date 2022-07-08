import discord
import random

bad = ['ㅅㅂ','시발','씨발','ㅂㅅ','ㅗ','병신','ㅄ']

class chatbot(discord.Client):

    async def on_ready(self):
        game = discord.Game("내용")
        await client.change_presence(status=discord.Status.online, activity=game)

        print("연결완료")



    async def on_message(self, message):
        if message.author.bot:
            return None

        if message.content.startswith('Ellis 랜덤2'):
            randomNum = random.randrange(1, 3)
            if randomNum==1:
                channel = message.channel
                msg = "1"
                await channel.send(msg)
            else:
                channel = message.channel
                msg = "2"
                await channel.send(msg)
       
                 
        
        if message.content.startswith('Ellis 오늘레식?'):
            randomNum = random.randrange(1, 3)
            if randomNum==1:
                channel = message.channel
                msg = "레식 각입니다."
                await channel.send(msg)
            else:
                channel = message.channel
                msg = "자러갑니다...."
                await channel.send(msg)




        if message.content == "Ellis 출력":
            await message.channel.send("Python Bot에 의해 출력됨.") #바뀜
        if message.content.startswith("Ellis 1부터10"):
            for x in range(10):
                await message.channel.send(x+1) #바뀜
        if message.content.startswith("Ellis계산"):
            global calcResult
            if message.content[7:].startswith("더하기"):
                calcResult = int(message.content[11:12])+int(message.content[13:14])
                await message.channel.send("Result : "+str(calcResult)) #바뀜
            if message.content[7:].startswith("빼기"):
                calcResult = int(message.content[10:11])-int(message.content[12:13])
                await message.channel.send("Result : "+str(calcResult)) #바뀜
            if message.content[7:].startswith("곱하기"):
                calcResult = int(message.content[11:12])*int(message.content[13:14])
                await message.channel.send("Result : "+str(calcResult)) #바뀜
            if message.content[7:].startswith("나누기"):
                try:
                    calcResult = int(message.content[11:12])/int(message.content[13:14])
                    await message.channel.send("Result : "+str(calcResult)) #바뀜
                except ZeroDivisionError:
                    await message.channel.send("You can't divide with 0.") #바뀜

        message_contant=message.content
        for i in bad:
            if i in message_contant:
                await message.channel.send('욕설 ㄴㄴ')
                await message.delete()


        if message.author == client.user:
            return

            
        if message.content == ("Ellis 나가") or message.content == ("엘리스 나가") or message.content == ("ellis 나가"):
            channel = message.channel
            msg = "ㅠㅠ" 
            await channel.send(msg)
            return None

        
        if message.content == ("Ellis") or message.content == ("엘리스") or message.content == ("ellis"):
            randomNum = random.randrange(1, 1)
            if randomNum==1:
                channel = message.channel
                msg = "안녕하세요 :D"
                await channel.send(msg)
            else:
                channel = message.channel
                msg = "안녕!! :D"
                await channel.send(msg)

        

        
        if message.content == ("Ellis  1부터100") or message.content ==  ("Ellis  1부터100 까지"):
            channel = message.channel
            msg = "아......."
            await channel.send(msg)
            return None
        
        if message.content == "Ellis 바보":
            channel = message.channel
            msg = "실망이에요  ㅠㅠ"
            await channel.send(msg)
            return None

        
        if message.content == ("엘라") or message.content == ("엘리스 엘라") :
            channel = message.channel
            msg = "Ella is my sister.  ¯ \_(ツ)_/¯ "
            await channel.send(msg)
            return None

        if message.content == ("멜라") or message.content == ("엘리") :
            channel = message.channel
            msg = "Ella is my sister.  ¯ \_(ツ)_/¯ "
            await channel.send(msg)
            return None
        

if __name__ == "__main__":
    client = chatbot()
    client.run("토큰")
