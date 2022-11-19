latter ='''Dear <|name|>,
You are selected!
<|date|>
'''
name= input('please type your name hare')
date= input('your joning Date???')
latter= latter.replace("<|name|>",name)
latter= latter.replace("<|date|>",date)
print(latter)