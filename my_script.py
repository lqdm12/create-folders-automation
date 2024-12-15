import os

# Dicionário com nome da matéria como chave e tópicos como lista de valores
materias = {
    "Química": [
        "Materiais: suas propriedades e uso/Estados físicos da matéria e mudanças de estado",
        "Materiais: suas propriedades e uso/Fenômenos físicos e químicos",
        "Materiais: suas propriedades e uso/Substância química: classificação e características gerais",
        "Materiais: suas propriedades e uso/Misturas: tipos e métodos de separação",
        "Átomo/Teorias e modelos atômicos dos átomos",
        "Átomo/Estrutura atômica: número atômico, número de massa, número de nêutrons, isótopos, isóbaros e isótonos",
        "Elementos químicos e tabela periódica/Elementos químicos: síntese, descoberta e simbologia. Construção e Organização",
        "Elementos químicos e tabela periódica/Propriedades periódicas: raio atômico, eletronegatividade, potencial de ionização e afinidade eletrônica",
        "Reações químicas e suas equações/Classificação das reações químicas",
        "Reações químicas e suas equações/Reações de combustão: o efeito estufa",
        "Introdução à química orgânica",
        "Funções orgânicas",
        "Isomeria",
        "Biomoléculas",
        "Mecanismo de reações orgânicas"
    ],
    "Biologia": [
        "Bases da Biologia Molecular/Glicídios e Lipídios",
        "Bases da Biologia Molecular/Estrutura do DNA e RNA",
        "Bases da Biologia Molecular/O código universal",
        "Bases da Biologia Molecular/Bases teóricas da Biotecnologia e suas aplicações",
        "Bases da Biologia Molecular/Vitaminas",
        "Citologia/Invenção do microscópio e a descoberta da célula",
        "Citologia/Relação entre forma e função da célula",
        "Citologia/Tipos de célula",
        "Citologia/Estrutura da membrana",
        "Citologia/Diferentes tipos de transporte de substâncias",
        "Citologia/Envoltórios e especializações da membrana",
        "Citologia/Citoplasma",
        "Divisão Celular/Mitose",
        "Divisão Celular/Meiose",
        "Bioenergética/Respiração celular",
        "Bioenergética/Fermentação",
        "Histologia/Tecido epitelial",
        "Histologia/Tecido conjuntivo",
        "Histologia/Tecido muscular",
        "Histologia/Tecido nervoso",
        "Fisiologia/Sistema digestório",
        "Fisiologia/Sistema circulatório",
        "Fisiologia/Sistema respiratório",
        "Fisiologia/Sistema excretor e de osmorregulação",
        "Fisiologia/Sistema locomotor",
        "Fisiologia/Sistema nervoso",
        "Fisiologia/Sistema endócrino",
        "Fisiologia/Órgãos dos sentidos",
        "Embriologia animal/Reprodução dos seres vivos",
        "Embriologia animal/Fases e anexos embrionários",
        "Embriologia animal/Gametogênese"
    ],
    "História": [
        "Antiguidade",
        "Grécia",
        "Roma",
        "Idade Média",
        "Islamismo",
        "Antecedentes da Expansão Comercial Marítimo Portuguesa",
        "Sistema Colonial e Colonização da América",
        "Absolutismo e Mercantilismo",
        "Renascimento Cultural e Reformas Religiosas",
        "Iluminismo",
        "Revoluções Burguesas/Inglaterra",
        "Revoluções Burguesas/Estados Unidos",
        "Revoluções Burguesas/França",
        "O Século do Ouro do Brasil",
        "Período Joanino e o Processo de Independência",
        "Brasil República/Crise do Brasil Imperial e a República das Espadas",
        "Brasil República/Era Vargas",
        "Brasil República/República Oligárquica",
        "Brasil Pós-64/Ditadura Militar",
        "Brasil Pós-64/Redemocratização e Populismo",
        "Nova República",
        "Atualidades e Conceitos",
        "Mundo Contemporâneo/China",
        "Mundo Contemporâneo/Independência das Colônias da África e Ásia"
    ],
    "Física": [
        "Cinemática Escalar",
        "Cinemática Vetorial",
        "Leis de Newton",
        "Atrito",
        "Forças em trajetória curva",
        "Energia (Principios da conservação)",
        "Gravitação",
        "Estática",
        "Hidrostática",
        "Temperatura e seus efeitos",
        "Calor",
        "Termodinâmica",
        "Gases",
        "Refração",
        "Lentes",
        "MHS",
        "Ondas",
        "Eletrostática",
        "Eletrodinâmica",
        "Eletromagnetismo",
        "Unidades e Física Moderna"
    ],
    "Língua Portuguesa e Arte": {
        "Gramática": {
            "Fonética": [
                "Ortografia",
                "Acentuação Gráfica"
            ],
            "Morfossintaxe": {
                "Classes de Palavras": [
                    "Substantivo",
                    "Artigo",
                    "Adjetivo",
                    "Numeral",
                    "Pronome",
                    "Verbo",
                    "Advérbio",
                    "Preposição",
                    "Conjunção",
                    "Interjeição"
                ],
                "Estrutura e Formação de Palavras": [],
                "Análise Sintática": [],
                "Concordância Nominal e Verbal": {
                    "Concordância Nominal": [],
                    "Concordância Verbal": []
                },
                "Regência Nominal e Verbal": {
                    "Regência Nominal": [],
                    "Regência Verbal": []
                },
                "Pontuação": []
            },
            "Estilística": {
                "Figuras de Linguagem": [],
                "Estilo Direto, Indireto e Indireto Livre": []
            }
        },
        "Literatura": {
            "Literatura Portuguesa": [
                "Trovadorismo",
                "Humanismo",
                "Classicismo",
                "Barroco",
                "Arcadismo",
                "Romantismo",
                "Realismo/Naturalismo",
                "Parnasianismo",
                "Modernismo"
            ],
            "Literatura Brasileira": {
                "Literatura de Informação": [
                    "Literatura dos Jesuítas"
                ],
                "Barroco Brasileiro": [],
                "Arcadismo Brasileiro": [],
                "Romantismo Brasileiro": [],
                "Realismo/Naturalismo Brasileiro": [],
                "Parnasianismo Brasileiro": [],
                "Simbolismo Brasileiro": [],
                "Pré-Modernismo": [],
                "Modernismo Brasileiro": [],
                "Pós-Modernismo": []
            }
        },
        "Arte": [
            "A música como forma de linguagem",
            "O teatro como forma de linguagem universal"
        ],
        "Textualidade, Produção e Interpretação de Texto": [],
        "Norma Ortográfica": []
    },
    "Geografia": [
        "Geografia na era da Informação",
        "Cartografia",
        "Geologia e Mineração",
        "Relevo e Solo",
        "Clima e Vegetação",
        "Hidrografia",
        "Domínios Morfoclimáticos no Brasil",
        "Questão Ambiental",
        "Conflitos Ético-Nacionalistas e Separatismo",
        "Geopolítica",
        "Globalização",
        "Transporte",
        "Energia",
        "Indústria",
        "Agricultura",
        "Agropecuária",
        "Urbanização",
        "Crescimento Populacional",
        "Migrações",
        "Brasil: Perspectivas e Regionalização"
    ],
    "Matemática": [
        "Conhecimentos Numéricos",
        "Função",
        "Trigonometria",
        "Matrizes e Sistemas",
        "Conhecimento de Probabilidade",
        "Geometria Espacial",
        "Geometria Analítica",
        "Conjuntos dos Números Complexos",
        "Estatística",
        "Polinômios"
    ]
}

# Caminho base onde as pastas serão criadas
base_path = 'materias_ensino'

# Função para criar as pastas
def criar_pastas(base_path, materias):
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    for materia, topicos in materias.items():
        # Cria pasta para cada matéria
        materia_path = os.path.join(base_path, materia)
        if not os.path.exists(materia_path):
            os.makedirs(materia_path)
        
        # Cria subpastas para os tópicos de cada matéria
        for topico in topicos:
            topico_path = os.path.join(materia_path, topico)
            if not os.path.exists(topico_path):
                os.makedirs(topico_path)

# Chama a função para criar as pastas
criar_pastas(base_path, materias)
