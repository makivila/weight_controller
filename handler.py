from telebot import types


class Handler:
    def __init__(self, bot, servises):
        self.bot = bot  
        self.servises = servises

    def run(self):
        @self.bot.message_handler(commands=["start"])
        def start(message, res=False):
            self.init_start_handler(message)
        @self.bot.message_handler(content_types=["text"])
        def text(message):
            self.init_text_handler(message)
        self.bot.polling(none_stop=True, interval=0)
            

    def init_text_handler(self, message):
        compare_answer = "Before you weighted: {}, now {}, difference {}"
        try:
            if message.text == "Compare with last week": 
                weight_result = self.servises.compare(message.chat.id, "WEEK") 
                answer = compare_answer.format(weight_result.last_weight, weight_result.current_weight, weight_result.difference)               
            elif message.text == "Compare with last month":
                weight_result = self.servises.compare(message.chat.id, "MONTH")
                answer = compare_answer.format(weight_result.last_weight, weight_result.current_weight, weight_result.difference)
            else: 
                self.servises.add_weight(message.chat.id, message.text.strip())
                answer = f"Added today weight: {message.text.strip()}"
        except Exception as e:
            answer = str(e)   
        
        self.bot.send_message(message.chat.id, answer)
        
    def init_start_handler(self, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Compare with last week")
        btn2 = types.KeyboardButton("Compare with last month")
        markup.add(btn1, btn2)
        self.bot.send_message(message.chat.id, text="Hello, friend. Its your weight controller. Welcome!", reply_markup=markup)
            



            
            