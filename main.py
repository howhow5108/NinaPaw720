from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.inlinequeryhandler import InlineQueryHandler
from telegram.ext import CallbackQueryHandler, Dispatcher
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram.ext.choseninlineresulthandler import ChosenInlineResultHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineQueryResultArticle, InputTextMessageContent, InputMessageContent, Bot
from itertools import permutations
from uuid import uuid4
import random
import threading
import time
import os



#PORT = int(os.environ.get('PORT', 8080))

TOKEN = "5511837706:AAFyKSIE_P6IPFiL-dr5DLNJ7GFOwXyUODI"

updater = Updater(TOKEN, use_context=True)

ky_id = 266799002


data = {}

global_discard = ""

clues_list = ["防盜攝影機","汽水","圖釘","鉈錶","零食","外置記憶體","內衣","手扣","手套","手提電筒","高跟鞋","電腦","戒指","冷氣","行李","日記","電話","藥方","簽名","雞蛋","蚊香","蚊子","茶葉","胸章","紙箱","文具","電路板","麵包","鐘鈴","塗鴉","塑膠","饅頭","鏡片","鏡子","藥材","針筒","謎題","迷宮","記號","記事簿","針線","印章","冰塊","皮包","外賣","古董","手鐲","手錶","貓咪","螞蟻","骨頭","鉗子","油畫","咖啡","外套","雜誌","鎖頭","鎖匙","禮物","蟑螂","西裝","衣架","血液","耳環","耳機","紅酒","信封","雨傘","雨衣","陀螺","灰塵","污垢","收據","安全扣針","字條","粉末","海綿","書本","扇子","唇膏","油漆","棉花","麻袋","帽子","報紙","牙簽","小提琴","子彈","口罩","快遞","麻雀","蛋糕","雪茄","情書","掃把","制服","昆蟲","果汁","杯子","油漬","假牙","木屑","木偶","毛絨娃娃","毛髮","字典","地圖","名片","紙巾","紋身","借據","香水","首飾","食材","音響","面具","花生","長笛","指甲","拼圖","皮鞋","飯盒","絲襪","太陽眼鏡","髮夾","燈泡","證件","錢包","齒輪","磁碟","號碼","樹葉","菜單","輸液袋","墨水","模型","標本","撲克牌","彈簧","骰子","蘋果","郵票","頸鏈","傳單","蔬菜","煙灰","鈕扣","硬幣","糖果","調味料","煙頭","開關掣","窗簾","內褲","骷髏","籌碼","証書","錄音帶","傳真","膠水","抹布","鑽石","光纖","鐵釘","襪子","滑鼠","鈔票","頭盔","積木","請柬","領帶","蜘蛛","網線","漫畫","枱燈","攝錄機","繃帶","試管","沙","試卷","工具箱","沙漏","熨斗","照片","手機","文件","日曆","木材","拖鞋","玫瑰","老鼠","玩具","粉筆","狗毛","面膜","植物","肥皂","彩票","密函","假髮"]

methods_list = ["鋼管","摺凳","石頭","硫酸","手槍","獎杯","放血","圍巾","啞鈴","中毒","雕塑","瘋狗","皮鞭","溜冰鞋","毛巾","輻射","拐杖","割喉","火藥","匕首","燭台","摩托車","竹尖","污水","水銀","撕咬","扳手","變形蟲","火柴","刀片","磚頭","注射","皮帶","推撞","手術","瘟疫","斧頭","棍棒","活埋","工作","機械","膠帶","打火機","徒手","化學品","踢打","枕頭","菜刀","密室","切割","砒霜","煙","砍刀","盆栽","炸藥","溺水","𠝹刀","鐵鈎","鐵鏈","狙擊","鐵鏟","鐵鎚","鐵絲","饑荒","藥粉","藥水","藥丸","繩索","縱火","剪刀","刀叉","毒針","毒氣","毒品","封箱膠紙","酒精","酒","病毒","拳擊","攪拌器","毒蝎","毒蛇","電鑽","電鋸","電線","電棒","電流","遊戲機","農藥","煤油"]

purple_list = ["窒息","重傷","失血","病發","中毒","意外"]

green_list = [["別墅","公園","超市","學校","樹林","銀行"], ["酒吧","書店","餐廳","酒店","醫院","地盤"],
["客廳","睡房","儲物房","浴室","廚房","露台"], ["操場","課室","宿舍","飯堂","升降機","廁所"]]

orange_list = {"\U0001F7E7死者職業":["老闆","專業人士","工人","學生","無業","退休"], 
"\U0001F7E7死者身分":["兒童","青年","中年","老人","男人","女人"],
"\U0001F7E7死者衣着":["整齊","凌亂","華麗","破爛","奇特","裸體"],
"\U0001F7E7死者體格":["肥胖","瘦弱","高大","矮小","畸形","強健"],
"\U0001F7E7死者表情":["安詳","掙扎","恐懼","痛苦","沒表情","憤怒"],
"\U0001F7E7屍體狀況":["餘溫","僵硬","腐爛","殘缺","完整","扭曲"],
"\U0001F7E7屍體疑點":["頭部","胸部","手部","腿部","局部","全身"],
"\U0001F7E7案發日子":["平日","周末","春天","夏天","秋天","冬天"],
"\U0001F7E7天氣情況":["晴朗","雷雨","乾燥","潮濕","寒冷","炎熱"],
"\U0001F7E7作案時長":["瞬間","短暫","逐漸","漫長","數日","模糊"],
"\U0001F7E7死亡時間":["黎明","上午","中午","下午","晚上","午夜"],
"\U0001F7E7現場狀況":["碎屑","灰燼","水漬","破裂","雜亂","整齊"],
"\U0001F7E7現場痕跡":["指紋","腳印","淤青","血漬","體液","傷痕"],
"\U0001F7E7進行事情":["娛樂","休閒","集會","交易","探訪","飯局"],
"\U0001F7E7兇手性格":["傲慢","卑鄙","暴怒","貪婪","強硬","變態"],
"\U0001F7E7社交關係":["親戚","朋友","同事","僱傭","情侶","陌生"],
"\U0001F7E7作案動機":["仇恨","權力","金錢","情愛","妒忌","公義"],
"\U0001F7E7遺留跡象":["自然的","藝術的","書寫的","人造的","個人的","不相關"],
"\U0001F7E7特發事件":["停電","起火","爭執","失竊","叫喊","無"],
"\U0001F7E7途人描述":["聲音突響","聲音長鳴","氣味","視像","動態","沒有特別"],
"\U0001F7E7整體印象":["平常","創新","蹺蹊","殘忍","恐怖","懸疑"]
}

event_obj = threading.Event()




for index, e in enumerate(clues_list):
    clues_list[index] = "\U0001F534" + clues_list[index]

for index, e in enumerate(methods_list):
    methods_list[index] = "\U0001F535" + methods_list[index]


dede = False


def debugmode():
    return dede #or (-1001689175065 in data)



