from file_slicer import split_audio_file
import transcript
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

# path for audio test
"""
path_audio_file = "StudyHack/audio_files_test/audio1.wav"
path_audio_segments ="StudyHack/audio_files_temp/"

# split audio files into smaller parts and make sure that it is only split when there is silence
split_audio_file(path_audio_file)

# Get the transcripts from the audio segments
notes = []
for file in os.listdir(path_audio_segments):
  if file.endswith(".wav"):
    notes.append(transcript.get_transcript(
      path_audio_segments + file, api_key))
"""
notes = []
notes.append('''[INTRIGUING MUSIC] DAVID MALAN: All right, so this is CS50. And this is week 1, zero index, so to speak. And it's not every day that you can say that you've learned a new language, but today is that day. Today, we explore a more traditional and older language called C. And rest assured that even if what you're about to see-- no pun intended-- looks very cryptic, very unusual, particularly if you're among those less comfortable, cling to the ideas from last week, week zero, wherein we talked about some of those fundamentals of functions and loops and conditionals, all of which are coming back today. 

Indeed, whereas last week, and with problem set 0, we focused on learning how to program with Scratch, which, again, you might have played with as a younger student days back. Today, we focus on C instead. But along the way, we're going to focus, as always, frankly, on learning how to solve problems. But among the goals for today and really on an entire class like this is just to give you week after week all the more tools for your toolkit, so to speak, via which to do exactly that. 

So for instance today, we'll learn how to solve problems all the more so with functions, as per last week. We'll do the same with variables. We'll do the same with conditionals, with loops, and with more. But we'll also learn at the end of today's class really how not to solve problems. It turns out as powerful as Macs, PCs, cell phones are nowadays, there's actually certain things that they can't do very well and information they can't represent very well. And that actually leads to a lot of real-world problems, both past and surely future. 

So more on what we're not going to be able to do with programming before long. But beyond that, let's come back to this picture here. So this was the very first program that I wrote, that you wrote presumably in some form. And all it does is say "Hello, world." But as promised, today, this puzzle piece, or these puzzle pieces together, are going to very quickly start to look more like this. 

And I've deliberately color coded it in a way so that the text on the screen now kind of resembles the puzzle piece. So if I go back, notice that we had this, when green flag clicked puzzle piece, mostly in yellow with the green flag, that sort of kicks off the whole process once you actually click the button at top right of Scratch's user interface. 

And then there's the purple block which actually is the verb, the action, the function that does something. So if I bring us back over to what we're about to see today, there's going to be some boilerplate, so to speak, some orange text here on the screen that for now you just type and take for granted, like you need to write your code like that. 

But more interesting is going to be the purple. And we're going to see today that the function previously called "say" in Scratch is now called "printf" in this language called C. But in white here, you'll see similar text to our white oval last week, whereby that's where user input, like your input as the programmer, can actually go. 

So there's a lot of distraction. And honestly, it's these kinds of things that tend to distract and get frustrating early on when learning to code for the first time. But the ideas, most importantly, are going to be the same. So how are we going to go about using this. Well, it turns out, like last week, you're going to start writing something called source code. 

So code as we know it, quote, unquote, is more technically called "source code." That's what you and I as humans actually write. And indeed it might look a little something like we just saw. But unfortunately, computers only speak this, binary-- zeros and ones-- more properly known as machine code, in other words, those same patterns of zeros and ones last week, someone guessed, print out "hello, world" on the screen because one of those patterns is an H. Another pattern is an E, an L, and L, and an O, and so forth. 

And then other patterns of those zeros and ones are commands or instructions to the computer that literally say, show H-E-L-L-O comma "world" on the screen. But machine code would not be nearly as much fun to write if it were indeed in zeros and ones. Entirely for us, ideally, you and I are going to write source code, which conceptually is sort of up here, high level. 
             ''')
notes.append('''But we're going to need a program to convert it to the lower-level machine code so that we don't spend our lives actually having to read and write zeros and ones, which back in the day, kind of in yesteryear, you kind of did with things called punch cards and holes on physical sheets of paper. We're beyond that because after years and years of innovation, folks have given us higher-level languages instead. 

So here's what we're going to need to do today. If at the end of the day you and I are writing source code but we want machine code as output, we need something in the middle that's going to convert that source code to machine code. You and I are not going to have to learn or talk about really any more zeros and ones. And the type of program we're going to start using today and introduce you to is called a compiler. 

So a compiler is a program that translates one language to another. And it can be any two languages. But today, and often, we'll talk about it in the context of source code to machine code. So this is Apple or Google or Microsoft or folks from other companies or even volunteers who have written software that do this conversion. You and I are essentially going to download a free compiler and use it to actually get our computer to understand the source code that you and I write in these higher-level languages. 

So where are we going to do that? Well, we could actually give you instructions and you could download the appropriate free open-source software onto your own Mac or PC. The reality is that creates so many technical support headaches because we all have slightly different computers. We all have slightly different versions of Windows or macOS or Linux or other operating systems. And that, too, tends to be a distraction at the beginning of any course like this or learning programming. 

So we're going to use the cloud instead. We're going to use a URL of the form https://cs50.dev. And what this will do for you is put inside of your browser window absolutely everything you need for the course, but it's going to use software, software called Visual Studio code, otherwise known as VS Code, that's actually free itself. It's very popular in industry. It's what "real" programmers use every day. But it's a cloud-based version thereof. 

And so everything will just work for you out of the box. But toward the end of CS50, the goal is going to be to get you off of CS50's infrastructure, to get you to download this freely available software onto your own Mac or PC if you so choose so that those training wheels, so to speak, can come off. And then even if you never take another class again, you don't need any class's infrastructure moving forward. You'll have everything you want and need on your own Mac or PC. But for now, it'll save us a bit of time. 

So in just a bit, I'm going to go to that URL myself on my computer. And I and you will see a user interface that looks a little something like this. The colors might be different based on your settings. Fonts might be different, and so forth. But in general, it consists of a few different regions. 

So over here at the top is where we are going to start writing code today. So it's a tabbed interface like any number of programs nowadays. And this is that same C code we saw a moment ago. So this is where, in a moment, I'm going to start to type it. Over here at the bottom is what we're going to call a terminal window, or a console. And the terminal window is where we're going to type commands for compiling our code, for running our code. 

And we'll see today a contrast between a graphical-user interface, or GUI, which has menus and icons and things you click and are very familiar with, versus a command-line interface, or CLI. And so we're using both of these together. And command-line interface just means, down here, you only use your keyboard. You can click, click, click if you want with your mouse. It's not going to generally do much because a command-line interface takes commands at the keyboard. 

So in a weird sense, it's going to feel like taking a step backwards from the Macs, the PCs, the iPhones, and Android phones we all have, which are very graphical. But it turns out, once you become a "computer" person or a programmer, you can be a lot more productive, a lot more efficient, I dare say, by learning to harness the command-line interface and using both types of interfaces for what each is good at. So more on that in just a bit. 

''')

