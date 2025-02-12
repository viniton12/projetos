#jogo de rpg
#cada pessoa escolhe uma classe com determinadas caracteristica já estabelecida

#definindo as classes de personagens:
classe0 = 0 
classe1 = 'Mago'
classe2 = 'Druida'
classe3 = 'Guerreiro'
classe4 = 'Assassino'
classe5 = 'Monge'

# descrevendo cada classe 
descricao_mago = """
🧙‍♂️ CLASSE: MAGO

O Mago é um mestre das artes arcanas, capaz de lançar feitiços poderosos. 
Embora tenha baixa defesa física, compensa com ataques mágicos devastadores.

📜 Características:
- Vida: 2000 pts
- Mana: 1000
- Ataque Físico: 80
- Ataque Mágico: 820
- Defesa Física: 130
- Defesa Mágica: 500
- Velocidade: 500

🪄 Habilidades:
🔥 Bola de Fogo – Lança uma esfera flamejante.
⚡ Raio Arcano – Dispara uma rajada de energia mágica.
🛡️ Escudo Místico – Reduz dano recebido.
❄️ Explosão de Gelo – Congela o inimigo.
✨ Teleporte – Move-se instantaneamente no campo de batalha.

✅ Forte contra: Guerreiros de ataque físico.
❌ Fraco contra: Ladinos e Arqueiros.

"""

descricao_druida = """
 🌿 Classe: Druida
O Druida é um guardião da natureza, conectando-se aos espíritos da floresta para manipular forças elementares. 
Versátil, pode alternar entre papéis de suporte, ataque e resistência, tornando-se um combatente adaptável.

📜 Características:
Vida: Média
Mana: Alta
Ataque físico: Médio
Ataque mágico: Alto
Defesa física: Média
Defesa mágica: Alta
Velocidade: Média
🌱 Habilidades Principais:
Raízes Espinhosas 🌿 – Prende o inimigo com vinhas, causando dano e reduzindo sua velocidade.
Chuva Revitalizante 💧 – Cura aliados ao longo do tempo.
Forma Bestial 🐺 – Transforma-se em uma fera, aumentando o ataque físico e a velocidade.
Explosão Solar ☀️ – Dispara uma rajada de luz que causa dano mágico e cega o oponente temporariamente.
Pele de Carvalho 🌳 – Aumenta sua defesa física e resistência a ataques por alguns turnos.
🎭 Estilo de Jogo:
O Druida se adapta conforme a situação, podendo ser curandeiro, atacante ou defensor.
Suas habilidades de suporte tornam-no essencial em grupos.
Em forma bestial, pode se tornar um combatente ágil e feroz.
✅ Fraquezas & Resistências:
✅ Forte contra: Magos e Necromantes (por resistir a feitiços e se curar).
❌ Fraco contra: Guerreiros e Bárbaros (que podem romper sua defesa rapidamente).
"""