def newgame(update: Update, context: CallbackContext):
    group_id = update.message.chat.id
    print(group_id)
    if debugmode() and group_id != -1001689175065:
        updater.bot.sendMessage(chat_id = group_id, text = "維護中...稍後再試")
        return    
    if group_id < 0:
        if not group_id in data:
            data[group_id]={'game_status':[0, 0], 'date':update.message.date, 'hardmode':False}  
            print(update.message.date, group_id, update.message.chat.title)
        if data[group_id]['game_status'] == [0, 0]: #未有遊戲
            data[group_id]['game_status'] = [1, 0]  #有遊戲
            data[group_id]['game_id'] = random.random()
            data[group_id]['players_list'] = []
            data[group_id]['players'] = {}
            new_game_msg = updater.bot.sendMessage(chat_id = group_id, text = "至少要4人先開得\n玩家\(0人\):\n", parse_mode="MarkdownV2", reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("/join 加入", callback_data = "join"),
                                                                                                                                                                      InlineKeyboardButton("/flee 離開", callback_data = "flee")]]))
            data[group_id]['new_game_msg_id'] = new_game_msg.message_id
        elif data[group_id]['game_status'] == [1, 0]: #有遊戲, 未開始
            players_list = ""
            for p in data[group_id]['players_list']:
                temp = p.first_name
                temp = no_sp(temp) 
                players_list += f"[{temp}](tg://user?id={p.id}), "
            players_list = players_list[:-2] #去掉最後的", 
            players_num = len(data[group_id]['players_list'])
            try:
                updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['new_game_msg_id'])
            except:
                print("message to delete not found")
            RM = [[InlineKeyboardButton("/join 加入", callback_data = "join"), InlineKeyboardButton("/flee 離開", callback_data = "flee")]]
            text = "至少要4人先開得"
            if debugmode() or players_num >= 4:                
                RM.append([InlineKeyboardButton("開始遊戲", callback_data = "startgame")])#, InlineKeyboardButton(f"困難模式({is_hardmode(group_id)})", callback_data = "hardmode")])
                text = "人齊可以開始啦"
            if ky_id in data:
                if data[ky_id][0] == group_id:
                    temp = f"{players_num-1}人1狗"
            else:
                temp = f"{players_num}人"
            new_game_msg = updater.bot.sendMessage(chat_id = group_id, text = f"{text}\n玩家\({temp}\):\n{players_list}", parse_mode="MarkdownV2", reply_markup = InlineKeyboardMarkup(RM))
            data[group_id]['new_game_msg_id'] = new_game_msg.message_id


def handler_join_flee_start(update: Update, context: CallbackContext):
    group_id = update.callback_query.message.chat.id
    if group_id not in data:
        return
    if update.callback_query.data == "join":
        join_game(group_id, update.callback_query.from_user, update)
    elif update.callback_query.data == "flee":
        flee_game(group_id, update.callback_query.from_user)
    elif update.callback_query.data == "startgame":
        start_game(update, context)


def join_game(group_id, player, update):
    if player.id in data:
        if data[player.id][0] == group_id:
            return
        else:
            updater.bot.sendMessage(chat_id = group_id, text = player.first_name + "你已經喺第2個group玩緊!")
            return
    if group_id not in data:
        return
    if data[group_id]['game_status'][1] == 1:
        return
    if player in data[group_id]['players_list'] and not debugmode():
        return
    try:
        updater.bot.sendMessage(chat_id = player.id, text = "你已經加入" + update.callback_query.message.chat.title + "的遊戲中!")        
    except:        
        updater.bot.sendMessage(chat_id = group_id, text = player.first_name + " 請先啟動我!", reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("按我啟動", url = "t.me/NinaPaw720_bot?start")]]))
        return
    print(player.first_name, player.id)
    data[group_id]['players_list'].append(player)
    data[group_id]['players'][player.id] = {}
    data[player.id] = [group_id, None]  #記錄在groupid玩緊[groupid, role]
    players_list = ""
    for p in data[group_id]['players_list']:
        temp = p.first_name
        temp = no_sp(temp)
        players_list += f"[{temp}](tg://user?id={p.id}), "
    players_list = players_list[:-2] #去掉最後的", "
    players_num = len(data[group_id]['players_list'])
    RM = [[InlineKeyboardButton("/join 加入", callback_data = "join"), InlineKeyboardButton("/flee 離開", callback_data = "flee")]]
    text = "至少要4人先開得"
    if ky_id in data:
        if data[ky_id][0] == group_id:
            temp = f"{players_num-1}人1狗"
    else:
        temp = f"{players_num}人"
    if debugmode() or players_num >= 4:                
        RM.append([InlineKeyboardButton("開始遊戲", callback_data = "startgame")])#, InlineKeyboardButton(f"困難模式({is_hardmode(group_id)})", callback_data = "hardmode")])
        text = "人齊可以開始啦"
    try:
        updater.bot.editMessageText(chat_id = group_id, message_id = data[group_id]['new_game_msg_id'], text = f"{text}\n玩家\({temp}\):\n{players_list}", parse_mode="MarkdownV2", reply_markup = InlineKeyboardMarkup(RM))
    except:
        print("?")
        return

def flee_game(group_id, player):
    if group_id not in data:
        return
    if data[group_id]['game_status'][1] == 1:
        return
    if player not in data[group_id]['players_list']:
        return
    data[group_id]['players_list'].remove(player)
    data[group_id]['players'].pop(player.id)
    data.pop(player.id)
    players_list = ""
    for p in data[group_id]['players_list']:
        temp = p.first_name
        temp = no_sp(temp)
        players_list += f"[{temp}](tg://user?id={p.id}), "
    players_list = players_list[:-2] #去掉最後的", "
    players_num = len(data[group_id]['players_list'])
    RM = [[InlineKeyboardButton("/join 加入", callback_data = "join"), InlineKeyboardButton("/flee 離開", callback_data = "flee")]]
    text = "至少要4人先開得"
    if ky_id in data:
        if data[ky_id][0] == group_id:
            temp = f"{players_num-1}人1狗"
    else:
        temp = f"{players_num}人"
    if players_num >= 4:                
        RM.append([InlineKeyboardButton("開始遊戲", callback_data = "startgame")])#, InlineKeyboardButton(f"困難模式({is_hardmode(group_id)})", callback_data = "hardmode")])
        text = "人齊可以開始啦"
    try:
        updater.bot.editMessageText(chat_id = group_id, message_id = data[group_id]['new_game_msg_id'], text = f"{text}\n玩家\({temp}\):\n{players_list}", parse_mode="MarkdownV2", reply_markup = InlineKeyboardMarkup(RM))
    except:
        print("?")
        return
    


def start_game(update: Update, context: CallbackContext):
    group_id = update.callback_query.message.chat.id
    if group_id not in data:
        return
    if data[group_id]['game_status'][1] == 1:
        return
    updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['new_game_msg_id'])
    data[group_id]['game_status'] = [1, 1]
    data[group_id]['phase'] = 'fs'
    RM = [[InlineKeyboardButton("我!!", callback_data = "fs_me"), InlineKeyboardButton("隨機", callback_data = "fs_random")], [InlineKeyboardButton("確認", callback_data = "fs_confirm")]]
    fs_msg = updater.bot.sendMessage(chat_id = group_id, text = "請選擇鑑證專家", reply_markup = InlineKeyboardMarkup(RM))
    data[group_id]['fs_msg'] = fs_msg



