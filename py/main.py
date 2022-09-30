from browser import document, console, alert, html, window
from browser.template import Template
from browser.local_storage import storage

def create_t(event, element):
  element.data.trf = "Nova tarefa: "+document["trfi"].value
  listaSalva = storage["tarefast"]
  newTarefa = document["trfi"].value
  salvar = listaSalva + "/" + newTarefa
  storage["tarefast"] = salvar
  listaNova = storage["tarefast"].replace("/", "<br>-> ")
  document["list-trfd"] <= html.SPAN("<p id='trfi'>-> {}</p>".format(document["trfi"].value))
  

  
Template("ins",[create_t]).render(trf="")

storage['foo'] = 'bar' 
# document["listah"] <= html.P(storage["tarefast"].replace("/","<br>-> "))




dt = storage["tarefast"].split("/")
if len(dt) == 1:
  document["list-trfd"] <= "Não tem tarefas!"
dt.remove("")
for lista in dt:
  document["list-trfd"] <= html.SPAN(f"<p id='trfi'>-> {lista}</p>")
  


document["btn-e"] <= html.BUTTON("Excluir tudo", ID="excluir")
buttonExcluir = document["excluir"]

def excluir(evt):
  storage["tarefast"] = ""
  
buttonExcluir.bind('click', excluir)