descricao_guerreiro = """
 ⚔️ Classe: Guerreiro
O Guerreiro é um combatente resistente e mestre no uso de armas pesadas. 
Ele confia na força bruta e resistência para enfrentar inimigos de frente.

📜 Características:
Vida: Alta
Mana: Baixa
Ataque físico: Alto
Ataque mágico: Baixo
Defesa física: Alta
Defesa mágica: Média
Velocidade: Média
🪄 Habilidades:
Golpe Poderoso 💥 – Ataque devastador que causa grande dano físico.
Investida 🏃‍♂️ – Corre até o inimigo e desfere um golpe com mais força.
Resistência de Ferro 🛡️ – Aumenta a defesa física por um tempo.
Grito de Guerra 📢 – Aumenta o ataque dos aliados próximos.
Esmagamento Terrestre 🌍 – Golpeia o chão, atordoando inimigos ao redor.
✅ Forte contra: Inimigos frágeis fisicamente, como Magos e Druidas.
❌ Fraco contra: Personagens ágeis, como Assassinos e Arqueiros
"""
descricao_assassino = """ 
🗡️ Classe: Assassino
O Assassino é um lutador ágil e letal, especializado em ataques rápidos e furtivos. Ele elimina alvos antes que possam reagir.

📜 Características:
Vida: Baixa
Mana: Média
Ataque físico: Muito Alto
Ataque mágico: Baixo
Defesa física: Baixa
Defesa mágica: Média
Velocidade: Muito Alta
🪄 Habilidades:
Golpe Sombrio 🖤 – Ataque veloz que ignora parte da defesa do inimigo.
Passo Fantasma 👣 – Torna-se invisível por alguns segundos.
Lâmina Envenenada ☠️ – Ataques aplicam veneno, causando dano contínuo.
Dança das Sombras 🌑 – Executa múltiplos golpes rápidos em um inimigo.
Execução Fatal ⚔️ – Se o alvo tiver pouca vida, finaliza instantaneamente.
✅ Forte contra: Magos e arqueiros, que têm pouca defesa.
❌ Fraco contra: Guerreiros e Monges, que podem resistir a seus golpes.
"""
descricao_monge = """ 
🥋 Classe: Monge
O Monge é um mestre das artes marciais, combinando força física com disciplina espiritual.
Ele luta sem armas ou com cajados, focando em combos e equilíbrio.

📜 Características:
Vida: Média
Mana: Média
Ataque físico: Médio
Ataque mágico: Médio
Defesa física: Média
Defesa mágica: Alta
Velocidade: Alta
🪄 Habilidades:
Golpe do Dragão 🐉 – Um chute poderoso que derruba o inimigo.
Meditação 🧘 – Regenera parte da vida e da mana.
Ataque em Combo 👊 – Sequência de socos rápidos que aumentam de dano a cada golpe.
Palma Explosiva 💥 – Concentra energia em um único ataque destrutivo.
Campo de Ki 🔥 – Aumenta sua defesa e velocidade temporariamente.
✅ Forte contra: Assassinos e Ladinos, por sua velocidade e resistência.
❌ Fraco contra: Magos e Necromantes, que atacam à distância.
"""

#escolhendo as classes dos personagens
print('Bem vindo ao D&D')
print('Para começar escolha uma classe:\n Mago\n Druida\n Guerreiro\n Assassino\n Monge')

for personagem in range(1, 3):
    escolha = str(input('Digite sua classe:')).capitalize()
    nome = str(input('Digite seu nome:')).capitalize()
    idade = int(input('Digite sua idade:'))
    especie = str(input('Digite sua especie:')).capitalize()

    if escolha == classe1:
        print(f'Seu nome é {nome}.\n Você tem {idade} anos.\n Sua espécie é {especie}.\n Sua  classe é {escolha}.')
        print(f'descrição da sua classe {descricao_mago}')
    elif escolha == classe2:
        print(f'Seu nome é {nome}.\n Você tem {idade} anos.\n Sua espécie é {especie}.\n Sua  classe é {escolha}.')
        print(f'descrição da sua classe {descricao_druida}')
    elif escolha == classe3:
        print(f'Seu nome é {nome}.\n Você tem {idade} anos.\n Sua espécie é {especie}.\n Sua  classe é {escolha}.')
        print(f'descrição da sua classe{descricao_guerreiro}')
    elif escolha == classe4:
        print(f'Seu nome é {nome}.\n Você tem {idade} anos.\n Sua espécie é {especie}.\n Sua  classe é {escolha}.')
        print(f'descrição da sua classe {descricao_assassino}')
    elif escolha == classe5:
        print(f'Seu nome é {nome}.\n Você tem {idade} anos.\n Sua espécie é {especie}.\n Sua  classe é {escolha}.')
        print(f'descrição da sua classe{descricao_monge}')
    else:
        print('Erro: A classe escolhida não está disponível')

