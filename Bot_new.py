from vk_api.longpoll import VkLongPoll , VkEventType
from threading import Thread
import vk_api , random , time , os

mytokenvk = '0c0151147883a61fcc4cf73fd9255c0d53045071fb0697f8995c14294abfb1add34f73f7dd754112452bd'
vk_session= vk_api.VkApi(token=mytokenvk)
longpull= VkLongPoll(vk_session)
vk=vk_session.get_api()

def answer():
	while True:
			for event in longpull.listen():
				if event.type == VkEventType.MESSAGE_NEW:
					if event.to_me:
						q=str(event.text)
						print(q)
						if 'отправьте' in q:
							mask1=q.split(" «",1)[-1]
							print(mask1)
							mask2=(str(mask1)).split("»",1)[0]
							print(mask2)
							vk.messages.send(
         	                 	  # chat_id= event.chat_id,
                       	   	  chat_id=48,
                	         	   message=mask2.lower(),
           	            	     random_id=random.randint(0, 10000000000000000)
                     	   )
						if 'поиграйте' in q:
							vk.messages.send(
	                         	   # chat_id= event.chat_id,
	                      	      chat_id=48,
	                      	      message='питомец поиграть',
	                     	       random_id=random.randint(0, 10000000000000000)
	                    	   )
						if 'покормите' in q:
	 						vk.messages.send(
	                  	          # chat_id= event.chat_id,
	            	                chat_id=48,
	                       	     message='питомец покормить',
	                      	      random_id=random.randint(0, 10000000000000000)
	                 	       )	             
						else:
							pass
			else:
				pass			
			
			
def gorilla_kopat():
    while True:
        for _ in range(5):
        	time.sleep(310)
        	vk.messages.send(
	                  	          # chat_id= event.chat_id,
	            	                chat_id=48,
	                       	     message='копать алмазы',
	                      	      random_id=random.randint(0, 10000000000000000)
	                 	       )
	                 	       	             
            

def gorilla_pitomec():
	while True:
           vk.messages.send(
                chat_id=48,
                message="питомец поход",
                random_id=random.randint(0, 10000000000000000)
            )
           time.sleep(3700)
        
            
def main():
	answervar=Thread(target=answer)
	kopat=Thread(target=gorilla_kopat)
	pitomec=Thread(target=gorilla_pitomec)
	гanswervar.start()
	kopat.start()
	pitomec.start()
	

if __name__ == '__main__':
    main()      			
