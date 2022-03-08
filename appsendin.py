import streamlit as st
#st.title('Aplicativo para Seleção das Proteções Contra Incêndio para Líquidos Igníferos')
#st.write('De acordo com a Instrução Técnica 25/19 do Corpo de Bombeiros do Estado de São Paulo e NBR 17.505.')
from PIL import Image
image1 = Image.open('liq.png')
st.image(image1, caption='')


# Menu lateral
st.sidebar.title('Cenário')
paginaselecionada = st.sidebar.selectbox('Selecione o cenário',['Defina o cenário','Parque de Tanques','Tanques em Edificações','Fracionados','Operações','Cais ou Pier','Destilarias','Refinarias','Postos de Serviços','Plataforma de Carregamento'])
st.sidebar.caption('Aplicativo desenvolvido em Python pelo Professor Silmar Sendin.')
# Fim do Menu Lateral

if paginaselecionada == 'Defina o cenário':
    st.title('Definição de Cenário')
    st.write('Escolha na caixa de seleção a esquerda qual cenário se aplica ao seu caso concreto.')
    definircenario = st.checkbox('Quero saber como definir o cenário com líquidos igníferos.')
    if definircenario:
       # video_file = open('https://youtu.be/e3a02Hl0ddM', 'rb')
        # video_bytes = video_file.read()
      #  st.video(video_bytes)

        st.video('https://youtu.be/e3a02Hl0ddM', format="video/mp4", start_time=0)

