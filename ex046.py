#Contagem regressiva com for;
import time
import emoji

for c in range(10, -1, -1):
    if c == 10:
        print('\n\nINICIANDO CONTAGEM!\n\n')
        time.sleep(1)
    print(c)
    time.sleep(1)
print('\n\nFELIZ ANO NOVO!!!\n')
print(emoji.emojize('🎆🎆🎆🎆🎆🎆🎆'))
print(emoji.emojize(' 🎆🎆🎆🎆🎆🎆'))
print(emoji.emojize('  🎆🎆🎆🎆🎆'))
print(emoji.emojize('   🎆🎆🎆🎆'))
print(emoji.emojize('    🎆🎆🎆'))
print(emoji.emojize('     🎆🎆'))
print(emoji.emojize('      🎆'))