def handler_fs(update: Update, context: CallbackContext):    
    group_id = update.callback_query.message.chat.id
    player = update.callback_query.from_user
    if group_id not in data:
        return
    if data[group_id]['game_status'] != [1, 1]:
        return
    if data[group_id]['phase'] != 'fs':
        return
    fs_msg = data[group_id]['fs_msg']
    if update.callback_query.data == "fs_confirm":
        if 'fs' not in data[group_id]:
            return
        fs = data[group_id]['fs']
        name = no_sp(fs.first_name)
        name = f"[{name}](tg://user?id={fs.id})"
        updater.bot.editMessageText(chat_id = group_id, message_id = fs_msg.message_id, text = f"\U0001F9D1\U0000200D\U0001F52C{name}", parse_mode="MarkdownV2")
        setup(update, context)
        return
    if update.callback_query.data == "fs_me":
        if player in data[group_id]['player_list']:
            data[group_id]['fs'] = player            
    elif update.callback_query.data == "fs_random":
        data[group_id]['fs'] = random.sample(data[group_id]['players_list'], 1)[0]
    RM = [[InlineKeyboardButton("\U0001F9D1\U0000200D\U0001F52C" + data[group_id]['fs'].first_name, callback_data = "fs_me"), InlineKeyboardButton("隨機", callback_data = "fs_random")], [InlineKeyboardButton("確認", callback_data = "fs_confirm")]]
    updater.bot.editMessageText(chat_id = group_id, message_id = fs_msg.message_id, text = fs_msg.text, reply_markup = InlineKeyboardMarkup(RM))    
    


def setup(update, context):
    group_id = update.callback_query.message.chat.id
    clues = random.sample(clues_list, (len(list_players(group_id)) - 1) * 4)
    methods = random.sample(methods_list, (len(list_players(group_id)) - 1) * 4)
    #data[group_id]['players_clues'] = {}
    #data[group_id]['players_methods'] = {}
    data[group_id]['guess_count'] = 0
    data[group_id]['orange_used'] = []
    data[group_id]['discarding'] = None
    data[group_id]['new_orr'] = None
    data[group_id]['round'] = 1
    players_num = len(data[group_id]['players_list'])
    data[group_id]['players_list'] = random.sample(data[group_id]['players_list'], players_num)
    players = data[group_id]['players_list']    
    fs = data[group_id]['fs']
    temp = list(set(players) - set([fs]))
    murderer = random.sample(temp, 1)[0]
    temp = list(set(temp) - set([murderer]))
    accomplice = None
    witness = None
    if players_num not in range(1, 6):            
        accomplice = random.sample(temp, 1)[0]
        temp = list(set(temp) - set([accomplice]))
        witness = random.sample(temp, 1)[0]
        temp = list(set(temp) - set([witness]))
    invests = temp
    temp = list(set(players) - set([fs]))
    if debugmode():
        #murderer = players[0]
        accomplice = players[0]
        witness = players[0]
        invests = [players[0]]
        temp = [murderer]
    for index, p in enumerate(temp):
        data[group_id]['players'][p.id]['clues'] = clues[index * 4 : (index + 1) * 4]
        data[group_id]['players'][p.id]['methods'] = methods[index * 4 : (index + 1) * 4]
        data[group_id]['players'][p.id]['speech'] = []
        data[group_id]['players'][p.id]['guess'] = None
    show_hands(group_id)
    updater.bot.sendMessage(chat_id = group_id, text = "遊戲開始 等待兇手行動...")
    RM = []
    for index, e in enumerate(data[group_id]['players'][murderer.id]['clues']):
        RM.append([InlineKeyboardButton(text = e, callback_data = "clue_" + e)])
    for index, e in enumerate(data[group_id]['players'][murderer.id]['methods']):
        RM[index].append(InlineKeyboardButton(text = e, callback_data = f"method_{e}"))
    RM.append([InlineKeyboardButton("確認", callback_data = "murder_confirm")])
    data[group_id]['phase'] = 'murder'
    data[group_id]['answer'] = {'clue':None, 'method':None}
    text = "大鑊\!你係\U0001F52A殺人兇手\!\n請選擇證物及手法:"
    if accomplice:
        accomplice_name = no_sp(accomplice.first_name)
        #text += f"[{accomplice_name}](tg://user?id={accomplice.id})"
        text = f"大鑊\!你係\U0001F52A殺人兇手\!\n[{accomplice_name}](tg://user?id={accomplice.id}) 係幫兇\!請選擇證物及手法:"
    #RM = [[InlineKeyboardButton(text = 'A', callback_data = "method_"),InlineKeyboardButton(text = 'B', callback_data = "method_")],
    #      [InlineKeyboardButton(text = 'C', callback_data = "method_"),InlineKeyboardButton(text = 'D', callback_data = "method_")],
    #      [InlineKeyboardButton(text = 'E', callback_data = "method_"),InlineKeyboardButton(text = 'F', callback_data = "method_")],
    #      [InlineKeyboardButton(text = 'G', callback_data = "method_"),InlineKeyboardButton(text = 'H', callback_data = "method_")]]
    murderer_msg = updater.bot.sendMessage(chat_id = murderer.id, text = text, parse_mode="MarkdownV2", reply_markup = InlineKeyboardMarkup(RM))
    data[group_id]['murderer_msg'] = murderer_msg
    data[group_id]['clues'] = clues
    data[group_id]['methods'] = methods
    print(data[group_id]['clues'], data[group_id]['methods'])
    data[group_id]['invests'] = invests
    data[group_id]['murderer'] = murderer
    data[group_id]['accomplice'] = accomplice
    data[group_id]['witness'] = witness


def show_hands(group_id):
    fs = data[group_id]['fs']
    players_list = data[group_id]['players_list']
    players = set(players_list) - set([fs])
    text = ""
    for index, p in enumerate(players):
        first_name = no_sp(p.first_name)
        text = text + f"[{first_name}](tg://user?id={p.id})\n證物:"
        for clue in data[group_id]['players'][p.id]['clues']:
            text = text + " " + clue
        text = text + "\n手法:"
        for method in data[group_id]['players'][p.id]['methods']:
            text = text + " " + method
        if index != len(players) - 1:
            text = text + "\n"
    data[group_id]['hands_msg'] = updater.bot.sendMessage(chat_id = group_id, text = text, parse_mode="MarkdownV2")
        


