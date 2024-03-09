import flet as ft  # importar

def main(pagina):  # cria a função principal 
    texto = ft.Text("ZapZap")

    def entrar_chat(evento):
        print("U're in chatZap.")
        popup.open = False

    titulo_popup = ft.Text("Welcome to ZapZap!")
    nome_usuario = ft.TextField(label="Write ur name")
    botao_entrar = ft.ElevatedButton("CHAT", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open =  True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar CHAT", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main)  # criar o app chamando a função principal
