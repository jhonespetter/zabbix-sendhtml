# zabbix-sendhtml

Script em Python para envio de email em HTML, feito com objetivo de utilizar no Zabbix.

== Syntaxe:
[root@zabbix ~]# ./sendhtml.py destinatario@email.com.br ASSUNTO '<h1>MENSAGEM</h1>'

== Macros padrao:
Host: {HOST.NAME}
Trigger: {TRIGGER.NAME}
Valor do Evento: {ITEM.VALUE}
Status: {TRIGGER.STATUS}
Severidade: {TRIGGER.SEVERITY}
Event ID: {EVENT.ID}
Data do Evento: {EVENT.DATE}
Hora do Evento: {EVENT.TIME}

== Sites gerar HTML
http://www.html.am/html-editors/online-html-editor.cfm
http://www.quackit.com/html/online-html-editor/

== Descricao
Colocar o script no AlertScripts, alterar as variaveis SRVSMTP, FROM e PASS, criar seu arquivo HTML e adicionar em ConfigurationAction no campo 'Default message' o HTML gerado.