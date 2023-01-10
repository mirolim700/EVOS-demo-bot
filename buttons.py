from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

menu = ReplyKeyboardMarkup (
	keyboard = [
		[
		KeyboardButton(text="Buyurtma berish")],
		[
		KeyboardButton(text="Sozlamalar"),
		KeyboardButton(text="Aloqa")
		],
	],
	resize_keyboard=True
)
glavniy_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Lavash 🌯",callback_data="lavash"),
		InlineKeyboardButton(text="Hot-dog 🌭",callback_data="hot-dog")
		],
		[
		InlineKeyboardButton(text="Sandwich 🥪",callback_data="sandwich"),
		InlineKeyboardButton(text="Shaurma 🌮",callback_data="shaurma")
		],
		[
		InlineKeyboardButton(text="Gazaklar 🍟🍟 ",callback_data="gazaklar"),
		InlineKeyboardButton(text="Ichimliklar 🍹🍹",callback_data="ichimliklar")
		],
		[
		InlineKeyboardButton(text="Desertlar 🍰🍰",callback_data="desertlar"),
		InlineKeyboardButton(text="Pizza 🍕",callback_data="pizza")
		],
		[
		InlineKeyboardButton(text="Burger 🍔",callback_data="burger"),
		InlineKeyboardButton(text="Donar 🍱",callback_data="donars")
		],
	]
)
lavash_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Mol go'shtlik 🥩",callback_data="molgo'shtli"),
		InlineKeyboardButton(text="Qalampirli molgo'shtli 🌶🥩",callback_data="qalampirlimol")
		],
		[
		InlineKeyboardButton(text="Tovuqli 🍗",callback_data="tovuqli"),
		InlineKeyboardButton(text="Qalampirli tovuqli 🌶🍗",callback_data="qalampirlitovuq")
		],
		[
		InlineKeyboardButton(text="Fitter 🥬🥙",callback_data="fitter")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga")
		],
	]
)
molgoshtli = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Classic 👍",callback_data="classic"),
		InlineKeyboardButton(text="Mini 👍",callback_data="mini")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga1")
		],

	],
)
clmol_lavash_soni = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="1stcl_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="secondcl_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="thirdcl_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourthcl_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifthcl_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixthcl_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventhcl_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eighthcl_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="ninecl_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga2")]

	]
)
firstcl_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
secondcl_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
thirdcl_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
fourthcl_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
fifthcl_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
sixthcl_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
seventhcl_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
eighthcl_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
ninethcl_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
minimol_lavash = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="firstmin_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="secondmin_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="thirdmin_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourthmin_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifthmin_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixthmin_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventhmin_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eighthmin_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="ninethmin_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga3")]

	]
)
firstmin_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
secondmin_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
thirdmin_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
fourthmin_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
fifthmin_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
sixthmin_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
seventhmin_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
eighthmin_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
ninethmin_mol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="📲 Raqam Qoldiring",callback_data="raqam"),
		InlineKeyboardButton(text="🏠 Manzil Qoldiring",callback_data="manzil")
		],
	]
)
acchiqmolgoshtli = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Classic 👍",callback_data="classic1"),
		InlineKeyboardButton(text="Mini 👍",callback_data="mini1")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga4")
		],

	],
)
classicbitter_lavash = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="1stclbitter_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="2ndclbitter_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="3rdclbitter_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="4thclbitter_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="5thclbitter_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="6thclbitter_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="7thclbitter_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="8thclbitter_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="9thclbitter_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga5")]

	]
)

