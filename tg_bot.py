"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from buttons import *
from config import API_TOKEN
# config faylda bot tokeni saqlanadi

from aiogram import Bot, Dispatcher, executor, types



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalamu aleikum",reply_markup=menu)
# main_menu
@dp.message_handler(text="Buyurtma berish")
async def button(message: types.CallbackQuery):
    await message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)
# lavash_menu
@dp.callback_query_handler(text="lavash")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavash_menu.jpg','rb'),
        caption="✅Marxamat lavashlar menusi!!!",reply_markup=lavash_menu)
# ortga
@dp.callback_query_handler(text="ortga")
async def button(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)
# lavashwithmeat
@dp.callback_query_handler(text="molgo'shtli")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=molgoshtli)
# ortga1
@dp.callback_query_handler(text="ortga1")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!",reply_markup=lavash_menu)
# soni_clmol_lavash
@dp.callback_query_handler(text="classic")
async def button(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/cllavashmeat.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=clmol_lavash_soni)   
# clmol1stbutton
@dp.callback_query_handler(text="1stcl_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 1 ta Go'shtlik Classik lavash jo'natiladi.
Narxi 22000  ming.""",reply_markup=firstcl_mol)
# clmol2button
@dp.callback_query_handler(text="secondcl_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 2 ta Go'shtlik Classik lavash jo'natiladi.
Narxi 44000  ming.""",reply_markup=secondcl_mol)
# clmol3button
@dp.callback_query_handler(text="thirdcl_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 3 ta Go'shtlik Classik lavash jo'natiladi.
Narxi 66000  ming.""",reply_markup=fourthcl_mol)
# clmol4stbutton
@dp.callback_query_handler(text="fourthcl_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 4 ta Go'shtlik Classik lavash jo'natiladi.
Narxi 88000  ming.""",reply_markup=fifthcl_mol)
# clmol5button
@dp.callback_query_handler(text="fifthcl_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 5 ta Go'shtlik Classik lavash jo'natiladi.
Narxi 110000  ming.""",reply_markup=sixthcl_mol)
# clmol6button
@dp.callback_query_handler(text="sixthcl_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 6 ta Go'shtlik Classik lavash jo'natiladi.
Narxi 132000  ming.""",reply_markup=seventhcl_mol)
# clmol7button
@dp.callback_query_handler(text="seventhcl_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 7 ta Go'shtlik Classik lavash jo'natiladi.
Narxi 154000  ming.""",reply_markup=eighthcl_mol)
# clmol8button
@dp.callback_query_handler(text="eighthcl_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 8 ta Go'shtlik Classik lavash jo'natiladi.
Narxi 176000  ming.""",reply_markup=ninethcl_mol)
# clmol9button
@dp.callback_query_handler(text="ninethcl_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 9 ta Go'shtlik Classik lavash jo'natiladi.
Narxi 198000  ming.""",reply_markup=firstcl_mol)
# ortga2
@dp.callback_query_handler(text="ortga2")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=molgoshtli)
# minimol_lavash_soni
@dp.callback_query_handler(text="mini")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cllavashmeat.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=minimol_lavash)
# firstminimolbutton
@dp.callback_query_handler(text="firstmin_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 1 ta Go'shtlik lavash jo'natiladi.
Narxi 18000  ming.""",reply_markup=firstmin_mol)
# secondminimolbutton
@dp.callback_query_handler(text="secondmin_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 2 ta Go'shtlik lavash jo'natiladi.
Narxi 36000  ming.""",reply_markup=secondmin_mol)
# thirdminimolbutton
@dp.callback_query_handler(text="thirdmin_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 3 ta Go'shtlik lavash jo'natiladi.
Narxi 54000  ming.""",reply_markup=thirdmin_mol)
# fourthminimolbutton
@dp.callback_query_handler(text="fourthmin_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 4 ta Go'shtlik lavash jo'natiladi.
Narxi 72000  ming.""",reply_markup=fourthmin_mol)
# fifthminimolbutton
@dp.callback_query_handler(text="fifthmin_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 5 ta Go'shtlik lavash jo'natiladi.
Narxi 90000  ming.""",reply_markup=fifthmin_mol)
# sixthminimolbutton
@dp.callback_query_handler(text="sixthmin_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 6 ta Go'shtlik lavash jo'natiladi.
Narxi 108000  ming.""",reply_markup=sixthmin_mol)
# seventhminimolbutton
@dp.callback_query_handler(text="seventhmin_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 7 ta Go'shtlik lavash jo'natiladi.
Narxi 126000  ming.""",reply_markup=seventhmin_mol)
# eghthminimolbutton
@dp.callback_query_handler(text="eighthmin_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 8 ta Go'shtlik lavash jo'natiladi.
Narxi 144000  ming.""",reply_markup=eighthmin_mol)
# ninethminimolbutton
@dp.callback_query_handler(text="ninethmin_mol")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Sizga 9 ta Go'shtlik lavash jo'natiladi.
Narxi 162000  ming.""",reply_markup=ninethmin_mol)
# ortga3
@dp.callback_query_handler(text="ortga3")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=molgoshtli)

