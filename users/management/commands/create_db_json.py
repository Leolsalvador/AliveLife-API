import json
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = [
            {
                "model": "auth.user",
                "pk": 1,
                "fields": {
                    "username": "admin",
                    "first_name": "Nome",
                    "last_name": "Sobrenome",
                    "email": "usuario1@example.com",
                    "password": make_password("admin"),
                    "is_staff": True,
                    "is_active": True,
                    "is_superuser": True
                }
            },
            {
                "model": "auth.user",
                "pk": 2,
                "fields": {
                    "username": "Leonardo",
                    "first_name": "Leonardo",
                    "last_name": "Alcantara",
                    "email": "leonardo@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 3,
                "fields": {
                    "username": "Athos",
                    "first_name": "Athos",
                    "last_name": "William",
                    "email": "Athos@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 4,
                "fields": {
                    "username": "Beatriz",
                    "first_name": "Beatriz",
                    "last_name": "Alvarenga",
                    "email": "Beatriz@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 5,
                "fields": {
                    "username": "Iane",
                    "first_name": "Iane",
                    "last_name": "Ramos",
                    "email": "Iane@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 6,
                "fields": {
                    "username": "Carlos",
                    "first_name": "Carlos",
                    "last_name": "Lessa",
                    "email": "Carlos@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 7,
                "fields": {
                    "username": "Thallys",
                    "first_name": "Thallys",
                    "last_name": "Xavier",
                    "email": "Thallys@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 8,
                "fields": {
                    "username": "Victor",
                    "first_name": "Victor",
                    "last_name": "Emanuel",
                    "email": "Victor@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 9,
                "fields": {
                    "username": "Rayssa",
                    "first_name": "Rayssa",
                    "last_name": "Paiva",
                    "email": "Rayssa@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 10,
                "fields": {
                    "username": "Humberto",
                    "first_name": "Humberto",
                    "last_name": "Dias",
                    "email": "Humberto@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 12,
                "fields": {
                    "username": "Gleidson",
                    "first_name": "Gleidson",
                    "last_name": "Porto",
                    "email": "Gleidson@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 13,
                "fields": {
                    "username": "Kadija",
                    "first_name": "Kadija",
                    "last_name": "Ramos",
                    "email": "Kadija@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 14,
                "fields": {
                    "username": "Leticia",
                    "first_name": "Leticia",
                    "last_name": "Alcantara",
                    "email": "Leticia@example.com",
                    "password": make_password("Alive&Life"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            # Adicionando mais 50 usuários
            {
                "model": "auth.user",
                "pk": 15,
                "fields": {
                    "username": "Ana",
                    "first_name": "Ana",
                    "last_name": "Silva",
                    "email": "ana.silva@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 16,
                "fields": {
                    "username": "Bruno",
                    "first_name": "Bruno",
                    "last_name": "Santos",
                    "email": "bruno.santos@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 17,
                "fields": {
                    "username": "Carla",
                    "first_name": "Carla",
                    "last_name": "Pereira",
                    "email": "carla.pereira@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 18,
                "fields": {
                    "username": "Diego",
                    "first_name": "Diego",
                    "last_name": "Alves",
                    "email": "diego.alves@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 19,
                "fields": {
                    "username": "Eliane",
                    "first_name": "Eliane",
                    "last_name": "Oliveira",
                    "email": "eliane.oliveira@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 20,
                "fields": {
                    "username": "Felipe",
                    "first_name": "Felipe",
                    "last_name": "Souza",
                    "email": "felipe.souza@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 22,
                "fields": {
                    "username": "Helena",
                    "first_name": "Helena",
                    "last_name": "Freitas",
                    "email": "helena.freitas@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 23,
                "fields": {
                    "username": "Igor",
                    "first_name": "Igor",
                    "last_name": "Cunha",
                    "email": "igor.cunha@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 24,
                "fields": {
                    "username": "Julia",
                    "first_name": "Julia",
                    "last_name": "Melo",
                    "email": "julia.melo@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 25,
                "fields": {
                    "username": "Kleber",
                    "first_name": "Kleber",
                    "last_name": "Nunes",
                    "email": "kleber.nunes@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 26,
                "fields": {
                    "username": "Larissa",
                    "first_name": "Larissa",
                    "last_name": "Gomes",
                    "email": "larissa.gomes@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 27,
                "fields": {
                    "username": "Marcio",
                    "first_name": "Marcio",
                    "last_name": "Tavares",
                    "email": "marcio.tavares@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 28,
                "fields": {
                    "username": "Natasha",
                    "first_name": "Natasha",
                    "last_name": "Pires",
                    "email": "natasha.pires@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 29,
                "fields": {
                    "username": "Otávio",
                    "first_name": "Otávio",
                    "last_name": "Barros",
                    "email": "otavio.barros@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 30,
                "fields": {
                    "username": "Patrícia",
                    "first_name": "Patrícia",
                    "last_name": "Silveira",
                    "email": "patricia.silveira@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 31,
                "fields": {
                    "username": "Quiteria",
                    "first_name": "Quitéria",
                    "last_name": "Duarte",
                    "email": "quiteria.duarte@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 32,
                "fields": {
                    "username": "Roberta",
                    "first_name": "Roberta",
                    "last_name": "Furtado",
                    "email": "roberta.furtado@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 33,
                "fields": {
                    "username": "Samuel",
                    "first_name": "Samuel",
                    "last_name": "Cavalcante",
                    "email": "samuel.cavalcante@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 34,
                "fields": {
                    "username": "Tatiane",
                    "first_name": "Tatiane",
                    "last_name": "Rocha",
                    "email": "tatiane.rocha@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 35,
                "fields": {
                    "username": "Ulisses",
                    "first_name": "Ulisses",
                    "last_name": "Pimentel",
                    "email": "ulisses.pimentel@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 36,
                "fields": {
                    "username": "Viviane",
                    "first_name": "Viviane",
                    "last_name": "Mota",
                    "email": "viviane.mota@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 37,
                "fields": {
                    "username": "Walter",
                    "first_name": "Walter",
                    "last_name": "Cordeiro",
                    "email": "walter.cordeiro@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 38,
                "fields": {
                    "username": "Yasmin",
                    "first_name": "Yasmin",
                    "last_name": "Xavier",
                    "email": "yasmin.xavier@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 39,
                "fields": {
                    "username": "Zé",
                    "first_name": "José",
                    "last_name": "Santos",
                    "email": "ze.santos@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 40,
                "fields": {
                    "username": "Adriana",
                    "first_name": "Adriana",
                    "last_name": "Vieira",
                    "email": "adriana.vieira@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 41,
                "fields": {
                    "username": "Bernardo",
                    "first_name": "Bernardo",
                    "last_name": "Lopes",
                    "email": "bernardo.lopes@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 42,
                "fields": {
                    "username": "Clara",
                    "first_name": "Clara",
                    "last_name": "Dias",
                    "email": "clara.dias@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 43,
                "fields": {
                    "username": "Eduardo",
                    "first_name": "Eduardo",
                    "last_name": "Barbosa",
                    "email": "eduardo.barbosa@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 44,
                "fields": {
                    "username": "Flávia",
                    "first_name": "Flávia",
                    "last_name": "Santos",
                    "email": "flavia.santos@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 45,
                "fields": {
                    "username": "Gustavo",
                    "first_name": "Gustavo",
                    "last_name": "Ribeiro",
                    "email": "gustavo.ribeiro@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 46,
                "fields": {
                    "username": "Heloísa",
                    "first_name": "Heloísa",
                    "last_name": "Ferreira",
                    "email": "heloisa.ferreira@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 48,
                "fields": {
                    "username": "Juliana",
                    "first_name": "Juliana",
                    "last_name": "Teixeira",
                    "email": "juliana.teixeira@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 49,
                "fields": {
                    "username": "Karla",
                    "first_name": "Karla",
                    "last_name": "Sampaio",
                    "email": "karla.sampaio@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 50,
                "fields": {
                    "username": "Lucas",
                    "first_name": "Lucas",
                    "last_name": "Diniz",
                    "email": "lucas.diniz@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 51,
                "fields": {
                    "username": "Mariana",
                    "first_name": "Mariana",
                    "last_name": "Pereira",
                    "email": "mariana.pereira@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 52,
                "fields": {
                    "username": "Nathan",
                    "first_name": "Nathan",
                    "last_name": "Martins",
                    "email": "nathan.martins@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 53,
                "fields": {
                    "username": "Olga",
                    "first_name": "Olga",
                    "last_name": "Santos",
                    "email": "olga.santos@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 54,
                "fields": {
                    "username": "Paulo",
                    "first_name": "Paulo",
                    "last_name": "Henrique",
                    "email": "paulo.henrique@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 55,
                "fields": {
                    "username": "Quinn",
                    "first_name": "Quinn",
                    "last_name": "Lopes",
                    "email": "quinn.lopes@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 56,
                "fields": {
                    "username": "Rafael",
                    "first_name": "Rafael",
                    "last_name": "Soares",
                    "email": "rafael.soares@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 57,
                "fields": {
                    "username": "Sofia",
                    "first_name": "Sofia",
                    "last_name": "Moreira",
                    "email": "sofia.moreira@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 58,
                "fields": {
                    "username": "Tânia",
                    "first_name": "Tânia",
                    "last_name": "Pereira",
                    "email": "tania.pereira@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 59,
                "fields": {
                    "username": "Uliana",
                    "first_name": "Uliana",
                    "last_name": "Cardoso",
                    "email": "uliana.cardoso@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 60,
                "fields": {
                    "username": "Vitor",
                    "first_name": "Vitor",
                    "last_name": "Almeida",
                    "email": "vitor.almeida@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 61,
                "fields": {
                    "username": "Wesley",
                    "first_name": "Wesley",
                    "last_name": "Fernandes",
                    "email": "wesley.fernandes@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 62,
                "fields": {
                    "username": "Xuxa",
                    "first_name": "Xuxa",
                    "last_name": "Macedo",
                    "email": "xuxa.macedo@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 63,
                "fields": {
                    "username": "Yuri",
                    "first_name": "Yuri",
                    "last_name": "Pacheco",
                    "email": "yuri.pacheco@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            },
            {
                "model": "auth.user",
                "pk": 64,
                "fields": {
                    "username": "Zaneta",
                    "first_name": "Zaneta",
                    "last_name": "Faria",
                    "email": "zaneta.faria@example.com",
                    "password": make_password("senha123"),
                    "is_staff": False,
                    "is_active": True,
                    "is_superuser": False
                }
            }
        ]

        with open('db.json', 'w') as f:
            json.dump(users, f, indent=4)

        self.stdout.write(self.style.SUCCESS('Arquivo db.json criado com sucesso!'))