notes.append('''Over here at left, you're going to see soon a folder interface like Mac OS or Windows where any of the files or folders we create in CS50 are going to end up, as well. So it gives you the best of both worlds. You can point and click on the left, or you can type commands at the bottom, as we'll soon see. 

And then along here is the so-called activity bar, where there's just VS Code-specific features but also CS50-specific features. And if you're in your own version of CS50.dev, you click through in the dot dot dot menu or zoom out so you can see everything. You'll see CS50's own rubber duck, virtually speaking, that will be there throughout the course to answer any and all of your questions, as well. So more on that soon, too. 

So here's the code that I propose that we write first, just like we wrote our very first Scratch program to say "hello, world." So let's go ahead and do exactly this. I'm going to switch over to this screen here, where I've already logged into CS50.dev on my computer. And just to keep the focus on the code, I've hidden the activity bar. I've hidden the File Explorer, so to speak. So you're seeing here the area where all of my tabs are about to go and the terminal window, where all of my commands are going to go. But I've just simplified the UI to keep our focus on the interesting parts for now. 

So how do I go about actually writing and compiling and running some code? Well, the teaser is going to be these three steps. One of these is a command called, aptly, Code. And Code is just going to let me to open or create a new file, like a file called "hello.c." 

Make is going to be, for now, my compiler that allows me to make the program, that is convert source code into machine code, so from C to zeros and ones. And then weirdly, but we'll soon see why, ./hello is going to be the command to run my actual code, so the textual equivalent of like double-clicking on a Mac or a PC icon or tapping an icon on your phone. 

So that's it. These three commands are going to allow me to write, to compile, and to run code ultimately. So let's go ahead and do that. I'm back in my VS Code interface. I'm going to go ahead and run "code hello.c." And notice a couple of details here. So one, there's this weird dollar sign, which has nothing to do with currency, but it's just a common convention in the programming world to represent your prompt. 

So if a TF, if I ever say, go to your prompt, we really mean, go to your terminal window. Go to the dollar sign. And the dollar sign is where you type the command. Sometimes it's a different symbol, but a dollar sign is conventional. Now that I've typed "code" space "hello.c," I'm going to go ahead and hit Enter. 

And maybe not surprisingly, this gives me a brand new tab, a new file if you will, called "hello.c." And just like Word documents have their own file extension, like DOC, DOCX, and Excel files have .XLSX and PDFs have .PDF and GIFs have .GIF and so forth, so do C files have a file extension by convention that is .C. 

Now, a couple of minor points. Notice that, by convention, I'm almost always going to name my files in lowercase. By convention, I'm never going to use spaces in my file names. And my file extension, too, is going to be lowercase. Long story short, accidentally hitting the spacebar or using file names with spaces just tends to make life harder when you're in a command-line environment. So just beware silly, stupid things like that. So all lowercase, no spaces for now. 

So my cursor is literally blinking because the program wants me to write some code. I'm going to do this from memory. It'll take you presumably some time to acquire the same instincts. But I'm going to go ahead and type this first line here, pronounced "include standard io.h"-- more on that soon-- int main(void), with some parentheses thrown in. ''')
# Send an API call to OpenAI to generate a summary of the notes
client = OpenAI(api_key=api_key)
resulting_notes = []
for note in notes:
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        # Testing messages
        {"role": "system", "content": "You will assist in summarizing large lecture transcripts for note-taking purposes." 
        "Your task is to condense the information efficiently, ensuring all key points and relevant details are preserved,"
        " while excluding unnecessary or repetitive information. Keep the notes clear and organized, leaving space for "
        "additional future notes but without adding any filler content. Only condense when necessary, maintaining "
        "essential context and meaning. Whenever possible, group related information and emphasize core concepts. Avoid "
        "restating unimportant or redundant points. Do not include any closing statements or prompts for future input."},
        {"role": "user", "content": note}
    ]
    )
    resulting_notes.append(response.choices[0].message.content)

# Print the resulting notes
for note in resulting_notes:
    print(note)
