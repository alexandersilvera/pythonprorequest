from pythonprorequest.libpythonpro.spam.enviador_de_email import Enviador


def test_crear_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

def test_remitente():
    enviador=Enviador()
    resultado=enviador.enviar(
        'alexandersilvera@hotmail.com',
        'Cursos Python Pro',
        'Primer grupo de Guido Von Rossum abierta'
    )
    assert 'alexandersilvera@hotmail.com' in resultado