def answer(update: Update, context: CallbackContext):
    chat_id = update.callback_query.message.chat.id
    player = update.callback_query.from_user
    query_data = update.callback_query.data
    if chat_id < 0:                     #from group
        if chat_id not in data:
            return    
        if player.id not in data:
            return
        if data[player.id][0] != chat_id:
            return
    else:                                #from pm
        if player.id not in data:
            return
        group_id = data[player.id][0]
        if group_id not in data:
            return
        if data[group_id]['game_status'] != [1, 1]:
            return
        if data[group_id]['phase'] == 'murder':
            murderer_msg = data[group_id]['murderer_msg']
            murderer = data[group_id]['murderer']
            if query_data == "murder_confirm":
                if data[group_id]['answer']['clue'] and data[group_id]['answer']['method']:
                    data[group_id]['murderer_RM'].pop()
                    RM = data[group_id]['murderer_RM']
                    updater.bot.editMessageReplyMarkup(chat_id = chat_id, message_id = murderer_msg.message_id, reply_markup = InlineKeyboardMarkup(RM))
                    after_murder(update, context)
                return
            elif "clue_" in query_data:            
                new_clue = query_data.replace("clue_", "")
                if new_clue not in data[group_id]['players'][player.id]['clues']:
                    return
                if data[group_id]['answer']['clue'] != new_clue:
                    data[group_id]['answer']['clue'] = new_clue
                else:
                    return
            elif "method_" in query_data:                
                new_method = query_data.replace("method_", "")
                if new_method not in data[group_id]['players'][player.id]['methods']:
                    return
                if data[group_id]['answer']['method'] != new_method:
                    data[group_id]['answer']['method'] = new_method
                else:
                    return
            else:
                return
            RM = []
            for index, e in enumerate(data[group_id]['players'][murderer.id]['clues']):
                temp = e
                if e == data[group_id]['answer']['clue']:
                    temp = "\U00002714" + temp
                RM.append([InlineKeyboardButton(temp, callback_data = "clue_" + e)])
            for index, e in enumerate(data[group_id]['players'][murderer.id]['methods']):
                temp = e
                if e == data[group_id]['answer']['method']:
                    temp = "\U00002714" + temp
                RM[index].append(InlineKeyboardButton(temp, callback_data = "method_" + e))
            RM.append([InlineKeyboardButton("確認", callback_data = "murder_confirm")])
            data[group_id]['murderer_RM'] = RM
            updater.bot.editMessageReplyMarkup(chat_id = chat_id, message_id = murderer_msg.message_id, reply_markup = InlineKeyboardMarkup(RM))
        elif data[group_id]['phase'] == 'discard':
            if data[group_id]['fs'] != player:
                return
            discard_msg = data[group_id]['discard_msg']
            if query_data == "discard_confirm":
                if data[group_id]['discarding']:
                    data[group_id]['discard_RM'].pop()
                    RM = data[group_id]['discard_RM']
                    updater.bot.editMessageReplyMarkup(chat_id = chat_id, message_id = discard_msg.message_id, reply_markup = InlineKeyboardMarkup(RM))
                    next_phase(group_id)
            elif "discard_" in query_data:
                temp = query_data.replace("discard_", "")
                if data[group_id]['discarding'] != temp:
                    data[group_id]['discarding'] = temp
                else:
                    return
                RM = [[]]
                for orr_index, orr in enumerate(data[group_id]['orange_now']):
                    orrr = orr
                    if orr == data[group_id]['discarding']:
                        orrr = "\U0000274C" + orr
                    RM[0].append(InlineKeyboardButton(orrr, callback_data = f"discard_{orr}"))
                    for index, e in enumerate(orange_list[orr]):
                        ee = e
                        if e in data[group_id]['marked']:
                            ee = f"\U00002757{e}"
                        if orr_index == 0:
                            RM.append([InlineKeyboardButton(ee, callback_data = f"{e}")])
                        else:
                            RM[index + 1].append(InlineKeyboardButton(ee, callback_data = f"{e}"))
                RM.append([InlineKeyboardButton("確認", callback_data = "discard_confirm")])
                data[group_id]['discard_RM'] = RM.copy()
                updater.bot.editMessageReplyMarkup(chat_id = chat_id, message_id = discard_msg.message_id, reply_markup = InlineKeyboardMarkup(RM))
        elif data[group_id]['phase'] == 'new_orr':
            if data[group_id]['fs'] != player:
                return
            new_orr_msg = data[group_id]['new_orr_msg']
            if query_data == "new_orr_confirm":
                if data[group_id]['new_orr']:
                    data[group_id]['new_orr_RM'].pop()
                    RM = data[group_id]['new_orr_RM']
                    updater.bot.editMessageReplyMarkup(chat_id = chat_id, message_id = new_orr_msg.message_id, reply_markup = InlineKeyboardMarkup(RM))
                    data[group_id]['marked'].append(data[group_id]['new_orr'][1])
                    next_phase(group_id)
            elif "new_orr_" in query_data:
                new_orr = query_data.replace("new_orr_", "")
                new_orr = new_orr.split(":")
                if data[group_id]['new_orr'] != new_orr:
                    data[group_id]['new_orr'] = new_orr
                else:
                    return
                RM = []
                RM.append([InlineKeyboardButton(new_orr[0], callback_data = f"{new_orr[0]}")])
                for index, e in enumerate(orange_list[new_orr[0]]):
                    ee = e
                    if e == new_orr[1]:
                        ee = "\U00002757" + e
                    RM.append([InlineKeyboardButton(ee, callback_data = f"new_orr_{new_orr[0]}:{e}")])
                RM.append([InlineKeyboardButton("確認", callback_data = "new_orr_confirm")])   
                data[group_id]['new_orr_RM'] = RM.copy()
                updater.bot.editMessageReplyMarkup(chat_id = data[group_id]['fs'].id, message_id = new_orr_msg.message_id, reply_markup = InlineKeyboardMarkup(RM))
                