elif paginaselecionada == 'Parque de Tanques':
    st.title('Parque de Tanques')
    st.write('O cenário selecionado é um parque de Tanques e as informações a seguir só se aplicam a este cenário.')

    mostrarclasses = st.checkbox('Quero saber como classificar um líquido ignífero.')
    if mostrarclasses:
        from PIL import Image
        image = Image.open('classes.png')
        st.image(image, caption='Classes dos Líquidos Igníferos')
        st.write('PF = Ponto de Fulgor, PV = Pressão de Vapor, e PE = Ponto de Ebulição')

    classeliq = st.selectbox('Qual a Classe do Líquido Armazenado:',['Classe I','Classe IA','Classe IB','Classe IC','Classe II','Classe IIIA','Classe IIIB'])
    volumetanques = st.number_input("Qual o volume total, em litros, armazenado sem isolamento:")
    if volumetanques < 20001 or classeliq == 'Classe IIIB':
        st.write('Não será necessário os sistemas de espuma e resfriamento')
        st.write('Prever Sistema de Extintor de acordo com a Tabela 1.2 da IT 25/19 SP ou Tabela A.11 da NBR 17.505 - Parte 7.')
    elif volumetanques > 20000 or classeliq != 'Classe IIIB':
        mostrarnbr = st.checkbox('Quero saber como proteger o cenário de acordo com a NBR 17.505.')
        if mostrarnbr:
            st.write('Prever Sistema de Espuma de acordo com o item 8 da NBR 17.505 - Parte 7.')
            st.write('Prever Sistema de Resfriamento de acordo com o item 4.2.2 e item 6 da NBR 17.505 - Parte 7, checar as exceções do item 4.2.1.')
            st.write('Prever Sistema de Contenção de acordo com o item 5.9 da NBR 17.505 - Parte 2.')
        mostrarit25 = st.checkbox('Quero saber como proteger o cenário de acordo com a IT 25/19 de SP.')
        if mostrarit25:
            st.write('Prever Sistema de Espuma de acordo com o item o item 7.2.2.1.1. da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Resfriamento de acordo com o item o item 7.4 da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Contenção de acordo com o item 2.3.7. da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
        mostrarcurso = st.checkbox('Quero saber mais sobre proteção contra incêndio para líquidos igníferos.')
        if mostrarcurso:
            st.write('Visite: https://www.silmarsendin.com/cursos-on-line-1 ')
#Exigências para Edificações com Tanques.
elif paginaselecionada == 'Tanques em Edificações':
    st.title('Tanques em Edificações')
    st.write('O cenário selecionado é uma Edificação contendo Tanques e as informações a seguir só se aplicam a este cenário.')

    mostrarclasses = st.checkbox('Quero saber como classificar um líquido ignífero.')
    if mostrarclasses:
        from PIL import Image
        image = Image.open('classes.png')
        st.image(image, caption='Classes dos Líquidos Igníferos')
        st.write('PF = Ponto de Fulgor, PV = Pressão de Vapor, e PE = Ponto de Ebulição')

    classeliq = st.selectbox('Qual a Classe do Líquido Armazenado:',['Classe I','Classe IA','Classe IB','Classe IC','Classe II','Classe IIIA','Classe IIIB'])
    volumetanques = st.number_input("Qual o volume total, em litros, armazenado sem isolamento:")
    if volumetanques < 20001 or classeliq == 'Classe IIIB':
        st.write('Não será necessário os sistemas de espuma e resfriamento de acordo com a NBR 17.505 mas pela IT 25/19 deverá ser previsto para IIIB com mais de 20 m3.')
        st.write('Prever Sistema de Extintor de acordo com a Tabela 1.2 da IT 25/19 SP ou Tabela A.11 da NBR 17.505 - Parte 7.')
    elif volumetanques > 20000 or classeliq != 'Classe IIIB':
        mostrarnbr = st.checkbox('Quero saber como proteger o cenário de acordo com a NBR 17.505.')
        if mostrarnbr:
            st.write('Caso haja apenas uma cobertura, sem paredes laterais e e não haja obstruções a dissipação de calor ou a dispersão dos vapores inflamáveis, considerar como Parque de Tanques.')
            st.write('Prever Sistema de Espuma de acordo com o item 8 da NBR 17.505 - Parte 7.')
            st.write('Prever Sistema de Resfriamento de acordo com o item 4.2.2 e item 6 da NBR 17.505 - Parte 7, checar as exceções do item 4.2.1.')
            st.write('Observar o item 7.4. da NBR 17.505 - Parte 2.')
            st.write('Prever Sistema de Contenção de acordo com o item 7.6 da NBR 17.505 - Parte 2.')
            st.write('Observar as demais exigências do item 7 da NBR 17.505 - Parte 2.')
        mostrarit25 = st.checkbox('Quero saber como proteger o cenário de acordo com a IT 25/19 de SP.')
        if mostrarit25:
            st.write('Prever Sistema de Espuma de acordo com o item o item 7.2.2.1.1. da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Resfriamento de acordo com o item o item 7.4 da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Contenção de acordo com o item 2.3.7. da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
        mostrarcurso = st.checkbox('Quero saber mais sobre proteção contra incêndio para líquidos igníferos.')
        if mostrarcurso:
            st.write('Visite: https://www.silmarsendin.com/cursos-on-line-1 ')

#Exigências para Fracionados.
elif paginaselecionada == 'Fracionados':
    st.title('Líquidos Fracionados')
    st.write('O cenário selecionado é um armazenamento de líquidos fracionados e as informações a seguir só se aplicam a este cenário.')

    mostrarclasses = st.checkbox('Quero saber como classificar um líquido ignífero.')
    if mostrarclasses:
        from PIL import Image
        image = Image.open('classes.png')
        st.image(image, caption='Classes dos Líquidos Igníferos')
        st.write('PF = Ponto de Fulgor, PV = Pressão de Vapor, e PE = Ponto de Ebulição')

    classeliq = st.selectbox('Qual a Classe do Líquido Armazenado:',['Classe I','Classe IA','Classe IB','Classe IC','Classe II','Classe IIIA','Classe IIIB'])
    volumetanques = st.number_input("Qual o volume total, em litros, armazenado sem isolamento:")
    if volumetanques < 20001 or classeliq == 'Classe IIIB':
        st.write('Não será necessário os sistemas de espuma e resfriamento de acordo com a NBR 17.505 mas pela IT 25/19 deverá ser previsto para IIIB com mais de 20 m3.')
        st.write('Prever Sistema de Extintor de acordo com a Tabela 1.2 da IT 25/19 SP ou Tabela A.11 da NBR 17.505 - Parte 7.')
    elif volumetanques > 20000 or classeliq != 'Classe IIIB':
       
        mostrarit25 = st.checkbox('Quero saber como proteger o cenário de acordo com a IT 25/19 de SP.')
        if mostrarit25:
            st.write('Prever Sistema de Espuma de acordo com a Tabela 4.25 para áreas abertas e 4.27 para áreas fechadas da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Resfriamento de acordo com a Tabela 4.26 para áreas abertas e 4.28 para áreas fechadas da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Contenção de acordo com o item 4.8 da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Caso os volumes armazenados ultrapassem os determinados na Tabela 4.9, prever Sistema de Chuveiros automáticos de acordo com o item 4.20 da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            mostrar49 = st.checkbox('Quero ver a Tabela 4.9.')
            if mostrar49:
                from PIL import Image
                image2 = Image.open('tabela49.png')
                st.image(image2, caption='Tabela 4.9: Quantidades máximas para armazéns de líquidos M-2 sem sistema de chuveiros automáticos')
                

        mostrarcurso = st.checkbox('Quero saber mais sobre proteção contra incêndio para líquidos igníferos.')
        if mostrarcurso:
            st.write('Visite: https://www.silmarsendin.com/cursos-on-line-1 ')

#Exigências para Operações.
elif paginaselecionada == 'Operações':
    st.title('Operações')
    st.write('O cenário selecionado é para Operações com líquidos inflamáveis ou combustíveis e as informações a seguir só se aplicam a este cenário.')

    mostrarclasses = st.checkbox('Quero saber como classificar um líquido ignífero.')
    if mostrarclasses:
        from PIL import Image
        image = Image.open('classes.png')
        st.image(image, caption='Classes dos Líquidos Igníferos')
        st.write('PF = Ponto de Fulgor, PV = Pressão de Vapor, e PE = Ponto de Ebulição')

    mostrarnbr = st.checkbox('Quero saber como proteger o cenário de acordo com a NBR 17.505.')
    if mostrarnbr:
        st.write('As estruturas das edificações e os apoios dos vasos e equipamentos de processamento, capazes de liberar quantidades apreciáveis de líquidos, que eventualmente possam resultar em um incêndio de considerável intensidade  duração, causadno danos substânciais à propriedade, devem ser protegidos por um ou mais dos seguintes a seguir:')
        st.write('a) drenagem para um local seguro, evitando o acúmulo de líquidos sob vaos, equipamentos ou ao redor de suportes de mola;')
        st.write('b) construção resistente ao fogo:')
        st.write('c) revestimentos resistentes ao fogo;')
        st.write('d) sistemas de chuveiros automáticos de água, projetados e instalados de acordo com a ABNT NBR 10.897;')
        st.write('e) outros recursos técnicos aprovados pela Corporação de Bombeiros local.')
        st.write('Prever Sistema de Extintor de acordo com a Tabela 1.2 da IT 25/19 SP ou Tabela A.11 da NBR 17.505 - Parte 7.')

    mostrarit25 = st.checkbox('Quero saber como proteger o cenário de acordo com a IT 25/19.')
    if mostrarit25:
        st.subheader('Sistema de Espuma')
        st.write('As edificações onde se manuseiam líquidos combustíveis e inflamáveis com volume total superior a 20 m3 devem ser protegidas por linhas manuais de espuma, considerando-se o comprimento máximo da mangueira de 45 m conforme item 5.2.9.2.1 da IT 25/19.')
        st.write('Podem ser utilizados mangueiras e esguichos de 65 mm ou 38 mm, desde que sejam atendidas as condições da Tabela 5.4.')
        mostrartabela54 = st.checkbox('Quero ver a Tabela 5.4 da IT 25/19')
        if mostrartabela54:
            from PIL import Image
            image1 = Image.open('tabela54.png')
            st.image(image1, caption='Tabela 5.4: Linhas de espuma para áreas de manuseio e processamento')

        st.subheader('Chuveiros Automáticos')
        st.write('Além das linhas manuais previstas, deve ser previsto sistema de proteção por espuma através de chuveiros automáticos do tipo tubo molhado com espuma ou dilúvio com espuma nas seguintes situaçes:')
        st.write('a. líquidos das classes IA e IB com volume acima de 30 m3;')
        st.write('b. líquidos de classes IC, II e IIIA com volume acima de 40 m3;')
        st.write('c. líquidos de classe IIIB com volume acima de 60 m3.')

        st.subheader('Sistema de Resfriamento')
        st.write('As edificações onde se manuseiam líquidos combustíveis e inflamáveis com volume total superior a 20 m3, devem ser protegidas por linhas manuais de resfriamento com esguichos reguláveis, considerando-se o comprimento máximo da mangueira de 30 m')
        st.write('Podem ser utilizados mangueiras e esguichos de 65 mm ou 38 mm, desde que seja atendida a Tabela 5.5.')
        mostrartabela55 = st.checkbox('Quero ver a Tabela 5.5 da IT 25/19')
        if mostrartabela55:
            from PIL import Image
            image2 = Image.open('tabela55.png')
            st.image(image2, caption='Tabela 5.5: Linhas de resfriamento para áreas de manuseio e processamento')

        st.subheader('Sistema de Extintores')
        st.write('Prever Sistema de Extintor de acordo com a Tabela 1.2 da IT 25/19 SP ou Tabela A.11 da NBR 17.505 - Parte 7.')

#Exigências para Cais ou Pier.
elif paginaselecionada == 'Cais ou Pier':
    st.title('Cais ou Pier')
    st.write('O cenário selecionado é para Caís ou Pier com líquidos inflamáveis ou combustíveis e as informações a seguir só se aplicam a este cenário.')

    mostrarclasses = st.checkbox('Quero saber como classificar um líquido ignífero.')
    if mostrarclasses:
        from PIL import Image
        image = Image.open('classes.png')
        st.image(image, caption='Classes dos Líquidos Igníferos')
        st.write('PF = Ponto de Fulgor, PV = Pressão de Vapor, e PE = Ponto de Ebulição')

    mostrarnbr = st.checkbox('Quero saber como proteger o cenário de acordo com a NBR 17.505.')
    if mostrarnbr:
        st.write('Em decorrência das muitas variáveis envolvidas, os requisitos exatos não podem ser previstos. Entretanto, a Tabela A.3 supre um guia do nível de proteção contra incêndios típicos disponibilizados em cais e em terminais marítimos que manueseiem líquidos inflamáveis.')
        mostrartabelaa3 = st.checkbox('Quero ver a Tabela 5.3 da IT 25/19')
        if mostrartabelaa3:
            from PIL import Image
            image2 = Image.open('tabelaa3.png')
            st.image(image2, caption='Tabela A.3: Proteção típica contra incêndios em cais e terminais marítimos')

    mostrarit25 = st.checkbox('Quero saber como proteger o cenário de acordo com a IT 25/19.')
    if mostrarit25:
        st.subheader('Sistema de Espuma e Resfriamento')
        st.write('Para proteção contra incêndio para cais/píer deve ser observada a Tabela 5.3.')
        mostrartabela53 = st.checkbox('Quero ver a Tabela 5.3 da IT 25/19')
        if mostrartabela53:
            from PIL import Image
            image2 = Image.open('tabela53.png')
            st.image(image2, caption='Tabela 5.3: Proteção típica contra incêndios em cais e terminais marítimos')

        st.subheader('Sistema de Extintores')
        st.write('Onde não for exigida rede de água para combate a incêndio, devem ser previstos, no mínimo, dois extintores de pó químico seco de 40-B:C. Os extintores devem ficar locali-zados em um raio máximo de 15 m da bomba ou da área do manifold, e devem ser facilmente acessíveis durante as situações de emergência')

#Exigências para Destilarias.
elif paginaselecionada == 'Destilarias':
    st.title('Destilarias')
    st.write('O cenário selecionado é para Destilaria e as informações a seguir só se aplicam a este cenário.')
    tipodestil = st.checkbox('Quero conhecer os tipos de Destilarias')
    if tipodestil:
            from PIL import Image
            image3 = Image.open('tipodestil.png')
            st.image(image3, caption='Tipos de Destilarias')
    tipodestilaria = st.selectbox('Escolha a categoria da Destilaria',['Tipo 1','Tipo 2','Tipo 3'])

    mostrarit25 = st.checkbox('Quero saber como proteger o cenário de acordo com a IT 25/19.')
    if mostrarit25:
        if tipodestilaria == 'Tipo 1':
            st.subheader('Destilaria do Tipo 1')
            st.subheader('Sistema de Espuma')
            st.write('As destilarias do Tipo 1 devem ser protegidas por sistemas de espuma, por linhas manuais ou canhões monitores com taxa de aplicação de no mínimo 6,9 lpm/m2 da área limitada pelo sistema de drenagem, porém, com vazão não inferior a 200 lpm, aplicada pelo tempo mínimo de 15 min.')
            st.subheader('Sistema de Resfriamento')
            st.write('As destilarias do Tipo 1 devem ser protegidas por sistema de resfriamento, adotando-se a combinação dos seguintes métodos:')
            st.write('a. canhões monitores fixos ou móveis;')
            st.write('b. linhas manuais;')
            st.write('c. aspersores.')
            st.write('Deve haver para destilaria Tipo 1, pelo menos um hidrante duplo externo, com duas linhas manuais, dotadas de esguichos reguláveis, com vazão mínima de 300 lpm cada, dispostas de tal forma que o pavimento térreo seja totalmente atendido, considerando o comprimento de 60 m de mangueiras através de seu trajeto real.')
            st.write('Deve ser previsto sistema de resfriamento por aspersores nas destilarias tipo 1, quando os equipamentos ultrapassarem 9 m de altura.')
            st.write('O sistema de aspersor deve ser projetado para resfriar vasos e equipamentos com líquidos inflamáveis ou combustíveis e para proteger a estrutura da edificação e das sustentações dos vasos e equipamentos contra exposição ao calor, sendo dimensionado conforme Norma Brasileira aplicável ou, na inexistência desta, conforme NFPA 15.')

        elif tipodestilaria == 'Tipo 2':
            st.subheader('Destilaria do Tipo 2')
            st.subheader('Sistema de Espuma')
            st.write('As destilarias do Tipo 2 devem ser protegidas por sistemas de espuma, por linhas manuais ou canhões monitores com taxa de aplicação de no mínimo 6,9 lpm/m2 da área limitada pelo sistema de drenagem, porém, com vazão não inferior a 200 lpm, aplicada pelo tempo mínimo de 15 min.')
            st.subheader('Sistema de Resfriamento')
            st.write('As destilarias do Tipo 2 devem ser protegidas por sistema de resfriamento, adotando-se a combinação dos seguintes métodos:')
            st.write('a. canhões monitores fixos ou móveis;')
            st.write('b. linhas manuais;')
            st.write('c. aspersores.')
            st.write('As destilarias dos tipos 2, onde a altura dos equipamentos for maior que 9 m, devem ser protegidas por no mínimo um canhão monitor com vazão mínima de 3.800 lpm, podendo ser dividido em dois canhões com vazão mínima de 1.600 lpm cada um.')
            st.write('Deve ser previsto sistema de resfriamento por aspersores nas destilarias dos tipos 2, quando os equipamentos ultrapassarem a altura de alcance dos canhões monitores, conforme rendimento real destes')
            st.write('O sistema de aspersor deve ser projetado para resfriar vasos e equipamentos com líquidos inflamáveis ou combustíveis e para proteger a estrutura da edificação e das sustentações dos vasos e equipamentos contra exposição ao calor, sendo dimensionado conforme Norma Brasileira aplicável ou, na inexistência desta, conforme NFPA 15.')

        elif tipodestilaria == 'Tipo 3':
            st.subheader('Destilaria do Tipo 3')
            st.subheader('Sistema de Espuma')
            st.write('As destilarias do Tipo 3 devem ser protegidas por sistemas de espuma, por linhas manuais ou canhões monitores com taxa de aplicação de no mínimo 6,9 lpm/m2 da área limitada pelo sistema de drenagem, porém, com vazão não inferior a 200 lpm, aplicada pelo tempo mínimo de 15 min.')
            st.subheader('Sistema de Resfriamento')
            st.write('As destilarias do Tipo 3 devem ser protegidas por sistema de resfriamento, adotando-se a combinação dos seguintes métodos:')
            st.write('a. canhões monitores fixos ou móveis;')
            st.write('b. linhas manuais;')
            st.write('c. aspersores.')
            st.write('As destilarias dos tipos 3, onde a altura dos equipamentos for maior que 9 m, devem ser protegidas por no mínimo um canhão monitor com vazão mínima de 3.800 lpm, podendo ser dividido em dois canhões com vazão mínima de 1.600 lpm cada um.')
            st.write('Deve ser previsto sistema de resfriamento por aspersores nas destilarias dos tipos 2, quando os equipamentos ultrapassarem a altura de alcance dos canhões monitores, conforme rendimento real destes')
            st.write('O sistema de aspersor deve ser projetado para resfriar vasos e equipamentos com líquidos inflamáveis ou combustíveis e para proteger a estrutura da edificação e das sustentações dos vasos e equipamentos contra exposição ao calor, sendo dimensionado conforme Norma Brasileira aplicável ou, na inexistência desta, conforme NFPA 15.')