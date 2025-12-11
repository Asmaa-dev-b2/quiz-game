import pygame
import sys

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (160, 100, 255)
DARK_PURPLE = (120, 70, 220)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GREY = (220, 220, 220)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Game")

question_font = pygame.font.SysFont("arial", 28, bold=True)
option_font = pygame.font.SysFont("arial", 24)
score_font = pygame.font.SysFont("arial", 34, bold=True)
title_font = pygame.font.SysFont("arial", 40, bold=True)

quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) Rome", "C) Madrid", "D) London"],
        "correct": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
        "correct": "C"
    },
    {
        "question": "What is 9 x 6?",
        "options": ["A) 42", "B) 54", "C) 36", "D) 64"],
        "correct": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Dickens", "B) Shakespeare", "C) Hugo", "D) Poe"],
        "correct": "B"
    },
    {
        "question": "Which animal lays eggs?",
        "options": ["A) Cat", "B) Dog", "C) Snake", "D) Horse"],
        "correct": "C"
    },
    {
        "question": "What is the chemical symbol for Water?",
        "options": ["A) H2O", "B) O2", "C) CO2", "D) HO"],
        "correct": "A"
    },
    {
        "question": "Which continent is the largest?",
        "options": ["A) Africa", "B) Asia", "C) Europe", "D) Antarctica"],
        "correct": "B"
    },
    {
        "question": "How many days are in a leap year?",
        "options": ["A) 364", "B) 365", "C) 366", "D) 367"],
        "correct": "C"
    },
    {
        "question": "Which gas do plants absorb?",
        "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Helium", "D) Hydrogen"],
        "correct": "B"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["A) Atlantic", "B) Arctic", "C) Indian", "D) Pacific"],
        "correct": "D"
    }
]

current_question = 0
score = 0
selected = None
show_result = False


def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def draw_option(text, rect, is_selected):
    color = DARK_PURPLE if is_selected else PURPLE
    pygame.draw.rect(screen, color, rect, border_radius=10)
    draw_text(text, option_font, WHITE, rect.x + 10, rect.y + 10)


running = True
while running:
    screen.fill((245, 230, 255)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not show_result:
            mx, my = pygame.mouse.get_pos()
            for i, rect in enumerate(option_rects):
                if rect.collidepoint(mx, my):
                    selected = "ABCD"[i]
                    if selected == quiz[current_question]["correct"]:
                        score += 1
                    current_question += 1
                    selected = None
                    if current_question >= len(quiz):
                        show_result = True

    if not show_result:
        q = quiz[current_question]
        draw_text(f"Question {current_question + 1}/10", title_font, DARK_PURPLE, 20, 20)
        draw_text(q["question"], question_font, BLACK, 20, 100)

        option_rects = []
        y_start = 200
        for i, opt in enumerate(q["options"]):
            rect = pygame.Rect(50, y_start + i * 70, 700, 50)
            option_rects.append(rect)
            draw_option(opt, rect, False)
    else:
        draw_text("Quiz Completed!", title_font, DARK_PURPLE, 260, 100)
        draw_text(f"Your Score: {score} / 10", score_font, BLACK, 330, 250)

        if score == 10:
            draw_text("🌟 Perfect! Amazing!", score_font, GREEN, 250, 340)
        elif score >= 7:
            draw_text("👍 Great Job!", score_font, GREEN, 300, 340)
        else:
            draw_text("📘 Keep practicing!", score_font, RED, 270, 340)

    pygame.display.update()

pygame.quit()
sys.exit()
