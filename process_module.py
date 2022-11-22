from output_module import output
from time_module import get_time
from database import get_answer_from_memory, insert_questions_and_answers
from input_module import take_input

def process(query):

    answer = get_answer_from_memory(query)
    
    if answer == "saati getiriyorum":

        return("Saat " + get_time())
    else:
        output("Ne demek istediğini bilmiyorum, bana öğretmek ister misin?")
        ans = take_input()
        if "anlamı" in ans:
            ans = ans.replace("analmı", "")
            ans = ans.strip()

            value = get_answer_from_memory(ans)
            if value == "":
                return "Bu konuda yardımcı olamam!"
            else:
                insert_questions_and_answers(query, value) 
                return "Bunu öğrettiğin için teşekkür ederim dostum :D"
                
        return "hata!"