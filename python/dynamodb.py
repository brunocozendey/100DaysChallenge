#-*- coding: utf-8 -*- 
# DYNAMO DB AWS TEST

import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

## Criando a tabela movies no Dynamo
## Em create_table, especificamos o nome da tabela, os atributos da chave primária e os tipos de dados. 
# O parametro ProvisionedThroughput é necessário mas o DynamoDB local o ignora.

table = dynamodb.Table('Movies')
if table.table_status != "ACTIVE":
    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    print("Table status:", table.table_status)
else:
## Agora vamos escrever na tabela movies criada.
## Para isso utilizei um bd do IMDB disponivel em JSON
## O dynamo vai utilizar o ano e o titulo como PK e o restante dentro de um atributo info.

    table = dynamodb.Table('Movies')
    create = False # Para não criar toda vez que o script é executado.
    if create == True:
        with open("moviedata.json") as json_file:
            movies = json.load(json_file, parse_float = decimal.Decimal)
            for movie in movies:
                year = int(movie['year'])
                title = movie['title']
                info = movie['info']

                print("Adding movie:", year, title)

                table.put_item(
                Item={
                    'year': year,
                    'title': title,
                    'info': info,
                    }
                )

## Create Item
    # Helper class to convert a DynamoDB item to JSON.
    class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                if abs(o) % 1 > 0:
                    return float(o)
                else:
                    return int(o)
            return super(DecimalEncoder, self).default(o)

    title = "The Big New Movie"
    year = 2015

    response = table.put_item(
    Item={
            'year': year,
            'title': title,
            'info': {
                'plot':"Nothing happens at all.",
                'rating': decimal.Decimal(0)
            }
        }
    )

    print("PutItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))