def after_murder(update: Update, context: CallbackContext):
    group_id = data[update.callback_query.message.chat.id][0]
    data[group_id]['phase'] = 'after_murder'
    data[group_id]['marked'] = []
    data[group_id]['marked_scene'] = []
    fs = data[group_id]['fs']    
    murderer = data[group_id]['murderer']
    accomplice = data[group_id]['accomplice']
    witness = data[group_id]['witness']
    invests = data[group_id]['invests']    
    answer = data[group_id]['answer']    
    #Send to FS
    text = "兇手及其幫兇:\n"
    murderer_name = no_sp(murderer.first_name)
    text += f"[{murderer_name}](tg://user?id={murderer.id})"
    if accomplice:
        accomplice_name = no_sp(accomplice.first_name)
        text += f", [{accomplice_name}](tg://user?id={accomplice.id})"
    text += "\n證物及手法:\n"
    text += answer['clue'] + ", " + answer['method']
    data[group_id]['forward'] = text
    if witness:
        witness_name = no_sp(witness.first_name)
        text += f"\n目擊者:\n[{witness_name}](tg://user?id={witness.id})"
    updater.bot.sendMessage(chat_id = fs.id, text = text,  parse_mode="MarkdownV2")
    #Send to murderer
    if accomplice:        
        pass
    #Send to accomplice
    if accomplice:
        text = f"恭喜\!你是\U0001F52A[{murderer_name}](tg://user?id={murderer.id})的幫兇\!\n證物及手法:\n"
        text += answer['clue'] + ", " + answer['method']
        updater.bot.sendMessage(chat_id = accomplice.id, text = text,  parse_mode="MarkdownV2")
    #Send to witness
    if witness:
        text = f"你係目擊者 你知道邊個係兇手:\n[{murderer_name}](tg://user?id={murderer.id})\n小心隱藏身份 不要被兇手發現"
        if accomplice:
            mur_team = [murderer, accomplice]
            mur_team = random.sample(mur_team, 2)
            mur_team_name = [no_sp(mur_team[0].first_name), no_sp(mur_team[1].first_name)]
            temp = f"[{mur_team_name[0]}](tg://user?id={mur_team[0].id}), [{mur_team_name[1]}](tg://user?id={mur_team[1].id}) "
            text = "你係目擊者 你見到兩條茂利 但唔知邊個係兇手邊個係幫兇\n" + temp + "\n小心隱藏身份 不要被兇手發現"
        updater.bot.sendMessage(chat_id = witness.id, text = text,  parse_mode="MarkdownV2")
    #Send to invests:
    for e in invests:
        text = "你係廢村"
        updater.bot.sendMessage(chat_id = e.id, text = text,  parse_mode="MarkdownV2")
    #Send to group
    updater.bot.sendMessage(chat_id = group_id, text = "兇手行動完畢\n《首次搜證》\n鑑證專家請放置標記")
    #Send to FS
    RM = []
    for index, e in enumerate(purple_list):
        RM.append([InlineKeyboardButton(e, switch_inline_query_current_chat = f"purple_{e}")])
    for arr_index, arr in enumerate(green_list):
        for index, e in enumerate(arr):
            RM[index].append(InlineKeyboardButton(e, switch_inline_query_current_chat = f"green_{arr_index}:{e}"))
    data[group_id]['purgreen_RM'] = RM.copy()
    data[group_id]['purgreen_msg'] = updater.bot.sendMessage(chat_id = group_id, text = "\U0001F7EA死亡原因|\U0001F7E9案發地點", reply_markup = InlineKeyboardMarkup(RM))
    RM = [[]]
    orange_now = random.sample([*orange_list], 4)
    text = "場景圖板"
    for orr_index, orr in enumerate(orange_now):
        RM[0].append(InlineKeyboardButton(orr, switch_inline_query_current_chat = f"{orr}"))
        for index, e in enumerate(orange_list[orr]):
            if orr_index == 0:
                RM.append([InlineKeyboardButton(e, switch_inline_query_current_chat = f"orange_{orr}:{e}")])
            else:
                RM[index + 1].append(InlineKeyboardButton(e, switch_inline_query_current_chat = f"orange_{orr}:{e}"))
    data[group_id]['orange_RM'] = RM.copy()
    data[group_id]['orange_msg'] = updater.bot.sendMessage(chat_id = group_id, text = text, reply_markup = InlineKeyboardMarkup(RM))
    data[group_id]['orange_now'] = orange_now
    data[group_id]['orange_used'] = data[group_id]['orange_used'] + orange_now
    '''
    orange_now = random.sample([*orange_list], 4)
    orange_notused = set(orange_list) - set(orange_now)
    for orr_index, orr in enumerate(orange_now):
        RM = [[],[]]
        for index, e in enumerate(orange_list[orr]):
            RM[index//3].append(InlineKeyboardButton(e, switch_inline_query_current_chat = f"or_{orr}:{e}"))
        data[group_id][f'or{orr_index}_RM'] = RM.copy()
        RM.append(InlineKeyboardButton())
        data[group_id][f'or{orr_index}_msg'] = updater.bot.sendMessage(chat_id = group_id, text = "場景圖板", reply_markup = InlineKeyboardMarkup(RM))
    '''


def inline_query(update: Update, context: CallbackContext):
    player = update.inline_query.from_user
    if player.id not in data:
        return
    group_id = data[player.id][0]
    if data[group_id]['game_status'][1] == 0:
        return
    query = update.inline_query.query
    if data[group_id]['phase'] == 'after_murder':
        if player != data[group_id]['fs']:
            return
        if len(data[group_id]['marked']) >= 6:
            return
        if "purple_" in query:
            temp = query.replace("purple_", "")
            if temp in purple_list:
                re = [InlineQueryResultArticle(id=str(uuid4()), title="確認", input_message_content = InputTextMessageContent(message_text = f"{temp}!!"))
                      ]
                update.inline_query.answer(re)
        elif "green_" in query:
            temp = query.replace("green_", "")
            temp = temp.split(":")
            if not is_num(temp[0]):
                return
            temp[0] = int(temp[0])
            print(temp)
            if temp[1] in green_list[temp[0]]:
                re = [InlineQueryResultArticle(id=str(uuid4()), title = "確認", input_message_content = InputTextMessageContent(message_text = f"{temp[1]}!!"))
                      ]
                update.inline_query.answer(re)
        elif "orange_" in query:
            temp = query.replace("orange_", "")
            temp = temp.split(":")
            if temp[0] not in data[group_id]['orange_now']:
                return
            if temp[1] in orange_list[temp[0]]:
                re = [InlineQueryResultArticle(id=str(uuid4()), title = "確認", input_message_content = InputTextMessageContent(message_text = f"{temp[1]}!!"))
                      ]
                update.inline_query.answer(re)
    elif data[group_id]['phase'] == 'present':
        if data[group_id]['presenting'][1] == player:
            if "發言 " in query:
                temp = query.replace("發言 ", "")
                re = [InlineQueryResultArticle(id=str(uuid4()), title = "送出", input_message_content = InputTextMessageContent(message_text = temp))
                      ]
                update.inline_query.answer(re)
        elif "跳過全部" == query:
            re = [InlineQueryResultArticle(id=str(uuid4()), title = "送出", description = "進入下一回合", input_message_content = InputTextMessageContent(message_text = "唔想傾喇!!"))]
            update.inline_query.answer(re)
        elif "跳過" == query:
            now_player = data[group_id]['presenting'][1]
            print(now_player.first_name)
            re = [InlineQueryResultArticle(id=str(uuid4()), title = "送出", description = "跳過此玩家發言", input_message_content = InputTextMessageContent(message_text = f"跳過{now_player.first_name}!"))]
            update.inline_query.answer(re, cache_time = 1)