# qalampirlimolgoshtli
@dp.callback_query_handler(text="qalampirlimol")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=acchiqmolgoshtli)
# ortga4
@dp.callback_query_handler(text="ortga4")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=lavash_menu)
# classicbittermol_soni
@dp.callback_query_handler(text="classic1")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cllavashbittermeat.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Tarkibi:Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=classicbitter_lavash)   
# ortga5
@dp.callback_query_handler(text="ortga5")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=acchiqmolgoshtli) 
# minibittermol_soni
@dp.callback_query_handler(text="mini1")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cllavashbittermeat.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=minibitter_lavash)   
# ortga6
@dp.callback_query_handler(text="ortga6")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=acchiqmolgoshtli)
# tovuqlilavash
@dp.callback_query_handler(text="tovuqli")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=tovuqlilavash) 
# ortga7
@dp.callback_query_handler(text="ortga7")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!",reply_markup=lavash_menu)
# classic2tovuq_soni
@dp.callback_query_handler(text="classic2")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuqlavash.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=clchicken_lavash) 
# ortga8
@dp.callback_query_handler(text="ortga8")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=tovuqlilavash)
# mini2tovuq_soni
@dp.callback_query_handler(text="mini2")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuqlavash.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=minichicken_lavash)      
# ortga9
@dp.callback_query_handler(text="ortga9")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=tovuqlilavash)
# qalampirlitovuqlavash
@dp.callback_query_handler(text="qalampirlitovuq")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=tovuqlibitterlavash)
# ortga10
@dp.callback_query_handler(text="ortga10")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!",reply_markup=lavash_menu)
# clbittertovuqli_soni
@dp.callback_query_handler(text="classic3")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/bittertovuqlavash.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Tarkibi:Xamir,garimdori tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=cltovuqlibitterlavash) 
# ortga11
@dp.callback_query_handler(text="ortga11")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=tovuqlibitterlavash)
# minibittertovuqli_soni
@dp.callback_query_handler(text="mini3")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/bittertovuqlavash.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=minitovuqlibitterlavash)     
# ortga12
@dp.callback_query_handler(text="ortga12")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=tovuqlibitterlavash)

# fiterlavash_soni
@dp.callback_query_handler(text="fitter")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/fitterlavash.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori go'sht, qarsildoq muztogʼ salati,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=fitterlavash) 
# ortga13
@dp.callback_query_handler(text="ortga13")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!",reply_markup=lavash_menu)
# hot_dog_menu
@dp.callback_query_handler(text="hot-dog")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Hot-Dog menusi!!!",reply_markup=hotdog_menu)
# ortga14
@dp.callback_query_handler(text="ortga14")
async def button(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)
# doublebaget_soni
@dp.callback_query_handler(text="baget_double")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/bagetdabl.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""",reply_markup=double_baget)
# ortga15
@dp.callback_query_handler(text="ortga15")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Hot-Dog menusi!!!",reply_markup=hotdog_menu)
# classic_hot-dog
@dp.callback_query_handler(text="classic_hotdog")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/clhotdog.jpg','rb'),
        caption="""Narxi:8000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""",reply_markup=classic_hotdog)
# ortga16
@dp.callback_query_handler(text="ortga16")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Hot-Dog menusi!!!",reply_markup=hotdog_menu)
# korolevskiy
@dp.callback_query_handler(text="korolevskiy")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/korolevskiy.jpg','rb'),
        caption="""Narxi:15000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""",reply_markup=korolevskiy)
# ortga17
@dp.callback_query_handler(text="ortga17")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Hot-Dog menusi!!!",reply_markup=hotdog_menu)
# tovuqli_hotdog
@dp.callback_query_handler(text="tovuqli_hotdog")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuqhotdog.jpg','rb'),
        caption="""Narxi:17000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""",reply_markup=tovuqli_hotdog)
# ortga18
@dp.callback_query_handler(text="ortga18")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Hot-Dog menusi!!!",reply_markup=hotdog_menu)
# sandwich_menu
@dp.callback_query_handler(text="sandwich")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat sandwich menusi!!!",reply_markup=sandwich_menu)
# ortga19
@dp.callback_query_handler(text="ortga19")
async def button(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)
# classic_sandwich
@dp.callback_query_handler(text="classic_sandwich")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/klabsandwich.jpg','rb'),
        caption="""Narxi:22000 ming so'm 
