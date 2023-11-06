import pyttsx3


def use_pyttsx3(text):
    engine = pyttsx3.init('nsss') #initialize a pyttsx3 engine
    rate = engine.getProperty("rate")
    engine.setProperty("rate",160)
    engine.setProperty("volue", 1.0)

    #voices = engine.getProperty("voices")
    #print(voices[0])
    #engine.setProperty("voice", voices[0].id)

    

    a = engine.say(text) #convert text to voice, and play
    engine.runAndWait() #start engine and wait the voice to finished. it would block the current thread until the audio is finished. 
    engine.stop()

    #saving the audio locally
    engine.save_to_file(text, filename = "test.wav", name = 'test')
    engine.runAndWait() #block current thread until file finished written
'''
if __name__ == "__main__":
    text = "Test test！ This is for test!"
    use_pyttsx3(text)
    '''