def chosen_inline(update, context):
    query = update.chosen_inline_result.query
    player = update.chosen_inline_result.from_user
    if player.id not in data:
        return
    group_id = data[player.id][0]
    if data[group_id]['phase'] == 'after_murder':        
        if player != data[group_id]['fs']:
            return
        if len(data[group_id]['marked']) >= 6:
            return
        if "purple_" in query:
            temp = query.replace("purple_", "")
            if temp in purple_list:
                if 'purple' in data[group_id]['marked_scene']:
                    return
                if temp not in data[group_id]['marked']:
                    data[group_id]['marked'].append(temp)
                    data[group_id]['marked_scene'].append('purple')
                    RM = []
                    for index, e in enumerate(purple_list):
                        ee = e
                        if e in data[group_id]['marked']:
                            ee = f"\U00002757{e}"
                        RM.append([InlineKeyboardButton(ee, switch_inline_query_current_chat = f"purple_{e}")])
                    for arr_index, arr in enumerate(green_list):
                        for index, e in enumerate(arr):
                            ee = e
                            if e in data[group_id]['marked']:
                                ee = f"\U00002757{e}"
                            RM[index].append(InlineKeyboardButton(ee, switch_inline_query_current_chat = f"green_{arr_index}:{e}"))
                    data[group_id]['purgreen_RM'] = RM.copy()
                    updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['purgreen_msg'].message_id)
                    data[group_id]['purgreen_msg'] = updater.bot.sendMessage(chat_id = group_id, text = "\U0001F7EA死亡原因|\U0001F7E9案發地點", reply_markup = InlineKeyboardMarkup(RM))                    
                else:
                    pass                
        elif "green_" in query:
            temp = query.replace("green_", "")
            temp = temp.split(":")
            if not is_num(temp[0]):
                return
            temp[0] = int(temp[0])
            if temp[1] in green_list[temp[0]]:
                if 'green' in data[group_id]['marked_scene']:
                    return
                if temp not in data[group_id]['marked']:
                    data[group_id]['marked'].append(temp[1])
                    data[group_id]['marked_scene'].append('green')
                    RM = []
                    for index, e in enumerate(purple_list):
                        ee = e
                        if e in data[group_id]['marked']:
                            ee = f"\U00002757{e}"
                        RM.append([InlineKeyboardButton(ee, switch_inline_query_current_chat = f"purple_{e}")])
                    for arr_index, arr in enumerate(green_list):
                        for index, e in enumerate(arr):
                            ee = e
                            if e in data[group_id]['marked']:
                                ee = f"\U00002757{e}"
                            RM[index].append(InlineKeyboardButton(ee, switch_inline_query_current_chat = f"green_{arr_index}:{e}"))
                    data[group_id]['purgreen_RM'] = RM.copy()
                    updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['purgreen_msg'].message_id)
                    data[group_id]['purgreen_msg'] = updater.bot.sendMessage(chat_id = group_id, text = "\U0001F7EA死亡原因|\U0001F7E9案發地點", reply_markup = InlineKeyboardMarkup(RM))  
                else:
                    pass
        elif "orange_" in query:
            orange_now = data[group_id]['orange_now']
            temp = query.replace("orange_", "")
            temp = temp.split(":")
            if temp[0] not in orange_now:
                return
            if temp[1] in orange_list[temp[0]]:
                if temp[0] in data[group_id]['marked_scene']:
                    return
                if temp[1] not in data[group_id]['marked']:
                    data[group_id]['marked'].append(temp[1])
                    data[group_id]['marked_scene'].append(temp[0])
                    RM = [[]]
                    text = "場景圖板"
                    for orr_index, orr in enumerate(orange_now):
                        RM[0].append(InlineKeyboardButton(orr, switch_inline_query_current_chat = f"{orr}"))
                        for index, e in enumerate(orange_list[orr]):
                            ee = e
                            if e in data[group_id]['marked']:
                                ee = f"\U00002757{e}"
                            if orr_index == 0:
                                RM.append([InlineKeyboardButton(ee, switch_inline_query_current_chat = f"orange_{orr}:{e}")])
                            else:
                                RM[index + 1].append(InlineKeyboardButton(ee, switch_inline_query_current_chat = f"orange_{orr}:{e}"))
                    data[group_id]['orange_RM'] = RM.copy()
                    #updater.bot.editMessageReplyMarkup(chat_id = group_id, message_id = data[group_id]['orange_msg'].message_id, reply_markup = InlineKeyboardMarkup(RM))
                    updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['orange_msg'].message_id)
                    data[group_id]['orange_msg'] = updater.bot.sendMessage(chat_id = group_id, text = "場景圖版", reply_markup = InlineKeyboardMarkup(RM))
                else:
                    pass
        if len(data[group_id]['marked']) >= 6:
            #text = ", ".join(data[group_id]['marked'])
            updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['purgreen_msg'].message_id)
            updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['orange_msg'].message_id)
            data[group_id]['purgreen_msg'] = updater.bot.sendMessage(chat_id = group_id, text = "\U0001F7EA死亡原因|\U0001F7E9案發地點", reply_markup = InlineKeyboardMarkup(data[group_id]['purgreen_RM']))            
            data[group_id]['orange_msg'] = updater.bot.sendMessage(chat_id = group_id, text = "場景圖版", reply_markup = InlineKeyboardMarkup(data[group_id]['orange_RM']))
            phase_present(group_id)
        print(data[group_id]['marked'])
    elif data[group_id]['phase'] == 'present':
        if data[group_id]['presenting'][1] == player:
            if "發言 " in query:
                players = players_nofs(group_id)
                temp = query.replace("發言 ", "")
                data[group_id]['players'][player.id]['speech'].append(temp)
                updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['present_msg'].message_id)
                if data[group_id]['presenting'][0] >= len(players) - 1:
                    next_round(group_id)
                    return
                data[group_id]['presenting'][0] = data[group_id]['presenting'][0] + 1
                data[group_id]['presenting'][1] = players[data[group_id]['presenting'][0]] 
                name = no_sp(data[group_id]['presenting'][1].first_name)
                RM = [[InlineKeyboardButton("按我發言", switch_inline_query_current_chat = "發言 "), InlineKeyboardButton("跳過", switch_inline_query_current_chat = "跳過")],
                      [InlineKeyboardButton("跳過全部", switch_inline_query_current_chat = "跳過全部")]]
                data[group_id]['present_msg'] = updater.bot.sendMessage(chat_id = group_id, text = f"[{name}](tg://user?id={data[group_id]['presenting'][1].id}) 請發言" , reply_markup = InlineKeyboardMarkup(RM), parse_mode="MarkdownV2")
        if query == "跳過":
            players = players_nofs(group_id)
            now_player = data[group_id]['presenting'][1]
            data[group_id]['players'][now_player.id]['speech'].append("-")
            updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['present_msg'].message_id)
            if data[group_id]['presenting'][0] >= len(players) - 1:
                next_round(group_id)
                return
            data[group_id]['presenting'][0] = data[group_id]['presenting'][0] + 1
            data[group_id]['presenting'][1] = players[data[group_id]['presenting'][0]] 
            name = no_sp(data[group_id]['presenting'][1].first_name)
            RM = [[InlineKeyboardButton("按我發言", switch_inline_query_current_chat = "發言 "), InlineKeyboardButton("跳過", switch_inline_query_current_chat = "跳過")],
                  [InlineKeyboardButton("跳過全部", switch_inline_query_current_chat = "跳過全部")]]
            data[group_id]['present_msg'] = updater.bot.sendMessage(chat_id = group_id, text = f"[{name}](tg://user?id={data[group_id]['presenting'][1].id}) 請發言" , reply_markup = InlineKeyboardMarkup(RM), parse_mode="MarkdownV2")
        elif query == "跳過全部":
            for k, v in data[group_id]['players'].items():
                if k != data[group_id]['fs'].id:                        
                    if len(data[group_id]['players'][k]['speech']) < data[group_id]['round']:
                        data[group_id]['players'][k]['speech'].append("-")
            updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['present_msg'].message_id)
            next_round(group_id)
                
            



            

def phase_present(group_id):    
    t1 = threading.Thread(target = present_start, args = [group_id])
    t1.start()


