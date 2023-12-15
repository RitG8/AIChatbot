import pygame
import chatbot
import os

pygame.init()
colors = {"fire engine red": "#db162f", "space cadet":"#1F2041", "english violet":"#4B3F72", "bright pink":"#FB6376", "melon":"#FCB1A6", "pale dogwood":"#FFDCCC",
          "viridian":"#53917E", "fire brick": "#AD2E24", "castleton green": "#226752", "african violet": "#9C89B8"}


def run_chatbot():
    screen = pygame.display.set_mode([500, 500])
    running = True

    base_font = pygame.font.Font(None, 32) 
    user_text = ''
    text_box_clicked = False
    response = "Hello. How may I help you today?"
    spoke = False
    mac = False
    pig_latin = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if input_box.collidepoint(event.pos): 
                    text_box_clicked = True
                elif train_box.collidepoint(event.pos):
                    train()
                elif pig_latin_box.collidepoint(event.pos):
                    pig_latin = not pig_latin
                else: 
                    text_box_clicked = False
    
            if event.type == pygame.KEYDOWN: 
                if text_box_clicked:
                    if event.key == pygame.K_BACKSPACE: 
                        # get text input from 0 to -1, excluding last character
                        user_text = user_text[:-1] 
                    elif event.key == pygame.K_RETURN:
                        response = chatbot.response(user_text)
                        if pig_latin:
                            response = chatbot.pig_latin(response)
                        user_text = ""
                        spoke = True
                    else: 
                        user_text += event.unicode
            
            
        screen.fill(colors["space cadet"])
        input_box = pygame.Rect(50, 250, 400, 200)

        if text_box_clicked:
            pygame.draw.rect(screen, colors["bright pink"], input_box)
        else:
            pygame.draw.rect(screen, colors["pale dogwood"], input_box)

        train_box = pygame.Rect(10, 10, 70, 30)
        pygame.draw.rect(screen, colors["melon"], train_box)
        text_train = base_font.render("Train!", True, colors["english violet"]) 
        screen.blit(text_train, (train_box.x+5, train_box.y + 5))

        #splits user text into lines of 35 characters each_text_arr = 
        user_text_arr = format_text(user_text)

        #renders user text
        start_y = 5
        for line in user_text_arr:
            text_surface = base_font.render(line, True, (255, 255, 255)) 
            # render at position stated in arguments 
            screen.blit(text_surface, (input_box.x+5, input_box.y+start_y))
            start_y += 18 

        #splits response text into lines of 35 characters each
        response_arr = format_text(response)

        #renders response text
        start_y_bot_offset = 40
        for line in response_arr:
            text_surface_bot = base_font.render(line, True, colors["fire brick"]) 
            # render at position stated in arguments 
            screen.blit(text_surface_bot, (25, 20+start_y_bot_offset))
            start_y_bot_offset += 18 

        if spoke and mac:
            out = "say "
            for char in response:
                if char.isalpha() or char.isspace():
                    out += char
            os.system(out)
            spoke = False
        
        pig_latin_box = pygame.Rect(200, 10, 172, 30)
        if pig_latin:
            pygame.draw.rect(screen, colors["african violet"], pig_latin_box)
            text_train = base_font.render("Pig Latin Mode!", True, colors["castleton green"]) 
        else:
            pygame.draw.rect(screen, colors["english violet"], pig_latin_box)
            text_train = base_font.render("Pig Latin Mode!", True, colors["castleton green"]) 

        screen.blit(text_train, (pig_latin_box.x+5, pig_latin_box.y + 5))
    
        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()

#def q_and_a_mode():

def train():

    screen = pygame.display.set_mode([500, 500])
    running = True

    base_font = pygame.font.Font(None, 32) 
    user_text = ''
    user_arr = []
    text_box_clicked = False
    question_entered = False
    instructions = "Enter a question."

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if input_box.collidepoint(event.pos): 
                    text_box_clicked = True
                elif train_box.collidepoint(event.pos):
                    run_chatbot()
                else: 
                    text_box_clicked = False
    
            if event.type == pygame.KEYDOWN: 
                if text_box_clicked:
                    if event.key == pygame.K_BACKSPACE: 
                        # get text input from 0 to -1, excluding last character
                        user_text = user_text[:-1] 
                    elif event.key == pygame.K_RETURN:
                        if user_text == "-1":
                            question_entered = False
                            chatbot.add_to_csv(user_arr)
                            user_arr = []
                        else:
                            user_arr += [user_text]
                            if not question_entered:
                                #if a question was just entered
                                question_entered = True
                        
                        if question_entered:
                            instructions = "Enter answer, or -1 to save your answers and ask a new question."
                        else:
                            instructions = "Enter a question."
                        user_text = ""
                    else: 
                        user_text += event.unicode

        screen.fill(colors["space cadet"])
        input_box = pygame.Rect(50, 250, 400, 200)
        if text_box_clicked:
            pygame.draw.rect(screen, colors["viridian"], input_box)
        else:
            pygame.draw.rect(screen, colors["castleton green"], input_box)

        train_box = pygame.Rect(10, 10, 70, 30)
        pygame.draw.rect(screen, colors["melon"], train_box)
        text_train = base_font.render("Chat!", True, colors["english violet"]) 
        screen.blit(text_train, (train_box.x+5, train_box.y + 5))

        #splits user text into lines of 30 characters each
        user_text_arr = format_text(user_text)

        start_y = 5
        for line in user_text_arr:
            text_surface = base_font.render(line, True, (255, 255, 255)) 
        
            # render at position stated in arguments 
            screen.blit(text_surface, (input_box.x+5, input_box.y+start_y))
            start_y += 18 

        start_y_bot_offset = 40
        instruction_arr = format_text(instructions)

        start_y_bot_offset = 40
        for line in instruction_arr:
            text_surface_bot = base_font.render(line, True, colors["fire brick"]) 
            # render at position stated in arguments 
            screen.blit(text_surface_bot, (25, 20+start_y_bot_offset))
            start_y_bot_offset += 18 


        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()

#returns a list of strings where each character is 35 characters long
def format_text(text):
    text = text.split(" ")
    res = [""]

    for string in text:
        if len(res[-1]) + len(string) + 1 < 35:
            res[-1] += (string + " ")
        else:
            res += [string + " "]
    
    return res

run_chatbot()