Tarkibi:✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang""",reply_markup=classic_sandwich)
# ortga20
@dp.callback_query_handler(text="ortga20")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat sandwich menusi!!!",reply_markup=sandwich_menu)
# tovuqli_sandwich
@dp.callback_query_handler(text="tovuqli_sandwich")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/klabsandwich.jpg','rb'),
        caption="""Narxi:22000 ming so'm 
Tarkibi:✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang""",reply_markup=tovuqli_sandwich)
# ortga21
@dp.callback_query_handler(text="ortga21")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat sandwich menusi!!!",reply_markup=sandwich_menu)

# shaurma_menu
@dp.callback_query_handler(text="shaurma")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurma_menu.jpg','rb'),
        caption="✅Marxamat shaurma menusi!!!",reply_markup=shaurma_menu)
# ortga22
@dp.callback_query_handler(text="ortga22")
async def button(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)
# molgoshtli_shaurma
@dp.callback_query_handler(text="molgoshtli_shaurma")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=molgoshtli_shaurma)
# ortga23
@dp.callback_query_handler(text="ortga23")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=shaurma_menu)
# clmolgoshtli_shaurma
@dp.callback_query_handler(text="classic4")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/molgoshtlishaurma.jpg','rb'),
        caption="""Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""",reply_markup=clmolgoshtli_shaurma)
# ortga24
@dp.callback_query_handler(text="ortga24")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=molgoshtli_shaurma)
# minimolgoshtli_shaurma
@dp.callback_query_handler(text="mini4")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/molgoshtlishaurma.jpg','rb'),
        caption="""Narxi:18000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""",reply_markup=minimolgoshtli_shaurma)
# ortga25
@dp.callback_query_handler(text="ortga25")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=molgoshtli_shaurma)

# molgoshtliqalampirli_shaurma
@dp.callback_query_handler(text="molgoshtliqalampirli_shaurma")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=molgoshtliqalampirli_shaurma)
# ortga26
@dp.callback_query_handler(text="ortga26")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=shaurma_menu)
# clmolgoshtliqalampirli_shaurma
@dp.callback_query_handler(text="classic5")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/molgoshtlishaurma.jpg','rb'),
        caption="""Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""",reply_markup=clmolgoshtliqalampirli_shaurma)
# ortga27
@dp.callback_query_handler(text="ortga27")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=molgoshtliqalampirli_shaurma)
# minimolgoshtliqalampirli_shaurma
@dp.callback_query_handler(text="mini5")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/molgoshtlishaurma.jpg','rb'),
        caption="""Narxi:18000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""",reply_markup=minimolgoshtliqalampirli_shaurma)
# ortga28
@dp.callback_query_handler(text="ortga28")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=molgoshtliqalampirli_shaurma)

# tovuqli_shaurma
@dp.callback_query_handler(text="tovuqli_shaurma")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=tovuqli_shaurma)
# ortga29
@dp.callback_query_handler(text="ortga29")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=shaurma_menu)
# cltovuqli_shaurma
@dp.callback_query_handler(text="classic6")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuqlishaurma.jpg','rb'),
        caption="""Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""",reply_markup=cltovuqli_shaurma)
# ortga30
@dp.callback_query_handler(text="ortga30")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=tovuqli_shaurma)
# minitovuqliqalampirli_shaurma
@dp.callback_query_handler(text="mini6")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuqlishaurma.jpg','rb'),
        caption="""Narxi:18000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""",reply_markup=minitovuqli_shaurma)
# ortga31
@dp.callback_query_handler(text="ortga31")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=tovuqli_shaurma)

# tovuqliqalampirli_shaurma
@dp.callback_query_handler(text="tovuqliqalampirli_shaurma")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=tovuqliqalampirli_shaurma)
# ortga32
@dp.callback_query_handler(text="ortga32")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=shaurma_menu)
# cltovuqliqalampirli_shaurma
@dp.callback_query_handler(text="classic7")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuqlishaurma.jpg','rb'),
        caption="""Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""",reply_markup=cltovuqliqalampirli_shaurma)
# ortga33
@dp.callback_query_handler(text="ortga33")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=tovuqliqalampirli_shaurma)
# minitovuqliqalampirli_shaurma
@dp.callback_query_handler(text="mini7")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuqlishaurma.jpg','rb'),
        caption="""Narxi:18000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""",reply_markup=minitovuqliqalampirli_shaurma)
# ortga34
@dp.callback_query_handler(text="ortga34")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat shaurma menusi!!!",reply_markup=tovuqliqalampirli_shaurma)

# gazaklar_menu
@dp.callback_query_handler(text="gazaklar")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat gazaklar menusi!!!",reply_markup=gazaklar_menu)
# ortga35
@dp.callback_query_handler(text="ortga35")
async def button(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)
#gram_fri 
@dp.callback_query_handler(text="gram_fri")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/15gramfri.jpg','rb'),
        caption="""Narxi:6000 ming so'm 
