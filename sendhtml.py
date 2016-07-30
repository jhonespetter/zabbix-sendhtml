#!/usr/bin/env python
"""
Autor: Jhones Petter
Versao: 1.0
Descricao: Envio email em html.
Pacotes base: libesmtp-devel, libesmtp
"""

import mimetypes, os, smtplib, sys
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FROM='noc@email.com.br'
SRVSMTP='smtp.email.com.br'
PASS='senha'

DESTINATION=sys.argv[1]
SUBJECT=sys.argv[2]
MESSAGE=sys.argv[3]

msg = MIMEMultipart()
msg['From'] = FROM
msg['Subject'] = SUBJECT

msg.attach(MIMEText(MESSAGE, 'html', 'utf-8'))
raw = msg.as_string()

smtp = smtplib.SMTP(SRVSMTP, 587)
smtp.login(FROM, PASS)
smtp.sendmail(FROM, DESTINATION, raw)
smtp.quit()