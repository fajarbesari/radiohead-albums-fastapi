import jwt


# class represent jwt token 
class Auth:
    token : str
    refresh_token : str
    

algorithm = "HS256"
key = '49a41479b6b9aea35f904fcfb4739064faabe42442cf664efb5b9bd80ed17893'


token = jwt.encode(payload={"username" : "rangga", "password" : "cinta"}, algorithm=algorithm, key=key)

decoded  = jwt.decode(token, algorithms=algorithm, key=key)

decoded_completed = jwt.decode_complete(token, algorithms=algorithm, key=key)

print(token)
print("////////////////////")
print(decoded)
print("////////////////////")
print(decoded_completed)
# print(decoded)