minibitter_lavash = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga6")]

	]
)
tovuqlilavash = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Classic 👍",callback_data="classic2"),
		InlineKeyboardButton(text="Mini 👍",callback_data="mini2")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga7")
		],

	],
)
clchicken_lavash = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga8")]

	]
)
minichicken_lavash = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga9")]

	]
)
tovuqlibitterlavash = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Classic 👍",callback_data="classic3"),
		InlineKeyboardButton(text="Mini 👍",callback_data="mini3")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga10")
		],
	],
)
cltovuqlibitterlavash = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga11")]

	]
)
minitovuqbitterlavash = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga12")]

	]
)
fitterlavash = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga13")]

	]
)
hotdog_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Hot-dog baget dabl 👍",callback_data="baget_double"),
		InlineKeyboardButton(text="Classic hot-dog 👍",callback_data="classic_hotdog")
		],
		[
		InlineKeyboardButton(text="Korolevskiy 👍",callback_data="korolevskiy"),
		InlineKeyboardButton(text="Tovuqli hot-dog 👍",callback_data="tovuqli_hotdog")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga14")
		],
	]
)
double_baget = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga15")]

	]
)
classic_hotdog = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga16")]

	]
)
korolevskiy = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga17")]

	]
)
tovuqli_hotdog = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga18")]

	]
)
sandwich_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Classic sandwich 👍",callback_data="classic_sandwich"),
		InlineKeyboardButton(text="Tovuqli sandwich 👍",callback_data="tovuqli_sandwich")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga19")
		],
	]
)
classic_sandwich = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga20")]

	]
)
tovuqli_sandwich = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga21")]

	]
)
shaurma_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Molgo'shtli shauma 👍",callback_data="molgoshtli_shaurma"),
		InlineKeyboardButton(text="Molgo'shtli+qalampirli shaurma 👍",callback_data="molgoshtliqalampirli_shaurma")
		],
		[
		InlineKeyboardButton(text="Tovuqli shaurma 👍",callback_data="tovuqli_shaurma"),
		InlineKeyboardButton(text="Tovuqgosjtli+qalampirli shaurma 👍",callback_data="tovuqliqalampirli_shaurma")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga22")
		],
	]
)
molgoshtli_shaurma  = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Classic 👍",callback_data="classic4"),
		InlineKeyboardButton(text="Mini 👍",callback_data="mini4")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga23")
		],
	],
)

clmolgoshtli_shaurma = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga24")]

	]
)
minimolgoshtli_shaurma = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga25")]

	]
)
molgoshtliqalampirli_shaurma  = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Classic 👍",callback_data="classic5"),
		InlineKeyboardButton(text="Mini 👍",callback_data="mini5")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga26")
		],
	],
)

clmolgoshtliqalampirli_shaurma = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga27")]

	]
)
minimolgoshtliqalampirli_shaurma = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga28")]

	]
)
tovuqli_shaurma  = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Classic 👍",callback_data="classic6"),
		InlineKeyboardButton(text="Mini 👍",callback_data="mini6")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga29")
		],
	],
)

