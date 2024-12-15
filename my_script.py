import os

# Dicionário com nome da matéria como chave e tópicos como lista de valores
materias = {
    "Química": [
        "Materiais: suas propriedades e uso": [
            "Estados físicos da matéria e mudanças de estado",
            "Fenômenos físicos e químicos",
            "Substância química: classificação e características gerais",
            "Misturas: tipos e métodos de separação",
        ],
        "Átomo": [
            "Teorias e modelos atômicos dos átomos",
            "Estrutura atômica: número atômico, número de massa, número de nêutrons, isótopos, isóbaros e isótonos",
        ], 
        "Elementos químicos e tabela periódica": [
            "Elementos químicos: síntese, descoberta e simbologia. Construção e Organização",
            "Propriedades periódicas: raio atômico, eletronegatividade, potencial de ionização e afinidade eletrônica",
        ],
        "Ligações químicas": [],
        "Funções inorgânicas": [],
        "Reações químicas e suas equações": [
            "Classificação das reações químicas",
            "Reações de combustão: o efeito estufa",
        ],
        "Introdução à química orgânica": [],
        "Estudo dos gases": [],
        "Estudo das soluções": [],
        "Propriedades coligativas": [],
        "Termoquímica": [],
        "Cinética química": [],
        "Equilíbrio químico": [],
        "Eletroquímica": [],
        "Reações nucleares": [],
        "Introdução à química orgânica": [],
        "Funções orgânicas": [],
        "Isomeria": [],
        "Biomoléculas": [],
        "Mecanismo de reações orgânicas": [], 
    ],
    "Biologia": [
        "Bases da Biologia Molecular": [
            "Glicídios e Lipídios",
            "Estrutura do DNA e RNA",
            "O código universal",
            "Bases teóricas da Biotecnologia e suas aplicações",
            "Vitaminas",
        ],
        "Citologia": [
            "Invenção do microscópio e a descoberta da célula",
            "Relação entre forma e função da célula",
            "Tipos de célula",
            "Estrutura da membrana",
            "Diferentes tipos de transporte de substâncias",
            "Envoltórios e especializações da membrana",
            "Citoplasma",
        ],
        "Divisão Celular": [
            "Mitose",
            "Meiose",
        ],
        "Bioenergética": [
            "Respiração celular",
            "Fermentação",
        ],
        "Histologia": [
            "Tecido epitelial"
            "Tecido conjuntivo",
            "Tecido muscular",
            "Tecido nervoso",
        ],
        "Fisiologia": [
            "Sistema digestório",
            "Sistema circulatório",
            "Sistema respiratório",
            "Sistema excretor e de osmorregulação",
            "Sistema locomotor",
            "Sistema nervoso",
            "Sistema endócrino",
            "Órgãos dos sentidos",
        ],
        "Embriologia animal": [
            "Reprodução dos seres vivos",
            "Fases e anexos embrionários",
            "Gametogênese",
        ],
        "Genética": [
            "1º e 2º lei de Mendel: lei da segregação genética",
            "Relação entre genótipo e fenótipo",
            "Lei da segregação independente dos genes",
            "O mapeamento dos genes nos cromossomos",
            "Herança e sexo",
            "Aplicação do conhecimento genético",
        ],
        "Classificação dos seres vivos": [
            "Taxonomia e sistemática",
            "Vírus",
            "Reino Monera",
            "Reino Protista",
            "Reino Fungi",
        ],
        "Zoologia": [
            "Poríferos",
            "Cnidários",
            "Platelmintos",
            "Nematelmintos",
            "Artrópodes",
            "Equinodermos",
            "Moluscos",
            "Anelídeos",
            "Protocordados",
            "Cordados",
        ],
        "Evolução": [],
        "Ecologia": [
            "Fundamentos da ecologia",
            "Energia e matéria nos ecossistemas",
            "Dinâmica das populações biológicas",
            "Relação ecológica entre seres vivos",
            "Sucessão ecológica e biomas",
        ],
        "Botânica": [],
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
        "Economia Açúcareira, Trabalho Colonial, União Ibérica e Invasões Holandesas",
        "Iluminismo",
        "Revoluções Burguesas",
        "Inglaterra",
        "Estados Unidos",
        "França", 
        "Expansão Territorial Brasileira",
        "O Século do Ouro do Brasil",
        "Período Joanino e o Processo de Independência",
        "Independência das Colônias Ibéricas",
        "Brasil Imperial",
        "Primeiro Império",
        "Perído Regencial",
        "Revoluções Liberais do Século XIX",
        "Segundo Império",
        "Brasil República",
        "Crise do Brasil Imperial e a República das Espadas",
        "Estados Unidos no Século XIX",
        "Imperialismo",
        "Primeira Guerra Mundial",
        "Revolução Russa",
        "Período Entre-Guerras",
        "Segunda Guerra Mundial",
        "República Oligárquica",
        "Era Vargas",
        "Guerra Fria",
        "Brasil Pós-64",
        "Ditadura Militar",
        "Redemocratização e Populismo",
        "Nova República",
        "Atualidades e Conceitos",
        "Mundo Contemporâneo",
        "China",
        "Independência das Colônias da África e Ásia",
        "Filosofia", 
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
                "Literatura de Informação/Literatura dos Jesuítas": [],
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
        "Conhecimentos Numéricos": [
            "Razão e Proporção",
            "Porcentagem",
            "Regras de três simples e composta",
            "Sequências Numéricas (PA e PG)",
            "Complexos",
        ],
        "Função": [
            "Função Linear Guadrática",
            "Equação Exponencial",
            "Função Logarítima",
        ],
        "Trigonometria": [
            "Triângulo Retângulo e seus fundamentos",
            "Funções Trigonométricas",
        ],
        "Matrizes e Sistemas": [
            "Conceito de Matrizes",
            "Operações Determinantes",
            "Sistemas Lineares",
        ],
        "Conhecimento de Probabilidade": [
            "Análise Combinatória: PFC. Fatorial. Arranjo. Permutação. Combinação.",
            "Probabilidade",
        ],
        "Geometria Espacial": [],
        "Geometria Analítica": [],
        "Conjuntos dos Números Complexos": [],
        "Estatística": [],
        "Polinômios": [],
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
