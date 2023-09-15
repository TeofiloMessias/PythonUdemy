def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'a gente so vive uma vez.'

    return f'Estou comendo {comida} porque {final}'

def dormir(num_horas):
    if num_horas > 8:
        return f'Ptz! Dormi muito! Estou atrasado para o trabalho'
    else:
        return f'Cintinuo cansado após dormir 4 horas. :('

def eh_engracada(pessoa):
    comediantes =['Jim Carry','Bozo']
    if pessoa in comediantes:
        return True
    return False
