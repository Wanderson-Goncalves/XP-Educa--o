# relação de dias da semana que cada médico atende
cardiologista = {'terca', 'quarta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}


# Calcula quais os dias possiveis para dois médicos
def disp_dois_especialistas(medico01, medico02):

    dias_combinados = set(medico01).intersection(medico02)

    if dias_combinados:
        print(
            f'Os médicos atendem no mesmo dias são:\t{list((dias_combinados))}.')
    else:
        print('Não há dias combinados')


# Calcula quais os dias possíveis para três médicos
def disp_tres_especialistas(medico01, medico02, medico03):

    dias_combinados = set(medico01).intersection(medico02, medico03)

    if dias_combinados:
        print(
            f'Os médicos atendem no mesmo dias são:\t{list((dias_combinados))}.')
    else:
        print('Não há dias combinados')


disp_tres_especialistas(psiquiatra, dermatologista, cardiologista)
