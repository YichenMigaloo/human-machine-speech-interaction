import customtkinter
import sys
import recordSpeech

recorder = recordSpeech.Recorder()

def load():
    loadMain()

def exit():
    sys.exit()

def loadKey():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.geometry("500*350")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady = 20, padx = 60, fill= "both", expand = True)

    label = customtkinter.CTkLabel(master = frame, text = "Load your API key", font=("Roboto", 24))
    label.pack(pady = 12, padx = 10)
    

    api = customtkinter.CTkEntry(master=frame, placeholder_text="API key", show="*")
    api.pack(pady = 12, padx = 10)
    

    button = customtkinter.CTkButton(master=frame, text = "Load", command=load)
    button.pack(pady = 12, padx = 10)

    root.mainloop()

def loadMain():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.geometry("500*350")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady = 20, padx = 60, fill= "both", expand = True)

    label = customtkinter.CTkLabel(master = frame, text = "I'm Listening..", font=("Roboto", 24))
    label.pack(pady = 12, padx = 10)

    button_start = customtkinter.CTkButton(master=frame, text = "start speaking", command=recorder.start_recording)
    button_start.pack(pady = 12, padx = 10)

    button_end = customtkinter.CTkButton(master=frame, text = "end speaking",command=recorder.stop_recording)
    button_end.pack(pady = 12, padx = 10)

    button = customtkinter.CTkButton(master=frame, text = "exit", command = exit)
    button.pack(pady = 12, padx = 10)
    
    #start.get_prompt()
    root.mainloop()
    

if __name__ == "__main__":
    loadKey()
    