def present_start(group_id):
    print('discussing', group_id)
    #updater.bot.sendMessage(chat_id = group_id, text = "1秒自由討論後進入輪流發言階段\n可打 /skip 提前結束自由討論")
    data[group_id]['phase'] = 'discuss'
    a = event_obj.wait(1)       
    event_obj.clear()
    data[group_id]['phase'] = 'present'
    fs = data[group_id]['fs']
    players = players_nofs(group_id)
    data[group_id]['presenting'] = [0, players[0]]
    name = no_sp(players[0].first_name)
    RM = [[InlineKeyboardButton("按我發言", switch_inline_query_current_chat = "發言 "), InlineKeyboardButton("跳過", switch_inline_query_current_chat = "跳過")],
          [InlineKeyboardButton("跳過全部", switch_inline_query_current_chat = "跳過全部")]]
    updater.bot.sendMessage(chat_id = group_id, text = "玩家輪流發言\n任何時間可打\"/accuse 證物 手法\"進行指控")
    data[group_id]['present_msg'] = updater.bot.sendMessage(chat_id = group_id, text = f"[{name}](tg://user?id={players[0].id}) 請發言" , reply_markup = InlineKeyboardMarkup(RM), parse_mode="MarkdownV2")


def abc(update, context):
    group_id = update.message.chat.id
    t1 = threading.Thread(target = present_start, args = [group_id])
    t1.start()


def skip(update, context):
    group_id = update.message.chat.id
    if group_id < 0:
        if group_id in data:
            if 'phase' in data[group_id]:
                if data[group_id]['phase'] == 'discuss':                
                    event_obj.set()
    



def next_round(group_id):
    data[group_id]['round'] = data[group_id]['round'] + 1
    if data[group_id]['round'] in [1, 2, 3]:
        fs = data[group_id]['fs']
        name = no_sp(fs.first_name)
        updater.bot.sendMessage(chat_id = group_id, text = f"第{data[group_id]['round']}回合開始, 等待鑑證專家\U0001F9D1\U0000200D\U0001F52C[{name}](tg://user?id={fs.id})行動\.\.\.", parse_mode="MarkdownV2")
        data[group_id]['phase'] = 'new_orr'
        temp_list = list(set([*orange_list]) - set(data[group_id]['orange_used']))
        orange_new = random.sample(temp_list, 1)[0]
        #data[group_id]['new_orr'] = orange_new
        data[group_id]['new_orr'] = None
        RM = []
        text = "請標記新的場景圖板"
        RM.append([InlineKeyboardButton(orange_new, callback_data = f"{orange_new}")])
        for index, e in enumerate(orange_list[orange_new]):
            RM.append([InlineKeyboardButton(e, callback_data = f"new_orr_{orange_new}:{e}")])        
        RM.append([InlineKeyboardButton("確認", callback_data = "new_orr_confirm")])   
        data[group_id]['new_orr_RM'] = RM.copy()
        data[group_id]['new_orr_msg'] = updater.bot.sendMessage(chat_id = data[group_id]['fs'].id, text = text, reply_markup = InlineKeyboardMarkup(RM))
    else:
        data[group_id]['phase'] = 'count_down'
        text = "最後一回合完左喇 倒數100秒 仲未指控既快D啦"        
        updater.bot.sendMessage(chat_id = group_id, text = text)
        game_id = data[group_id]['game_id']
        t1 = threading.Thread(target = count_down, args = [group_id, game_id])
        t1.start()


def count_down(group_id, game_id):
    a = event_obj.wait(100)       
    event_obj.clear()
    if group_id not in data:
        return
    if game_id != data[group_id]['game_id']:
        return
    lose_game(group_id, data[group_id]['fs'])


def next_phase(group_id):
    if data[group_id]['phase'] == 'new_orr':
        data[group_id]['discarding'] = None
        data[group_id]['phase'] = 'discard'
        RM = [[]]
        text = "請選擇要棄掉的場景圖板"
        for orr_index, orr in enumerate(data[group_id]['orange_now']):
            RM[0].append(InlineKeyboardButton(orr, callback_data = f"discard_{orr}"))
            for index, e in enumerate(orange_list[orr]):
                ee = e
                if e in data[group_id]['marked']:
                    ee = f"\U00002757{e}"
                if orr_index == 0:
                    RM.append([InlineKeyboardButton(ee, callback_data = f"{e}")])
                else:
                    RM[index + 1].append(InlineKeyboardButton(ee, callback_data = f"{e}"))            
        RM.append([InlineKeyboardButton("確認", callback_data = "discard_confirm")])
        data[group_id]['discard_RM'] = RM.copy()
        data[group_id]['discard_msg'] = updater.bot.sendMessage(chat_id = data[group_id]['fs'].id, text = text, reply_markup = InlineKeyboardMarkup(RM))
    elif data[group_id]['phase'] == 'discard':        
        data[group_id]['orange_now'].remove(data[group_id]['discarding'])
        data[group_id]['orange_now'].append(data[group_id]['new_orr'][0])
        data[group_id]['orange_used'].append(data[group_id]['new_orr'][0])
        RM = []
        for index, e in enumerate(purple_list):
            ee = e
            if e in data[group_id]['marked']:
                ee = f"\U00002757{e}"
            RM.append([InlineKeyboardButton(ee, callback_data = f"{e}")])
        for arr_index, arr in enumerate(green_list):
            for index, e in enumerate(arr):
                ee = e
                if e in data[group_id]['marked']:
                    ee = f"\U00002757{e}"
                RM[index].append(InlineKeyboardButton(ee, callback_data = f"{e}"))
        data[group_id]['purgreen_RM'] = RM.copy()
        data[group_id]['purgreen_msg'] = updater.bot.sendMessage(chat_id = group_id, text = "\U0001F7EA死亡原因|\U0001F7E9案發地點", reply_markup = InlineKeyboardMarkup(RM))
        RM = [[]]
        text = "場景圖板"
        for orr_index, orr in enumerate(data[group_id]['orange_now']):
            RM[0].append(InlineKeyboardButton(orr, callback_data = f"{orr}"))
            for index, e in enumerate(orange_list[orr]):
                ee = e
                if e in data[group_id]['marked']:
                    ee = f"\U00002757{e}"
                if orr_index == 0:
                    RM.append([InlineKeyboardButton(ee, callback_data = f"{orr}:{e}")])
                else:
                    RM[index + 1].append(InlineKeyboardButton(ee, callback_data = f"{orr}:{e}"))
        data[group_id]['orange_RM'] = RM.copy() 
        data[group_id]['orange_msg'] = updater.bot.sendMessage(chat_id = group_id, text = text, reply_markup = InlineKeyboardMarkup(RM))
        updater.bot.sendMessage(chat_id = group_id, text = f"{data[group_id]['discarding']}已被替換成{data[group_id]['orange_now'][-1]}")
        data[group_id]['phase'] = 'present'
        phase_present(group_id)
    


def list_players(group_id):
    if group_id not in data:
        return
    return data[group_id]['players_list']

def players_nofs(group_id):
    fs = data[group_id]['fs']
    players_list = data[group_id]['players_list']
    return list(set(players_list) - set([fs]))




def no_sp(str):
    sp = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!' ]
    for e in sp:
        str = str.replace(e, f"\{e}")
    return str

def is_num(e):
    try:
        e = int(e)
        return True
    except:
        return False

'''
def unknown_text(update: Update, context: CallbackContext):
    if not update.message:
        return
    group_id = update.message.chat.id
    player = update.message.from_user
    if player.id not in data:
        return
    if data[player.id][0] != group_id:
        return
    if group_id not in data:
        return
    if 'phase' not in data[group_id]:
        return
'''


