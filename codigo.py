import flet as ft  # importar

def main(pagina):  # cria a função principal 
    texto = ft.Text("ZapZap")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        # adc msg no chat 
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        # limpa campo de mensagem 
        campo_mensagem.value=""
        pagina.update()

    campo_mensagem = ft.TextField(label="Type ur message", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Send", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        print("U're in chatZap.")
        # fechar o popup
        popup.open = False
        # tirar o botao 
        pagina.remove(botao_iniciar)
        # tirar o titulo 
        pagina.remove(texto)
        # criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        # campo de digitar
        pagina.add(linha_enviar) 

        pagina.update()

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

ft.app(target=main, view=ft.WEB_BROWSER)  # criar o app chamando a função principal
