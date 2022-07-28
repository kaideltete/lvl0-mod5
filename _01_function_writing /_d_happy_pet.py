"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    u_score = 0
    pet = simpledialog.askstring(title='pet', prompt="what pet do you want, cat or dog?")

    q1 = simpledialog.askstring(title='feed, play, or walk?', prompt="looking at food bowl")
    q2 = simpledialog.askstring(title='feed, play, or walk?', prompt="looking at door")
    q3 = simpledialog.askstring(title='feed, play, or walk?', prompt="looking at toys")
    q4 = simpledialog.askstring(title='feed, play, or walk?', prompt="looking at door")
    q5 = simpledialog.askstring(title='feed, play, or walk?', prompt="looking at food bowl")
    q6 = simpledialog.askstring(title='feed, play, or walk?', prompt="looking at toys")
    q7 = simpledialog.askstring(title='feed, play, or walk?', prompt="looking at door")
    q8 = simpledialog.askstring(title='feed, play, or walk?', prompt="looking at toys")
    q9 = simpledialog.askstring(title='feed, play, or walk?', prompt="looking at food bowl")
    q10 = simpledialog.askstring(title='feed, play, or walk?', prompt="looking at toys")

    if (q1 == "feed"):
        u_score += 1
    if (q2 == "walk"):
        u_score += 1
    if (q3 == "play"):
        u_score += 1
    if (q4 == "walk"):
        u_score += 1
    if (q5 == "feed"):
        u_score += 1
    if (q6 == "play"):
        u_score += 1
    if (q7 == "walk"):
        u_score += 1
    if (q8 == "play"):
        u_score += 1
    if (q9 == "feed"):
        u_score += 1
    if (q10 == "play"):
        u_score += 1

    if u_score > 7:
        messagebox.showinfo(message="you keept your " +pet+ " happy")
    else:
        messagebox.showinfo(message="you didn't keep your " + pet + " happy")
    pass
