# coding=utf-8
import random


ROLE = ['Detective', 'Vigilante', 'Duplicador', 'Protector', 'Anulador', 'Healer', 'Jailor', 'Decisor', 'Taxista', 'Mayor', 'Serial Killer', 'Líder da Máfia', 'Homem-Bomba', 'Traidor', 'Emo', 'Armadura']

EQUIPA = ['Inocente', 'Máfia', 'OMT', 'Neutro']

CHARACTER = ['Kyoko Kirigiri', 'Cristiano Ronaldo', 'Donald Trump', 'Floribella', 'Chopper', 'Jorge Mendes','Hiro Nakamura', 'Gabriel Sylar', 'Jorge Jesus', 'Bin Laden', 'Justin Bieber', 'Santa', 'Voldemort', 'Doflamingo','Ribombee', 'Garchomp', 'Inês Brasil', 'Grimes', 'Monokuma', 'Forsen', 'Cheshire Cat', 'Isaac', 'Junko Enoshima', 'Jesus Cristo', 'Kaceytron', 'Big Mom', 'John Cena', 'King', 'Maria Rose', 'Undyne', 'Loki', 'Mr. Jefferson', 'Nagito Komaeda', 'Shrek', 'Rexxar', 'Deathwing', 'Shaco', 'Harry Potter', 'Quintino Aires', 'Abel Xavier', 'Brock Lesnar', 'Buggy', 'Agumon', 'Teresa Faria', 'Cálcio+', 'Ambrósio', 'Katya Zamolodchikova', 'Ice Poseidon', 'Mandingo', 'Ágata']

TEMPO_G = ['Durante o dia', 'Ao final da tarde', 'No início da madrugada', 'Já pela noite', 'Às 4:20 da tarde', 'À hora da missa', 'Quando os sinos tocaram', 'Após voltar do WC', 'Após acabar o almoço', 'Com o ruído dos patos', 'Antes do banho', 'Não saindo impune', 'Aos berros']

JOGADOR = ['EP', 'Maggot', 'JVS', 'Space Ninja', 'Drizzy', 'Saya', 'Angel', 'Chester', 'SirCouve', "Mahn'ell", "Toon", "Benny", "Dave", "Knightmare", "Shadow", "Arceus_17", "Exclamation!", "Victory Star", "Tobi", "Kibation", "Linus", "InvictaWave", "Yakuza", "Diamond", "WhiteNoise", "Pearl", "Guroqueen", "Lyncetream", "Captainjonh", "Norleon", "DkM", "Ignis", 'KUYASHII', 'Nando', 'Icemander']

ACTION_P = ['investigado', 'atacado', 'duplicado', 'protegido', 'anulado', 'curado', 'preso', 'assediado', 'morto', 'insultado', 'trocado com [JOGADOR]']

ACTION_A = ['investigou', 'atacou', 'duplicou', 'protegeu', 'anulou', 'curou', 'prendeu', 'assediou', 'matou', 'insultou', 'trocou [JOGADOR] com']

ACTION_R = ['investigaria', 'atacaria', 'duplicaria', 'protegeria', 'anularia', 'curaria', 'prenderia', 'assediaria', 'mataria', 'insultaria']

ACTION_V = ['investigar', 'atacar', 'duplicar', 'proteger', 'anular', 'curar', 'prender', 'assediar', 'matar', 'insultar']

TEMA = ['Pokémon', 'Heroes', 'Marvel', 'Inspector Max', 'Danganronpa', 'Undertale', 'Mixed Games', 'Mixed Animes', 'Fairy Tail', 'Tekken', 'Mitologia', 'Hearthstone', 'Futebol', 'Digimon', 'League of Legends', 'Cereais Integrais', 'Harry Potter', 'Século [NUMERO_VOTE]', 'Tecnologias', 'Matemática', 'Animais de Estimação', 'FCUL', 'Técnico', 'Profissões', 'Europa', 'Políticos', 'Rock in Rio', 'Corpo Humano', 'Jogos Olímpicos', 'Steam Sales', 'Religião', 'Twitch Drama', 'Fire Emblem', '[ROLE] à Solta', '[CHARACTER] e Companhia', 'Arte Contemporânea', 'WWE', 'Guerra dos Ingredientes', 'Pré-História', 'Férias de Natal', 'MasterChef', 'Feministas', 'Redes Sociais', 'Club Penguin', 'Memorial do Convento', 'Drama Nacional', 'África']

EXPR_P = ['entregou-lhe o seu corpo', 'pensou na sua mãe', 'descobriu a sua função', 'ficou feliz com isso', 'gritou de raiva', 'sorriu, morto por dentro', 'riu-se com o sucedido', 'não quer admitir mas gostou', 'não sentiu nada', 'ficou sedento de vingança', 'pensou que era um meme', 'pediu para repetir', 'apagou a sua conta', 'ficou triggered', 'berrou']

EXPR_JDD = ['Foi um desastre', 'Para a primeira vez, safou-se bem', 'Houve drama entre [JOGADOR] e [JOGADOR]', 'Foi dos melhores JDDs da liga', 'Os inocentes foram cepos outra vez', 'Pôr [CHARACTER] como [ROLE] foi uma má decisão', 'O [JOGADOR] foi escolhido como melhor jogador', 'Foi arruinado pela inactividade', 'O [JOGADOR] fez roletrade', 'Só ficou um [EQUIPA] vivo no final do jogo', 'Os canos de [JOGADOR] ficaram entupidos']

EXPR_ACC = ['na primeira noite','o [JOGADOR] duas vezes seguidas','alguém com full HP', 'ao invés de [ACTION_V] o [JOGADOR]']

EXPR_EXEC = ['mas sobreviveu', 'e morreu. Era [CHARACTER], o [ROLE] [EQUIPA]',', embora se tenha defendido bem', 'depois de postar um meme de [TEMA]', 'por ter sido [ACTION_P] na noite passada',', mas a sua execução foi cancelada', 'e perdeu [NUMERO_JDD] HP']


constant_dic = {'ROLE': ROLE, 'EQUIPA': EQUIPA, 'CHARACTER': CHARACTER, 'JOGADOR': JOGADOR, 'ACTION_P': ACTION_P, 'ACTION_A': ACTION_A, 'NUMERO_JDD': map(str,range(1,100)), 'NUMERO_VOTE': map(str,range(1,22)), 'TEMA': TEMA, 'EXPR_P': EXPR_P, 'TEMPO_G': TEMPO_G, 'ACTION_R': ACTION_R, 'ACTION_V': ACTION_V, 'EXPR_JDD': EXPR_JDD, 'EXPR_ACC': EXPR_ACC, 'EXPR_EXEC': EXPR_EXEC}
