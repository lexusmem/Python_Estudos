from collections import defaultdict, Counter
# Dicionario
# Conjunto de Chave e Valor
# Exemplo: Agenda, Dicionário

texto_1 = """
Christopher Columbus was a hero to some and a villain to others. He was a brave explorer, but he also enslaved, murdered, and stole from native people across the Americas. He first met the Arawak natives in the Bahamas in 1492. They generously traded everything they owned. Columbus saw this as a weakness. He wrote in his journal, “They brought us parrots and balls of cotton and spears and many other things. They do not bear arms and do not know them. They would make fine servants.”

Eleven years later, Christopher Columbus was still taking advantage of the Arawak’s hospitality.

On his fourth and final voyage in 1503, Columbus found himself in dire straits. Shipworms had destroyed two of his ships. He was forced to abandon them and send the rest of his ships to an island we now know as Jamaica.

The Arawaks were initially keen to help Columbus. They offered him and his sailors food and shelter. However, after six months, tensions grew. The ships had still not been repaired. Some of Columbus’s crew had mutinied and started to run amok on the island, robbing and murdering some of the natives. The Arawaks also grew tired of trading fresh food for Columbus’s trinkets. They decided to burn their bridges with the visitors and cut off their food supply.

Faced with starvation, the crafty Columbus studied his almanac. He learned that on the evening of Thursday, Feb. 29th, 1504, a total lunar eclipse would occur.

He met with the Arawak chief three days before the eclipse and said his Christian god was angry with the natives for no longer supplying his men with food. He said in three nights time, his god would make the moon red with anger.

Just as Columbus said, the moon rose and slowly turned blood red as it passed into the shadow of the earth. Columbus’s son Ferdinand said the Arawaks were terrified.

He wrote how they howled in fear and came running to the ships. They screamed and begged Columbus to ask his god for mercy.

They promised they would cooperate with Columbus if he would turn the moon back to normal. Columbus said he would talk privately with his god.

Columbus spent 50 minutes in his cabin calculating the end of the eclipse. He reappeared and announced his god had forgiven the Arawaks. Almost in the same instance, the moon slowly began to reappear in all its glory.
"""
texto_2 = """
Ludwig van Beethoven was one of the greatest composers of all time. Yet by the time he was writing his last few masterpieces, he was completely deaf.

Beethoven wasn’t born deaf. He gradually lost all his hearing from the age of 30 onwards.

He first had an inkling something was wrong when he began to hear buzzing noises in his ears. He was only 26 at the time.

Beethoven kept his hearing problems a secret. He believed the truth would ruin his blossoming career.

By the time he turned 30, Beethoven feared he was growing deaf.

He complained to a doctor that his hearing had grown weaker over the previous three years. He explained he could not hear the high notes unless he was standing very close to the musicians.

Beethoven wrote, “For two years, I have avoided almost all social gatherings. It is impossible for me to say to people, ‘I am deaf.’ If I belonged to any other profession it would be easier.”

Fellow composer Ferdinand Ries recalled a turning point in Beethoven’s deafness. During a walk in the country, the two musicians saw a shepherd playing a pipe. Beethoven could see by his friend’s expression the shepherd was playing beautiful music. All Beethoven could hear was the sound of silence. The composer was no longer the same after the incident. He had finally confronted and surrendered to his loss of hearing.

By the age of 44, Beethoven was almost completely deaf. He could no longer hear other people’s voices or the sounds of his beloved countryside.

No one knows what exactly caused Beethoven’s deafness. A range of causes has been blamed. It could have been syphilis, lead poisoning, or typhus. It could even have been the composer’s habit of burying his head in a bucket of ice water to stay awake.

Beethoven often blamed his deafness on a fall. He also suggested gastrointestinal problems were the cause.

Whatever the reason, Beethoven refused to let his deafness conquer his passion. He continued to write music.

Although he could no longer hear the music, he could still feel and imagine it.

Beethoven’s housekeepers recall watching him sit at the piano with a pencil in his mouth. With the other end, he would touch the piano’s soundboard to feel the note’s vibration.

Beethoven wrote his famed Ninth Symphony without ever hearing a note of it. Upon its premiere, Beethoven insisted upon conducting. The orchestra hired another conductor to stand next to him. The orchestra followed his lead instead of the man who had composed the piece.

When the music was over, the audience broke out into applause. Beethoven didn’t hear any of it.
"""
# For para imprimir todas as palavras
for palavra in texto_1.split():
    # print(palavra)
    pass

# For para imprimir letras em um texto
for letra in texto_1:
    # print(letra)
    pass


def analise_frequencia_letras(texto):
    qtd_letras = Counter(texto.lower())
    total_caracteres = sum(qtd_letras.values())

    proporcoes = [(letra, frequencia / total_caracteres)
                  for letra, frequencia in qtd_letras.items()]

    proporcoes = Counter(dict(proporcoes))

    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f'{caractere} => {proporcao*100:.2f}%.')


analise_frequencia_letras(texto_1)

analise_frequencia_letras(texto_2)
