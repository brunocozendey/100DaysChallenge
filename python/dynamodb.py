#-*- coding: utf-8 -*- 
# DYNAMO DB AWS TEST

import boto3
import json
import decimal
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

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


    ## Procurar item no BD
    ## Busca pela combinação de chaves PK
    title = "The Big New Movie"
    year = 2015

    try:
        response = table.get_item(
            Key={
                'year': year,
                'title': title
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print("GetItem succeeded:")
        print(json.dumps(item, indent=4, cls=DecimalEncoder))

    ## Atualizar um atributo de um item.
    ## usar update_item , pode atualizar atributos existentes e adicionar um item não existente.

    title = "The Big New Movie"
    year = 2015

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating = :r, info.plot=:p, info.actors=:a",
        ExpressionAttributeValues={
            ':r': decimal.Decimal(5.5),
            ':p': "Everything happens all at once.",
            ':a': ["Larry", "Moe", "Curly"]
        },
        ReturnValues="UPDATED_NEW"
    )

    print("UpdateItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))


    title = "The Big New Movie"
    year = 2015

    try:
        response = table.get_item(
            Key={
                'year': year,
                'title': title
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print("GetItem succeeded:")
        print(json.dumps(item, indent=4, cls=DecimalEncoder))


## Incremento atômico: Pode atualizar apenas um item, podendo incrementar ou decrementar.

    title = "The Big New Movie"
    year = 2015

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating = info.rating + :val",
        ExpressionAttributeValues={
            ':val': decimal.Decimal(1)
        },
        ReturnValues="UPDATED_NEW"
    )

    print("UpdateItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))

## Update an Item (Conditionally), usa o UpdateItem com uma condição. Se a condição for true, o update acontece; O item é atualizado apenas se a condição for verdadeira.


    title = "The Big New Movie"
    year = 2015

    # Conditional update
    print("Attempting conditional update...")

    try:
        response = table.update_item(
            Key={
                'year': year,
                'title': title
            },
            UpdateExpression="remove info.actors[0]",
            ConditionExpression="size(info.actors) >= :num",
            ExpressionAttributeValues={
                ':num': 3
            },
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        print("UpdateItem succeeded:")
        print(json.dumps(response, indent=4, cls=DecimalEncoder))


## Deletar items

## Usando o método delete_item para apagar um item específico utilizando a chave primária. 
## De forma opcional pode fornecer uma ConditionExpression para criar uma condição para o item ser apagado.

    title = "The Big New Movie"
    year = 2015

    print("Attempting a conditional delete...")

    try:
        response = table.delete_item(
            Key={
                'year': year,
                'title': title
            },
            ConditionExpression="info.rating >= :val",
            ExpressionAttributeValues= {
                ":val": decimal.Decimal(5)
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        print("DeleteItem succeeded:")
        print(json.dumps(response, indent=4, cls=DecimalEncoder))

## Query e escaneando dados
# A query resgata dados da tabela e para isso é necessário especificar uma cave valor. A ordem da chave é opcional. 
# A chave primária para a tabela Movies é composta de:
# year – partition key. Que o tipo de atributo é um número. 
# title – sort key. do tipo string.

# Por exemplo para encontrar todos os filmes durante um ano específico. 
# Pode também, definir um título para retornar um conjunto de filmes baseados em alguma condição (da sort key). 
# Por exemplo, é possível encontrar filmes feitos em 2014 que tenham o título começando com a letra "A".
# Em adição ao método da query é possível usar o métodos scan para retornar tdos os dados da tabela.

    print("Movies from 1985")

    response = table.query(
        KeyConditionExpression=Key('year').eq(1985)
    )

    for i in response['Items']:
        print(i['year'], ":", i['title'])



# Vamos agora retornar todos os filmes feitos em 1992 com o título iniciando com a letra "A" até "L".

    table = dynamodb.Table('Movies')

    print("Movies from 1992 - titles A-L, with genres and lead actor")

    response = table.query(
        ProjectionExpression="#yr, title, info.genres, info.actors[0]",
        ExpressionAttributeNames={ "#yr": "year" }, # Expression Attribute Names for Projection Expression only.
        KeyConditionExpression=Key('year').eq(1992) & Key('title').between('A', 'L')
    )

    for i in response[u'Items']:
        print(json.dumps(i, cls=DecimalEncoder))


# O método scan lê todo item na tabela toda e retora todos os dados da tabela. Você pode fornecer uma expressão opcional então os únicos items que atenderem o critério serao retornados. 
# No entnado o filtro é aplicado apenas depois de todos os campos da tabela ser escaneado.
# O scan specifies o filtro opcional para retornar apenas os filmes de 1950 e descartar todos os demais.
# ProjectionExpression especifica os atributos se você quer scanear. 
# FilterExpression specifica a condição que retornar apenas os items que satisfazem a condição. 
# O método scan retornar um conjunto de items cada vez.
# O valor LastEvaluatedKey da resposta é então passado através do parâmetro ExclusiveStartKey. Quando a última página é returnada, LastEvaluatedKey não é parte da resposta.


    fe = Key('year').between(1950, 1959)

    pe = "#yr, title, info.rating"
    
    # Expression Attribute Names for Projection Expression only.
    ean = { "#yr": "year", }
    esk = None


    response = table.scan(
        FilterExpression=fe,
        ProjectionExpression=pe,
        ExpressionAttributeNames=ean
        )

    for i in response['Items']:
        print(json.dumps(i, cls=DecimalEncoder))

    while 'LastEvaluatedKey' in response:
        response = table.scan(
            ProjectionExpression=pe,
            FilterExpression=fe,
            ExpressionAttributeNames= ean,
            ExclusiveStartKey=response['LastEvaluatedKey']
            )

        for i in response['Items']:
            print(json.dumps(i, cls=DecimalEncoder))

    
    # Para deletar a tabela basta descomentar a linha abaixo.
    # table.delete()
    