cltovuqli_shaurma = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga30")]

	]
)
minitovuqli_shaurma = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga31")]

	]
)
tovuqliqalampirli_shaurma  = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Classic 👍",callback_data="classic6"),
		InlineKeyboardButton(text="Mini 👍",callback_data="mini6")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga32")
		],
	],
)
cltovuqliqalampirli_shaurma = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga33")]

	]
)
minitovuqliqalampirli_shaurma = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga34")]

	]
)
gazaklar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="15gramm fri 👍",callback_data="gram_fri"),
		InlineKeyboardButton(text="Kartoshka derevenskiy 👍",callback_data="derevenskiy_kartoshka")
		],
		[
		InlineKeyboardButton(text="Guruch katta 👍",callback_data="guruch_katta"),
		InlineKeyboardButton(text="Guruch kichik 👍",callback_data="guruch_kichik")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga35")
		],
	]
)
gram_fri = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga36")]

	]
)
derevenskiy_kartoshka = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga37")
		],

	],
)
guruch_katta = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga38")]

	]
)
guruch_kichik = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga39")]

	]
)
ichimliklar_menusi = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Choy va kofe 👍",callback_data="teacofe"),
		InlineKeyboardButton(text="Yaxna ichimliklar 👍",callback_data="yaxnaichimliklar")
		],
		[
		InlineKeyboardButton(text="Fresh va tabiiy soklar 👍",callback_data="fresh_soklar")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga40")
		],
	]
)
tea_cofe  = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Choy 👍",callback_data="choy"),
		InlineKeyboardButton(text="Kofe 👍",callback_data="cofe")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga41")
		],
	],
)
choy = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Qora choy 👍",callback_data="qora_choy"),
		InlineKeyboardButton(text="Kok choy 👍",callback_data="kok_choy")
		],
		[
		InlineKeyboardButton(text="Limon choy 👍",callback_data="limon_choy")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga42")
		],
	],
)
qora_choy = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga43")]

	]
)
kok_choy = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga44")]

	]
)
limon_choy = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga45")]

	]
)
kofe = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Americano 👍",callback_data="americano"),
		InlineKeyboardButton(text="Cappucino 👍",callback_data="cappucino")
		],
		[InlineKeyboardButton(text="Cofe 3v1 👍",callback_data="cofeuchbir"),
		InlineKeyboardButton(text="Latte 👍",callback_data="latte")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga46")
		],
	],
)
americano = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga47")]

	]
)
cofeuchbir = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga48")],

	],
)
cappucino = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga49")],

	],
)
latte = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga50")],

	],
)
yaxna_ichimliklar = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Fanta 👍",callback_data="fanta"),
		InlineKeyboardButton(text="Sprite 👍",callback_data="sprite")],
		[
		InlineKeyboardButton(text="Nestle 👍",callback_data="nestle"),
		InlineKeyboardButton(text="Coca-cola 👍",callback_data="cola")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga51")
		],
	],
)
fanta = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga52")]

	]
)
sprite = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga53")]

	]
)
nestle = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga54")]

	]
)
cola = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga55")]

	]
)
freshsoklar = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Bliss 👍",callback_data="bliss"),
		InlineKeyboardButton(text="Olma va sabzi fresh 👍",callback_data="olmavasabzi_fresh")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga56")
		],
	],
)
bliss = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga57")],

	],
)
olmavasabzi_fresh = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga58")],

	]
)
desertlar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Medovik 'Asalim' 👍",callback_data="medovik_asalim"),
		InlineKeyboardButton(text="Qulupnay 👍",callback_data="qulupnay")
		],
		[
		InlineKeyboardButton(text="Choko 👍",callback_data="choko")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga59")
		]
	]
)
medovik_asalim = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga60")]

	]
)
qulupnay = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga61")]

	]
)
choko = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga62")]

	]
)
pizza_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Peperoni 👍",callback_data="peperoni"),
		InlineKeyboardButton(text="Ananaslik 👍",callback_data="ananaslik")
		],
		[
		InlineKeyboardButton(text="Margarita 👍",callback_data="margarita")
		],
		[
		InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga63")
		],
	]
)
peperoni = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga64")]

	]
)
ananaslik = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga65")]

	]
)
margarita = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga66")]

	]
)
burger_menu = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Gamburger 👍",callback_data="gamburger"),
		InlineKeyboardButton(text="Chizburger 👍",callback_data="chizburger")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga67")
		],
	],
)
gamburger = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga68")]

	]
)
chizburger = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga69")]

	]
)
donar_menu = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="Go'shtli 👍",callback_data="goshtlidonar"),
		InlineKeyboardButton(text="Tovuqli 👍",callback_data="tovuqlidonar")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga70")
		],
	],
)
goshtlidonar = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga71")]

	]
)
tovuqlidonar = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="1️⃣",callback_data="first_mol"),
		InlineKeyboardButton(text="2️⃣",callback_data="second_mol"),
		InlineKeyboardButton(text="3️⃣",callback_data="third_mol")
		],
		[
		InlineKeyboardButton(text="4️⃣",callback_data="fourth_mol"),
		InlineKeyboardButton(text="5️⃣",callback_data="fifth_mol"),
		InlineKeyboardButton(text="6️⃣",callback_data="sixth_mol")
		],
		[
		InlineKeyboardButton(text="7️⃣",callback_data="seventh_mol"),
		InlineKeyboardButton(text="8️⃣",callback_data="eight_mol"),
		InlineKeyboardButton(text="9️⃣",callback_data="nine_mol")
		],
		[InlineKeyboardButton(text="⬅️ Ortga",callback_data="ortga72")]

	]
)