def killgame(update: Update, context: CallbackContext):
    group_id = update.message.chat.id
    if group_id not in data:
        return
    try:
        updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['new_game_msg_id'])
    except:
        print("message to delete not found")
    updater.bot.sendMessage(chat_id = group_id, text = "遊戲已結束!")
    for e in data[group_id]['players_list']:
        if e.id in data:
            data.pop(e.id)
    data.pop(group_id)

def win_game(group_id, player):
    if group_id not in data:
        return
    try:
        updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['new_game_msg_id'])
    except:
        print("message to delete not found")
    updater.bot.sendMessage(chat_id = group_id, text = f"遊戲結束 {player.first_name}帶領好人搵出真兇!")
    updater.bot.sendMessage(chat_id = group_id, text = data[group_id]['forward'], parse_mode = "MarkdownV2")
    if data[group_id]['witness']:
        updater.bot.sendMessage(chat_id = group_id, text = "兇手一方搵到邊個係目擊者可以反勝")
        history_end(group_id)
    for e in data[group_id]['players_list']:
        if e.id in data:
            data.pop(e.id)
    data.pop(group_id)

def lose_game(group_id, player):
    if group_id not in data:
        return
    try:
        updater.bot.deleteMessage(chat_id = group_id, message_id = data[group_id]['new_game_msg_id'])
    except:
        print("message to delete not found")
    updater.bot.sendMessage(chat_id = group_id, text = "遊戲結束 兇手贏左!")
    updater.bot.sendMessage(chat_id = group_id, text = data[group_id]['forward'], parse_mode = "MarkdownV2")
    for e in data[group_id]['players_list']:
        if e.id in data:
            data.pop(e.id)
    data.pop(group_id)



def hands(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    player = update.message.from_user
    if chat_id < 0:
        if chat_id in data:
            if 'round' in data[chat_id]:
                show_hands(chat_id)
    else:
        if player.id in data:
            group_id = data[player.id][0]
            show_hands(group_id)



def accuse(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    player = update.message.from_user
    if chat_id < 0:
        if chat_id in data:
            if 'round' in data[chat_id]:
                if player == data[chat_id]['fs']:
                    return
                if data[chat_id]['players'][player.id]['guess']:
                    return
                guess = update.message.text.replace("/accuse ", "")
                guess = guess.split(" ")                                
                if len(guess) == 2:
                    guess = [f"\U0001F534{guess[0]}", f"\U0001F535{guess[1]}"]
                    if guess[0] in data[chat_id]['clues'] and guess[1] in data[chat_id]['methods']:
                        data[chat_id]['players'][player.id]['guess'] = guess
                        data[chat_id]['guess_count'] += 1
                        if guess == [data[chat_id]['answer']['clue'], data[chat_id]['answer']['method']]:
                            win_game(chat_id, player)
                            return
                        else:
                            update.message.reply_text("估錯喇sosad")
                        if data[chat_id]['guess_count'] >= len(data[chat_id]['players_list']) - 1:
                            lose_game(chat_id, player)
                            
    
def help(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    updater.bot.sendMessage(chat_id = chat_id, text = "指控打/accuse XX YY\n\U0001F534XX是證物 \U0001F535YY是手法")

def callaccuse(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    player = update.message.from_user
    if chat_id < 0:
        if chat_id in data:
            if 'round' in data[chat_id]:
                text = "未指控既人:\n"
                text2 = ""
                for p in players_nofs(chat_id):
                    name = no_sp(p.first_name)
                    if not data[chat_id]['players'][p.id]['guess']:                        
                        text += f"[{name}](tg://user?id={p.id}), "
                    else:
                        text2 += f"[{name}](tg://user?id={p.id}): {' '.join(data[chat_id]['players'][p.id]['guess'])}"
                text = text[:-2]
                text = f"{text}\n{text2}"
                updater.bot.sendMessage(chat_id = chat_id, text = text, parse_mode="MarkdownV2")


def history(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    if chat_id < 0:
        if chat_id in data:
            if 'round' in data[chat_id]:
                players = players_nofs(chat_id)
                text = "第一回合:\n"
                for player in players:
                    text = f"{text}{player.first_name}\n{get_speech(chat_id, player.id, 1)}\n"
                if data[chat_id]['round'] == 2:
                    text = text + "第二回合:\n"
                    for player in players:
                        text = f"{text}{player.first_name}\n{get_speech(chat_id, player.id, 2)}\n"
                if data[chat_id]['round'] == 3:
                    text = text + "第三回合:\n"
                    for player in players:
                        text = f"{text}{player.first_name}\n{get_speech(chat_id, player.id, 2)}\n"
                text = text[:-1]
                updater.bot.sendMessage(chat_id = chat_id, text = text)#, parse_mode="MarkdownV2")


def history_end(chat_id):
    if chat_id < 0:
        if chat_id in data:
            if 'round' in data[chat_id]:
                players = players_nofs(chat_id)
                text = "第一回合:\n"
                for player in players:
                    text = f"{text}{player.first_name}\n{get_speech(chat_id, player.id, 1)}\n"
                if data[chat_id]['round'] == 2:
                    text = text + "第二回合:\n"
                    for player in players:
                        text = f"{text}{player.first_name}\n{get_speech(chat_id, player.id, 2)}\n"
                if data[chat_id]['round'] == 3:
                    text = text + "第三回合:\n"
                    for player in players:
                        text = f"{text}{player.first_name}\n{get_speech(chat_id, player.id, 2)}\n"
                text = text[:-1]
                updater.bot.sendMessage(chat_id = chat_id, text = text)#, parse_mode="MarkdownV2")     




def get_speech(gid, pid, rd):
    if len(data[gid]['players'][pid]['speech']) >= rd:
        return data[gid]['players'][pid]['speech'][rd-1]
    else:
        return "~"               
                            
                        





updater.dispatcher.add_handler(CommandHandler('skip', skip))
updater.dispatcher.add_handler(CommandHandler('history', history)) 
updater.dispatcher.add_handler(CommandHandler('newgame', newgame))
updater.dispatcher.add_handler(CommandHandler('killgame', killgame))
updater.dispatcher.add_handler(CommandHandler('hands', hands))
updater.dispatcher.add_handler(CommandHandler('accuse', accuse))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('callaccuse', callaccuse))
updater.dispatcher.add_handler(CallbackQueryHandler(handler_join_flee_start, pattern = r'^(join|flee|startgame|hardmode)$'))
updater.dispatcher.add_handler(CallbackQueryHandler(handler_fs, pattern = r'^(fs_confirm|fs_me|fs_random)$'))
updater.dispatcher.add_handler(CallbackQueryHandler(answer)) # 回答問題
updater.dispatcher.add_handler(InlineQueryHandler(inline_query))
updater.dispatcher.add_handler(ChosenInlineResultHandler(chosen_inline))



updater.start_webhook(listen="0.0.0.0",
                          port=8080,
                          url_path=TOKEN,
                      webhook_url='https://ninapaw720.fly.dev/' + TOKEN)

updater.idle()








