import g4f
g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args
# response = g4f.ChatCompletion.create(
#     model=g4f.models.gpt_4,
#     messages=[{"role": "user", "content": "Explain like i'm five years old: Internal architecture of 8086"}],
# )  # alternative model setting

# print(response)

response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    # messages=[{"role": "user", "content": "Explain like i'm five years old: Internal architecture of 8086"}],
    messages=[{'role':'user', 'content':'Dijkstras algorithm'},{'role':'system', 'content':'You are an teacher who summarizes and simplifies large concepts to small like even a weak student can understand'}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')