Miqdorini tanlang""",reply_markup=gram_fri)
# ortga36
@dp.callback_query_handler(text="ortga36")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat gazaklar menusi!!!",reply_markup=gazaklar_menu)
#derevenskiy_kartoshka
@dp.callback_query_handler(text="derevenskiy_kartoshka")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/kartoshkader.jpg','rb'),
        caption="""Narxi:6000 ming so'm 
Miqdorini tanlang""",reply_markup=derevenskiy_kartoshka)
# ortga37
@dp.callback_query_handler(text="ortga37")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat gazaklar menusi!!!",reply_markup=gazaklar_menu)
#guruch_katta
@dp.callback_query_handler(text="guruch_katta")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/guruchkatta.jpg','rb'),
        caption="""Narxi:6000 ming so'm 
Miqdorini tanlang""",reply_markup=guruch_katta)
# ortga38
@dp.callback_query_handler(text="ortga38")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat gazaklar menusi!!!",reply_markup=gazaklar_menu)
#guruch_kichik
@dp.callback_query_handler(text="guruch_kichik")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/guruchkatta.jpg','rb'),
        caption="""Narxi:6000 ming so'm 
Miqdorini tanlang""",reply_markup=guruch_kichik)
# ortga38
@dp.callback_query_handler(text="ortga39")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat gazaklar menusi!!!",reply_markup=gazaklar_menu)


# ichimliklar_menu
@dp.callback_query_handler(text="ichimliklar")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat ichimliklar menusi!!!",reply_markup=ichimliklar_menusi)
# ortga40
@dp.callback_query_handler(text="ortga40")
async def button(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)
#tea_cofe
@dp.callback_query_handler(text="teacofe")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=tea_cofe)
# ortga41
@dp.callback_query_handler(text="ortga41")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat ichimliklar menusi!!!",reply_markup=ichimliklar_menusi)

# choy_menu
@dp.callback_query_handler(text="choy")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=choy)
# ortga42
@dp.callback_query_handler(text="ortga42")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=tea_cofe)
# tea_black
@dp.callback_query_handler(text="qora_choy")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/kokchoy.jpg','rb'),
        caption="✅ Qora  choy 3000mig so'm!!!",reply_markup=qora_choy)
# ortga43
@dp.callback_query_handler(text="ortga43")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=choy)
# tea_green
@dp.callback_query_handler(text="kok_choy")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/kokchoy.jpg','rb'),
        caption="✅ Ko'k  choy 3000mig so'm!!!",reply_markup=kok_choy)
# ortga44
@dp.callback_query_handler(text="ortga44")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=choy)
# tea_limon
@dp.callback_query_handler(text="limon_choy")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/limonchoy.jpg','rb'),
        caption="✅Limon choy 5000mig so'm!!!",reply_markup=limon_choy)
# ortga45
@dp.callback_query_handler(text="ortga45")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=choy)

# cofe_menu
@dp.callback_query_handler(text="cofe")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=kofe)
# ortga46
@dp.callback_query_handler(text="ortga46")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=tea_cofe)
# americano
@dp.callback_query_handler(text="americano")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/americano.jpg','rb'),
        caption="""✅Americano narxi 12000!!!!!!""",reply_markup=americano)
# ortga47
@dp.callback_query_handler(text="ortga47")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=kofe)
# 3v1
@dp.callback_query_handler(text="cofeuchbir")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cofe3v1.jpg','rb'),
        caption="""✅Kofe 3 v 1☕️ 3000ming so'm!!!!""",reply_markup=cofeuchbir)
