#Script Python para envio de email em HTML, feito com objetivo de utilizar no Zabbix.

#Descricao
Colocar o script no AlertScripts, alterar as variaveis SRVSMTP, FROM e PASS, criar seu arquivo HTML e adicionar em ConfigurationAction no campo 'Default message' o HTML gerado.

#Syntax:
<pre><code>
[root@zabbix ~]# ./sendhtml.py destinatario@email.com.br ASSUNTO MENSAGEM
</code></pre>

#Macros padrao:
<pre><code>
Host: {HOST.NAME}
Trigger: {TRIGGER.NAME}
Valor do Evento: {ITEM.VALUE}
Status: {TRIGGER.STATUS}
Severidade: {TRIGGER.SEVERITY}
Event ID: {EVENT.ID}
Data do Evento: {EVENT.DATE}
Hora do Evento: {EVENT.TIME}
</code></pre>

#Sites gerar HTML
<pre><code>
http://www.html.am/html-editors/online-html-editor.cfm
http://www.quackit.com/html/online-html-editor/
</code></pre>

