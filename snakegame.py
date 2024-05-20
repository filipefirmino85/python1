import pygame # importar biblioteca pygame
import random # importar biblioteca para a aleatoriedade de onde aparecerá a comida 

pygame.init()
pygame.display.set_caption("Snake Game in Python") #nomear jogo
largura, altura = 1200, 800 # tamanho da tela
tela = pygame.display.set_mode((largura, altura)) #executar o comando de tamanho da tela
relogio = pygame.time.Clock() #usado na variavel velocidade_snake

# cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0,0,255)
branco = (255,255,255)


# parametros da snake
tamanho_quadrado = 20
velocidade_jogo = 13

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado) # a posição começa em zero e vai até a lagura total da tela, e está sendo subtraída pelo tamanho do quadrado para que ela possa aparecer com o seu quadrado completo na tela. Ele é dividido por 20 (tamanho do snake), arredondado e multiplicado pelo tamanho para garantir que a snake esteja na mesma linha da comida
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho, tamanho]) #pixel 0 é a posição x onde fiará a snake e 1 é a posição y


def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, azul)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:   #deslocou para baixo ao clicar (Key Dow)
        velocidade_x = 0    # não move no eixo x
        velocidade_y = tamanho_quadrado #deslocamento em eixo y
    elif tecla == pygame.K_UP: # deslocou para cima
        velocidade_x = 0 # não move no eixo x
        velocidade_y = -tamanho_quadrado #deslocou para cima é -1 tamanho
    elif tecla == pygame.K_RIGHT: # desloca o corpo para a direita
        velocidade_x = tamanho_quadrado # moveu o corpo por um tamanho
        velocidade_y = 0 # eixo y não move
    elif tecla == pygame.K_LEFT: # deslocamento esquerda
        velocidade_x = -tamanho_quadrado #desloca um tamanho a menos para a esquerda
        velocidade_y = 0  # eixo y não move
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False #criação do gameover

    x = largura / 2 #posição inicial da snake
    y = altura / 2 #posição inicial da snake

    velocidade_x = 0 # é zero porque a snake começa parada tanto no eixo x como no y 
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = [] # Lista vazia

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN: #Keydown faz movimentar a cobrinha dando comando no teclado
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # desenhar_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar a posicao da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:  #se a snake bater nas extremidades da tela é fim de jogo
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        # desenhar_cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra: # a snake anda uma casa e deleta a primeira posição (posição zero)
            del pixels[0]

        # se a cobrinha bateu no proprio corpo é fim de jogo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)

        # desenhar_pontos
        desenhar_pontuacao(tamanho_cobra - 1)

        # atualizacao da tela
        pygame.display.update()

        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)


rodar_jogo()


# Observação: não foi criada regra para quando a cobra está sobre um eixo e quer voltar por ele mesmo, ou seja, caso isso seja executado é considerado que a snake bateu no próprio corpo e é fim de jogo