# ortga48
@dp.callback_query_handler(text="ortga48")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=kofe)
# cappucino
@dp.callback_query_handler(text="cappucino")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cappucino.jpg','rb'),
        caption="""✅Cappuccino Narxi 18000!!!!!!""",reply_markup=cappucino)
# ortga49
@dp.callback_query_handler(text="ortga49")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=kofe)
# latte
@dp.callback_query_handler(text="latte")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/latte.jpg','rb'),
        caption="""✅Latte big 120g☕️ 15000mig so'm!!!!""",reply_markup=latte)
# ortga50
@dp.callback_query_handler(text="ortga50")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=kofe)


#yaxna_ichimliklar
@dp.callback_query_handler(text="yaxnaichimliklar")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=yaxna_ichimliklar)
# ortga51
@dp.callback_query_handler(text="ortga51")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat ichimliklar menusi!!!",reply_markup=ichimliklar_menusi)
# fanta
@dp.callback_query_handler(text="fanta")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/fanta.jpg','rb'),
        caption="""✅Fanta 11000 so'm!!!!""",reply_markup=fanta)
# ortga52
@dp.callback_query_handler(text="ortga52")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=yaxna_ichimliklar)
# sprite
@dp.callback_query_handler(text="sprite")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sprite.jpg','rb'),
        caption="""✅Sprite 11000 so'm!!!!""",reply_markup=sprite)
# ortga53
@dp.callback_query_handler(text="ortga53")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=yaxna_ichimliklar)
# nestle
@dp.callback_query_handler(text="nestle")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/nestle.jpg','rb'),
        caption="""✅Nestle 4000 so'm!!!!""",reply_markup=nestle)
# ortga54
@dp.callback_query_handler(text="ortga54")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=yaxna_ichimliklar)
# cola
@dp.callback_query_handler(text="cola")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cola.jpg','rb'),
        caption="""✅Cola 11000 so'm!!!!""",reply_markup=cola)
# ortga55
@dp.callback_query_handler(text="ortga55")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=yaxna_ichimliklar)

# fresh_soklar
@dp.callback_query_handler(text="fresh_soklar")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=freshsoklar)
# ortga56
@dp.callback_query_handler(text="ortga56")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat ichimliklar menusi!!!",reply_markup=ichimliklar_menusi)
# bliss
@dp.callback_query_handler(text="bliss")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/bliss.jpg','rb'),
        caption="""✅Sok Bliss 10000mig so'm!!!""",reply_markup=bliss)
# ortga57
@dp.callback_query_handler(text="ortga57")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=freshsoklar)
# olmavasabzi_fresh
@dp.callback_query_handler(text="olmavasabzi_fresh")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/olmavasabzi.jpg','rb'),
        caption="""✅Fresh sabzi + olma 13000mig so'm!!!""",reply_markup=olmavasabzi_fresh)
# ortga58
@dp.callback_query_handler(text="ortga58")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!!""",reply_markup=freshsoklar)


# desertlar_menu
@dp.callback_query_handler(text="desertlar")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/desertlar_menusi.jpg','rb'),
        caption="✅Marxamat desertlar menusi!!!",reply_markup=desertlar_menu)
# ortga59
@dp.callback_query_handler(text="ortga59")
async def button(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)

# medovik_asalim
@dp.callback_query_handler(text="medovik_asalim")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/asalim.jpg','rb'),
        caption="""Narxi:14000 ming so'm 
