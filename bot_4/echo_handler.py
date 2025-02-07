from aiogram.types import Message

import whorehouse.wb as wb
import utils.wb_analiz as wb_analiz
import utils.ghost as ghost
import utils.citation as citation

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        begin = message.text.upper().find('WB')
        help = message.text.upper().find('HELP')
        ost = message.text.upper().find('OST')
        game = message.text.upper().find('GAME')
        cit = message.text.upper().find('CIT')
        if ghost.isStarted():
            if not is_number(message.text): return ghost.end()                    
            else: return await message.answer(ghost.ask(int(message.text)))
        if game>-1: return await message.answer(ghost.start())

        if begin>-1:
            ans = wb.getWB()        
            await message.answer(ans)
        elif cit>-1:
            await message.answer(citation.nextCitation())
        elif help>-1:
            await message.answer(f"wb - склады\n ost- Остатки\n ost463- Остатки по артикулу")
        elif ost>-1:
            articulText = message.text[3:]
            if articulText == '0':
                 print (' 84848448 СОЗДАВАТЬ БУДЕТ')
                 wb_analiz.getAnaliz('0')
                 await message.answer('Создан новый файл аналитики') 

            elif not articulText:
                await message.answer(
                        text='Выбери или пиши ost463',
                        reply_markup=keyboard
                )
           
            
            else:
                ans = wb_analiz.getAnaliz(articulText)
                await message.answer(ans) 
                


                   
        else: await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
