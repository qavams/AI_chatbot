import random
from tkinter import *
import tkinter.scrolledtext as scrolledtext
G_var = 1
nans = []


def checkstring(fulstr, substr):
    for sublist in substr:
        if sublist in fulstr:
            return 1
    return 0


def randansw(anslist):
    ansselect = random.choice(anslist)
    return ansselect


root = Tk()
root.title("راسل چت by Qavamodin Soleimani")


def _key_(k):
    send.invoke()


nans = ['هي ، چخبر', 'ايشلا سلامتي، گفتي چن سالته', 'هميشه همه چي روال باشه،سرکيفي عزيز ؟  ',
        'بخندي هميشه، کجايي', 'اهان،بگما من همه ي اطلاعاتم رو بهت نميدم', 'برو بابا،اسمت چي بود؟ ', 'کاش قوام هم بود ']


def sendd():
    global G_var
    global nans
    sendt = "پيام شما : "+e.get()
    Font_tuple2 = ("b zar", 10, "bold")
    txt.insert(END, "\n"+sendt, 'tag-left')
    user = e.get().lower()

    if G_var == 1:

        if(checkstring(user, ['جان', 'چطور'])):
            txt.insert(END, "\n" + " يه جوراي خوبي ", 'tag-right')
        elif(checkstring(user, [ 'خوبم', 'مرسي', 'ممنون', 'عالي', 'شکر', 'الحمد', 'هي', 'هعي', 'سلامت باش', 'گذر', 'سلامتي','سلام'])):
            hilist = ["زنده باشي هنوز رواله اوضاع؟", "الهي شکر حالا چه ميکني؟",
                      'شادي به دلت ، بيشتر آشنا بشيم ؟']
            G_var = 0
            hiselect = random.choice(hilist)
            txt.insert(END, "\n" + "راسل چت : " + hiselect, 'tag-right')
        elif(checkstring(user, ['ديگه', 'خبر', 'خوبي'])):
            txt.insert(
                END, "\n" + "راسل چت : عاليه همه چي عالي ، تو چه طور؟ بيا بيشتر آشنا شيم ", 'tag-right')
            G_var = 0
        elif(checkstring(user, ['خوب', 'بد', 'هي', 'عالي', 'کاش', 'بله', 'چخبر'])):
            txt.insert(
                END, "\n" + "راسل چت : امان از روزگار  ، ديگه کاري از دستم برمياد انجام بدم برات؟ ", 'tag-right')
            G_var = 0
        elif(checkstring(user, ['سن', 'چن', 'سال'])):
            txt.insert(
                END, "\n" + "راسل چت : چقدره بنظر خودت؟ ", 'tag-right')
            G_var = 0
        elif(checkstring(user, ['نام', 'اسم'])):
            txt.insert(
                END, "\n" + "راسل چت : چي باشه خوبه؟", 'tag-right')
            G_var = 0
        elif(checkstring(user, ['کسي', 'کي', 'کجا', 'امروز', 'جور', 'چه', 'چرا', 'چي'])):
            txt.insert(
                END, "\n" + "راسل چت : بنظرم به سازندم بگو  ", 'tag-right')
            G_var = 0
        elif(checkstring(user, ['قوام' , 'ساخت' , 'درست','ساز'])):
            txt.insert(
                END, "\n" + "راسل چت : قوام سازندم هست . کاش الان بودش   ", 'tag-right')
        elif(checkstring(user, ['برم', 'باي', 'خدانگهدار', 'خداحافظ'])):
            txt.insert(
                END, "\n" + "من فک کنم بايد برم خداحافظ تا بعد ", 'tag-right')
            exit()

        else:
            txt.insert(
                END, "\n" + "راسل چت : عزيز متوجه اين صحبتت نشدم  ", 'tag-right')
            G_var = 0
    else:

        elans = randansw(nans)
        enumber = nans.index(elans)
        del nans[enumber]
        if len(nans) == 0:
            nans.append(" شارژم تموم شده ديگه پرت و پلا ميگم ")
        txt.insert(
            END, "\n" + elans, 'tag-right')
        G_var = 1
    e.delete(0, END)


Font_tuple2 = ("b zar", 10, "bold")
txt = Text(root)
txt = scrolledtext.ScrolledText(root, undo=True)
txt.tag_configure('tag-right', justify='right', font=Font_tuple2)
txt.pack()
# txt.grid(row=0, column=0, columnspan=2)
Font_tuple3 = ("b badr", 10, "italic")
e = Entry(root, width=100, justify='right', font=Font_tuple3)
e.pack()
# e.grid(row=1, column=0)
Font_tuple = ("b nazanin", 12, "bold")

txt.tag_configure("center", justify='center', font=Font_tuple)
txt.insert(
    "1.0", "سلام و ادب خدمت شما کاربرمحترم \n، اين يک پاسخگوي واکنشي ساده است\n  اميدوارم از استفاده ازين چت‌بات لذت ببريد  \n جواب بعضي از سوالاتونم ميده")
txt.tag_add("center", "1.0", "end")
txt.insert(END, "\n" + " راسل چت : سلام من راسل چتم. خوبي ؟ ", 'tag-right')
send = Button(root, text="بفرست براش ببين چي ميگه", justify=CENTER,
              command=sendd, font=Font_tuple2)
send.pack()
root.bind('<Return>', _key_)

root.mainloop()