✅Аnʼnaviy taʼm - asal asosidagi biskvit va krem
Miqdorini tanlang""",reply_markup=medovik_asalim)
# ortga60
@dp.callback_query_handler(text="ortga60")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Marxamat desertlar menusi!!!""",reply_markup=desertlar_menu)
# qulupnay
@dp.callback_query_handler(text="qulupnay")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qulupnaymuss.jpg','rb'),
        caption="""Narxi:14000 ming so'm 
✅Qulupnayli Muss.
Miqdorini tanlang""",reply_markup=qulupnay)
# ortga61
@dp.callback_query_handler(text="ortga61")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Marxamat desertlar menusi!!!""",reply_markup=desertlar_menu)
# choko
@dp.callback_query_handler(text="choko")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/choko.jpg','rb'),
        caption="""Narxi:14000 ming so'm 
✅Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem.
Miqdorini tanlang""",reply_markup=choko)
# ortga62
@dp.callback_query_handler(text="ortga62")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Marxamat desertlar menusi!!!""",reply_markup=desertlar_menu)

# pizza_menu
@dp.callback_query_handler(text="pizza")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat burger menusi!!!",reply_markup=pizza_menu)
# ortga63
@dp.callback_query_handler(text="ortga63")
async def button(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)
# peperoni
@dp.callback_query_handler(text="peperoni")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/peperoni.jpg','rb'),
        caption="""Narxi:65000 ming so'm 
✅Пицца Пепперони
Пицца Пепперони     33см.
Соус Томатный Для Пиццы
Тонкое тесто.
Сыр 110 гр.
Miqdorini tanlang""",reply_markup=peperoni)
# ortga64
@dp.callback_query_handler(text="ortga64")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Marxamat pizza menusi!!!""",reply_markup=pizza_menu)
# ananaslik
@dp.callback_query_handler(text="ananaslik")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ananasli.jpg','rb'),
        caption="""Narxi:65000 ming so'm 
✅Пицца с Ананасом.
Пицца с Колбасой     33см.
Соус Томатный Для Пиццы
3 вида колбас 130гр.
Тонкое тесто
Кукуруза
Сыр 100гр.
ГрибыMiqdorini tanlang""",reply_markup=ananaslik)
# ortga65
@dp.callback_query_handler(text="ortga65")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Marxamat pizza menusi!!!""",reply_markup=pizza_menu)
# margarita
@dp.callback_query_handler(text="margarita")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/margarita.jpg','rb'),
        caption="""Narxi:65000 ming so'm 
✅Пицца Маргарита
Пицца Маргарита  33см.
Соус Томатный Для Пиццы 
Тонкое тесто 
Сыр 100гр.
Помидоры
Miqdorini tanlang""",reply_markup=margarita)
# ortga66
@dp.callback_query_handler(text="ortga66")
async def button(call: types.CallbackQuery):
    await call.message.answer("""✅Marxamat pizza menusi!!!""",reply_markup=pizza_menu)

# burger_menu
@dp.callback_query_handler(text="burger")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat burger menusi!!!",reply_markup=burger_menu)
# ortga67
@dp.callback_query_handler(text="ortga67")
async def button(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)
# gamburger
@dp.callback_query_handler(text="gamburger")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/gamburger.jpg','rb'),
        caption="""Narxi:22000 ming so'm 
Miqdorini tanlang""",reply_markup=gamburger)
# ortga68
@dp.callback_query_handler(text="ortga68")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat burger menusi!!!",reply_markup=burger_menu)
# chizburger
@dp.callback_query_handler(text="chizburger")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/chizburger.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Miqdorini tanlang""",reply_markup=chizburger)
# ortga69
@dp.callback_query_handler(text="ortga69")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat burger menusi!!!",reply_markup=burger_menu)

# donar_menu
@dp.callback_query_handler(text="donars")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat donar menusi!!!",reply_markup=donar_menu)
# ortga70
@dp.callback_query_handler(text="ortga70")
async def button(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=glavniy_menu)
# goshtlidonar
@dp.callback_query_handler(text="goshtlidonar")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/goshtlidonar.jpg','rb'),
        caption="""Narxi:23000 ming so'm 
Miqdorini tanlang""",reply_markup=goshtlidonar)
# ortga71
@dp.callback_query_handler(text="ortga71")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat donar menusi!!!",reply_markup=donar_menu)
# tovuqlidonar
@dp.callback_query_handler(text="tovuqlidonar")
async def button(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuqlidonar.jpg','rb'),
        caption="""Narxi:23000 ming so'm 
Miqdorini tanlang""",reply_markup=tovuqlidonar)
# ortga72
@dp.callback_query_handler(text="ortga72")
async def button(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat donar menusi!!!",reply_markup=donar_menu)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)