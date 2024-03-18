with open ('text.txt', 'w') as file:
    for i in range(1,300000):
        file.write('insert into users(id,access_token,created_at,updated_at)' + 'values(' + str(i) + ', "/VB7whncWu9ACxYa7FFz2A==",now(),now());')
        file.write('\n')