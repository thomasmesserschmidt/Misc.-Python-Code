# GPT-3 text Interface
import openai #for the GPT 3 library
import json
#import zzzkeys
#openai.api_key = zzzkeys.key2
openai.api_key = "YOUR KEY GOES HERE" #os.getenv("OPENAI_API_KEY")
myInput = "Starting"

while myInput != "bye" :
  myInput = input('(Enter input or "bye" to exit)\n')
  print("myInput: ", myInput)
  response = openai.Completion.create(
    model="text-davinci-002",
    #prompt="You: What have you been up to? \n Me: Just hanging out.\n You: Are you having fun?\ nFriend:",
    prompt=myInput,
    max_tokens=60,
    top_p=1.0,
    temperature=0.5,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
  )

  MyText = json.dumps(str(response))
  MyText = MyText.split("text\\")
  MyText = MyText[1].split("]")

  MyText[0] = MyText[0].replace('\\n', '')
  MyText[0] = MyText[0].replace('\\', '')
  MyText[0] = MyText[0].replace('}', '')
  MyText[0] = MyText[0].replace(':', '')
  MyText[0] = MyText[0].replace('"', '')
  MyText[0] = MyText[0].strip()

  print(MyText[0])



print('(Conversation is over)')




